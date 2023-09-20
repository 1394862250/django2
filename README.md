基于django的简单博客
==============================

## 功能
- [x] 用户注册/登录/登出
- [ ] 用户修改密码（目前只能通过管理员修改）
- [x] 创建、修改、删除文章
- [x] 创建、修改、删除评论（修改和删除只能管理员操作）
- [x] 分类和子分类
- [x] 后台管理

## 已知问题

* 首先：别的大佬的项目，还在修改学习中
* 2：管理系统不能上传文章呢，学习一阵子我给写写把
* 3：前端界面美化稍等等吧
* 4：logo不能更改中
## 依赖

使用用poetry安装依赖
```bash
pip install pipx
pipx install poetry
poetry install
```

## 运行
首次运行需要初始化数据库和静态文件!!!
首次运行需要初始化数据库和静态文件!!!
首次运行需要初始化数据库和静态文件!!!
很重要！
```bash
pip install pymysql
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

然后在cmd运行
```bash
python manage.py runserver
```

联系我一起学习的话：    先发邮件到我邮箱：    1394862250@qq.com

# django2
