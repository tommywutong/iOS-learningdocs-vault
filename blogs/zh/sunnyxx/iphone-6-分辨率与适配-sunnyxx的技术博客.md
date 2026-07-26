---
title: iPhone 6 分辨率与适配 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2014/09/10/iphone6-resolution/'
original_language: zh
published: 2014-09-10
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:a2c6057ee54c6842'
translated: n/a
---

> 原文：[iPhone 6 分辨率与适配 · sunnyxx的技术博客](http://blog.sunnyxx.com/2014/09/10/iphone6-resolution/)　·　sunnyxx (孙源)

# iPhone 6 分辨率与适配

2014年9月10日

# [#分辨率和像素](#分辨率和像素)分辨率和像素

经新xcode6模拟器验证（分辨率为pt，像素为真实pixel）：

1. iPhone5分辨率320x568，像素640x1136，@2x
2. iPhone6分辨率375x667，像素750x1334，@2x
3. iPhone6 Plus分辨率414x736，像素1242x2208，@3x，（注意，在这个分辨率下渲染后，图像等比降低pixel分辨率至1080p(1080x1920)）

![](http://ww3.sinaimg.cn/mw690/51530583gw1ek7mqv36zxj20go099jrm.jpg)

PaintCode做了[几个图讲解的非常明了](http://www.paintcodeapp.com/news/iphone-6-screens-demystified)

# [#自动适配](#自动适配)自动适配

不处理时自动等比拉伸，如果在老工程打印屏幕frame，依然是`320x568`  
对比自动适配的和完美适配的导航栏就能看出问题：

![](http://ww1.sinaimg.cn/large/51530583gw1ek7mze3ckrj219y060glw.jpg)

因为拉伸所以会有一些虚，导航栏明显比64要大，但相比3.5寸到4寸的留黑边还是好很多。  
如何关闭自动适配方案呢？这个还是老思路，换启动图：

![](http://ww4.sinaimg.cn/mw690/51530583gw1ek7n9aqlnsj20oc08maa9.jpg)

除了换启动图外，不得不说的是，新Xcode中可以使用一个`xib`来设置启动图：

![](http://ww2.sinaimg.cn/mw690/51530583gw1ek7nce5e1uj20pe07cgmj.jpg)

不过这个xib不能关联任何的代码（不能自定义View的Class，不能IBOutlet，不能加Object），可以理解成这个xib就是一张截图，这个方案的好处在于可以使用到`Size Classes`来针对不同屏幕布局这个xib（感兴趣可以看[《Size Classes初探》](http://blog.sunnyxx.com/2014/09/09/ios8-size-classes/)）

# [#关于手动适配](#关于手动适配)关于手动适配

只要手动指定了启动图或者那个xib，屏幕分辨率就已经变成应有的大小了，老代码中所有关于写死frame值的代码通通倒霉，如果去手动适配就要全部适配，建议**在找到个可行方案前先不要做修改**，自动适配方案还算不影响使用。

面对4个分辨率的iPhone，建议使用`Auto Layout`布局 + `Image Assets`管理各个分辨率的图片 + `Interface Builder`（xib+storyboard）构建UI，`Size Classes`在低版本iOS系统的表现未知。想要这套手动适配方案，起码你的工程需要部署在iOS6+，还不用AutoLayout布局的会死的蛮惨。

# [#关于Xcode6](#关于Xcode6)关于Xcode6

1. 模拟器路径被换成了 `~/Library/Developer/CoreSimulator/Devices/`
2. xcode6中已经找不到iOS6的模拟器了，是时候说服大家放弃iOS7-了
3. ~~现在起提交App Store强制需要支持64位，是时候梳理一遍所有依赖的第三方lib，更新到64位~~

---

One more thing…按这名命的规律…

`iPhone6` -\> `iPhone6+` -\> `iPhone6++`? -\> `iPhone6#`?
