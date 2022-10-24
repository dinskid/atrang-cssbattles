import sys
from PIL import Image
from diff import *

def main():
    args = sys.argv
    if (len(args) != 3):
        print("Usage: <name> file1 file2")
        return
    try:
        imga = Image.open(args[1])
        imgb = Image.open(args[2])

        aw, ah = imga.size
        bw, bh = imgb.size
        if (aw != bw or ah != bh):
            print("The images must be of equal dimension")
        w1 = (1 - pixel_diff(imga, imgb))
        print(w1 * 100)
        print(w1 * 10)

        w2 = (1 - color_diff(imga, imgb))
        print(w2 * 100)
        print(w2 * 10)

        w3 = ssim(imga, imgb)
        print(w3 * 100)
        print(w3 * 20)

    except Exception as e:
        print("Error!:", e)

if __name__ == '__main__':
    main()

