import os
import sys

label_path = "test/labels"
label_files = os.listdir(label_path)
# print(label_files)

# ROOT_PATH = sys.path[0]  # 项目根目录


def txt2list(filepath):
    f = open(filepath, "r")
    contents = f.readlines()
    f.close()
    # contents = [f"{line.strip()}" for line in contents]

    return contents


def label2txt(filepath, contents):
    f = open(filepath, "w")
    f.writelines(contents)
    f.close()
    print(f"{filepath} 保存成功！")


label_list = []
label_cls_yolo_list = []
for i in label_files:
    label_cls_yolo_list = txt2list(f"{label_path}/{i}")
    tmp_list = [f"{i} {j}" for j in label_cls_yolo_list]
    label_list += tmp_list


# print(label_list)
out_path = "out.txt"
label2txt(out_path, label_list)
label_cls_index_list = [i.split(" ")[1] for i in label_list]
print(label_cls_index_list)
