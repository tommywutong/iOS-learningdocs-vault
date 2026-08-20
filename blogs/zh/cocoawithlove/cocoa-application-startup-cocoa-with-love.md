---
title: 'Cocoa 应用启动 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/03/cocoa-application-startup.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:2a138bd328b295f1'
translated: true
---

> 原文：[Cocoa Application Startup | Cocoa with Love](https://www.cocoawithlove.com/2008/03/cocoa-application-startup.html)　·　Cocoa with Love (Matt Gallagher)

Cocoa 应用是如何启动的？哪些地方是放置启动时运行代码的主要位置？在本系列启动图中寻找答案。

## 很自然会问到的第一个问题

在完成最初的 Cocoa 教程、学习了如何把基本方法连接到按钮和菜单之后，我听到 Cocoa 新手最常问的问题是：

> 我应该把代码放在哪里，让它在 Cocoa 应用启动时运行？

Cocoa 虽然可以很方便地在 Interface Builder 中编辑和连接东西，但你会很快触及这种简单程序设定的限制。文稿和应用窗口可以神奇地出现，但最终你会希望对这些默认操作拥有控制权。

一旦你需要做更多事情，你就需要开始揭开 Cocoa 应用启动的神秘面纱，理解 NSApplication 做了什么、Interface Builder 的 NIB 文件是如何出现的，以及如何为文稿和其他元素运行自定义代码。

关于程序启动工作原理的问题是切中要害的——你需要控制你的程序，让它为你所用。而这要从最开头开始。但决定把代码放在哪里可能很棘手：Cocoa 为你提供了许多不同的地方来初始化不同组件，以便在适当的位置执行适当的设置。我将展示一个 Cocoa 应用中所有常见的启动时代码运行位置。希望了解这些选项能帮你选对地方。

## Objective-C 运行时初始化

Objective-C 运行时在其启动过程中提供了初始化类的位置，如下图所示：

![](https://www.cocoawithlove.com/assets/objc-era/startupMain.png)

main() 方法在 Objective-C 中的工作方式和在任何标准 C 程序中一样，如果需要，你也可以在这里执行全局初始化。不过，典型的 Cocoa 应用在这里除了调用 NSApplicationMain() 之外什么也不做。很大程度上忽略这个入口点的原因是，类、应用实例、文稿和用户界面元素都有各自的初始化方式，使用这些位置更有意义。

传统上，在 C 语言中，main() 是执行启动和初始化的最早位置。在 Objective-C 中，提供的第一次初始化甚至比这还要早：+(void)load 方法。任何类都可以拥有 +(void)load 方法，当该类被加载时，运行时将调用它。对于普通的编译类，这发生在“映像加载”期间（在 main() 被调用之前的一段时间）。由于类的加载没有特定顺序，其他类可能尚未加载，你需要谨慎对待在这里做的事情——通常，你不应该在 +(void)load 方法中引用其他类。

Objective-C 还提供了一个类似（但更安全，因为你_可以_引用其他类）的设置方法：+(void)initialize。这是执行类特定设置最常见的地方。在首次向某个类的对象发送消息之前，+(void)initialize 会被发送给该类及其所有超类（如果它们尚未被初始化）。这些消息按层级顺序发送（超类在子类之前收到消息）。虽然更安全（因为此时所有类都已加载），但它的调用时机确定性较低，因为 +(void)initialize 只在首次实际向该类发送消息时被调用——如果一个类从未被使用，该消息就不会被发送。

## NSApplication 初始化

以下是 NSApplication 的典型启动流程（通过上图中的 NSApplicationMain() 调用）：

![](https://www.cocoawithlove.com/assets/objc-era/startupNSApp.png)

此图显示了应用（通常是 NSApplication，但这可以在 Info.plist 文件中配置）被初始化和运行的过程。尽管你_可以_更改应用的主类，但建议你不要这么做——因此这不是考虑放置启动代码的首选位置。

相反，你应该关注应用在启动时执行的三个主要功能（加载 main NIB、加载第一个文稿、通知 NSApplication delegate）。这些是需要切入的关键区域。

> 只有当 Info.plist 文件中配置了 CFBundleDocumentTypes 时，NSApplication 才被认为处理文稿。如果在 Info.plist 中没有这个值，NSApplication 将跳过文稿处理（非文稿应用）。

首先要考虑的区域是“main NIB”文件。NIB 文件是标准的用户界面文件，在 Interface Builder 中创建。“main NIB”通常包含菜单栏和其他“启动时”资源的用户界面文件。它也是 NSApplication delegate 的常见存放位置。如果你不知道什么是 delegate，可以阅读 [Apple 对 delegate 的描述](http://developer.apple.com/documentation/Cocoa/Conceptual/CocoaFundamentals/CommunicatingWithObjects/chapter_6_section_4.html)，但本质上，它指的是通过 NSApplication 的“delegate” outlet（通常在 Interface Builder 中）连接到 NSApplication 的任何对象。delegate 之所以特殊，是因为 NSApplication 会响应某些事件向它发送消息。这些就是 delegate 方法。

在启动时，NSApplication delegate 会收到它最重要的消息之一，applicationDidFinishLaunching:。几乎每个应用都实现了这个方法。这是在所有东西都创建和加载完之后，处理整个程序的设置的最佳位置。

如果你需要为某个窗口或文稿进行更具体的初始化，那么你需要切入其他步骤之一。如果你正在编写一个使用单个固定窗口的非文稿应用，那么该窗口很可能与 main NIB 一起加载，因此你需要阅读关于 NIB 加载的下一节。如果你正在编写一个文稿应用，则需要查看文稿加载一节。

## NIB 加载

Interface Builder 中 NIB 文件的加载过程如下：

![](https://www.cocoawithlove.com/assets/objc-era/startupNib.png)

应用窗口、文稿窗口、菜单栏和 NSApplication delegate 通常都是通过这种方式从 NIB 文件加载的。

这里需要注意的一点是，你的对象的 init 方法是在其 IBOutlet 连接根据 NIB 文件中的设置进行配置_之前_被调用的，因此你可以初始化自己的对象，但还不能读取通过 Interface Builder 连接的对象。

因此，对于从 NIB 文件加载的对象，一种常见的初始化方式是在该对象上实现 -(void)awakeFromNib 方法。如果对象中存在此方法，NIB 加载器会在整个 NIB 初始化并连接完成之后调用它，这使得它成为执行涉及多个对象的配置的绝佳位置。

## 文稿加载

文稿的加载过程如下：

![](https://www.cocoawithlove.com/assets/objc-era/startupDocument.png)

初始化文稿的关键位置包括：它的 init 方法、在加载文稿的 NIB 文件时，以及在 windowControllerDidLoadNib: 中。简单来说，这些位置分别提供了在加载文稿窗口资源之前、期间和之后的配置点。

## 结论

我并没有展示所有可以在启动时使用的位置。如果你确实需要，还有很多其他的 delegate 方法、通知和可重写方法。我所展示的是最常见且最有用的一些位置。

这些位置包括：

- +(void)initialize
- -(void)awakeFromNib
- -(void)windowControllerDidLoadNib:
- -(void)applicationDidFinishLaunching:

以及你自己子类的常规 init 方法。

了解这些方法各自的作用、它们何时被调用，以及理解它们所负责的对象。它们将让你能够在 Cocoa 应用启动时执行几乎所有的配置。
