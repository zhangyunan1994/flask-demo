# flask-demo

## 其他可选方案

1. fastapi
2. django

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

**2. 初始化数据库**

数据库使用的 MySQL, 初始化语句在 `docs/schema.sql` 里，如果要修改用户名密码，可以修改 `conf/app.ini` 文件

### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

### 参与贡献

1.  新建 feature_xxx 分支
1.  提交代码
1.  新建 Pull Request

## 教程

1. [Git 基础](https://www.liaoxuefeng.com/wiki/896043488029600)
1. [Python 基础](https://www.liaoxuefeng.com/wiki/1016959663602400)
1. [简单的 MySQL 基础](https://www.liaoxuefeng.com/wiki/1177760294764384)
1. [Flask 入门](http://www.pythondoc.com/flask/)
1. [Flask-SQLAlchemy 快速入门](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)
1. [Bootstrap 参考](https://v3.bootcss.com/)
1. [jQuery 教程](https://www.w3school.com.cn/jquery/index.asp)
1. [Axios 简单使用](https://blog.csdn.net/zyndev/article/details/107215871)

## 常用学习网站

1. [Python 中文学习大本营 (主要是Flask 相关教程) ](http://www.pythondoc.com/)
