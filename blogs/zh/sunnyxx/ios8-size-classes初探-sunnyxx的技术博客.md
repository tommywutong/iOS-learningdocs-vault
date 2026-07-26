---
title: iOS8 Size Classes初探 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2014/09/09/ios8-size-classes/'
original_language: zh
published: 2014-09-09
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a461056d6119d463'
translated: n/a
---

> 原文：[iOS8 Size Classes初探 · sunnyxx的技术博客](http://blog.sunnyxx.com/2014/09/09/ios8-size-classes/)　·　sunnyxx (孙源)

# iOS8 Size Classes初探

2014年9月9日

iOS8 新特性，`Size Classes`，是对老式UI思路的全新抽象：把各个设备屏幕（iphone4, 5, 6, iPad, Apple Watch?）以及它们的屏幕旋转状态都抽象成屏幕 Size 的变化，将这些Size归纳成几个类别（Class）

![](http://7xtel4.com1.z0.glb.clouddn.com/2016-05-13-1.png)

宽（正常，任意， 紧凑），高（正常，任意， 紧凑）

3 x 3 共 9 种 Size，每种 Size 都可以设置特定的一套布局，如果不特殊指定，默认是在（宽任意，高任意）模式下设置，且其他 8 种布局继承它。

听过有人说，我们不用学 autolayout 了，直接学 Size Classes 就一步到位了。这个说法是不对的，因为 Size Classes 在将屏幕分类后，执行布局的还是Autolayout。

# Size Classes与Interface Builder

当然不出所料的是，Xcode 6 中 Interface Builder 对 Size Classes 有了很强大的支持：

![](http://7xtel4.com1.z0.glb.clouddn.com/2016-05-13-2-1.png)

启用 Size Classes 后，IB 中就会出现 Size Classes 切换的菜单

![](http://7xtel4.com1.z0.glb.clouddn.com/2016-05-13-3.png)

我们可以切换到 `wAny,hAny`模式去编辑通用的控件和布局，也可以切换到某个特定 Class，立刻可以预览到变化，于是有个问题：

假如 iPad 和 iPhone 的布局有差异，老式写法是分成 iPad.storyboard 和iPhone.storyboard 来分别写，这本身就是个 bug，因为大部分控件其实并没差别，新 Size Class 解决这个问题了木？

答案是肯定的，Size Class 的方案比老式的好了几条街：  
IB 中某个 View 的出现与否，**约束的出现与否以及约束的值都是可以根据 Size Class 单独设置的**，也就是说现在一个 storyboard 是 `9合1` 的。  
比如下面有个 Label，我只希望它出现在长宽紧缩的屏幕上时（脑补 Apple Watch），这么勾选下就可以（出现或不出现被命名为 “Installed” ，这个选项可以从 9 个 Size Class 中多选）

![](http://7xtel4.com1.z0.glb.clouddn.com/2016-05-13-4.jpeg)

# Size Classes的xml文件改动

说到9合1的时候肯定会有疑问，这样的storyboard文件会不会很大？源文件会不会很乱导致多人开发经常冲突？

答案是不会的，源于 apple 对 Size Class 在 xml 中的描述方法是针对变化配置的，什么意思呢？对比下 storyboard 的 xml 源文件就知道了：  
wAny,hAny 模式下刚才只有一个 Label 的页面：

![](http://7xtel4.com1.z0.glb.clouddn.com/2016-05-13-5.png)

假如在 `wC,hC` 紧缩模式下设置不出现这个 label 时，在 label 的父 view 层级出现了下面的配置：

![](http://7xtel4.com1.z0.glb.clouddn.com/2016-05-13-6.png)

所以说 IB 中以附加的描述字段来表示哪些元素是被哪些 Size Classes 包含或排除的，也正因为这样的描述方式，使得新的 xml 格式**可以被低版本兼容**（低版本不解析这个字段，但其他字段正常解析）

# Size Classes与xcassets

既然 storyboard 变成了 9 合 1，配套的 `xcassets` 必须也有所表示才行， Xcode 6 后向 `xcassets` 中添加图片时增加了选择对应 Size Classes 的菜单，展开后会像下面一样：

![](http://ww1.sinaimg.cn/mw690/51530583gw1ek7k01ldj9j20j40k4aat.jpg)

通过符号表示确实不错 `-`对应紧缩，`*`对应 Any，`+`对应宽松  
（@3x 是 iPhone6 Plus）

# 总结

总的来说，iOS 对 UI 这块的改动是跨时代性的，Autolayout 的出现使得布局的复杂度减少到了 View 与 View 的关系上，再由根 View（也就是屏幕）指定frame，随后所有子 View 相对布局，把 frame 的概念归一化到根 View 的 frame 上；但有了 Size Classes 后，根视图的 frame 概念也被移除了，这下整个 app 的 UI 和 frame 这个单词已然脱离关系，这也正是apple想要达到的目的。

Farewell，frame 和那些还奋战在手写UI的 iOS coder 们…
