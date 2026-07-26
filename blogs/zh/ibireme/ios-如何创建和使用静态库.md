---
title: iOS 如何创建和使用静态库
source: ibireme (郭曜源)
source_key: ibireme
source_url: 'https://blog.ibireme.com/2013/09/18/create-ios-static-framework/'
original_language: zh
published: 2013-09-18
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f5238762b00a86c1'
translated: n/a
---

> 原文：[iOS 如何创建和使用静态库](https://blog.ibireme.com/2013/09/18/create-ios-static-framework/)　·　ibireme (郭曜源)

iOS里可以用静态链接库和动态链接库，但由于Appstore的政策限制，上架应用只能用苹果提供的动态链接库，第三方的库只能做成静态库。这里介绍一下静态链接库的创建方法和常见的一些问题。

1. 最常见的方法就是Xcode自带的模板”Cocoa Touch Static Library”。这个很好理解，苹果自己有一个[简单的教程](https://developer.apple.com/library/ios/technotes/iOSStaticLibraries/Articles/creating.html)，网上也有[大把的说明](https://www.google.com.hk/?q=iOS+static+library#q=iOS+static+library)。最终的结果就是一个.a文件和一堆.h头文件。用起来也相对简单：把头文件导入，关联.a静态库，就可以编译了。

下面是一些示例：[新浪微博SDK](http://open.weibo.com/wiki/SDK#iOS_SDK)，[微信SDK](http://open.weixin.qq.com/document/gettingstart/ios/?lang=zh_CN)。

2.通过一些方法，将静态库打包成.framework，虽然是静态库，但使用表现上比较接近系统的动态库。目前来看这种方法比第1种好一些，所以推荐用这种方法。手动创建一个静态.framework是非常繁琐的一件事情，详细的过程可以看[这里](https://github.com/jverkoey/iOS-Framework#how-to-create-a-static-framework-for-ios)或者[这里](http://blog.csdn.net/fengsh998/article/details/8290687)(中文)。懒人们可以用这个已经做好的模板：[iOS-Universal-Framework](https://github.com/kstenerud/iOS-Universal-Framework)。制作好后，用起来也就非常简单了，把.framework拖到工程里面就好。

下面是一些示例：[百度分享SDK](http://developer.baidu.com/wiki/index.php?title=docs/social/sdk)，[人人网SDK](http://wiki.dev.renren.com/wiki/V2/sdk/objectivec_sdk)。

### 常见问题：

1.制作出的静态库只能用在真机，不能用在模拟器，或者相反。

这时就需要把不同的代码（armv7/armv7s/i386…）的代码合并为通用的静态库。如果用上面的iOS-Universal-Framework，它会自动用脚本帮你完成。

为了在build时创建支持多架构的代码，可以这样设置：在Xcode里面的Build Setting -\> Valid Architectures 里面，添加 armv7 armv7s arm64 i386 x86_64这几个类型； Build Setting -\> Build Active Architecture Only 选项设置为NO。

构建完成后，可以运行命令 lipo -info \<FILE\> 来查看静态库实际包含的架构，正常情况下，会显示类似这样的提示： Architectures in the fat file: \<FILE\> are: armv7 armv7s arm64 i386 x86_64。

(2014-09-11 update: 传言，从这天起提交AppStore的应用必须包含64位架构，所以提供SDK的人最好要确保库中包含arm64架构)

2.静态库里有Category方法，但是调用时报错“unrecognized selector send to instance.”等。

这个算是一个官方的已知bug，详情见[苹果文档](https://developer.apple.com/library/mac/qa/qa1490/_index.html)。简单点说，如果你写了一个静态库并且里面有Category，那你就需要让使用者在他们工程的编译参数”`Other Linker Flags`“里面添加 “`-ObjC` “选项。

另外，如果你写了一个.m文件，并且里面只有一个Category，这时就需要使用者添加”-all_load”来加载全部资源，或者添加”-force_load xxx”来强制加载你的库的资源。如果这么做会非常影响速度，为了修复这个问题，通常的解决办法是在这个.m文件里写一个空的Class来占位。下面是一个宏定义：

```
// Use dummy class for category in static library.
#ifndef DUMMY_CLASS
#define DUMMY_CLASS(name) \
    @interface DUMMY_CLASS_ ## name : NSObject @end \
    @implementation DUMMY_CLASS_ ## name @end
#endif

//使用示例:
//UIColor+YYAdd.m
#import "UIColor+YYAdd.h"
DUMMY_CLASS(UIColor+YYAdd)

@implementation UIColor(YYAdd)
...
@end
```

3.添加了静态库后，编译报错”有重复定义的符号(duplicate symbol )”。

这通常是静态库中的某些定义和使用者的工程有冲突。由于ObjC没有命名空间或者包管理这样的东西，所以静态库的开发者一定要把静态库中的东西全部加上Prefix来做保护。例如，某个SDK用到了[JSONKit](https://github.com/johnezang/JSONKit)，那就尽量把JSONKit里面的声明都加上前缀，例如XXXJSONDecoder。

如果你是在用到别人制作的库时遇到这个问题，并且那人没有提供源码，赶紧去联系那人让他改！！ 我所知度厂鹅厂啊，从网什么的都干过这事儿(尤其是鹅厂SDK)。。

其他注意事项：发布静态库时要注意选项”Release/Debug”。如果修改了静态库，但代码不起作用，一定要清除各种缓存和关联。
