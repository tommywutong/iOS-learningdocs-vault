---
title: 绘制贝塞尔曲线 – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/drawing-bezier-curves/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:70bc12d465a4fd29'
translated: true
---

> 原文：[Drawing Bézier Curves – Bartosz Ciechanowski](https://ciechanow.ski/drawing-bezier-curves/)　·　Bartosz Ciechanowski

# [绘制贝塞尔曲线](https://ciechanow.ski/drawing-bezier-curves/)

几个月前，我发布了我的最新 iPad App——[Revolved](http://revolvedapp.com)。Revolved 的核心概念非常简单：你在屏幕右侧绘制曲线，它们会绕轴旋转，生成一个 3D 模型。

在这篇文章中，我将逐步讲解如何在 iPad 屏幕上显示[贝塞尔曲线](http://en.wikipedia.org/wiki/B%C3%A9zier_curve)，正如该 App 中所实现的那样。由于 Revolved 的线条绘制引擎基于 OpenGL，因此在屏幕上呈现曲线并不像调用某些 [Core Graphics](https://developer.apple.com/library/ios/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html) 函数那样简单。

为了增加趣味性，我制作了一些交互演示，它们应该能帮助你更轻松地理解所介绍的概念。下面是在你的浏览器中运行的 Revolved 的一个小片段。这就是我们要构建的内容：

_注意：这些演示使用 HTML5 和 canvas API 制作，但（不幸的是）它无法与完整的基于 OpenGL 的渲染相提并论。虽然浏览器中可能会出现一些小故障或瑕疵，但 Revolved 不会有这些问题。_

Revolved 中用于线条绘制的 OpenGL 代码已在 [我的 GitHub](https://github.com/Ciechan/Drawing-Bezier-Curves-GL) 上提供。另外，我还发布了[Canvas/JS 版本](https://github.com/Ciechan/Drawing-Bezier-Curves-JS)，本文中的演示就是基于它运行的。

# 贝塞尔曲线[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#bézier-curves)

我对贝塞尔曲线非常着迷。它们不仅在计算机图形学中无处不在，而且操作起来也非常有趣。拖动控制点（control point），观察曲线扭动，这本身就是一种享受。

目前最流行的贝塞尔曲线是[三次贝塞尔曲线](http://en.wikipedia.org/wiki/B%C3%A9zier_curve#Cubic_B.C3.A9zier_curves)。它们由四个控制点定义。第一个和最后一个控制点指定绘制曲线的端点（endpoint）位置，而第二个和第三个控制点则影响曲线的切线方向（tangency）。

如果你对深入理解贝塞尔曲线感兴趣，我强烈推荐阅读 [A Primer on Bézier Curves](http://pomax.github.io/bezierinfo/)，这是该领域最权威的资源。不过，本文只需要你对曲线的工作原理有直观的理解，不需要任何深入的背景知识。

在决定在 Revolved 中使用曲线后，我面临了一个挑战：如何使用 OpenGL 图元在 GPU 上渲染平滑的三次贝塞尔曲线。

# 细分（Subdivision）[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#subdivisions)

近似任何曲线形状的最简单方法之一就是将其分割成线段。我们将把一条贝塞尔曲线分割成一组相连的线性组件，目的是让足够多的线段看起来足够平滑。我们需要解决的最重要问题是找到这些线段的连接点。

幸运的是，贝塞尔曲线是参数化的，即它们的 _x_ 和 _y_ 分量由参数 _t_ 定义，_t_ 的取值范围是从 0 到 1。当 _t_ 等于 0 时，我们位于曲线的第一个端点；当 _t_ 等于 1 时，我们位于曲线的最后一个端点。对于介于 0 和 1 之间的 _t_ 值，我们得到位于这两个端点之间曲线上的点。

![贝塞尔曲线参数化](https://ciechanow.ski/images/bezierParametric@2x.jpg)

贝塞尔曲线参数化

要使用 2 条线段来近似贝塞尔曲线的形状，可以计算当 _t_ 等于 0、0.5 和 1 时 3 个连接点的位置。使用 10 条线段则需要 11 个点，对应的 _t_ 值分别为 0、0.1、0.2、…、0.9 和 1.0。

## 细分实战[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#subdivision-in-action)

下面这个小型模拟器展示了这种方法。尝试拖动两个端点和控制点。你可以通过滑块调整线段数量。灰色的细线是使用 HTML5 canvas 图元绘制的精确（希望如此）贝塞尔曲线。

贝塞尔曲线的一个非常好的特性是，细分点会聚集在曲率大的区域附近。尝试制作一条 V 形曲线，注意红色的节点（knot）是如何在尖端附近聚集的，它们不会将曲线等分。此外，即使线段数量很少，绘制的形状也与精确曲线相差不远。

## 绘制线条[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#drawing-lines)

虽然 OpenGL 确实支持线条绘制，但我出于两个原因不想使用这个功能。首先，线条宽度只能在每次绘制调用（draw call）中设置一次。要制作曲线粗细变化的动画，需要将绘制命令分散到不同的批次中，从而可能需要多次绘制调用来渲染所有线段。这过于复杂了。

最重要的因素是，OpenGL 渲染的线条效果很差：

![这是 OpenGL 绘制的实际斜线](https://ciechanow.ski/images/bezierLinesGL@2x.jpg)

这是 OpenGL 绘制的实际斜线

这个“算法”似乎是在水平或垂直方向上克隆像素，使得线条看起来像平行四边形，而不是旋转后的矩形。不用说，这无法满足我对质量的要求。虽然简单的线条绘制对于非常细的线条可能有效，但我希望 Revolved 中的曲线粗壮且醒目地显示在屏幕上。

# 增加宽度（Adding Width）[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#adding-width)

在掌握了用线段近似贝塞尔曲线形状的方法后，我们应该专注于让它们变得更宽。放弃 OpenGL 的线条绘制方法，迫使我们必须求助于 GPU 的常用手段——三角形（triangle）。单个线段将由两个三角形组成，形成一个四边形。我们只需要计算给定线段的 4 个角点，然后用边将它们连接起来：

![](https://ciechanow.ski/images/bezierAddingWidth@2x.jpg)

1. 从一条线性线段开始。
2. 沿垂线方向延伸。
3. 在新的端点处创建顶点（vertex）。
4. 连接它们以创建两个三角形。

虽然这个高层概述听起来相对简单，但细节中往往藏着魔鬼。

## 垂线（Perpendicular）[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#the-perpendicular)

给定一个向量，找到它的垂直向量是向量数学中最简单的技巧之一。只需交换坐标，并取反其中一个即可。就是这样：

![垂直向量的坐标被交换，其中一个被取反](https://ciechanow.ski/images/bezierPerpendicularity@2x.jpg)

垂直向量的坐标被交换，其中一个被取反

有了垂直方向，就可以轻松计算出将用于三角形渲染的顶点位置。

## 糟糕的切线（Tangent）[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#the-bad-tangent)

我们距离渲染具有一定宽度的贝塞尔曲线只差一步了。不幸的是，通过应用上述垂线方法来加宽直线段不会有好效果。再次尝试制作 V 形，注意观察不连续的地方：

问题在于我们将这些线性段视为独立的实体，忘记了它们其实是曲线的一部分。

![两个矩形线段产生了裂缝](https://ciechanow.ski/images/bezierBadTangent@2x.jpg)

两个矩形线段产生了裂缝

虽然我们可以在中点处设法合并顶点，但这不会是完美无缺的。由于贝塞尔曲线是用纯粹的数学术语定义的，我们可以更精确地获取顶点位置。

## 正确的切线[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#the-good-tangent)

上述方法的问题在于，我们忽略了曲线，嗯，它是一条曲线这一事实。如前所述，要得到垂直于曲线方向的方向，我们必须计算曲线本身的真实局部方向。换句话说，如果我们在曲线的给定点画一个箭头来指示其局部方向，那么箭头应该指向哪个方向？这个点上的切线（tangent）是什么？

![一个切线向量](https://ciechanow.ski/images/bezierTangent@2x.jpg)

一个切线向量

[导数（Derivative）](http://en.wikipedia.org/wiki/Derivative)可以帮上忙。由于贝塞尔曲线是以 _t_ 为参数，表示为 _x(t)_ 和 _y(t)_ 的形式，我们可以简单地对这两个方程求关于 _t_ 的导数。我就不在这里列出方程了，你可以直接在源代码中查找具体的解法。

有了切线向量，就可以正确地生成顶点位置了：

![正确的线段，顶点间相互连接](https://ciechanow.ski/images/bezierGoodTangent@2x.jpg)

正确的线段，顶点间相互连接

推导出曲线在给定点的_精确_方向后，我们可以生成_精确_的垂直方向，最终得到_精确_的顶点位置：

注意，对于少量的线段，紧绷的曲线看起来非常奇怪。这其实很容易解释——对于足够长的线段，切线向量可能会有很大的变化，因此多余的宽度可能会在完全不同的方向上加进来。然而，当线段足够短时，切线向量就很难造成这种混乱了。

# 自动分段（Auto-Segmentation）[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#auto-segmentation)

至此，我们几乎已经复现了 Revolved 中使用的线条绘制技术。最后一步，我们不会为绘制例程添加任何新内容。相反，我们将减少交互的复杂性。我们要去掉那个滑块。

滑块的作用是定义曲线应该被分割成多少段。我们不想固定使用一个很大的值并就此了事。即使对最短的线段也渲染几十个三角形，显然是一种浪费。相反，我们将找到一种方法来_自动_计算所需的线段数。

## 估算长度[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#estimating-length)

如果你仔细观察一条贝塞尔曲线，你会注意到它的形状总是类似于连接所有四个控制点的直线的形状。

![曲线的形状类似于连接控制点的直线](https://ciechanow.ski/images/bezierResemblance@2x.jpg)

曲线的形状类似于连接控制点的直线

曲线的长度永远不会超过连接它们的折线（polyline）的长度。计算 AB、BC 和 CD 线段的总长度，我们就得到了曲线长度的上界：

```objc
float estimatedLength = (GLKVector2Length(GLKVector2Subtract(b, a)) +
                         GLKVector2Length(GLKVector2Subtract(c, b)) +
                         GLKVector2Length(GLKVector2Subtract(d, c)));
```

你可能已经注意到，我在向量运算中使用了 [Apple 的 GLKit](https://developer.apple.com/library/ios/documentation/GLkit/Reference/GLKit_Collection/_index.html)。虽然 GLKit 的大部分功能在严肃的 OpenGL 编程中很快变得过于原始，但其数学部分非常出色。它唯一的真正缺点是过于冗长，但这对大多数 Cocoa 开发者来说应该已经习惯了。

## 估算线段数量[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#estimating-number-of-segments)

有了估算长度后，只需计算显示曲线所需的线段数量即可。虽然我们可以简单地将估算长度除以某个值并取 ceil，但这意味着对于非常短的曲线，我们最终可能只有一两条线段。相反，我们应该选择一个略有偏倚的函数，它能提升较小的输入值。我们选择[双曲线（hyperbola）](http://en.wikipedia.org/wiki/Hyperbola)——它太棒了：

![双曲线](https://ciechanow.ski/images/bezierHyperbola@2x.jpg)

双曲线

对于小的输入值，双曲线会提高输出值；对于大的输入值，该函数在渐近意义上类似于简单的线性函数。花几分钟调整参数，就能得到最终的解决方案。注意当曲线变长或变短时，节点数量是如何变化的：

## 基于 Block 的细分器[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#block-based-subdivider)

在编写 Revolved 时，我发现 Objective-C block 的另一个很好的用途。我没有将模型对象传递到渲染系统中，而是选择使用一个细分器 block。给定一个 _t_ 值（与参数化曲线的那个 _t_ 相同），它返回一个 `SegmentSubdivision`，这是一个 `struct`，定义了曲线在给定点的位置和垂直向量。自然地，这个 block 是一个 `typedef`。似乎我不是唯一一个[记不住 block 语法](http://fuckingblocksyntax.com)的人。

```c
typedef struct SegmentSubdivision {
    GLKVector2 p;
    GLKVector2 n;
} SegmentSubdivision;

typedef SegmentSubdivision (^SegmentDivider)(float t);
```

然后，线条网格（mesh）生成器可以利用传入的 block 来生成顶点位置：

```objc
for (int seg = 0; seg <= segmentsCount; seg++) {
	
	SegmentSubdivision subdivision = subdivider((double)seg/(double)segmentsCount);
	v[0] = GLKVector2Add(subdivision.p, GLKVector2MultiplyScalar(subdivision.n, +_lineSize /2.0f));
	v[1] = GLKVector2Add(subdivision.p, GLKVector2MultiplyScalar(subdivision.n, -_lineSize /2.0f));
	...	
}
```

# 为什么不用 Core Graphics？[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#why-not-core-graphics)

在读完所有这些之后，你可能会想：为什么还要费心使用 OpenGL 绘制呢？对于任何经验丰富的 iOS 开发者来说，显而易见的选择是使用 Core Graphics 并利用其函数来绘制曲线。我们来讨论一下我本可以使用的选项。

为了便于说明，我应该指出，Revolved 目前限制为 60 条曲线，App 的绘制区域大小为 448x768 点（在 Retina 设备上为 896x1536 像素）。

## 所有曲线使用单个图层[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#a-single-layer-for-all-the-curves)

第一个基于 Quartz 的解决方案非常明显——一个具有自定义 `- drawRect:` 实现的单个视图。每当用户拖动任何内容时，整个视图都必须重绘。删除线段？重绘整个视图。一个简单的动画？每秒重绘整个视图 60 次。

祝你好运，能在如此快速和频繁的情况下重绘那么多线段。我有没有提到 Core Graphics 调用的光栅化[发生在 CPU 上，_而不是_ GPU 上](https://devforums.apple.com/message/643497#643497)（需要 Apple Dev 账户）？

## 每条曲线使用一个图层[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#one-layer-per-curve)

单个视图肯定不是一个好主意。或者，我可以为每个线段分配一个单独的视图。

首先，让我们考虑内存需求。每个像素有四个 8 位分量（RGBA）。为每条曲线存储在 `- drawRect:` 中绘制的数据将总共占用 60*896*1536*4 字节，也就是 315 MB！即使现代 iPad 能够处理如此巨大的 RAM 需求，我们仍然需要绘制 3D 模型。再加上为 OpenGL 缓冲区分配的空间，情况就更糟了。

其次，过度绘制（overdraw）问题非常严重。由于图层必须是透明的，屏幕右侧的每个像素最多会被重绘 60 次。总计起来，GPU 必须以每秒 60 帧的速度推送超过 26 个全屏的像素量。这不是你想要在你的 App 中出现的情况。

## 优化[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#optimizations)

我在最新最强的 iPad Air 上测试了这些方法，卡顿情况非常糟糕。

两种方法的性能都可以通过实施各种优化来改善，主要是通过保持重绘区域尽可能小。这需要大量的代码来动态调整视图大小、裁剪贝塞尔路径以及执行其他疯狂的技巧，仅仅是为了_期望_变得更好。所有这些努力在绘制覆盖整个绘图区域的曲线时仍然会变得毫无价值。

绘制数十条动画曲线，正如 Revolved 中所做的那样，是一个抽象开始泄露的案例，迫使程序员与简洁的高层 API 作斗争，去完成那些在更低层级上可以_高效得多_完成的工作。

## 把工作丢给 GPU[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#throwing-stuff-at-gpu)

Revolved 使用 3D 模型，因此很明显 App 的某些部分会依赖 OpenGL。生成模型的网格需要将贝塞尔曲线这个抽象的数学概念转换为具体的顶点和面集合。这让我思考——如果我必须经历将贝塞尔曲线转换为 3D 模型顶点表示的过程，为什么不将同样的过程用于 2D 线条呢？这是选择 GPU 路线的一个重要原因。

选择 OpenGL 的关键因素是它使得动画和交互的可能性变得_无穷无尽_。我已经实现或（和）构思的一些线条效果，使用 Core Graphics 几乎是不可能完成的。

# 结语[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/drawing-bezier-curves/#final-words)

在易用的高层 API 的包裹下，人们常常忽略底层概念和事物如何运作的细节。有意识地放弃 Core Graphics 的便利，迫使我从“_如何_？”的角度思考如何绘制贝塞尔曲线。理解指导绘制形状的数学基础是一件值得经历的事情，即使只是为了满足好奇心。

本文介绍的方法并非最先进的。实际上还有更[复杂和健壮的方法](https://agg.sourceforge.net/antigrain.com/research/adaptive_bezier/)来绘制曲线，但 Revolved 中实现的方法完全符合要求（当然了，我几天前才找到那个链接的资源，这当然没帮上忙）。

至于渲染实现，OpenGL 是正确的选择。虽然 Revolved 中一些不太重要的元素（如按钮、教程和致谢面板）基于 UIKit，但 App 的核心部分_完全_在 OpenGL 中运行。这仍然没有达到[完全的 Brichter](http://atp.fm/episodes/22-full-brichter)，但用这种方式编写 App 是一种绝对的享受。

如果你厌倦了剖析贝塞尔曲线，我鼓励你尝试在 3D 中[用你的 iPad](https://itunes.apple.com/app/revolved/id689658680?mt=8) 玩玩它们。
