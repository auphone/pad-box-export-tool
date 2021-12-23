mkdir -p ./out/screenshots
rm ./out/screenshots/*
ffmpeg -i videos/box.mp4 -vf fps=10 ./out/screenshots/%d.jpg
mogrify -crop 750x720+0+400 ./out/screenshots/*.jpg