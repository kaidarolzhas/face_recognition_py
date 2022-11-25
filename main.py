import os
import face_recognition
from PIL import Image, ImageDraw, ImageFont
import time
start_time = time.time()
# image = face_recognition.load_image_file('data/tokaev/61323a807075e2ba81c7c29a266ceeb2.jpg')
# face_encoding = face_recognition.face_encodings(image)[0]
# known_face_encodings = [
#     face_encoding
# ]
# known_face_names = [
#     "Tokaev"
# ]

image = face_recognition.load_image_file('data/bayzakova/Dnqr0pCn6mE.jpg')
face_encoding = face_recognition.face_encodings(image)[0]
known_face_encodings = [
    face_encoding
]
known_face_names = [
    "Ayzhan Bayzakova"
]

# image = face_recognition.load_image_file('data/golovkin/e74fa2cb7c4240b3.jpeg')
# face_encoding = face_recognition.face_encodings(image)[0]
# known_face_encodings = [
#     face_encoding
# ]
# known_face_names = [
#     "GGG"
# ]
for file in os.listdir("bayzakova"):
    test_image = face_recognition.load_image_file(f"bayzakova/{file}")
    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)
    pil_image = Image.fromarray(test_image)
    draw = ImageDraw.Draw(pil_image)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown Person"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0))
        fnt = ImageFont.truetype("comicbd.ttf", 14)
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(255, 255, 0), outline=(255, 255, 0))
        draw.text((left + 6, bottom - text_height - 5), name, font=fnt, fill=(0, 0, 0))
    del draw
    pil_image.show()
print("finish all" + "--- %s seconds ---" % (time.time() - start_time))

# Ayzhan Bayzakova 7 ошибок из 50 фотографии процент верного предсказания 86% 255 sec// 4 min 15 sec
# из 25 фотографии Айжан Байзаковы верно определил определить 23 92%
# 21548745210, Ayzhan_Bayzakova_26_18160955.jpg, b02308654fff927f25e64f70505091b7.jpg
# из 25 фотографии неизвестных людей опредил 5 человек как Айжан Байзакову
# 881bf3c090ca8609.jpeg, 1540180052_5a24e9a80fe1c.jpg,  21548745210, screen-3.jpg, 25018118_1516117478478823_5187373715272237056_n.jpg

# Golovkin 4 ошибок из 50 фотографии процент 92% //366 sec // 6 min 6 sec
# из 25 фотографии головкина верно определил 22 88%
# ec9a1406-f5e1-4e22-a04c-450be78dbc57-800x450.jpg, photo_24906.jpg, photo_75221.jpg
# из 25 фотографии неизвестных людей опредил 1 человек как Головкина
# 500_6306f329f15e9.jpg


# Tokaev 5 ошибок из 50 фотографии процент 90%//// 323.0687 sec// 5 min 23 sec
# из 25 фотографии токаева верно определил 22 88%
# 33da33e173f5d977df619d03376547bc.jpg, 6.jpg, be5c55e82bbe0cbf62e79be72fe0201c.jpg
# из 25 фотографии неизвестных людей опредил 2 человек как токаева
# 1645425603_KZ3_5508.jpg, EvEl3yBXcAI6ZOl.jpg,

