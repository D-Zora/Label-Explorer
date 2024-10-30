# 解析 Label Studio文件


def txt2list(filepath):
    f = open(filepath, "r")
    contents = f.readlines()
    f.close()
    contents = [f"{line.strip()}" for line in contents]

    return contents


def list2dict(label_path):
    cls_list = txt2list(label_path)

    cls_dict = {}

    for i in cls_list:
        cls_dict[i] = 0

    return cls_dict


if __name__ == "__main__":
    cls_dict = {}
    label_path = "./test/classes.txt"

    cls_dict = list2dict(label_path)
    print(cls_dict)
    print(list(cls_dict.keys()))
