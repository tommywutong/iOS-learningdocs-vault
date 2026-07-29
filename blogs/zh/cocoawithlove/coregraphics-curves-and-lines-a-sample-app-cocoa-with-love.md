---
title: 'CoreGraphics 曲线与线条：示例 App | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/07/coregraphics-curves-and-lines-sample.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:cc37208c25be92c8'
translated: true
---

> 原文：[CoreGraphics curves and lines: a sample app | Cocoa with Love](https://www.cocoawithlove.com/2008/07/coregraphics-curves-and-lines-sample.html)　·　Cocoa with Love (Matt Gallagher)

这是一款小型应用，展示了基本的 CoreGraphics 线条绘制图元。它包含可用鼠标编辑的控制点，以便你以图形方式操作这些图元。

## CurveDrawing

这篇文章与我一贯的风格有所不同。它其实只是一个你可以动手实践的例子，目的是让你感受在 Cocoa 应用中基本控制和绘图是如何运作的。

本文的项目和代码可在此下载：

- [CurveDrawing.zip (45kB)](https://www.cocoawithlove.com/assets/objc-era/CurveDrawing.zip)

> 该项目为 XCode 3.0 Universal。  
> 如果你使用的是 Intel Mac 且未安装 PPC SDK，可能会看到 "warning... missing required architecture PPC" 警告。要解决此问题，可以禁用 PPC 构建（Project->Project Settings->Build->Architecures），或者从 "Active Build Configuration" 中选择 "Debug" 而非 "Release"。

该应用的代码展示了：

- NSView 子类化（subclassing）
- 使用 NSSegmentedControl 在选项之间切换
- 使用 CoreGraphics C 函数进行线条和矩形绘制
- 通过 -[NSGraphicsContext graphicsPort] 获取当前 NSGraphicsContext 的 CGContextRef
- 使用 -[NSWindow nextEventMatchingMask:(NSLeftMouseDraggedMask | NSLeftMouseUpMask)] 进行鼠标跟踪和拖拽
- 使用 NSSlider 并通过 -[NSControl setContinuous:YES] 将其配置为持续更新

编译完成后，结果如下图所示：

![](https://www.cocoawithlove.com/assets/objc-era/samplescreenshot.png)

该程序没有实现任何 Model-View-Controller 架构（“模型”实际上只是 4 个 NSPoint 值——太微不足道了，不值得为其建立抽象层）。它也没有展示 CoreGraphics 线条绘制的*所有*图元——我略去了两个无法用 4 个控制点轻松描述的图元。

## 理解程序

该程序始终在窗口中显示 4 个控制点，它们呈小型灰色方块。每个控制点都可以用鼠标点击和拖拽。

这些控制点用于绘制当前选定的图元（在窗口顶部的分段控制中选定）。

“ArcToPoint” 使用函数 CGContextAddArcToPoint 进行绘制。该图元通常用于绘制圆角矩形，但它也可以用于绘制任意角度线条之间的曲线段（倒角和圆角）。曲线的半径由窗口底部的滑块控制。

“CurveToPoint” 使用函数 CGContextAddCurveToPoint 进行绘制。它使用全部四个点绘制一条三次贝塞尔曲线（cubic Bézier）。

“EllipseInRect” 使用函数 CGContextAddEllipseInRect 进行绘制。它会在包含所有四个控制点的矩形内绘制一个椭圆。

“Lines” 使用函数 CGContextAddLineToPoint 进行绘制。它会通过所有控制点绘制线段。

“QuadCurve” 使用函数 CGContextAddQuadCurveToPoint 进行绘制。它使用前三个点绘制一条二次贝塞尔曲线（quadratic Bézier）。

“Rect” 使用函数 CGContextAddRect 进行绘制。它会绘制一个包含所有四个控制点的矩形。

## 理解代码

程序的全部代码都位于 “CurveView.m” 源文件中。它包含以下方法：

- **initWithFrame:**  
  在 NIB 加载时调用。将点数组初始化为其初始值。
- **awakeFromNib**  
  在 NIB 加载器将 CurveView 连接到滑块后调用。将滑块设置为连续模式（以便在调整滑块时接收更新），并将初始 “radius” 值设置为滑块的中间值。
- **drawRect:**  
  NSView 默认绘制方法的实现。当视图需要在窗口中绘制或视图被故意更新时，由 Cocoa 自动调用。它会绘制：

    - 背景，为一个带有黑色边框的白色矩形
    - 从点 0 到 1、1 到 2 以及 2 到 3 的线条
    - 当前选定的绘制图元（使用控制点）
    - 代表四个控制点的方块
- **mouseDown:**  
  判断在视图中的点击是否发生在某个控制点方块内，并在鼠标保持按下状态时拖拽该控制点。
- **setRadius:**  
  由 NIB 文件中设置的绑定自动调用，该绑定连接了滑块与 NIB 中 NSObjectController 的 “radius” 值。由于 NSObjectController 的 “content” 被设置为 “CurveView”，因此这会将该滑块绑定到 CurveView 的 radius 属性。  
  我们实现此方法（而不是让绑定直接设置该值）是为了在更改 “radius” 后触发视图重绘。
- **changeSegment:**  
  当点击 NSSegmentedControl 时，作为其 action 的目标被调用。我们更改选定的索引并重绘。
- **resetControlPoints:**  
  从 “initWithFrame:” 方法和窗口中的按钮调用。将数组中的点设置为其默认值。
- **controlPointRectForPoint:**  
  从 “drawRect:” 和 “mouseDown:” 中调用。返回与给定点对应的控制点矩形的边界。
- **boundsOfAllControlPoints**  
  计算并返回一个包含所有控制点的矩形。

## 理解 MainMenu.xib 文件

XIB 文件是 NIB 文件的新版 XML 格式。它在项目构建时仍会被编译成 .nib 文件。

应用中的大多数对象都是从 NIB 文件创建的。这些对象包括：

- 菜单栏中的所有菜单及其所有内容（这些是默认的 Cocoa Application 菜单）
- 窗口及其所有内容，包括 CurveView（在 InterfaceBuilder 中建模为 Custom NSView）
- 一个 NSObjectController，它仅用于通过绑定将窗口中的 NSSlider 连接到 CurveView 的 “radius” 值

对象之间建立的连接：

- “Reset Control Points” 按钮的 action 连接到 CurveView 的 resetControlPoints: 方法，以使按钮生效。
- “ArcToPoint radius” 滑块的 value 绑定连接到 “Object Controller” 的 “radius” 值，以公布滑块的变化。
- “Object Controller” NSObjectController 的 “content” 设置为 CurveView，以使控制器能够将事物（特别是滑块）与 CurveView 的值保持同步。
- NSSegmentedControl 的 action 设置为 CurveView 的 changeSegment: 方法。
- CurveView 的 “sliderControl” 设置为 “ArcToPoint radius” 滑块。
