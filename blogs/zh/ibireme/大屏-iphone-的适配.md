---
title: 大屏 iPhone 的适配
source: ibireme (郭曜源)
source_key: ibireme
source_url: 'https://blog.ibireme.com/2014/09/16/adapted_to_iphone6/'
original_language: zh
published: 2014-09-16
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:157db1fe484c918c'
translated: n/a
---

> 原文：[大屏 iPhone 的适配](https://blog.ibireme.com/2014/09/16/adapted_to_iphone6/)　·　ibireme (郭曜源)

自从苹果出了大屏 iPhone 后，iOS 开发也要做适配了，想必 Android 程序员正在偷着乐呢 :lol: , 这里大概总结下这几天了解到的大屏适配的注意事项。

### 启用高分辨率模式

从 Xcode6 GM 版本开始，模拟器新增了 iPhone6 和 iPhone6 Plus 两种，如果旧的工程直接跑到这两个模拟器中时，默认是”兼容模式”，即系统会简单的把内容等比例放大，显示效果有些模糊但尚可接受。此时 App 内部获取到的设备分辨率和 iPhone5 是一样的：320*568 point。

启用高分辨率模式有2个方法(目前我能找到的)：

1.添加大屏的 LaunchImage:  
 在 Images.xcassets 里，新建或更改 LaunchImage 组，添加对应高分辨率的图片。对此，这里有一篇更详细的图文介绍：[How to Add a Launch Image for the iPhone 6](http://matthewpalmer.net/blog/2014/09/10/iphone-6-plus-launch-image-adaptive-mode/)。如果想要快速测试一下新的效果，[这里](https://blog.ibireme.com/wp-content/uploads/2014/09/iPhone6LaunchBlanks.zip)有3张示例图片下载。

2.添加 Launch Screen File  
 Launch Screen 是 Xcode6 和 iOS8 新加的功能，它用一个 xib 文件来作为启动画面。App 在旧版 iOS 启动时，该属性会被自动忽略，不会造成异常。  
 首先，点击 New File -\>iOS User Interface -\>Launch Screen，然后在工程设置项里启用它：

[![LaunchFile](https://blog.ibireme.com/wp-content/uploads/2014/09/LaunchFile.png)](https://blog.ibireme.com/wp-content/uploads/2014/09/LaunchFile.png)

上面两处设置，只要启用任意一个即可让 App 进入高分辨率模式；但如果两处都没有设置，则 App 会回退到兼容模式。鉴于现在不少 App 还需要兼容 iOS5，而第一种方法在 iOS5 上据说可能有[bug](http://stackoverflow.com/questions/19220082/support-of-ios-5-0-icons-with-xcode-5)，所以这里推荐用第二种方法。

### 资源的显示

一图胜千言，首先这里是一个完整的图表： [http://www.paintcodeapp.com/news/ultimate-guide-to-iphone-resolutions](http://www.paintcodeapp.com/news/ultimate-guide-to-iphone-resolutions)。

简单的说：iPhone4、iPhone5、iPhone6 这几个设备的 ppi 都是相同的，默认图片优先是 @2x。iPhone6 Plus 的像素密度更高，默认图片优先是 @3x。

另外，iPhone6 Plus 有一点和其他设备不同：在 App 内部获得的屏幕分辨率是 1242*2208，但设备实际分辨率是 1920*1080，这时系统会把整体的显示内容做一个缩放，downscale 到1/1.15。这个特性在 OSX 上也有出现过：

[![DownScale](https://blog.ibireme.com/wp-content/uploads/2014/09/DownScale.png)](https://blog.ibireme.com/wp-content/uploads/2014/09/DownScale.png)

下面列举一些可能有用的数据：

|  | iPhone | iPhone4 | iPhone5 | iPhone6 | iPhone6+ |
|---|---|---|---|---|---|
| Point | 320*480 | 320*480 | 320*568 | 375*667 | 414*736 |
| Pixel | 320*480 | 640*960 | 640*1136 | 750*1334 | 1242*2208 |
| Pexel(设备) | ～ | ~ | ~ | ~ | 1920*1080 |
| Scale | 1 | 2 | 2 | 2 | 3 |
| PPI | 163 | 326 | 326 | 326 | 401 |
