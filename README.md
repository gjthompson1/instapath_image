# Instapath Interview

## Liveness

curl http://localhost/ping

## Image Create

curl -X POST -H "Content-Type: multipart/form-data" -F "username=glen" -F "image=@test_images/boji.png" http://localhost:5000/images
