import numpy as np
import os
from PIL import Image


def resize_image(input_path, output_path, new_width=70, new_height=70):
    try:
        # 打开图片
        with Image.open(input_path) as image:
            # 调整图片大小
            resized_image = image.resize((new_width, new_height), Image.LANCZOS)
            # 保存调整后的图片
            resized_image.save(output_path, 'PNG')
        print(f"图片已成功调整大小并保存到 {output_path}")
    except Exception as e:
        print(f"处理图片时出现错误: {e}")


# 设定梯度大小
min_val = 100
max_val = 400
# sizeList = np.linspace(min_val, max_val, 11, dtype=int).tolist()
sizeList = [100, 130, 160, 190, 240, 250, 260, 270, 280, 290, 300]
# 输入图片路径
input_image_folder = 'dantaImgs_raw'
# 输出图片路径
output_image_folder = 'dantaImgs_conv'
# 调用函数进行图片调整
# files = os.listdir(input_image_folder)
files = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png']
for i, f in enumerate(files):
    input_image_path = os.path.join(input_image_folder, f)
    output_image_path = os.path.join(output_image_folder, f)
    resize_image(input_image_path, output_image_path, new_width=sizeList[i], new_height=sizeList[i])
