---
title: iOS View Controller 编程指南（旧版）
apple_id: TP40011381
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerPGforiOSLegacy/AboutViewControllers/AboutViewControllers.html
archived_at: '2026-07-18T02:23:34.749689Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 编程指南（旧版）](About%20View%20Controllers.md)


[下一页](Custom%20View%20Controllers.md)[上一页](About%20View%20Controllers.md)

# View Controller 基础

View Controller 提供了实现 iOS 应用程序所需的基础设施。本章概述了 View Controller 在应用程序中所扮演的角色，以及你如何使用它们来实现不同类型的用户界面。

在 [Model-View-Controller (MVC) 设计模式](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MVC.html#//apple_ref/doc/uid/TP40008195-CH32)中，[控制器对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11)提供了将应用程序的数据与用于向用户呈现该数据的视图及其他可视化实体连接起来所需的自定义逻辑。在 iOS 应用程序中，_View Controller_ 是一种特定类型的控制器对象，你用它来呈现和管理一组视图。View Controller 对象是 UIKit 框架中定义的 [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 类的后代。

View Controller 在 iOS 应用程序的设计与实现中扮演着非常重要的角色。运行在基于 iOS 的设备上的应用程序，其用于显示内容的屏幕空间有限，因此在向用户呈现信息的方式上必须富有创意。内容较多的应用程序可能需要将内容分布到多个屏幕上，或者在不同时间显示和隐藏内容的不同部分。View Controller 对象提供了管理与内容相关的视图、并协调这些视图显示和隐藏的基础设施。

在应用程序中使用 View Controller 的理由有很多，而回避它们的理由却很少。View Controller 让你更容易实现 iOS 应用程序中常见的许多标准界面行为。它们提供了默认行为，你可以直接使用，也可以在需要时进行自定义。它们还为组织应用程序的用户界面和内容提供了一种便捷的方式。

图 1-1 展示了一个管理食谱的 iPhone 应用程序中三个不同（但相关）屏幕的示例。第一个屏幕列出了该应用程序管理的所有食谱。点按其中一个食谱会显示第二个屏幕，展示该食谱的详细信息。在这个详情视图中点按食谱图片，会显示第三个屏幕，展示成品菜肴的全屏图片。管理这些屏幕的分别是各自独立的 View Controller 对象，其职责是呈现相应的视图对象、用数据填充这些视图，并响应与该视图的交互。

__图 1-1__  不同的屏幕由各自独立的 View Controller 管理

!

除了显示和管理视图之外，你还可以使用 View Controller 来管理屏幕之间的导航。在 iOS 中，有几种呈现新屏幕的标准技术。所有这些技术都是通过 View Controller 实现的，本文档的不同部分会分别加以讨论。

大多数 iOS 应用程序至少有一个 View Controller，有些则有多个。广义而言，View Controller 可分为三大类，分别反映了 View Controller 在你的应用程序中所扮演的角色。

_自定义 View Controller_ 是你出于在屏幕上呈现特定内容这一明确目的而定义的[控制器对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11)。大多数 iOS 应用程序使用几组不同的视图来呈现数据，每一组都以特定方式处理数据的呈现。例如，你可能有一组视图用于在表格中呈现条目列表，另一组则用于显示该列表中单个条目的详细信息。这类应用程序对应的架构会涉及创建各自独立的 View Controller，以管理每一组视图的编排与显示。

_容器 View Controller_ 是一种特定类型的 View Controller 对象，用于管理其他 View Controller 并定义它们之间的导航关系。navigation controller、tab bar controller 和 split view controller 都是容器 View Controller 的例子。你不需要自己定义容器 View Controller，而是直接使用系统提供的容器 View Controller。

_模态 View Controller_ 是由另一个 View Controller 以特定方式呈现的 View Controller（可以是容器 View Controller 或自定义 View Controller）。模态 View Controller 在应用程序中定义了一种特定的导航关系。以模态方式呈现 View Controller 最常见的原因，是为了提示用户输入一些数据。例如，你可能会以模态方式呈现一个 View Controller，让用户填写表单或从选择器界面中选择一个选项。不过，模态 View Controller 还有其他用途，详见 [模态 View Controller](Modal%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjrgewvgvzr)。

图 1-2 展示了 UIKit 框架中提供的 View Controller 类，以及一些与 View Controller 搭配使用的关键类。这些附加类通常由 View Controller 对象在内部使用，以实现特殊类型的界面。例如，`UITabBarController` 对象管理着一个 `UITabBar` 对象，后者实际负责显示与 tab bar 界面相关联的标签。其他框架也可能定义额外的 View Controller 对象，以呈现特定类型的界面。

__图 1-2__  UIKit 中的 View Controller 类

!

接下来的各节将更详细地介绍你用来组织和呈现应用程序内容的各类 View Controller。

自定义 View Controller 是应用程序内容的主要协调对象。几乎每个应用程序都至少有一个自定义 View Controller，复杂的应用程序可能会有很多个。自定义 View Controller 包含了促成应用程序部分数据与用于呈现该数据的视图之间进行交互所需的逻辑和粘合代码。该 View Controller 还可能与应用程序中的其他[控制器对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11)进行交互，包括[应用程序委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)和其他 View Controller。

你创建的每个自定义 View Controller 对象都负责管理单个视图层级中的所有视图。在 iPhone 应用程序中，视图层级中的视图传统上会覆盖整个屏幕，而在 iPad 应用程序中，它们可能只覆盖屏幕的一部分。View Controller 与其视图层级中的视图之间的一一对应关系，是关键的设计考量。你不应该使用多个自定义 View Controller 来管理同一视图层级的不同部分。同样，你也不应该使用单个自定义 View Controller 对象来管理多屏内容。

你可以通过直接[子类化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassDefinition.html#//apple_ref/doc/uid/TP40008195-CH6) [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 并向子类添加自定义代码来创建自定义 View Controller。一个典型的 `UIViewController` 子类的声明通常包括以下内容：

- 指向包含相应视图待显示数据的对象的[成员变量](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassDefinition.html#//apple_ref/doc/uid/TP40008195-CH6)
- 指向 View Controller 必须与之交互的关键视图对象的成员变量（或 outlet）
- 执行与视图层级中按钮及其他控件相关联任务的动作方法
- 实现 View Controller 自定义行为所需的其他任何方法

由于你使用它来管理自定义内容，这类 View Controller 中的大部分代码都将是应用程序特有的。不过，所有 View Controller 也都能支持一些共通的行为。针对这些共通行为，`UIViewController` 类定义了一些方法，你可以重写这些方法来实现所需的行为。这些共通行为包括视图管理、界面旋转管理以及低内存警告支持。

图 1-3 展示了示例项目 _BubbleLevel_ 中自定义 View Controller 的一个例子。该应用程序定义了 `LevelViewController` 类，它是 `UIViewController` 的直接后代。这个类监视加速度计数据中设备俯仰角的变化，并利用这些数据更新其关联的视图对象。View Controller 的 [view](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621460-view) 属性提供了对实际呈现内容的视图对象的引用。

__图 1-3__  BubbleLevel 应用程序中的自定义 View Controller

!

有关管理所有 View Controller 都需要的标准行为的信息，请参阅[自定义 View Controller](Custom%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzr)。

[UITableViewController](https://developer.apple.com/documentation/uikit/uitableviewcontroller) 类是另一种自定义 View Controller，专门用于管理表格数据。虽然不使用 table view controller 也完全可以管理表格，但该类为许多标准的表格相关行为（例如选择管理、行编辑、表格配置等）添加了自动支持。这些额外的支持能够最大限度地减少你创建和初始化基于表格的界面时所需编写的代码量。你可以在使用自定义 View Controller 的任何场合使用 table view controller。你也可以对其进行子类化，实现额外的自定义行为。当然，由这类 View Controller 管理的任何视图层级都应该包含一个 table view 对象。

图 1-4 展示了 table view controller 配置的一个例子。由于它是 [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 的子类，table view controller 仍然持有指向界面根视图的指针（通过其 [view](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621460-view) 属性），但它还另外持有一个指向该界面中所显示 table view 的指针。

__图 1-4__  管理表格数据

!

本文档仅涵盖所有 View Controller 共通的行为，不涉及 table view controller 特有的任何信息。有关 table view controller 中与表格相关行为的具体信息，请参阅 _[UITableViewController Class Reference](https://developer.apple.com/documentation/uikit/uitableviewcontroller)_。有关管理 table view 的更多一般性信息，请参阅 _[Table View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/AboutTableViewsiPhone/AboutTableViewsiPhone.html#//apple_ref/doc/uid/TP40007451)_。

navigation controller 是一种容器 View Controller，用于呈现按层级组织的数据。navigation controller 是 [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) 类的实例，这是一个你直接使用而不需要子类化的类。该类的方法支持管理一个基于栈的自定义 View Controller 集合。这个栈代表了用户在层级数据中所走过的路径，栈底反映了起始点，栈顶反映了用户在数据中的当前位置。

尽管 navigation controller 的主要职责是作为其他 View Controller 的管理者，但它也管理着少量视图。具体来说，它管理着一个导航栏，用于显示用户在数据层级中当前位置的信息、一个用于导航回上一屏幕的返回按钮，以及当前 View Controller 所需的任何自定义控件。navigation controller 还管理一个可选的工具栏，用于显示与当前屏幕相关的命令。在大多数情况下，你不会直接修改这些视图，而是通过 [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 类中提供的支持来配置它们。

图 1-5 展示了通讯录（Contacts）应用程序的一些屏幕，该应用程序使用 navigation controller 向用户呈现联系人信息。呈现给用户的每个屏幕都由一个自定义 View Controller 对象管理，该对象呈现数据层级中特定层级的信息。例如，根 View Controller 和列表 View Controller 以不同方式管理表格式联系人信息的呈现。详情 View Controller 则使用完全不同类型的屏幕来显示某个特定联系人的信息。当用户与界面中的控件交互时，这些控件会告诉 navigation controller 显示序列中的下一个 View Controller，或消除当前 View Controller。

__图 1-5__  在层级化的应用程序数据中导航

!

有关如何配置和使用 navigation controller 对象的信息，请参阅 [navigation controller](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzr)。

tab bar controller 是一种容器 View Controller，用于将应用程序划分为两种或更多种不同的操作模式。tab bar controller 是 [UITabBarController](https://developer.apple.com/documentation/uikit/uitabbarcontroller) 类的实例，这是一个你直接使用而不需要子类化的类。tab bar controller 的各个模式通过一个 tab bar 视图来呈现，该视图为每种受支持的模式显示一个标签。选择某个标签会使相关联的 View Controller 在屏幕上呈现其界面。

当你的应用程序需要呈现不同类型的数据，或以显著不同的方式呈现相同数据时，就可以使用 tab bar controller。tab bar controller 能够根据用户在 tab bar 视图上的点按，自动切换模式。如果模式数量超过了标签所能容纳的空间，tab bar controller 还会负责管理那些通常不可见标签的选择，以及可见标签的自定义。

图 1-6 展示了时钟（Clock）应用程序的几种模式，以及对应 View Controller 之间的关系。每种模式都有一个根 View Controller 来管理主要内容区域。以时钟应用程序为例，Clock 和 Alarm 这两个 View Controller 都显示了 navigation 风格的界面，以便在屏幕顶部容纳一些额外的控件。其他模式则使用自定义 View Controller 来呈现单个屏幕。

__图 1-6__  时钟应用程序的不同模式

!

有关如何配置和使用 tab bar controller 的信息，请参阅 [tab bar controller](Tab%20Bar%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgiwvgvzr)。

split view controller 是一种容器 View Controller，通常用于实现主从（master-detail）界面。split view controller 是 [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) 类的实例，这是一个你直接使用而不需要子类化的类。split view 界面的内容来自你提供的两个 View Controller。在横屏方向下，split view controller 会并排显示另外两个 View Controller 的内容。在竖屏方向下，它只会直接显示其中一个 View Controller，另一个则通过 popover 提供。

图 1-7 展示了示例应用程序 _[MultipleDetailViews](../../../samplecode/MultipleDetailViews/MultipleDetailViews.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzxgu)_ 中的 split view 界面。该界面的横屏版本并排显示列表视图和详情视图。在竖屏模式下，只显示详情视图，列表视图则通过 popover 提供。列表视图和详情视图都由一个自定义 View Controller 管理。

__图 1-7__  竖屏和横屏模式下的主从界面

!!

有关如何配置和使用 split view controller 的信息，请参阅 [Split View Controller](iPad-Specific%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqnrnknlte)。

模态 View Controller 并不是一个特定的 View Controller 类，而是一种向用户呈现任意 View Controller 的方式。容器 View Controller 定义了其所管理的 View Controller 之间的特定关系，而模态 View Controller 则让你自己定义这种关系。任何 View Controller 对象都可以以模态方式呈现任何其他 View Controller 对象。大多数情况下，你以模态方式呈现 View Controller，是为了从用户处收集信息，或是为了某个特定目的吸引用户的注意力。一旦该目的达成，你就会消除这个模态 View Controller，让用户继续在你的应用程序中导航。

图 1-8 展示了通讯录应用程序中的一个例子。当用户点击加号按钮以添加新联系人时，Contacts View Controller 会以模态方式呈现 New Contact View Controller。这就在这两个 View Controller 之间建立了父子关系。New Contact 屏幕会一直保持可见，直到用户取消操作，或提供了足够的联系人信息以便保存到联系人数据库中，此时 Contacts View Controller 就会消除其子级。

__图 1-8__  呈现一个模态 View Controller

!

值得注意的是，以模态方式呈现的 View Controller，其自身也可以再以模态方式呈现另一个 View Controller。这种链式呈现模态 View Controller 的能力，在你需要依次执行多个模态操作的情况下会很有用。例如，如果用户在前图的 New Contact 屏幕中点按 Add Photo 按钮，想要选择一张已有的图片，New Contact View Controller 就会以模态方式呈现一个图片选择器界面。用户必须先消除图片选择器屏幕，再单独消除 New Contact 屏幕，才能返回联系人列表。

有关模态 View Controller 用途以及如何在应用程序中呈现它们的更多信息，请参阅 [模态 View Controller](Modal%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjrgewvgvzr)。

大多数用于 iOS 应用程序的 Xcode 项目模板初始时都会为你提供至少一个 View Controller 类，有些还会提供多个 View Controller。这些初始类为你提供了典型 View Controller 中所包含的代码，旨在帮助你快速开始编写应用程序。不过要记住，这些模板只是一个起点。

模板应用程序的目的是向你展示针对特定类型应用程序进行开发的最佳入门方式。从与你想要创建的界面最相近的模板入手，总是最简单的做法。例如，如果你要创建一个类似股市（Stocks）或天气（Weather）的应用程序，就应该从 Utility Application 模板入手。另一方面，如果你打算使用 tab bar 将应用程序划分为不同的模式，就应该从 Tab Bar Application 模板入手。

如果你想探索基本的 View Controller 行为，View-based Application 模板是一个不错的起点。这类应用程序使用单个自定义 View Controller 来显示应用程序的内容。你可以通过以模态方式呈现额外的 View Controller，来扩展这一基本行为。

如果你想从零开始构建应用程序的用户界面，就从 Window-based Application 模板入手。该模板提供了一个配置极简的项目，你可以对其进行修改，加入所需的 View Controller。

有关在 Xcode 中创建项目的更多信息，请参阅 _[Xcode Project Management Guide](../../Developer%20Tools/Xcode%20Project%20Management%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmjx)_。

[下一页](Custom%20View%20Controllers.md)[上一页](About%20View%20Controllers.md)

