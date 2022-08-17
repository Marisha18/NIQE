import matplotlib.pyplot as plt
from PIL import Image

if __name__ == "__main__":
    
    plt.figure(figsize=(32, 16))
    plt.subplot(131)
    plt.title('Original HR Image')
    plt.imshow(Image.open('./test_imgs/image5301_hr.bmp'))
    plt.subplot(132)
    plt.title('ESRGAN')
    plt.imshow(Image.open('./test_imgs/image5301_lr_rlt.png'))
    plt.subplot(133)
    plt.title('Real-ESRGAN')
    plt.imshow(Image.open('./test_imgs/image5301_lr_out.bmp'))
    plt.show(block=False)