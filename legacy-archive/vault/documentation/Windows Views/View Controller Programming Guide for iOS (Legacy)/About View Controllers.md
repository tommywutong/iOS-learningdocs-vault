---
title: iOS View Controller 编程指南（旧版）
apple_id: TP40011381
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerPGforiOSLegacy/Introduction/Introduction.html
archived_at: '2026-07-18T02:23:49.611019Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](View%20Controller%20Basics.md)

# 关于 View Controller

对于 iOS 应用程序而言，View Controller 在应用程序的数据与其视觉外观之间提供了至关重要的联系。理解何时以及如何使用 View Controller，对 iOS 应用程序的设计至关重要。View Controller 是 [Model-View-Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MVC.html#//apple_ref/doc/uid/TP40008195-CH32) 设计范式中的传统控制器对象，但它们所做的远不止于此。在 iOS 应用程序中，View Controller 提供了管理应用程序基本行为所需的大部分逻辑。例如，View Controller 管理内容在屏幕上的呈现与移除，并管理视图响应设备方向变化时的重新定向。

View Controller 的存在是为了让你更轻松地创建符合平台设计规范的应用程序。然而，默认的 View Controller 类所能做的终究有限。在某个阶段，你的自定义代码必须接管并完成剩下的工作。本文档将向你展示所有 View Controller 都提供的基本行为，以及你可以在哪些地方对这些行为进行自定义，以满足自己的需求。

### View Controller 管理视图层级

每个 View Controller 负责管理应用程序用户界面中独立的一部分。View Controller 直接关联着单个视图对象，但该对象往往只是一个更大的视图层级（view hierarchy）的根视图，而这个视图层级同样由该 View Controller 管理。View Controller 充当视图层级的中央协调代理，负责处理其视图与任何相关控制器或数据对象之间的交互。单个 View Controller 通常管理与单屏内容对应的视图，不过在 iPad 应用程序中情况未必总是如此。

### 你使用自定义 View Controller 管理内容

每当你想要呈现应用程序特有的内容时，都要使用自定义 View Controller 来完成。你可以直接子类化 [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 或 [UITableViewController](https://developer.apple.com/documentation/uikit/uitableviewcontroller) 来创建自定义 View Controller，并实现呈现内容所需的方法。自定义 View Controller 至少必须能够呈现和管理与自定义内容相关联的视图。你可能还需要实现其他 View Controller 方法，以自定义诸如旋转、内存管理、事件处理等行为，并与应用程序中的其他 View Controller 进行交互。

### navigation controller 管理其他 View Controller 的栈

navigation controller 是 [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) 类的实例，你可以在应用程序中直接使用它，无需修改。包含结构化内容的应用程序可以使用 navigation controller 在不同层级的内容之间导航。navigation controller 本身管理着一个或多个自定义 View Controller 的显示，每个自定义 View Controller 负责管理数据层级中某一特定层级的数据。navigation controller 还提供了控件，用于确定在该数据层级中的当前位置，以及沿层级向上返回导航。

### tab bar controller 管理独立的 View Controller 集合

tab bar controller 是 [UITabBarController](https://developer.apple.com/documentation/uikit/uitabbarcontroller) 类的实例，你可以在应用程序中直接使用它，无需修改。应用程序使用 tab bar controller 来管理多个各自独立的界面，每个界面都由任意数量的自定义视图和 View Controller 组成。tab bar controller 还负责管理与 tab bar 视图的交互，用户点按该视图即可切换当前所选的界面。例如，iPhone 和 iPod touch 上的 iPod 应用程序使用了 tab bar 界面，其中每个标签代表一种查看用户音乐和媒体内容的不同方式。

### iPad 为你的内容提供专属容器

iPad 更大的屏幕尺寸为内容呈现提供了新的可能。[UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) 类负责管理主从（master-detail）界面的实现，其中主视图和从视图部分本身也都由 View Controller 管理。尽管 [UIPopoverController](https://developer.apple.com/documentation/uikit/uipopovercontroller) 类本身并不是一个 View Controller，但它会与应用程序中的 View Controller 协同工作，以在浮动视图中呈现内容。

### 模态 View Controller 临时打断当前工作流程

任何 View Controller 都可以被模态呈现。模态 View Controller 的目的是临时打断当前的工作流程，以收集或呈现信息。例如，你可以使用模态 View Controller 来显示偏好设置或配置选项、从用户处收集数据，甚至在当前屏幕的竖屏和横屏表现形式之间辅助过渡。由于模态呈现总是涉及全屏过渡，因此在 iPad 应用程序中只会谨慎使用，但在 iPhone 应用程序中则相当常见。

撰写（compose）View Controller 是一种特定类型的 View Controller，几乎总是以模态方式呈现。撰写 View Controller 由系统定义，用于呈现特定的界面，例如撰写电子邮件或短信。在 iPhone 和 iPod touch 上，你总是以模态方式呈现撰写控制器，而在 iPad 上，你也可以使用 popover 来呈现它们。

### View Controller 可以组合以创建复杂布局

除了最简单的应用程序之外，通常都会看到多个 View Controller 协同工作。navigation controller、tab bar controller 和 split view controller 总是需要与其他 View Controller 配合使用，甚至你自己的自定义 View Controller 有时也需要以模态方式呈现其他 View Controller。不过，某些 View Controller 的组合方式效果会优于其他方式。以合理的方式组合 View Controller，对于打造简洁、易于导航的用户界面至关重要。

在开始阅读本文档之前，你至少应该对以下 Cocoa 概念有基本的了解：

- 关于 Xcode 和 Interface Builder 及其在应用程序开发中所扮演角色的基本信息
- 如何定义新的 [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43) 类
- 如何[管理内存](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)，包括如何在 Objective-C 中[创建和释放](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)对象
- [委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)在管理应用程序行为中所扮演的角色
- 对 [Model-View-Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MVC.html#//apple_ref/doc/uid/TP40008195-CH32) 范式的基本理解

刚接触 Cocoa 和 Objective-C 的开发者可以在 _[Cocoa Fundamentals Guide](../../Cocoa/Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu)_ 中获取关于上述所有主题的信息。

开发 iOS 应用程序需要一台运行 Mac OS X v10.5 或更高版本的基于 Intel 的 Macintosh 计算机。你还必须下载并安装 iOS SDK。有关如何获取 iOS SDK 的信息，请访问 [Apple 开发者网站](https://developer.apple.com/devcenter/ios/)。

有关应用程序设计的更多信息，请参阅 _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_。

有关如何设计 iOS 应用程序的指导，请参阅 _iOS Human Interface Guidelines_。

有关本文档中讨论的 View Controller 类的信息，请参阅 _[UIKit Framework Reference](https://developer.apple.com/documentation/uikit)_。

[下一页](View%20Controller%20Basics.md)

