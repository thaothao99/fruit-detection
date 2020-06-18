from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import argparse

model = load_model('trained_vgg16.h5')


ap = argparse.ArgumentParser()
ap.add_argument("-s", "--src_path", required=True, help="source image path")
args = ap.parse_args()
img = image.load_img(args.src_path, target_size=(100, 100))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
target_labels = np.array(["Apple Braeburn", "Apple Crimson Snow", "Apple Golden 1", "Apple Golden 2"
 "Apple Golden 3", "Apple Granny Smith", "Apple Pink Lady", "Apple Red 1"
 "Apple Red 2", "Apple Red 3", "Apple Red Delicious", "Apple Red Yellow 1"
 "Apple Red Yellow 2", "Apricot", "Avocado", "Avocado ripe", "Banana"
 "Banana Lady Finger", "Banana Red", "Beetroot", "Blueberry", "Cactus fruit"
 "Cantaloupe 1", "Cantaloupe 2", "Carambula", "Cauliflower", "Cherry 1"
 "Cherry 2", "Cherry Rainier", "Cherry Wax Black", "Cherry Wax Red"
 "Cherry Wax Yellow", "Chestnut", "Clementine", "Cocos", "Dates", "Eggplant"
 "Ginger Root", "Granadilla", "Grape Blue", "Grape Pink", "Grape White"
 "Grape White 2", "Grape White 3", "Grape White 4", "Grapefruit Pink"
 "Grapefruit White", "Guava", "Hazelnut", "Huckleberry", "Kaki", "Kiwi"
 "Kohlrabi", "Kumquats", "Lemon", "Lemon Meyer", "Limes", "Lychee", "Mandarine"
 "Mango", "Mango Red", "Mangostan", "Maracuja", "Melon Piel de Sapo"
 "Mulberry", "Nectarine", "Nectarine Flat", "Nut Forest", "Nut Pecan"
 "Onion Red", "Onion Red Peeled", "Onion White", "Orange", "Papaya"
 "Passion Fruit", "Peach", "Peach 2", "Peach Flat", "Pear", "Pear Abate"
 "Pear Forelle", "Pear Kaiser", "Pear Monster", "Pear Red", "Pear Williams"
 "Pepino", "Pepper Green", "Pepper Red", "Pepper Yellow", "Physalis"
 "Physalis with Husk", "Pineapple", "Pineapple Mini", "Pitahaya Red", "Plum"
 "Plum 2", "Plum 3", "Pomegranate", "Pomelo Sweetie", "Potato Red"
 "Potato Red Washed", "Potato Sweet", "Potato White", "Quince", "Rambutan"
 "Raspberry", "Redcurrant", "Salak", "Strawberry", "Strawberry Wedge"
 "Tamarillo", "Tangelo", "Tomato 1", "Tomato 2", "Tomato 3", "Tomato 4"
 "Tomato Cherry Red", "Tomato Maroon", "Tomato Yellow", "Walnut"])
classes = model.predict_classes(images, batch_size=10)
print(classes, target_labels[classes])