import cv2
import mediapipe 



mp_hands = mediapipe.solutions.hands
hands = mp_hands.Hands()
mp_draw = mediapipe.solutions.drawing_utils
cap = cv2.VideoCapture(0)




while True:
    ret, img = cap.read()
    if ret:
     img = cv2.flip(img, 1)
     h, w, c = img.shape
     results = hands.process(img)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

            x, y = int(lm_list[8].x * w), int(lm_list[8].y * h)

            if lm_list[8].y > lm_list[6].y:
                pointerDown = True
            else:
                pointerDown = False

            if lm_list[12].y > lm_list[10].y:
                middleDown = True
            else:
                middleDown = False

            if lm_list[16].y > lm_list[14].y:
                ringDown = True
            else:
                ringDown = False

            if lm_list[20].y > lm_list[18].y:
                pinkyDown = True
            else:
                pinkyDown = False
            if lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and lm_list[16].y > lm_list[14].y and  lm_list[20].y > lm_list[18].y:

                print("Help!!!")
                hop = "bob"
                idk=cv2.imwrite(r"C:\Users\javis\Downloads\final\smt.png", img)
               




            mp_draw.draw_landmarks(img, hand_landmark,
                                   mp_hands.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                                   mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                   )

    if cv2.waitKey(1) & 0xFF == ord('e'):
       cap.release()
       cv2.destroyAllWindows()

        

    cv2.imshow("idk", img)
    cv2.waitKey(1)