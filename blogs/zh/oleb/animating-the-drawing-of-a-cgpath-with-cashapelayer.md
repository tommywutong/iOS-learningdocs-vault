---
title: 用 CAShapeLayer 动画化 CGPath 的绘制
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/12/animating-drawing-of-cgpath-with-cashapelayer/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:adf7224a18abd24c'
translated: true
---

> 原文：[Animating the Drawing of a CGPath With CAShapeLayer](https://oleb.net/blog/2010/12/animating-drawing-of-cgpath-with-cashapelayer/)　·　Ole Begemann

# 用 CAShapeLayer 动画化 CGPath 的绘制

iOS SDK 4.2 中一项不错的补充是 [`CAShapeLayer`](http://developer.apple.com/library/ios/#documentation/GraphicsImaging/Reference/CAShapeLayer_class/Reference/Reference.html) 的两个新属性：[`strokeStart`](http://developer.apple.com/library/ios/documentation/GraphicsImaging/Reference/CAShapeLayer_class/Reference/Reference.html#//apple_ref/doc/uid/TP40008314-CH1-SW16) 和 [`strokeEnd`](http://developer.apple.com/library/ios/documentation/GraphicsImaging/Reference/CAShapeLayer_class/Reference/Reference.html#//apple_ref/doc/uid/TP40008314-CH1-SW15)。两者都是 float 类型，取值范围在 `0.0` 到 `1.0` 之间，表示在形状图层（shape layer）的路径上开始和停止描边的相对位置。

默认值自然是 `strokeStart` 为 `0.0`，`strokeEnd` 为 `1.0`，这使得形状图层的路径沿其整个长度被描边。如果你设置 `layer.strokeEnd = 0.5f`，则只描边路径的前半部分。到这里都很好理解。

这些属性的真正妙处在于它们是可动画的。通过将 `strokeEnd` 从 `0.0` 动画化到 `1.0`，持续几秒钟，我们可以轻松地展示路径被绘制的过程：

```
CABasicAnimation *pathAnimation = [CABasicAnimation animationWithKeyPath:@"strokeEnd"];
pathAnimation.duration = 10.0;
pathAnimation.fromValue = [NSNumber numberWithFloat:0.0f];
pathAnimation.toValue = [NSNumber numberWithFloat:1.0f];
[self.pathLayer addAnimation:pathAnimation forKey:@"strokeEndAnimation"];
```

最后，添加一个包含钢笔图像的第二个图层，并使用 [`CAKeyframeAnimation`](http://developer.apple.com/library/ios/#documentation/GraphicsImaging/Reference/CAKeyframeAnimation_class/Introduction/Introduction.html) 以相同速度沿路径为它添加动画，使效果更加逼真：

```
CAKeyframeAnimation *penAnimation = [CAKeyframeAnimation animationWithKeyPath:@"position"];
penAnimation.duration = 10.0;
penAnimation.path = self.pathLayer.path;
penAnimation.calculationMode = kCAAnimationPaced;
[self.penLayer addAnimation:penAnimation forKey:@"penAnimation"];
```

<sub>[下载视频](https://oleb.net/media/AnimatedPathsHausVomNikolaus.mp4)</sub>

这同样适用于文本；我们只需要将字形转换为 `CGPath`。Core Text 提供了一个函数来实现这一点：[`CTFontCreatePathForGlyph()`](http://developer.apple.com/library/ios/documentation/Carbon/Reference/CTFontRef/Reference/reference.html#//apple_ref/c/func/CTFontCreatePathForGlyph)。要使用它，我们需要创建一个包含要渲染文本的属性字符串，首先将其拆分为行，然后拆分为字形。将字形转换为路径后，我们将它们全部作为子路径添加到一个 `CGPath` 中。详情请参阅 [Ohmu](http://www.codeproject.com/script/Membership/View.aspx?mid=2887692) 的精彩文章 [Low-level text rendering](http://www.codeproject.com/KB/iPhone/Glyph.aspx)。结果看起来很棒：

<sub>[下载视频](https://oleb.net/media/AnimatedPathsHelloWorld.mp4)</sub>

在 GitHub 上[获取示例项目](https://github.com/ole/Animated-Paths)（适用于 iPad）。我以 [MIT 许可证](http://www.opensource.org/licenses/mit-license.php) 发布了我编写的部分，而我从上述文章中引用的代码则以同样宽松的 [Code Project 开放许可证](http://www.codeproject.com/info/cpol10.aspx) 发布。
