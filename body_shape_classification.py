import ultralytics 
from ultralytics import YOLO
import cv2
import os
from utils import * 

select = 'camera'


if __name__ == '__main__':
    if select == 'train':
        # ============ TRAIN CODE ================= last training dir is rins/detect/train28 
        model = YOLO('yolov8s.yaml') #runs/detect/YOLO_new_weights/weights/best.pt')
        model.train(data='cfg/body_shape_classification.yaml', epochs=1000, imgsz=256, batch=32, patience=0)        
    elif select == 'predict':
        ############ DETECT PORTION ############################
        model = YOLO('final_body_classification_/weights/best.pt')
        path = "test_img/inverted_traiangle_women_0001.png" # dataset_ket_final/yolo_data/Connector_reference/train/images" # small_connectors_molds_white/normal/test/te    st_examples' #train_mold_mixed_data/val/images'
        model.predict(source=path, show=False, conf=0.1, save=True, batch=1,save_crop=False)

    elif select == 'vis':
        # ============ DEMO CODE =======================
        # Load the YOLOv8 model
        model = YOLO('final_body_classification_/weights/best.pt') #RTDETR("rtdetr-l.pt")
        # Open the video file
        video_path = "DATA/mold_anom_norm.mp4"
        cap = cv2.VideoCapture(video_path)

        # Loop through the video frames
        while cap.isOpened():
            # Read a frame from the video
            success, frame = cap.read()

            if success:
                # Run YOLOv8 inference on the frame
                results = model.predict(frame) 

                # Visualize the results on the frame
                annotated_frame = results[0].plot()

                # Display the annotated frame
                cv2.imshow("YOLOv8 Inference", annotated_frame)

                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                # Break the loop if the end of the video is reached
                break

        # Release the video capture object and close the display window
        cap.release()
        cv2.destroyAllWindows()
        print('End of prgramme !!!')
    elif select=='camera':
        # define a video capture object 
        vid = cv2.VideoCapture(0) 
        model = YOLO('final_body_classification_/weights/best.pt')
        while(True): 
            
            # Capture the video frame 
            # by frame 
            ret, frame = vid.read() 
            # Run YOLOv8 inference on the frame
            results = model.predict(frame,conf=0.3) 
            for result in results:
                boxes = result.boxes  # Boxes object for bounding box outputs
            
            # Visualize the results on the frame
            annotated_frame = results[0].plot()
            
            if boxes.cls.detach().cpu().numpy().size>0:
                annotated_frame =   result_to_condition(int(boxes.cls[0].item()),annotated_frame)
                
            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            # Display the resulting frame 
            #cv2.imshow('frame', frame) 
            
            # the 'q' button is set as the 
            # quitting button you may use any 
            # desired button of your choice 
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
        
        # After the loop release the cap object 
        vid.release() 
        # Destroy all the windows 
        cv2.destroyAllWindows() 
    else:
        raise NotImplementedError("Selection was wrong!") 
        