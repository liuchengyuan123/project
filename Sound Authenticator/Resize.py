from PIL import Image

'''
plot绘制出的图像大小并不一定能适配GUI的大小，所以需要调整
该参数已经调好，将图片resize到合适大小
'''
def resize(name):
    infile = name
    outfile = name
    im = Image.open(infile)
    (x, y) = im.size
    x_s = 500
    y_s = y * x_s // x
    out = im.resize((x_s, y_s), Image.ANTIALIAS)
    out.save(outfile)
