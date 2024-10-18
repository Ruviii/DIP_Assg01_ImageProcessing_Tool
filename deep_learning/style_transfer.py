import tensorflow as tf
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
from tensorflow.keras.applications import vgg19

# Check the number of GPUs available
num_gpus = len(tf.config.experimental.list_physical_devices('GPU'))
print("Num GPUs Available: ", num_gpus)

# Check if TensorFlow is using the GPU
if num_gpus > 0:
    print("TensorFlow is using the GPU.")
else:
    print("TensorFlow is not using the GPU.")

class StyleTransfer:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.style_image_path = None 
        self.style_image_label = None
        self.img_nrows = 300  
        self.img_ncols = None
        self.total_variation_weight = 1e-6
        self.style_weight = 1e-2  
        self.content_weight = 1e-4 
        print("StyleTransfer class initialized")

    def set_style_image_label(self, style_image_label):
        self.style_image_label = style_image_label
        print("Style image label set")

    def upload_style_image(self):
        self.style_image_path = filedialog.askopenfilename(title="Select Style Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if self.style_image_path:
            print(f"Style image selected: {self.style_image_path}")
            image = Image.open(self.style_image_path)
            image.thumbnail((100, 100))
            photo = ImageTk.PhotoImage(image)
            self.style_image_label.config(image=photo, text="")  
            self.style_image_label.image = photo
            print("Style image uploaded and displayed")

    def delete_style_image(self):
        if self.style_image_label:
            self.style_image_label.config(image='', text="No image uploaded")
            self.style_image_label.image = None
            self.style_image_path = None
            print("Style image deleted")

    def preprocess_image(self, image_path, target_size):
        img = Image.open(image_path).convert('RGB')  # Ensure image is RGB
        img = img.resize(target_size)
        img = np.array(img)
        img = np.expand_dims(img, axis=0)
        img = vgg19.preprocess_input(img)
        return tf.convert_to_tensor(img)

    def deprocess_image(self, x):
        x = x.reshape((self.img_nrows, self.img_ncols, 3))
        x[:, :, 0] += 103.939
        x[:, :, 1] += 116.779
        x[:, :, 2] += 123.68
        x = x[:, :, ::-1]
        x = np.clip(x, 0, 255).astype("uint8")
        return x

    def apply_style_transfer(self):
        if self.file_handler.processed_img is not None and self.style_image_path is not None:
            self.file_handler.save_undo_state()
            print("Undo state saved")

            content_image_path = self.file_handler.img_path
            base_image = Image.open(content_image_path)
            original_size = base_image.size
            width, height = base_image.size
            self.img_ncols = int(width * self.img_nrows / height)
            target_size = (self.img_ncols, self.img_nrows)

            base_image = self.preprocess_image(content_image_path, target_size)
            style_reference_image = self.preprocess_image(self.style_image_path, target_size)
            combination_image = tf.Variable(self.preprocess_image(content_image_path, target_size))

            model = vgg19.VGG19(weights="imagenet", include_top=False)
            outputs_dict = dict([(layer.name, layer.output) for layer in model.layers])
            feature_extractor = tf.keras.Model(inputs=model.inputs, outputs=outputs_dict)

            style_layer_names = [
                "block1_conv1",
                "block2_conv1",
                "block3_conv1",
                "block4_conv1",
                "block5_conv1",
            ]
            content_layer_name = "block5_conv2"

            def compute_loss(combination_image, base_image, style_reference_image):
                input_tensor = tf.concat([base_image, style_reference_image, combination_image], axis=0)
                features = feature_extractor(input_tensor)
                loss = tf.zeros(shape=())

                layer_features = features[content_layer_name]
                base_image_features = layer_features[0, :, :, :]
                combination_features = layer_features[2, :, :, :]
                loss += self.content_weight * tf.reduce_sum(tf.square(combination_features - base_image_features))

                for layer_name in style_layer_names:
                    layer_features = features[layer_name]
                    style_reference_features = layer_features[1, :, :, :]
                    combination_features = layer_features[2, :, :, :]
                    sl = tf.reduce_sum(tf.square(self.gram_matrix(style_reference_features) - self.gram_matrix(combination_features)))
                    loss += (self.style_weight / len(style_layer_names)) * sl

                loss += self.total_variation_weight * tf.image.total_variation(combination_image)
                return loss

            @tf.function
            def compute_loss_and_grads(combination_image, base_image, style_reference_image):
                with tf.GradientTape() as tape:
                    loss = compute_loss(combination_image, base_image, style_reference_image)
                grads = tape.gradient(loss, combination_image)
                grads = tf.clip_by_value(grads, -1.0, 1.0) 
                
                return loss, grads

            optimizer = tf.keras.optimizers.Adam(learning_rate=5.0) 

            iterations = 400
            for i in range(1, iterations + 1):
                loss, grads = compute_loss_and_grads(combination_image, base_image, style_reference_image)
                if tf.math.is_nan(loss):
                    print(f"NaN loss encountered at iteration {i}")
                    break
                optimizer.apply_gradients([(grads, combination_image)])
                if i % 20 == 0:
                    print(f"Iteration {i}: loss={loss}")

            img = self.deprocess_image(combination_image.numpy())
            img = Image.fromarray(img)
            img = img.resize(original_size)
            img = np.array(img)
            self.file_handler.processed_img = img
            self.file_handler.display_image(img, self.file_handler.img_canvas2)
            print("Style transfer applied and displayed")

    def gram_matrix(self, x):
        x = tf.transpose(x, (2, 0, 1))
        features = tf.reshape(x, (tf.shape(x)[0], -1))
        gram = tf.matmul(features, tf.transpose(features))
        return gram

    def undo_action(self):
        self.file_handler.undo_action()

    def redo_action(self):
        self.file_handler.redo_action()