# 计算标签类别分布

import os
import sys

from .label_studio_parse import list2dict

YOLOv8_DIR = ["datasets", "images", "labels", "train", "val"]

# 图片、标签的目标路径
label_train_dir = f"{YOLOv8_DIR[0]}/{YOLOv8_DIR[2]}/{YOLOv8_DIR[3]}"
label_val_dir = f"{YOLOv8_DIR[0]}/{YOLOv8_DIR[2]}/{YOLOv8_DIR[4]}"


def txt2list(filepath):
    f = open(filepath, "r")
    contents = f.readlines()
    f.close()
    # contents = [f"{line.strip()}" for line in contents]

    return contents


# 统计每个实例的个数
def dict_stat(label_train_val_path, label_path):
    label_train_val_list = os.listdir(label_train_val_path)

    cls_dict = {}

    cls_dict = list2dict(label_path)
    cls_list = list(cls_dict.keys())

    label_cls_yolo_list = []
    for i in label_train_val_list:
        label_cls_yolo_list = txt2list(f"{label_train_val_path}/{i}")
        # print([j[0] for j in label_cls_yolo_list])
        cls_sub_list = [int(j[0]) for j in label_cls_yolo_list]
        for k in cls_sub_list:
            cls_dict[cls_list[k]] += 1

    return cls_dict


# 计算每个实例的比例
def peer_cls_ratio(cls_train_dict, cls_val_dict):
    cls_all_dict = cls_train_dict.copy()
    cls_train_ratio = {}
    cls_val_ratio = {}

    for k in cls_train_dict.keys():
        if k in cls_val_dict.keys():
            cls_all_dict[k] += cls_val_dict[k]

    for k in cls_all_dict.keys():
        cls_train_ratio[k] = round(cls_train_dict[k] / cls_all_dict[k], 2)
        cls_val_ratio[k] = round(cls_val_dict[k] / cls_all_dict[k], 2)

    return cls_train_ratio, cls_val_ratio


if __name__ == "__main__":
    label_path = "./test/classes.txt"
    cls_train_dict = {}
    cls_val_dict = {}

    cls_train_dict = dict_stat(label_train_dir, label_path)
    cls_val_dict = dict_stat(label_val_dir, label_path)

    print(cls_train_dict)
    print(cls_val_dict)

    cls_train_ratio, cls_val_ratio = peer_cls_ratio(cls_train_dict, cls_val_dict)
    print(cls_train_ratio)
    print(cls_val_ratio)
