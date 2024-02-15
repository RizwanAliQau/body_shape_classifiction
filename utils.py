import cv2

def add_text(image, text='',pos=(1,20),color = (0, 0, 255)):
    # font 
    font = cv2.FONT_HERSHEY_SIMPLEX 
    
    # org 
    org = (00, 185) 
    
    # fontScale 
    fontScale = 0.3

    # Line thickness of 2 px 
    thickness = 1
    
    # Using cv2.putText() method 
    image = cv2.putText(image, text, pos, font, fontScale,  
                    color, thickness, cv2.LINE_AA, False) 
    return image



def result_to_condition(class_id,annotated_frame):
    if class_id==0:
        annotated_frame =   add_text(annotated_frame,'***** Clothes Recommendations: A-line Silhouttes, flowy tunics, V-necks, fitted sleeves, trench-style coats, wrap dress, skinny jeans *****',color = (0, 255, 0))
        annotated_frame =   add_text(annotated_frame, text='***** Clothes to Avoid: Fitted or Structured Tops, Bright Color Tops, V-necks, Jackets, Dark Colored Pants, Necklaces, Earrings *****',pos=(1,50))
    elif class_id==1:
        annotated_frame =   add_text(annotated_frame, text='***** Clothes Recommendations: form fitting jersey knits, wrap tops, peplum blouses, V-necks, fitted blazers, wrap dress, stretchy skinny jeans, fitted jumpsuits *****',color = (0, 255, 0))
        annotated_frame =   add_text(annotated_frame, text='***** Clothes to Avoid: shapeless clothing, smock dresses, turtle-necks, drop waist *****',pos=(1,50)) 
    elif class_id==2:
        annotated_frame =   add_text(annotated_frame, text='***** Clothes Recommendations: weighty fabrics, tapered sleeves, wide straps, darker colored shirts, fitted and past-hip shirts, straight cut jackets, baggy trousers *****',color = (0, 255, 0))
        annotated_frame =   add_text(annotated_frame, text='***** Clothes to Avoid: boat necks, V-necks, heavy shoulder pads, skinny trousers *****',pos=(1,50)) 
    elif class_id==3:
        annotated_frame =   add_text(annotated_frame, text='***** Clothes Recommendations: Slim-fit shirts, Jeans, Straight-leg trousers, Slim-fit Jackets, Horizontal stripes, Trousers with larger seat drop *****',color = (0, 255, 0))
        annotated_frame =   add_text(annotated_frame, text='***** Clothes to Avoid: Structured tailoring, prints, patterns, scoop necklines *****',pos=(1,50)) 
    elif class_id==4:
        annotated_frame =   add_text(annotated_frame, text='***** Clothes Recommendations: slightly fitted pants, oversized sweaters, structured jackets, blazers, dark solid colors, fabrics with small patterns *****',color = (0, 255, 0))
        annotated_frame =   add_text(annotated_frame, text='***** Clothes to Avoid: horizontal patterns, stripes, tight clothing *****',pos=(1,50)) 
    elif class_id==5:
        annotated_frame =   add_text(annotated_frame, text='***** Clothes Recommendations: fitted or structured tops, bright colored tops, V-necks, jackets, dark colored pants, necklaces, earrings *****',color = (0, 255, 0))
        annotated_frame =   add_text(annotated_frame, text='***** Clothes to Avoid: Tight tops, hip-length&lowrise jackets, skinny jeans, leggings *****',pos=(1,50)) 
    elif class_id==6:
        annotated_frame =   add_text(annotated_frame, text='***** Clothes Recommendations: halter styles, peacoats, dusters, flowy outerwear, Empire line dresses, princess seam dresses, and wrap dresses, belts *****',color = (0, 255, 0))
        annotated_frame =   add_text(annotated_frame, text='***** Clothes to Avoid: shapeless and boxy styles, pea coats, baggy jeans *****',pos=(1,50)) 
    elif class_id==7:
        annotated_frame =   add_text(annotated_frame,'***** Clothes Recommendations: Horizontal stripes, Structurec *****',color = (0, 255, 0))
        annotated_frame =   add_text(annotated_frame, text='***** Clothes to Avoid: Double-Breasted Jackets *****',pos=(1,50))
    elif class_id==8:
        annotated_frame =   add_text(annotated_frame, text='***** Clothes Recommendations: Close-fit trousers, blaze and suits, vertical striped shirts, Normal lengthed neckties, check and plaid shirts *****',color = (0, 255, 0))
        annotated_frame =   add_text(annotated_frame, text='***** Clothes to Avoid: Loose and saggy clothing, bland clothing *****',pos=(1,50)) 
    elif class_id==9:
        annotated_frame =   add_text(annotated_frame, text='***** Clothes Recommendations: Tailored patterned blazers, Vertical stripes, Jackets with structured shoulders, Single-breasted suits, Brighter color panels *****',color = (0, 255, 0))
        annotated_frame =   add_text(annotated_frame, text='***** Clothes to Avoid: Fitted polo shirts, Roll necks, Oversized clothing, Skinny fits *****',pos=(1,50)) 
    
    return annotated_frame