# Algorithmia

Algorithmia is a Open Market Place for Algorithms.

## Text Detection (CTPN)

[Text Detection Algorithm](https://algorithmia.com/algorithms/character_recognition/TextDetectionCTPN) 
detects text or words in a given input image including scanned documents or natural images. <br>
The Algorithm also annotates the source image with the bounding boxes around the text or words.

### Usage:

<b>CURL</b>
```shell
curl -X POST -d '{"input": "http://3.media.collegehumor.cvcdn.com/57/40/45795b7aa3650756ad94f776add650fd.jpg",
"output": "data://.algo/character_recognition/TextDetectionCTPN/temp/receipt.png"}
' -H 'Content-Type: application/json' -H 'Authorization: Simple YOUR_API_KEY' https://api.algorithmia.com/v1/algo/character_recognition/TextDetectionCTPN/0.2.0
```

<b>Python</b>
```shell
import Algorithmia

input = {
  "input": "http://3.media.collegehumor.cvcdn.com/57/40/45795b7aa3650756ad94f776add650fd.jpg",
  "output": "data://.algo/character_recognition/TextDetectionCTPN/temp/receipt.png"
}
client = Algorithmia.client('YOUR_API_KEY')
algo = client.algo('character_recognition/TextDetectionCTPN/0.2.0')
print(algo.pipe(input))
```

<b><i>Sample Result</i></b>
```shell
{  
   "boxes":[  
      {  
         "confidence":0.9616782665252686,
         "x0":368,
         "x1":575,
         "y0":58.95378875732422,
         "y1":106.28519439697266
      },
      {  
         "confidence":0.9594982266426086,
         "x0":224,
         "x1":271,
         "y0":367.0335998535156,
         "y1":381.1184387207031
      },
      {  
         "confidence":0.949138641357422,
         "x0":352,
         "x1":575,
         "y0":397.1089782714844,
         "y1":440.8250122070313
      },
      {  
         "confidence":0.9071121215820312,
         "x0":432,
         "x1":687,
         "y0":300.0794677734375,
         "y1":353.77691650390625
      }
   ],
   "output":"data://.algo/temp/img.png"
}
```

For Examples Visit the [Algorithmia Site](https://algorithmia.com/algorithms/character_recognition/TextDetectionCTPN/docs).

---

## Face Detection

[Face Detection]() Algorithm detects Human Face (or Faces) in a given source image.<br>
The Algorithm returns thee position of where the face was found along with an annotated image 
containing bounding box around the face (or faces). 

### Usage

<b>CURL</b>
```shell
curl -X POST -d '{
  "images": [
    {
      "url": "https://en.wikipedia.org/wiki/Barack_Obama#/media/File:DIG13623-230.jpg",
      "output": "data://.algo/temp/detected_faces.png"
    }
  ]
}' -H 'Content-Type: application/json' -H 'Authorization: Simple YOUR_API_KEY' https://api.algorithmia.com/v1/algo/dlib/FaceDetection/0.2.1
```
<b>Python</b>
```shell
import Algorithmia

input = {
  "images": [
    {
          "url": "https://en.wikipedia.org/wiki/Barack_Obama#/media/File:DIG13623-230.jpg",
          "output": "data://.algo/temp/detected_faces.png"
    }
  ]
}
client = Algorithmia.client('YOUR_API_KEY')
algo = client.algo('dlib/FaceDetection/0.2.1')
print(algo.pipe(input))
```

<b><i>Sample Result</i></b>
```shell
{
     "images": [
        {
          "detected_faces": [
            {
              "bottom": 350,
              "left": 349,
              "right": 617,
              "top": 82
            }
          ],
     "imageDimensions": {
       "height": 960,
       "width": 960
     }
}
```

---
