import requests

url = 'https://mediafirewall-ai.millionvisions.ai/mfw/media/mohan12.prakash89@gmail.com/url/filters'

params = {
  'filters': 'Nudity(HalfNude),CelebrityDetection,Disturbing,Violence,Watermark',
  'apikey': 'Xi1G9pVWAacYW6hthVCiXBnfSTOHL4Rh',
  'mediaUrl': 'https://media-recycle-service.s3.ap-south-1.amazonaws.com/bella.jpg',
}

headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im1vaGFuMTIucHJha2FzaDg5QGdtYWlsLmNvbSIsInN1YiI6Im1vaGFuMTIucHJha2FzaDg5QGdtYWlsLmNvbSIsImlzcyI6Ik1OQTkzdTFXeUpQVzlPMDBIbXRxUTFsZWM0N1Jvclh2IiwiYXVkIjoiVGhlTWlsbGlvblZpc2lvbnMuY29tIiwiaWF0IjoxNzEyNzMxMTU2LCJleHAiOjE3MTI4MTc1NTZ9.ArroQ0pSQCVX23qiQTPLHxEzy5SbADFeoo8VFi3d1S0',
}

response = requests.post(url, params=params, headers = headers)
print(response.text)