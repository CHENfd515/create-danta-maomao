import os


def rename_png_images(directory):
    try:
        # 获取指定目录下所有文件
        files = os.listdir(directory)
        # 过滤出所有的 PNG 文件
        png_files = [f for f in files if f.lower().endswith('.png')]
        # 按原文件名排序
        png_files.sort()

        for i, file in enumerate(png_files):
            # 构建原文件的完整路径
            old_path = os.path.join(directory, file)
            # 构建新文件名
            new_name = f"{i}.png"
            # 构建新文件的完整路径
            new_path = os.path.join(directory, new_name)
            # 重命名文件
            os.rename(old_path, new_path)
            print(f"已将 {old_path} 重命名为 {new_path}")
    except Exception as e:
        print(f"处理图片时出现错误: {e}")


# 指定目录路径
directory = 'dantaImgs_raw'
# 调用函数进行图片重命名
rename_png_images(directory)
