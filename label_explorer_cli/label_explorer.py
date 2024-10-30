# Label Explorer
# 创建人：曾逸夫 邓乙华
# 创建时间：2024-01-30


import os
import shutil
import time

import click
from rich.console import Console

from .label_cls_parse import dict_stat, peer_cls_ratio
from .utils.time_format import time_format

console = Console()

YOLOv8_DIR = ["datasets", "images", "labels", "train", "val"]
image_train_dir = f"{YOLOv8_DIR[0]}/{YOLOv8_DIR[1]}/{YOLOv8_DIR[3]}"
image_val_dir = f"{YOLOv8_DIR[0]}/{YOLOv8_DIR[1]}/{YOLOv8_DIR[4]}"
label_train_dir = f"{YOLOv8_DIR[0]}/{YOLOv8_DIR[2]}/{YOLOv8_DIR[3]}"
label_val_dir = f"{YOLOv8_DIR[0]}/{YOLOv8_DIR[2]}/{YOLOv8_DIR[4]}"

CLS_TRAIN_DICT = {}
CLS_VAL_DICT = {}


# 目录检查
def is_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"{dir_name}目录不存在，创建完成")
    else:
        print(f"{dir_name}目录已存在")


# yolov8目录检查
def is_yolov8_dir(dir_name, mk_new=True):
    if os.path.exists(dir_name) and mk_new:
        shutil.rmtree(dir_name)  # 删除所有目录
    os.makedirs(dir_name)
    print(f"{dir_name} 创建完成")


# 构建YOLOv8训练数据集框架
def build_YOLOv8_dir():
    is_yolov8_dir(YOLOv8_DIR[0])

    is_yolov8_dir(f"{YOLOv8_DIR[0]}/{YOLOv8_DIR[1]}")  # datasets/images
    is_yolov8_dir(f"{YOLOv8_DIR[0]}/{YOLOv8_DIR[2]}")  # datasets/labels

    is_yolov8_dir(
        f"{YOLOv8_DIR[0]}/{YOLOv8_DIR[1]}/{YOLOv8_DIR[3]}"
    )  # datasets/images/train
    is_yolov8_dir(
        f"{YOLOv8_DIR[0]}/{YOLOv8_DIR[1]}/{YOLOv8_DIR[4]}"
    )  # datasets/images/val

    is_yolov8_dir(
        f"{YOLOv8_DIR[0]}/{YOLOv8_DIR[2]}/{YOLOv8_DIR[3]}"
    )  # datasets/labels/train
    is_yolov8_dir(
        f"{YOLOv8_DIR[0]}/{YOLOv8_DIR[2]}/{YOLOv8_DIR[4]}"
    )  # datasets/labels/val

    print("---------------------- YOLOv8数据集框架构建完成 ----------------------")


# 复制对应的图片及标签
def copy_images_label(source_image_dir, source_label_dir, prob):
    # 记录已经复制训练集和验证集的图片数量
    cp_imgs_train = 0
    cp_imgs_val = 0

    # 遍历图片目录中的文件
    src_imgs_names = os.listdir(source_image_dir)
    file_image_count = len(src_imgs_names)  # 图片文件总数

    # 设置训练集图片数量
    target_image_count = int(file_image_count * prob)

    # 复制图片到训练集目录
    for filename in src_imgs_names:
        # 获取图片的名称，不带后缀
        image_label_filename = filename.split(".")[0]

        # 构造对应的标签文件路径
        label_filename = f"{source_label_dir}/{image_label_filename}.txt"

        # 如果存在相同名称的，则复制对应标签到训练集
        if os.path.exists(label_filename):
            if cp_imgs_train < target_image_count:
                shutil.copy(
                    f"{source_image_dir}/{filename}", image_train_dir
                )  # 图片复制
                shutil.copy(label_filename, label_train_dir)  # 标签复制
                cp_imgs_train += 1  # 训练集计数

                print(
                    f"{filename} 完成复制 {round(cp_imgs_train*100/file_image_count, 2)}%"
                )

            else:
                # 将剩下的图片复制到验证集
                shutil.copy(
                    os.path.join(source_image_dir, filename), image_val_dir
                )  # 图片复制
                shutil.copy(label_filename, label_val_dir)  # 标签复制
                cp_imgs_val += 1  # 训练集计数

                print(
                    f"{filename} 完成复制 {round((cp_imgs_val+cp_imgs_train)*100/(file_image_count), 2)}%"
                )

        else:
            print(f"{label_filename} 不存在，程序结束！")
            break

    print("---------------------- YOLOv8数据集创建完成 ----------------------")
    print("对应图片和标签复制成功！")
    print(f"训练集：{cp_imgs_train} | 验证集：{file_image_count - cp_imgs_train}")


@click.command()
@click.option(
    "--src_label_dir",
    "-sld",
    default="raw_datasets/labels",
    type=str,
    help="source label directory",
)
@click.option(
    "--src_img_dir",
    "-sid",
    default="raw_datasets/images",
    type=str,
    help="source images directory",
)
@click.option("--prob", "-p", default=0.8, type=float, help="parse prob")
@click.option(
    "--label_path",
    "-lp",
    default="raw_datasets/classes.txt",
    type=str,
    help="parse prob",
)
def entrypoint(src_label_dir, src_img_dir, label_path, prob):
    s_time = time.time()
    # ----------- 构建YOLOv8数据集架构 -----------
    build_YOLOv8_dir()

    # ----------- 完成复制 -----------
    copy_images_label(src_img_dir, src_label_dir, prob)

    # ----------- 统计实例个数 -----------
    cls_train_dict = dict_stat(label_train_dir, label_path)
    cls_val_dict = dict_stat(label_val_dir, label_path)
    print(f"训练集：{cls_train_dict}")
    print(f"验证集：{cls_val_dict}")

    # ----------- 计算实例比例 -----------
    cls_train_ratio, cls_val_ratio = peer_cls_ratio(cls_train_dict, cls_val_dict)
    print(f"当前参数比例为 {prob*10}:{10-prob*10}")
    print(f"训练集比例：{cls_train_ratio}")
    print(f"验证集比例：{cls_val_ratio}")

    e_time = time.time()  # 终止时间
    total_time = e_time - s_time  # 程序用时
    # 格式化时间格式，便于观察
    outTimeMsg = f"[bold blue]用时：[/bold blue]{time_format(total_time)}"
    console.print(outTimeMsg)  # 打印用时
