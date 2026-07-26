---
title: YYKit — iOS 工具代码库
source: ibireme (郭曜源)
source_key: ibireme
source_url: 'https://blog.ibireme.com/2013/09/09/yykit/'
original_language: zh
published: 2013-09-09
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8ee65b5a90ff3620'
translated: n/a
---

> 原文：[YYKit — iOS 工具代码库](https://blog.ibireme.com/2013/09/09/yykit/)　·　ibireme (郭曜源)

注意：这篇文章已经过期。

代码在:[Github](https://github.com/ibireme/YYKit), 文档在:[YYKit](http://github.ibireme.com/yykit/doc/).

做开发有时需要一些常见的功能，通常随手写一个工具类或是Category就扔到工程里了。次数多了总是想整理出一份常用的代码库。本着“如果有别人洗好的类裤那就直接拿来用”的原则，我还是首先到Github转了一转。[sstoolkit](https://github.com/soffes/sstoolkit)无疑是和我的想法最接近的了，但是既然是别人的内裤(雾)，穿着总是不太舒服，又闲fork太麻烦，所以到底还是自己搞了一套。

我希望尽量提供和iOS系统风格类似的API，所以代码尽量加到了Category里面并且没有prefix保护。这样，如果把YYKit.framework放到pch文件里面，代码中的方法配色就会变得和系统API一样～～ 坏处就是Category太多了，会占用内存、影响启动速度的（虽然是微乎其微）。 另外不加prefix的话，有可能和系统或者其他第三方库中的同名方法冲突，造成不确定性。。

目前放进去的功能大概有下面这些：

NSObject：添加了一些任意数量的performSelector方法，包装了一些运行时方法。

NSData：添加了常见的Hash算法(md5、sha、hmac、crc32)，AES加解密，hex、base64编码/解码，gzip/zlib压缩解压的方法。

NSString：添加了常见的Hash算法(md5、sha、hmac、crc32)，一些常见的encode/decode方法等等。

NSArray、NSDictionary、NSDate、NSNumber：添加了一些本来就应该出现的方法～

UIColor：添加了常见的HSL、HSB、CMYK、HEX之间的转换方法，UIColor的一些创建方法。

UIImage：几个常见的功能。。

UIControl：添加了block支持等。

UIView：添加了截图功能，添加了几个常用的属性。

UIScrollView：添加了滚动到上/下/左/右的方法。

UIDevice：添加了判断设备类型、取MAC/IP/内存、判断是否越狱等方法。

UIApplication：添加了常用文件夹访问方法，判断App是否被破解的方法。

。。。。。。

以后再一点点加吧～～

所有的类和方法都有加详细文档，并且可以用appledoc生成和安装。

关于如何创建一个静态库，稍后再单独写吧~

P.S.

YY是我名字的缩写。。
