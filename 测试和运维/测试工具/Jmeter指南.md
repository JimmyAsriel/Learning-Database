安装

（转）开源java压力测试工具JMeter安装

 

文章分类:Java编程

首先非常感谢：blogjava的小蚂蚁，他的文章给了我很大的帮助，他的文章已经写分非常详细，我这里直接转载过来，然后再对可能引起疑问的地方进行注释。 

转自：http://www.blogjava.net/lijun_li/archive/2009/09/25/296453.ht

 

编写背景： 

 

  昨天把ruby和watir装上了，今天决定把jmeter也装上，这样平常只要有空就可以玩一玩，实践和整理这两方面的技术文档，第一次装jmeter，还是遇到了问题，再次记录方便想学jmeter的同行参考；网上给的安装资料很多，可是没有一个是可以按照所描述的从头到尾安装成功。 

 

一、      Apache JMeter介绍 

 

\1.    Apache JMeter是什么 

 

Apache JMeter 是Apache组织的开放源代码项目，是一个100%纯Java桌面应用，用于压力测试和性能测量。它最初被设计用于Web应用测试但后来扩展到其它测试领域。最新的版本大家可以到http://jakarta.apache.org/site/downloads/downloads_jmeter.cgi下载。 

 

\2.    用它能做什么 

 

Apache JMeter可以用于对静态的和动态的资源（文件，Servlet，Perl脚本，Java对象，数据库和查询，FTP服务器或是其它资源）的性能进行测试。JMeter可以用于在服务器，网络或对象模拟繁重的负载来测试它们提供服务的受压能力或者分析不同压力条件下的总体性能情况。你可以使用JMeter提供的图形化界面，分析性能指标或者在高负载情况下测试你的服务器/脚本/对象。 

 

\3.    Apache JMeter能做什么 

 

?     能够对HTTP和FTP服务器进行压力和性能测试，也可以对任何数据库进行同样的测试（通过JDBC）。 

 

?     完全的可移植性和100%纯Java。 

 

?     完全Swing的轻量级组件支持（预编译的JAR使用 javax.swing.*）包。 

 

?     完全多线程框架允许通过多个线程并发取样和通过单独的线程组对不同的功能同时取样。 

 

?     精心的GUI设计允许快速操作和更精确的计时。 

 

?     缓存和离线分析/回放测试结果。 

 

?     高可扩展性： 

 

1)     可链接的取样器允许无限制的测试能力。 

 

2)     各种负载统计表和可链接的计时器可供选择。 

 

3)     数据分析和可视化插件提供了很好的可扩展性以及个性化。 

 

4)     具有提供动态输入到测试的功能（包括JavaScript）。 

 

5)     支持脚本变成的取样器（在1.9.2及以上版本支持BeanShell）。 

 

 

 

\4.    Apache JMeter的由来 

 

JMeter最早是由Apache软件项目的开发工程师Stefano Mazzocchi 开发出来的。他当初开发JMeter主要用于测试Apache JServ(一个被Apache Tomcat 工程取代了的项目)的性能。之后又再次设计了JMeter，增加了图形化界面和一些功能测试能力。 

 

 

 

\5.    Apache JMeter的未来 

 

随着开发人员借助它的可嵌入的结构，希望看到JMeter的能力也随之快速的被扩大。更进一步的主要发展目标是把JMeter在没有减弱它的负载测试的能力的同时尽可能的做成最有效的回归测试工具。 

 

二、      Apache JMeter安装说明 

 

\1.    安装环境要求： 

 

Java版本 

 

JMeter要求充分满足JVM1.3或更高。 

 

操作系统 

 

JMeter可以在当前任何一个已经部署了Java的操作系统上运行。 

 

l     Unix(Solaris，Linux，etc) 

 

l     Windows(98，NT，2000，XP) 

 

l     Open VMS Alpha 7.3+ 

 

\2.    安装步骤： 

 

l     安装环境：Windows XP 

 

l     安装包准备： 

 

JDK1.5.0_12 具体可在官方网站下载 

 

jakarta-jmeter-2.3.4 具体下载地址： 

 

http://jakarta.apache.org/site/downloads/downloads_jmeter.cgi 

 

l     安装过程： 

 

1）JDK安装 

 

点击下载的jdk-1_5_0_12-windows-i586-p.exe，选择安装路径即可。 

 

2） JDK环境配置 

 

桌面上选择“我的电脑”(右键)/高级/环境变量, 在“系统变量”栏中点击“新建”, 在变量名中输入：CLASSPATH，变量值中输入：C:\JDK安装目录\lib\dt.JAR; C:\JDK安装目录\lib\TOOLS.JAR;点击确定即可。 

 

再按“新建”，在变量名中输入：java_home，变量中输入：C:\JDK安装目录；修改PATH变量，添加% java_home %\bin；然后确定即可。 

 

修改系统变量path的值，在前面增加%java_home%\bin;然后确定即可。 

 

3）检查JDK安装是否OK 

 

具体是：点击“开始”/“运行”，输入命令cmd进入dos操作界面，输入命令：java –version 查看java版本，如果显示为：1.5.0_12，则安装OK 

 

4）Jmeter安装 

 

解压jakarta-jmeter-2.3.4文件至c盘，本文解压至C:\jmeter-2.3.4目录下。 

桌面上选择“我的电脑”(右键)/高级/环境变量, 在“系统变量”栏中点击“新建”, 在变量名中输入：JMETER_HOME，变量值中输入：C:\ jmeter-2.3.4，点击确定即可。 

 

再修改CLASSPATH变量，变量值中添加如下值： 

 

%JMETER_HOME%\lib\ext\ApacheJMeter_core.jar;%JMETER_HOME%\lib\jorphan.jar;%JMETER_HOME%\lib\logkit-1.2.jar; 然后确定即可。 

 

