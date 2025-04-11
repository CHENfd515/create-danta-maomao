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


# from
# bgRaw = "dantaImgs_bg/background.png"
bgRaw = "dantaImgs_bg/background_v1.png"
# to
bgOrg = "assets/Imgs/background.png"
bgReshape = bgOrg
# resize
resize_image(bgRaw, bgReshape, 720, 1280)
