from PIL import Image, ImageDraw, ImageFilter
import face_recognition
import os

def face_detection(directory):
    count = 0

    for filename in os.listdir(directory):
        if not filename.startswith('.'):
            image = face_recognition.load_image_file(directory + '/' + filename)
            face_landmarks_list = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
            print("I found {} faces in this photograph".format(len(face_landmarks_list)))
            print(filename)
            # print(face_landmarks_list[0]['left_eye'])

            for face_landmark in face_landmarks_list:
                top, right, bottom, left = face_landmark
                #print("A face in" + " " + filename + " " + "is located at pixel location: Top: {}, Left: {}, Bottom: {}, Right: {} ".format(top, left, bottom, right))

                im = Image.open(directory + '/' + filename)
                y1 = top
                y0 = bottom
                x0 = left
                x1 = right

                mask = Image.new("L", im.size, 0)
                draw = ImageDraw.Draw(mask)
                draw.rectangle([(x0,y0),(x1, y1)], fill=255)
                mask.save('mask.png')

                blurred = im.filter(ImageFilter.GaussianBlur(20))

                im.paste(blurred, mask=mask)
                im.save("blurredImg" + "_" + filename + ".png")

            count = count +1
            print(count)




