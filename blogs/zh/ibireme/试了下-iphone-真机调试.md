---
title: 试了下 iPhone 真机调试~
source: ibireme (郭曜源)
source_key: ibireme
source_url: 'https://blog.ibireme.com/2010/09/30/try_iphone_dev/'
original_language: zh
published: 2010-09-30
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:59450cd86480f271'
translated: n/a
---

> 原文：[试了下 iPhone 真机调试~](https://blog.ibireme.com/2010/09/30/try_iphone_dev/)　·　ibireme (郭曜源)

今天突然想试着学学开发iPhone程序，当然首先要能把编译好的程序放到机子里(我只有一个iTouch3)

上网搜了一通终于弄明白了。。我可没有99美元去注册个开发者账号~咱自己玩玩就好啦~

我的环境是PC+Mac OS X 10.6.3+iPhoneSDK 3.2.2

先按照[这里](http://www.weiphone.com/thread-222380-1-1.html)的教程做好自己的证书（主要就是用钥匙串管理程序创建证书，在最后一步要用“登录”选项保存）

然后再终端中执行以下代码以破解Xcode的证书限制 …

#!/bin/bash   
cd/Developer/Platforms/iPhoneOS.platform/Developer/Library/Xcode/Plug-ins/iPhoneOSBuild System Support.xcplugin/Contents/MacOS/   
dd if=iPhoneOS Build System Support of=working bs=500 count=255   
printf “x8fx2ax00x00” \>\> working   
dd if=iPhoneOS Build System Support of=working bs=1 skip=127504 seek=127504   
/bin/mv -n iPhoneOS Build System Support iPhoneOS Build System Support.original   
/bin/mv working iPhoneOS Build System Support   
chmod a+x iPhoneOS Build System Support

再在终端里执行下面的代码

_（实际作用就是联网下载[gen_entitlements.txt](http://www.alexwhittemore.com/iphone/gen_entitlements.txt) 并改扩展名为py并放到_

_/Developer/iphoneentitlements30文件夹内，改权限为777__）_

mkdir /Developer/iphoneentitlements30   
cd /Developer/iphoneentitlements30   
curl -O [http://www.alexwhittemore.com/iphone/gen_entitlements.txt](http://www.alexwhittemore.com/iphone/gen_entitlements.txt)   
mv gen_entitlements.txt gen_entitlements.py   
chmod 777 gen_entitlements.py

然后修改”/Developer/Platforms/iPhoneOS.platform/Info.plist”文件，添加：

PROVISIONING_PROFILE_ALLOWED = NO

PROVISIONING_PROFILE_REQUIRED = NO

下面就是修改编好的程序：

在project的info.list里面增加一行：

SignerIdentity=iPhone Developer

把iPhone或iTouch连接到电脑,提示连接成功后

在xcode菜单,window-\>Organizer里面,把iphone设为调试设备. 之后就可以选择iPhone Device模式build & run了。

===========================================

我的iTouch版本号是4.0,这个版本的Xcode不能识别，只能用软件把编译完的程序传到/Applications文件夹里，然后改下权限就能运行啦~

看看我以后还有兴趣的话就继续学一下了~谁知道呢。。。
