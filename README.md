# Label Explorer

#### 介绍

🚀 基于 Electron 的 YOLO 标签分析与整合工具

<p>
<a href="https://pypi.org/project/label-explorer"><img src="https://static.pepy.tech/personalized-badge/label-explorer?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads" alt="PyPI All Downloads"></a>
<a href="https://snyk.io/advisor/python/label-explorer"><img src="https://snyk.io/advisor/python/label-explorer/badge.svg" alt="PyPI Package Health"></a>
</p>

### 作者简介

#### 👨‍🏫 导师

曾逸夫，从事人工智能研究与开发；主研领域：计算机视觉；[YOLOv8官方开源项目代码贡献人](https://github.com/ultralytics/ultralytics/graphs/contributors)；[YOLOv5官方开源项目代码贡献人](https://github.com/ultralytics/yolov5/graphs/contributors)；[YOLOv5 v6.1代码贡献人](https://github.com/ultralytics/yolov5/releases/tag/v6.1)；[YOLOv5 v6.2代码贡献人](https://github.com/ultralytics/yolov5/releases/tag/v6.2)；[YOLOv5 v7.0代码贡献人](https://github.com/ultralytics/yolov5/releases/tag/v7.0)；[Gradio官方开源项目代码贡献人](https://github.com/gradio-app/gradio/graphs/contributors)

✨  Github：https://github.com/Zengyf-CVer

#### 👩‍🎓 学生

邓乙华，从事计算机视觉的研究和 JavaScript 项目的开发。

### Label Studio

https://github.com/HumanSignal/label-studio

对Label Studio导出的格式进行转换

#### Label Studio YOLO格式

```shell
├── raw_datasets							# 原始数据集
│   ├── images								# 图片集
│   │   ├── 1.jpg							# 图片名称
│   │   ├── 2.jpg							# 图片名称
│   ├── labels								# 标签集
│   │   ├── 1.txt							# 标签名称
│   │   ├── 2.txt							# 标签名称
│   ├── classes.txt							# 类别文件
│   ├── notes.json							# 类别JSON文件
```

##### raw_datasets/classes.txt

```shell
cls01
cls02
cls03
cls04
```

##### raw_datasets/notes.json

```json
{
  "categories": [
    {
      "id": 0,
      "name": "cls01"
    },
    {
      "id": 1,
      "name": "cls02"
    },
    {
      "id": 2,
      "name": "cls03"
    },
    {
      "id": 3,
      "name": "cls04"
    }
  ],
  "info": {
    "year": 2024,
    "version": "1.0",
    "contributor": "Label Studio"
  }
}
```

```shell
yarn add electron --dev
```

### 安装教程

```shell
# Electron版
yarn install
yarn run start

# Python CLI版
pip install label-explorer
```

### 使用教程

#### Python CLI

```shell
# 使用默认参数
label-explorer

# 自定义图片路径和标签路径
label-explorer -sld path/to/labels -sid path/to/imgs

# 自定义训练集和验证集比例
label-explorer -p 0.9
label-explorer -p 0.7
label-explorer -p 0.75

# 导入Label Studio类别文件
label-explorer -lp path/to/classes.txt
```
