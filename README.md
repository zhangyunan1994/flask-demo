# flask-demo

## 介绍

本项目为 Flask 示例项目，旨在试验各种可能的情况，并不保证代码为最新的写法，
同时部分前端页面采用了比较老的写法 jQuery + Bootstrap 写法，主要为了复现
15 年的写法，同时降低点理解难度

### 软件架构

```
├── README.md
├── app.py              启动入口
├── conf                一些配置项
│   └── app.ini         配置
├── config.py
├── docs                一些项目文档
│   └── schema.sql
├── exts
│   └── exts.py
├── models              一些数据库实体模型
│   └── models.py
├── requirements.txt    必要的依赖描述
├── static              页面静态资源
│   ├── css
│   │   └── bootstrap.min.css
│   ├── fonts
│   │   ├── glyphicons-halflings-regular.eot
│   │   ├── glyphicons-halflings-regular.svg
│   │   ├── glyphicons-halflings-regular.ttf
│   │   ├── glyphicons-halflings-regular.woff
│   │   └── glyphicons-halflings-regular.woff2
│   └── js
│       ├── bootstrap.min.js
│       └── jquery.min.js
├── templates            页面模板
│   ├── app
│   │   ├── index.html
│   │   ├── layout.html
│   │   └── user
│   │       └── index.html
│   ├── index.html
│   └── login.html
└── views                一些 view
    └── user_manager.py
```


### 安装教程

**1. Python 环境**

开发用的 Python 3.9, 其实 3.6+ 应该就没有问题
   
请根据 `requirements.txt` 自行安装依赖
    
```pip install -r requirements.txt -i "https://pypi.doubanio.com/simple/"```


### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

### 参与贡献

1.  新建 feature_xxx 分支
1.  提交代码
1.  新建 Pull Request
