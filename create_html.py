from html4vision import Col, imagetable
import os

# table description

#curr_dir = '/Users/helenjiang/Downloads/HTML4Vision/html4vision_code/'

#loop through vis_gt to get the img ids
#sort the img ids

# tp_fp_images = []
# for tp_fp_image in sorted(os.listdir('full/vis_gt/')):
# 	tp_fp_image_path = os.path.join('full/vis_gt', tp_fp_image)
# 	tp_fp_images.append(tp_fp_image_path)

# detection_images = []
# for detection_image in sorted(os.listdir('full/vis_detect/')):
# 	detection_image_path = os.path.join('full/vis_detect', detection_image)
# 	detection_images.append(detection_image_path)

# print(tp_fp_images[0])
# print(detection_images[0])
# cols = [
#   # Col('id1', 'ID'),                                               # make a column of 1-based indice
#   # Col('img', 'Images with TP/FP', 'full/vis_gt/*.png'),             # specify image content for column 2
#   Col('img', 'Images with TP/FP', tp_fp_images),
#   Col('img', 'Images with Detections', detection_images),     # specify image content for column 3
# ]

cols_all = [
  # Col('id1', 'ID'),                                               # make a column of 1-based indice
  # Col('img', 'Images with TP/FP', 'full/vis_gt/*.png'),             # specify image content for column 2
  Col('img', 'CHAIR', 'vis_top_detections/chair/*'),
  Col('img', 'BED', 'vis_top_detections/bed/*'),
#  Col('img', 'BED ONLY FALSE POSITIVES', 'vis_top_detections_bed_fp_only/bed/*'),
  Col('img', 'TOILET', 'vis_top_detections/toilet/*'),
  Col('img', 'TV', 'vis_top_detections/tv/*'),
  Col('img', 'COUCH', 'vis_top_detections/couch/*'),
  Col('img', 'POTTED PLANT', 'vis_top_detections/potted_plant/*'),
  #Col('img', 'Images with Detections', detection_images),     # specify image content for column 3
]

cols_chair = [
  Col('img', 'CHAIR', 'vis_top_detections/chair/*'),
]

cols_bed = [
  Col('img', 'BED', 'vis_top_detections/bed/*'),
]

cols_toilet = [
  Col('img', 'TOILET', 'vis_top_detections/toilet/*'),
]

cols_tv = [
  Col('img', 'TV', 'vis_top_detections/tv/*'),
]

cols_couch = [
  Col('img', 'COUCH', 'vis_top_detections/couch/*'),
]

cols_pottedplant = [
  Col('img', 'POTTED PLANT', 'vis_top_detections/potted_plant/*'),
]

# html table generation
imagetable(cols_all, imscale=0.6)

imagetable(cols_chair, 'chair.html')

imagetable(cols_bed, 'bed.html')

imagetable(cols_toilet, 'toilet.html')

imagetable(cols_tv, 'tv.html')

imagetable(cols_couch, 'couch.html')

imagetable(cols_pottedplant, 'potted_plant.html')
