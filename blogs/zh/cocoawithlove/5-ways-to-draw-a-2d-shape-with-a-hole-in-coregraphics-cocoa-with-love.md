---
title: '在 CoreGraphics 中绘制带洞 2D 形状的 5 种方法 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/05/5-ways-to-draw-2d-shape-with-hole-in.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:c6711baad70cdac6'
translated: true
---

> 原文：[5 ways to draw a 2D shape with a hole in CoreGraphics | Cocoa with Love](https://www.cocoawithlove.com/2010/05/5-ways-to-draw-2d-shape-with-hole-in.html)　·　Cocoa with Love (Matt Gallagher)

在这篇文章中，我将介绍 5 种不同的方法，用以绘制一个非常简单的形状：一个中心带三角形洞的正方形。在 CoreGraphics 这样支持双缓冲、缠绕计数（winding count）路径填充、奇偶路径填充和裁剪区域（clipping region）的绘图环境中，并没有单一的答案。随文提供了一个包含代码的 iPhone 示例项目，但所有绘图函数在 Mac 上都是相同的。

## 引言

本文将介绍绘制以下形状的不同方法：

![](https://www.cocoawithlove.com/assets/objc-era/shape.png)

这是一个非常简单的形状，但它需要非简单拓扑：你必须切掉形状的中心才能绘制它。本文将介绍 5 种不同的实现方法以及各自的优缺点。

为便于解释，我给绘制形状所用的每个坐标都命了名：

```objc
// Coordinates are:
//
// A-------------B     A(0,0), B(100,0), C(100,100), D(0,100)
// |      E      |     E(50,10), F(10,90), G(90,90)
// |     / \     |     H(50,90), I(50,100)
// |    /   \    |
// |   /     \   |
// |  F---H---G  |
// D------I------C
```

## 技巧 1：覆盖绘制

绘制该形状最朴素的方法是先以形状的颜色绘制正方形（ABCD），然后在上面以背景色绘制三角形（EFG）。

需要明确的是：这是一个你**不应当**使用的技巧示例。

```objc
// Technique 1: overpaint
CGContextMoveToPoint(context, Ax, Ay);
CGContextAddLineToPoint(context, Bx, By);
CGContextAddLineToPoint(context, Cx, Cy);
CGContextAddLineToPoint(context, Dx, Dy);
CGContextAddLineToPoint(context, Ax, Ay);
CGContextSetRGBFillColor(context, 0.5, 0, 0, 1);
CGContextFillPath(context);
CGContextMoveToPoint(context, Ex, Ey);
CGContextAddLineToPoint(context, Fx, Fy);
CGContextAddLineToPoint(context, Gx, Gy);
CGContextAddLineToPoint(context, Ex, Ey);
CGContextSetRGBFillColor(context, 1, 1, 1, 1);
CGContextFillPath(context);
```

**优点**：如果你只熟悉「画家算法」——即所有内容都是简单地覆盖在其他内容之上绘制——那么这可能最容易理解。

**缺点**：如果你的背景发生变化，效果将不起作用。

![](https://www.cocoawithlove.com/assets/objc-era/shape1problem.png)

这种方法还存在一个问题：图像中三角形内部的像素在离屏缓冲区中被绘制了两次（一次是正方形的颜色，一次是背景色）。如果你要以这种方式绘制大量的形状，那么这种过度绘制将比一开始不绘制中心像素的方法更慢。

## 技巧 2：假洞

绘制此形状时的另一种取巧尝试是将其绘制为单个简单多边形——即沿着 H 与 I 之间的线段切开形状，然后像马蹄铁一样绘制（先 ABCI，然后 HGEFH，最后以 IDA 结尾）。

同样地，这也是一个你**不应当**使用的技巧示例。

```objc
// Technique 2: false hole
CGContextMoveToPoint(context, Ax, Ay);
CGContextAddLineToPoint(context, Bx, By);
CGContextAddLineToPoint(context, Cx, Cy);
CGContextAddLineToPoint(context, Ix, Iy);
CGContextAddLineToPoint(context, Hx, Hy);
CGContextAddLineToPoint(context, Gx, Gy);
CGContextAddLineToPoint(context, Ex, Ey);
CGContextAddLineToPoint(context, Fx, Fy);
CGContextAddLineToPoint(context, Hx, Hy);
CGContextAddLineToPoint(context, Ix, Iy);
CGContextAddLineToPoint(context, Dx, Dy);
CGContextAddLineToPoint(context, Ax, Ay);
CGContextSetRGBFillColor(context, 0, 0.5, 0, 1);
CGContextFillPath(context);
```

**优点**：避免了上一个问题中背景以错误颜色被覆盖绘制的情况。

**缺点**：包含了多余的边缘，如果你尝试对形状描边（stroke），这些边缘将无法正确绘制。

![](https://www.cocoawithlove.com/assets/objc-era/shape2problem.png)

这种方法还可能受到精度问题的困扰：如果底部的切开处实际上没有重叠，那么在非常高的分辨率下绘制时（例如在 Mac 上，一旦分辨率独立（resolution independence）变为用户可设置，并且对象可以以意外的大小被绘制），它可能会显示为对象中的一条缝隙。

## 技巧 3：缠绕计数

这是绘制路径中孔洞的第一种正确方法，使用「缠绕计数」（winding count）多边形内部算法将三角形内部标记为路径边界之外的「外部」。

缠绕计数是 CoreGraphics 确定像素是在路径内部还是外部的默认方式。其工作原理如下：

1. CoreGraphics 在路径的边界矩形内从左到右绘制每一行。
2. 在每一行的开头，CoreGraphics 将形状的缠绕计数设为零。
3. 如果在行的任意一点，CoreGraphics 穿过形状中的一条线，它会记录下该线在穿越点处是向上还是向下。
4. 向上的线将形状的缠绕计数加 1。
5. 向下的线将形状的缠绕计数减 1。
6. 如果形状的缠绕计数在任何时候为非零值（无论正负），则根据形状的颜色填充像素。

如果这有点难以理解，那么关于缠绕计数的简单描述是：

> **简单缠绕计数**：如果一个边界是顺时针绘制的，那么它内部的逆时针边界将关闭形状。如果一个边界是逆时针绘制的，那么它内部的顺时针边界将关闭形状。

以下是我们使用缠绕计数绘制形状的方法：

```objc
// Technique 3: winding count fill rule
CGContextMoveToPoint(context, Ax, Ay);
CGContextAddLineToPoint(context, Bx, By);
CGContextAddLineToPoint(context, Cx, Cy);
CGContextAddLineToPoint(context, Dx, Dy);
CGContextAddLineToPoint(context, Ax, Ay);
CGContextClosePath(context);
CGContextMoveToPoint(context, Ex, Ey);
CGContextAddLineToPoint(context, Fx, Fy);
CGContextAddLineToPoint(context, Gx, Gy);
CGContextClosePath(context);
CGContextSetRGBFillColor(context, 0.5, 0.0, 0.75, 1);
CGContextFillPath(context);
```

ABCD 边界是顺时针的，因此逆时针的 EFG 创建了一个孔洞。要开始内部边界，我们只需关闭第一个边界并移动到下一个边界（所有边界都成为当前路径的一部分）。

**优点**：真正绘制了一个带有孔洞的形状。

**缺点**：如果不小心按 EGF 的顺序绘制内部形状，它将不起作用（顺时针加顺时针会导致缠绕计数为 2——仍然是非零值，形状仍将被填充）。

缠绕计数需要额外注意，以确保始终维持正确的方向。

## 技巧 4：奇偶路径

奇偶（even-odd）是 CoreGraphics 中用于路径的另一种规则。该规则比缠绕计数更简单些：在奇偶规则中，最外层的边界开始填充，次外层再次停止填充，对于其他嵌套路径依此类推。

代码与缠绕计数的版本非常相似，除了我们使用 `CGContextEOFillPath` 进行填充，并且 EFG 相对于 ABCD 的顺序无关紧要。

```objc
// Technique 4: even-odd fill rule
CGContextMoveToPoint(context, Ax, Ay);
CGContextAddLineToPoint(context, Bx, By);
CGContextAddLineToPoint(context, Cx, Cy);
CGContextAddLineToPoint(context, Dx, Dy);
CGContextAddLineToPoint(context, Ax, Ay);
CGContextClosePath(context);
CGContextMoveToPoint(context, Ex, Ey);
CGContextAddLineToPoint(context, Fx, Fy);
CGContextAddLineToPoint(context, Gx, Gy);
CGContextClosePath(context);
CGContextSetRGBFillColor(context, 0.75, 0.5, 0, 1);
CGContextEOFillPath(context);
```

**优点**：比缠绕计数更不易出现排序问题。

**缺点**：在某些情况下，缠绕计数可能给出更好的结果。考虑下面这个用单一连续路径 12345 绘制的五角星。

![](https://www.cocoawithlove.com/assets/objc-era/eoversuswinding.png)

在这种情况下，如果你确实想要填充形状的中心，就需要使用缠绕计数（该形状是以连续的顺时针方向绘制的，因此缠绕计数始终为正）。

## 技巧 5：裁剪区域

我要展示的最后一种方法是使用裁剪区域从启用的绘图区域中移除形状中心的三角形。

```objc
// Technique 5: remove the inner hole using a clipping region
CGContextSaveGState(context);
CGContextAddRect(context, CGContextGetClipBoundingBox(context));
CGContextMoveToPoint(context, Ex, Ey);
CGContextAddLineToPoint(context, Fx, Fy);
CGContextAddLineToPoint(context, Gx, Gy);
CGContextClosePath(context);
CGContextEOClip(context);
CGContextMoveToPoint(context, Ax, Ay);
CGContextAddLineToPoint(context, Bx, By);
CGContextAddLineToPoint(context, Cx, Cy);
CGContextAddLineToPoint(context, Dx, Dy);
CGContextAddLineToPoint(context, Ax, Ay);
CGContextSetRGBFillColor(context, 0, 0, 0.5, 1);
CGContextFillPath(context);
CGContextRestoreGState(context);
```

你可以看到，这种方法实际上相当复杂，因为带有孔洞的裁剪区域需要的处理与带有孔洞的形状相同：我使用奇偶裁剪规则从裁剪区域的边界矩形中减去了三角形。

**优点**：裁剪区域可以非常简单地减去或切割非常复杂的形状——甚至是一组形状。

**缺点**：对于像这样切割单个形状而言，保存旧图形状态（graphics state）并在完成后恢复所需的额外工作，加上裁剪区域本身就和形状一样复杂的事实，使得这种方法比前两种更费力。

## 结论

> 你可以在此处下载用于绘制这些形状的代码：[GraphicalSubtraction.zip](https://www.cocoawithlove.com/assets/objc-era/GraphicalSubtraction.zip)（25kB）

一个非常简单的形状，但你可以通过一些截然不同的方式绘制它。正如你所见，「错误」的解决方法实际上并没有节省任何代码——正确的解决方案长度大致相同。

解决这个问题的最佳方法是使用奇偶或缠绕计数方法。虽然形状看起来像是中心被裁剪掉了，但裁剪区域反而需要更多工作，并且非矩形的裁剪区域在计算上也更困难。
