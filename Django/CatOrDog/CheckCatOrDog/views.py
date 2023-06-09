from django.shortcuts import render
import pickle
import numpy as np
# from keras.preprocessing import image
import tensorflow as tf
from django.core.files.storage import default_storage

# from tensorflow.keras.utils import load_img, img_to_array


def home(request):
    return render(request, 'CheckCatOrDog/index.html')

def getPredictions(file_url):
    cnn = pickle.load(open('ml_model.sav', 'rb'))

    test_image = tf.keras.preprocessing.image.load_img(file_url, target_size = (64, 64))
    test_image = tf.keras.preprocessing.image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = cnn.predict(test_image)
    print(result)
    if result[0][0] == 1:
        print('dog')
        return 'dog'
    else:
        print('cat')
        return 'cat'



def result(request):

    if request.method == "POST":
        # file = (request.POST.get('checkImage'))
        print('entered')
        file = request.FILES['checkImage']
        print(file)
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)

        # print(f"Fetched {Country }")

        result = getPredictions(file_url)
        print(result)
        return render(request, 'CheckCatOrDog/result.html', {'result': result})