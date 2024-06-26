from ultralytics import YOLO
import cv2
import math 
import matplotlib.pyplot as plt
import numpy as np
import locale
locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')


def determine_color_bias(image):
    olgunluk_duzeyi = "0"
    # Görüntüyü BGR'den RGB'ye dönüştür
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Kırmızı ve yeşil kanalları elde et
    r_channel = image_rgb[:, :, 0]
    g_channel = image_rgb[:, :, 1]

    # R ve G kanallarının ortalamalarını hesapla
    r_mean = np.mean(r_channel)
    g_mean = np.mean(g_channel)

    # R ve G kanallarının farkını hesapla
    diff = r_mean - g_mean
    #print("fark", diff)

    if diff < 0:
        if diff < -30:
            olgunluk_duzeyi = "0"
        elif -30 <= diff <= -10:
            olgunluk_duzeyi = "1"
        elif -10 < diff <= 0:
            olgunluk_duzeyi = "2"
        else:
            olgunluk_duzeyi = "?"
    else:
        if diff < 10:
            olgunluk_duzeyi = "3"
        elif 10 <= diff <= 30:
            olgunluk_duzeyi = "4"
        elif 30 < diff <= 50:
            olgunluk_duzeyi = "5"
        elif 50 < diff <= 70:
            olgunluk_duzeyi = "6"
        elif 70 < diff <= 90:
            olgunluk_duzeyi = "7"
        elif 90 < diff <= 110:
            olgunluk_duzeyi = "8"
        elif diff > 110:
            olgunluk_duzeyi = "10"
        else:
            olgunluk_duzeyi = "?"

    return olgunluk_duzeyi


def domates_olgunluk(box_image):
    #Görüntünün boyutlarını al
    height, width, _ = box_image.shape

    #Kesilecek bölgenin boyutu
    crop_percentage = 40 / 100
    crop_size = int(width * crop_percentage), int(height * crop_percentage)

    center_x, center_y = width // 2, height // 2
    half_width, half_height = crop_size[0] // 2, crop_size[1] // 2
    cropped_image = box_image[center_y - half_height:center_y + half_height,
                          center_x - half_width:center_x + half_width]

    cropped_image_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
    box_image_rgb = cv2.cvtColor(box_image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(box_image_rgb)
    plt.title('Tam Görüntü')

    plt.subplot(1, 2, 2)
    plt.imshow(cropped_image_rgb)
    plt.title('Kesit Görüntüsü')

    plt.show()

    color_bias = determine_color_bias(cropped_image)

    print("Domates", color_bias)
    return color_bias


cap = cv2.VideoCapture(0)
cap.set(3, 1024)
cap.set(4, 768)

# model
model = YOLO("best.pt")

# object classes
classNames = ["Fasulye", "Kivi", "PATLICAN", "BAL KABAGI", "BEYAZ KUDRET NARI", 
              "Beyaz Lahana", "Biber", "Brinjal", 
              "Brokoli", "Domates", "Karnabahar", "KUDRET NARI", "Papaya", "SALATALIK", "UZUM"]


while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            confidence = math.ceil((box.conf[0]*100))/100
            if (confidence>0.5):
                
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values
                
                box_image = img[int(y1):int(y2), int(x1):int(x2)]
                # put box in cam
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
    
                # confidence
                #confidence = math.ceil((box.conf[0]*100))/100
                print("Confidence --->",confidence)
    
                # class name
                cls = int(box.cls[0])
                class_name = classNames[cls]
                print("Class name -->", class_name)
                if(class_name=="Domates"):
                    seviye = domates_olgunluk(box_image)
                    label=f"{class_name}"
                    label2= f"Olgunluk duzeyi: {seviye}"
                    # object details
                    org = (x1, y1 - 30)
                    org2 = (x1, y1 - 10)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 1
                    fontScale2 = 0.65
                    color = (255, 0, 0)
                    color2 = (255,128,0)
                    thickness = 2
        
                    cv2.putText(img, label, org, font, fontScale, color, thickness,cv2.LINE_AA)
                    cv2.putText(img, label2, org2, font, fontScale2, color2, thickness,cv2.LINE_AA)
                else:
                    # Combine class name with confidence score
                    label = f"{class_name}: {confidence:.2f}"
                    # object details
                    org = [x1, y1]
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 1
                    color = (255, 0, 0)
                    thickness = 2
        
                    cv2.putText(img, label, org, font, fontScale, color, thickness,cv2.LINE_AA)
                


    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()