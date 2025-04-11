import shutil
import os


def copy_files(source_folder, destination_folder):
    try:
        # 检查源文件夹是否存在
        if not os.path.exists(source_folder):
            print(f"源文件夹 {source_folder} 不存在。")
            return
        # 检查目标文件夹是否存在，如果不存在则创建
        if not os.path.exists(destination_folder):
            raise FileNotFoundError()
        # 遍历源文件夹中的所有文件和文件夹
        for root, dirs, files in os.walk(source_folder):
            # 计算相对于源文件夹的相对路径
            relative_path = os.path.relpath(root, source_folder)
            # 构建目标文件夹中的对应路径
            target_folder = os.path.join(destination_folder, relative_path)
            # 如果目标文件夹不存在，则创建
            if not os.path.exists(target_folder):
                raise FileNotFoundError()
            # 遍历当前文件夹中的所有文件
            for file in files:
                # 构建源文件的完整路径
                source_file = os.path.join(root, file)
                # 构建目标文件的完整路径
                target_file = os.path.join(target_folder, file)
                # 复制文件
                shutil.copy2(source_file, target_file)
                print(f"已复制文件: {source_file}\t到 {target_file}")
        print("文件复制完成。")
    except Exception as e:
        print(f"复制文件时出现错误: {e}")


# 源文件夹路径
input_image_folder = 'dantaImgs_conv'
# 目标文件夹路径
output_image_folder = 'assets/Imgs/fruit'
# 调用函数进行文件复制
files = os.listdir(input_image_folder)
copy_files(input_image_folder, output_image_folder)
