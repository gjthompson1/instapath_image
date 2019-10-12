# Instapath Interview

curl http://localhost:5000/ping

curl http://localhost:5000/images

curl \
  -d "username=Glen" \
  -F "image=@/Users/glendonthompson/Desktop/instapath/boji.png" \
  localhost:5000/images


curl -X POST -H "Content-Type: multipart/form-data" -F "image=@manaslu.jpg; user_id=glen" http://localhost:5000/images

curl -X POST -H "Content-Type: multipart/form-data" -F "username=glen" -F "image=@test_images/boji.png" http://localhost:5000/images
