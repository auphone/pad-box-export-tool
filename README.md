## About this project

This is a project aim to extract my pets from Puzzle and dragons for development usage

## How does it works?

Use ffmpeg + ImageMagick to extract the pet icons from screen recording that scroll through the in-game box from top to bottom. Then use opencv features matching (SIFT + FLANN) to match the extracted icons with the original pet images

## Before you start

Please note that there are a lot of hardcoded stuff inside the scripts, you should read the code and adjust the values by yourself.

If you know Chinese, you can also check out my blog to get "slightly" more detail there

https://auphone.net/posts/%E5%8C%AF%E5%87%BA%E9%BE%8D%E6%97%8F%E6%8B%BC%E5%9C%96%EF%BC%88Puzzle-Dragons%EF%BC%89%E5%AF%B5%E7%89%A9%E6%B8%85%E5%96%AE%E7%9A%84%E6%96%B9%E6%B3%95/

## Pre-request

The version on my DEV env, FYI

```
Python 3.9
OpenCv 4.5
FFmpeg 4.4
ImageMagick 7.1
```

# Getting started

1. Clone the project

2. Create `videos` folder

```
cd pad-pet-extractor
mkdir videos
```

3. Put the video inside the videos folder and name it as `box.mp4`

4. Get the original pet images (Use your method)

I got the images from one of the Chinese wiki website. I don't recommend it, but I will provide the script in `./lib/image_downloader.js` anyway

5. Run the script one by one

```
./1_extract_video.sh
./2_extract_pet.sh
./3_matching.sh
```

At the end you will get an ID list located at `./out/ids.txt`

#### Have fun ( ﾟДﾟ)σ