5）检查jmeter安装是否OK 

 

具体是：进入jmeter目录下的bin文件夹，点击jmeter.bat，查看页面显示，如果能显示jmeter操作页面则安装成功。 

 

提醒：通常安装到这一步会报下面这个错误： 

 

unrecognized vm option '+heapdumponoutofmemoryerror' 

 

原因是：安装的JDK版本是：1.5.0的就会出错，把JDK卸载，重新下载JDK1.5.0_12版本或Jdk1.6也可以，重新安装就OK了，之前我就是装的1.5.0版本报的错，后来更新JDK版本就好了。

 

 

 

使用的信息

=====================================================================

1、右键单击测试计划，选择添加-〉线程组

　　在线程组里设置负载信息，即线程属性。我向测试计划中增加相关负载设置是Jmeter需要模拟十个请求者，每个请求者在测试过程中并发请求，并且连续请求10次。

　　线程数： 10

　　Ramp-up period（inseconds）： 0

　　循环次数： 10

　　说明：线程数代表发送请求的用户数目，Ramp-up period（inseconds）代表每个请求发生的总时间间隔，单位是秒。假如我的请求数目是5，而这个参数是10，那么每个请求之间的间隔就是10／5，也就是2秒。如果设置为0就代表并发请求。Loop Count代表请求发生的重复次数，如果选择后面的forever（默认），那么 请求将一直继续，如果不选择forever，而在输入框中输入数字，那么请求将重复 指定的次数，如果输入0，那么请求将执行一次。

　　2、添加HTTP默认请求值

　　右键单击线程组，选择添加-〉配置元件-〉HTTP默认请求值，以下是我设置的信息：

　　说明

　　名称： HTTP 默认请求值 该元素的名称

　　服务器名称或IP：

　　localhost 被测试服务器的 IP或者名字

　　端口号： 8080 服务器提供服务的端口号，我用的服务器是 Tomcat，所以端口号是8080

　　协议： http 发送测试请求时使用的协议

　　路径： /hrbin/hg_admin/khxx_xg.jsp 默认的起始位置。

　　　3、添加HTTP请求

　　右键单击线程组，选择添加-〉Sampler-〉HTTP请求，以下是我设置的信息

　　说明

　　名称： HTTP 默认请求值 该元素的名称

　　服务器名称或IP：

　　localhost 被测试服务器的IP或者名字

　　端口号： 8080 服务器提供服务的端口号，我用的服务器是Tomcat，所以端口号是8080

　　协议： http 发送测试请求时使用的协议

　　路径： /hrbin/hg_admin/khxx_xg.jsp 默认的起始位置。

　　因为我测试的是查询，故添加了一个同请求一起发送的参数（in_id=dsgds）：

　　　4、添加监听器，存放测试结果。

　　右键单击测试计划，选择测试计划-〉添加-〉监听器-〉聚合报告

　　你也可以选择用表格查看结果、图形结果、查看结果树等。

　　4）运行测试

单击运行，选择启动。

 

测试分析

过这个Listener，我们可以看到很详细的每个transaction它所返回的结果，其中红色是指出错的transaction，绿色则为通过的。

如果你测试的场景会有很多的transaction完成，建议在这个Listener中仅记录出错的transaction就可以了。要做到这样，你只需要将Log/Display:中的Errors勾中就可以了。

二、.jtl文件的分析

在性能测试过程中，我们往往需要将测试结果保存在一个文件当中，这样既可以保存测试结果，也可以为日后的性能测试报告提供更多的素材。

Jmeter中，结果都存放在.jtl文件。这个.jtl文件可以提供多种格式的编写，而一般我们都是将其以csv文件格式记录，这样做是因为csv文件格式看起来比较方便，更重要的是这样做可以为二次分析提供很多便利。

我这里所说的二次分析是指除了使用Listener之外，我们还可以对.jtl文件进行再次分析。

a.设置jtl文件格式

我们从jmeter官方网站中下载下来的Jmeter解压后是可以直接使用的。但是，使用默认配置生成的jtl文件内容并不能满足我们的需要。于是 我们必须进行必要的设置。在2.2版本中，如果要修改jtl设置必须要到jmeter.properties文件中设置；但是在2.3版本中，我们只需要 在界面上设置就可以了。你只需要选择某个Listener，点击页面中的configure按钮。此时，一个设置界面就会弹出来，建议多勾选如下 项：Save Field Name，Save Assertion Failure Message。

b.jtl文件中的各项

经过了以上设置，此时保存下来的jtl文件会有如下项：

timeStamp,elapsed,label,responseCode,responseMessage,threadName,dataType,success,failureMessage,bytes,Latency

请求发出的绝对时间，响应时间，请求的标签，返回码，返回消息，请求所属的线程，数据类型，是否成功，失败信息，字节，响应时间

其中聚合报告中的，吞吐量=完成的transaction数/完成这些transaction数所需要的时间；平均响应时间=所有响应时间的总和/完成的transaction数；失败率=失败的个数/transaction数

温馨提示：在jmeter2.2和2.3版本中，都存在的一个问题是当我们重新打开jmeter，使用某个Listener来查看jtl文件 时，jmeter是会报错的。因此当你使用命令行方式完成了一个场景的测试后，你得到的只是一堆保存在jtl文件中的原始数据。所以知道聚合报告中的各项 的来源是可以方便大家摆脱测试工具来进行结果的分析。

 

总的来说，对于jmeter的结果分析，主要就是对jtl文件中原始数据的整理，我是使用一些小脚本进行相关的分析的，不知道你打算怎么做呢？

反正实践后，你总能找到一条属于自己的数据分析之路。

 

 