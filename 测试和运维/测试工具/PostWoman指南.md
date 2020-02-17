Postwoman是一个Postman的免费、快速且美观的替代方案

**GitHub项目官网：**

```
https://github.com/liyasthomas/postwoman
```

### 相关特性

Postwoman是基于NodeJs编写的，主要特点除了可以支持主流的Restful接口调试之外，还支持 GraphQL和 WebSocket。

作为一款开源的 Postman 替代品，主打特性有如下一些：

- 轻盈，可直接在线访问；
- 简约，采用简约的 UI 设计精心打造；
- 支持 GET, HEAD, POST, PUT, DELETE, OPTIONS, PATCH 方法；
- 支持验证；
- 实时，发送请求即可获取响应。

除了这些，还可自定义背景，前景色和强调色组合。

 

**1、自定义选项：**

- 选择主题：Kinda Dark（默认），Clearly White，Just Black和System主题
- 选择强调颜色：绿色（默认），黄色，粉红色，红色，紫色，橙色，青色和蓝色

 

**2、PWA：**

可以通过PWA的方式安装。

PS: PWA全称Progressive Web App，即渐进式WEB应用。

**特性：**

- 与Service Workers同时加载
- 离线支持
- 低RAM /内存和CPU使用率
- 添加到主屏幕（页脚中的按钮）
- 桌面PWA支持（页脚中的按钮）

**3、WebSocket：**

通过单个TCP连接建立全双工通信通道。发送和接收数据

#### 启动运行与定制开发

------

Postwoman是一个基于Vue构建的Web项目，且可以构建成PWA应用，下述提供三种本地开发运行方式。

**方式一：npm本地构建运行：**

```
git clone https://github.com/liyasthomas/postwoman.git
npm install
npm run dev
```

#### 方式二：docker-compose （需要本地先安装docerk-compose）:

```
git clone https://github.com/liyasthomas/postwoman.git
docker-compose up
```

#### 方式三：docker (需要本地先安装docker环境):

```
#pull
docker pull liyasthomas/postwoman
#run
docker run -p 3000:3000 liyasthomas/postwoman:latest
#build
docker build -t postwoman:latest
```

三种方式，任一一种，本地运行成功后，打开浏览器，访问`http://localhost:3000` 即可。以方式一为例，通过`npm run dev`本地运行