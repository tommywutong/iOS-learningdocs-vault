---
title: iOS 视图编程指南
apple_id: TP40009503
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html
archived_at: '2026-07-18T02:24:12.070353Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](View%20and%20Window%20Architecture.md)

# 关于窗口与视图

在 iOS 中，你用窗口（window）和视图（view）把应用的内容呈现到屏幕上。窗口本身没有任何可见内容，它只是为应用的视图提供一个基本容器。视图则划定了窗口中的一块区域，你可以往这块区域里填充内容。例如，你可能会用视图来显示图像、文本、图形，或是它们的组合。你也可以用视图来组织和管理其他视图。

每个应用至少有一个窗口和一个视图来呈现其内容。UIKit 和其他系统框架提供了一批预定义的视图，你可以直接拿来展示内容。这些视图既包括简单的按钮和文本标签，也包括表视图、选取器视图、滚动视图这类更复杂的视图。如果预定义视图无法满足你的需求，你还可以定义自定义视图，自行管理绘制和事件处理。

### 视图管理应用的可视内容

视图是 [UIView](https://developer.apple.com/documentation/uikit/uiview) 类（或其子类）的一个实例，负责管理应用窗口中的一块矩形区域。视图要负责绘制内容、处理多点触控事件，以及管理所有子视图的布局。绘制指的是使用 Core Graphics、OpenGL ES 或 UIKit 等图形技术，在视图的矩形区域内绘制图形、图像和文本。视图既可以通过手势识别器，也可以通过直接处理触摸事件，来响应其矩形区域内的触摸。在视图层级中，父视图负责确定子视图的位置和大小，并且可以动态调整。这种动态修改子视图的能力，让你的视图能够适应界面旋转、动画等各种变化。

你可以把视图看作构建用户界面的积木。与其用一个视图来呈现全部内容，不如用若干个视图搭建出一个视图层级。层级中的每个视图呈现用户界面的某一特定部分，通常针对某一类内容做过优化。例如，UIKit 就提供了专门用于呈现图像、文本和其他类型内容的视图。

### 窗口协调视图的显示

窗口是 [UIWindow](https://developer.apple.com/documentation/uikit/uiwindow) 类的一个实例，负责应用用户界面的整体呈现。窗口与视图（以及持有它们的 View Controller）协同工作，管理与可见视图层级的交互及其变化。多数情况下，应用的窗口不会发生变化。窗口一经创建就保持不变，变的只是它所显示的视图。每个应用至少有一个窗口，用于在设备主屏幕上显示应用的用户界面。如果设备连接了外接显示屏，应用还可以创建第二个窗口，把内容呈现到那块屏幕上。

### 动画为界面变化提供可见反馈

动画能让用户直观地感知到视图层级的变化。系统为呈现模态视图以及在不同视图组之间切换定义了标准动画。此外，视图的许多属性也可以直接做动画。例如，通过动画你可以改变视图的透明度、它在屏幕上的位置、大小、背景色或其他属性。而如果你直接操作视图底层的 Core Animation 图层对象，还能实现更多其他动画效果。

### Interface Builder 的作用

Interface Builder 是一个用于以图形化方式构建和配置应用窗口与视图的应用程序。使用 Interface Builder，你可以组装视图并把它们放进一个 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)中——这是一种资源文件，保存了视图和其他对象的“冻干”版本。当你在运行时加载 nib 文件时，其中的对象会被还原成真实的对象，你的代码随后就可以通过编程方式操作它们。

Interface Builder 大大简化了创建应用用户界面所需的工作。由于整个 iOS 都内置了对 Interface Builder 和 nib 文件的支持，把 nib 文件融入应用设计几乎不费什么力气。

关于如何使用 Interface Builder 的更多信息，请参阅 _[Interface Builder 用户指南](../../Developer%20Tools/Interface%20Builder%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbu)_。关于 View Controller 如何管理包含其视图的 nib 文件，请参阅 _[iOS View Controller 编程指南](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_ 中的“创建自定义内容 View Controller”。

由于视图是非常复杂而灵活的对象，一份文档不可能涵盖它们的全部行为。不过还有其他文档可以帮助你了解视图管理和整个用户界面的其他方面。

- View Controller 是管理应用视图的重要一环。一个 View Controller 统管单个视图层级中的所有视图，并负责把这些视图呈现到屏幕上。关于 View Controller 及其作用的更多信息，请参阅 _[iOS View Controller 编程指南](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_。
- 视图是应用中手势和触摸事件的主要接收者。关于使用手势识别器和直接处理触摸事件的更多信息，请参阅 _iOS 事件处理指南_。
- 自定义视图必须使用现有的绘图技术来渲染自己的内容。关于如何使用这些技术在视图中绘制，请参阅 _[iOS 绘图与打印指南](../../Drawing%20and%20Printing%20Guide%20for%20iOS/About%20Drawing%20and%20Printing%20in%20iOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjw)_。
- 当标准视图动画不够用时，你可以使用 Core Animation。关于如何用 Core Animation 实现动画，请参阅 _[Core Animation 编程指南](../../Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_。
[下一页](View%20and%20Window%20Architecture.md)

