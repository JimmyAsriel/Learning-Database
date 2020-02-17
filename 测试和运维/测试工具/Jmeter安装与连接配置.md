#### Apache JMeter安装说明 

------

安装环境要求： JMeter要求充分满足JVM1.3或更高。 

操作系统 :JMeter可以在当前任何一个已经部署了JDK的操作系统上运行。

#### 安装过程

------

##### JDK安装 

点击安装包，选择默认安装路径即可。 （注意要将路径记录下来，接下来的环境配置要用到）

##### JDK环境配置 

* 桌面上右键选择“我的电脑”/属性/高级系统设置/环境变量, 在“系统变量”栏中点击“新建”, 在变量名中输入:CLASSPATH，变量值中输入：C:\JDK安装目录\lib\dt.JAR; C:\JDK安装目录\lib\TOOLS.JAR;点击确定即可。 

* 按“新建”，在变量名中输入:java_home，变量中输入:C:\JDK安装目录；

* 修改系统变量path的值，在前面增加%java_home%\bin;然后确定即可。 

##### Jmeter安装 

* 解压jakarta-jmeter-2.3.4文件至c盘，C:\jmeter-2.3.4目录下。 

* 桌面上右键选择“我的电脑”/属性/高级系统设置/环境变量, 在“系统变量”栏中点击“新建”, 在变量名中输入：JMETER_HOME，变量值中输入：C:\ jmeter-2.3.4，点击确定即可。 

* 修改CLASSPATH变量，变量值中添加如下值： 

%JMETER_HOME%\lib\ext\ApacheJMeter_core.jar;

%JMETER_HOME%\lib\jorphan.jar;

%JMETER_HOME%\lib\logkit-1.2.jar; 然后确定即可。 

##### 启动Jmeter

* 进入jmeter目录下的bin文件夹，点击jmeter.bat，查看页面显示，如果能显示jmeter操作页面则安装成功。
* 进入jmeter目录下的bin文件夹 ,  点击ApacheJMeter，若成功显示jmeter操作界面则安装成功。

#### JMeter连接Oracle数据库

------

Jmeter的本身是纯Java开发，对Oracle数据库的连接需要Oracle自带的连接库。这意味着需要一份来自本机或者服务器主机上的Jar包文件用于配置Jmeter.

* 复制ORACLE的JDBC驱动Jar包文件

```
E:\oracle\product\10.2.0\client_1\jdbc\lib\ojdbc14.jar
```

到 JMeter 的lib目录下

```
C:\jmeter-2.3.4\lib
```

##### 连接到数据库服务器

* 左侧默认测试计划的控制面板右下角手动添加ojdbc14.jar添加到classpath

* 建立线程组：右键测试计划->添加->Threads->线程组
* 建立JDBC Connection Configuration：右击线程组->添加->配置原件->JDBC Connection Configuration
* 在Database Connection Configuration控制面板中的Virable Name Bound to Pool栏的Variable Name项填写Oracle数据库的数据库实例名称，例如Oracle安装时自带的数据库。例：orcl
  * 输入数据库配置信息
    * Validation Query：Select 1 from dual
    * Database URL: jdbc:oracle:thin:@192.168.1.100:1521:orcl
    * JDBC Driver class: oracle.jdbc.driver.OracleDriver
    * Username: scott
    * Password:scott

* 建立JDBC Request：
  * 右击线程组->添加->Sampler->JDBC Request
  * Variable Name：和上面的JDBC Connection Configuration填写同样的内容：orcl
  * SQL Query：输入SQL语句来进行测试（这里选用最基础的查询操作）
    * 注意：这里的SQL语句后不能加“；”，否则会报错
  * 添加监听器：右键线程组，选择添加,  监听器  ,  建议添加以下四种（如果想添加其他也可以，自由搭配）

  * 点击保存，选择默认路径保存即可

  * 通过更改JDBC Connection Configuration中的数值来测试不同压力下数据库的反应

  * 点击绿色三角运行

  * 通过刚才的监听器查看测试结果

#### Troubleshooting

------

1. Validation Query：Select 1 from dual 该项必须填写此命令
2. ORA12705错误：如果被测试数据库在本机，该错误往往出现在多次安装Oracle数据库后注册表没有删除相应字段，仅仅是将其置空，故需要删除多余字段或者将对应字段重新置为中文环境。如果测试机器为网络环境，注意Jmeter自身启动环境的字符应该和Oracle数据库相对应，例如都为中文。



