# Instapath Interview

http://18.190.60.60

## POST images

```
curl -X POST -H "Content-Type: multipart/form-data" -F "username=glen" -F "image=@boji.png" http://18.190.60.60
```

## Test Locally

```
curl -X POST -H "Content-Type: multipart/form-data" -F "username=glen" -F "image=@test_images/boji.png" http://localhost:5000/images
```