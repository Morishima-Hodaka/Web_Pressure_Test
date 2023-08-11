# Web_Pressure_test


### install.bat(安装自动化)

```bat
rem 关闭命令行窗口中的命令回显
@echo off
echo 作者:浩
echo github https://github.com/Morishima-Hodaka/Web_Pressure_Test
rem 65001 是Windows操作系统中的一种代码页（Code Page），它对应于UTF-8编码
rem chcp是Windows命令行中用于显示或更改当前代码页的命令
chcp 65001 > nul

rem 标题
title 自动安装 


echo 请选择一个选项：
echo 1.默认源
echo 2.阿里云
echo 3.清华大学
set /p choice=请输入选项的数字：
if "%choice%"=="1" (
    echo 默认源
	set source="https://pypi.org/simple/"
) else if "%choice%"=="2" (
    echo 阿里云
	set source="http://mirrors.aliyun.com/pypi/simple/"
	
) else if "%choice%"=="3" (
    echo 清华大学
	set source="https://pypi.tuna.tsinghua.edu.cn/simple/"
) else (
    echo 无效的选项
)



:Installation

rem 升级
python -m pip install --upgrade pip

rem 安装
pip install -r requirements.txt -i %source%

pause
```
