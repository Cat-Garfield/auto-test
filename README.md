# auto-test

## 简述
基于pytest和allure的自动化测试框架，可通过yaml文件驱动测试

## 目录结构说明
* common 公共的方法封装
* conf 项目的配置文件，区别于pytest配置
* data 存放测试数据
* logs 存放日志
* plugin 存放插件
* reports 生成的报告位置
* testcase 测试用用例
  * conftest.py 定义全局夹具
* pytest.ini pytest框架的配置文件
* run.py 项目启动文件

## 使用说明
### 环境准备
1. 安装**python3.10**
2. 安装依赖包 ``` pip install -r requirement.txt```
3. 安装java环境，版本为**JDK20**
4. 添加jdk环境变量
5. 解压**allure-2.23.1**安装包至plugin目录下
6. 添加allure环境变量
### 启动说明，具体参数查看run.py文件
1. 命令行运行  
```pytest -v``` 
2. 调试运行  
```pytest.main(["-v"])```    

## Q&A


## todo-list
1. 搭配jenkins使用
2. 实时日志收集和分析平台