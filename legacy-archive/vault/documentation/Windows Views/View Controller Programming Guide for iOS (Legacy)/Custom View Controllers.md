---
title: iOS View Controller 编程指南（旧版）
apple_id: TP40011381
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerPGforiOSLegacy/BasicViewControllers/BasicViewControllers.html
archived_at: '2026-07-18T02:23:39.426794Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 编程指南（旧版）](About%20View%20Controllers.md)


[下一页](Navigation%20Controllers.md)[上一页](View%20Controller%20Basics.md)

# 自定义 View Controller

自定义 View Controller 是你用来呈现应用程序内容的方式。任何 View Controller 的职责都是管理某些内容的呈现，并协调该内容与应用程序底层数据对象之间的更新与同步。对于自定义 View Controller 而言，这意味着要创建一个用于呈现内容的视图，并实现将该视图的内容与应用程序数据结构同步所需的基础设施。

[UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 类提供了所有 View Controller（无论是否自定义）都需要的基本行为。本章将说明该类提供的基础行为，并展示如何按应用程序的需要修改这些行为。理解这些行为以及如何修改它们，对于实现应用程序的自定义 View Controller 至关重要；这些知识在与任何类型的 View Controller 交互时也同样有用。

[UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 类为实现所有自定义 View Controller 提供了基础设施。虽然你可以配置一个 `UIViewController` 类的实例来显示一些视图，但如果想实现更有意思的功能，就需要[定义一个自定义子类](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassDefinition.html#//apple_ref/doc/uid/TP40008195-CH6)。在子类中，你会用自定义方法给视图填充数据，并响应按钮和其他控件上的点按。不过，当你想调整 View Controller 的默认行为时，就需要[重写 `UIViewController` 类的方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57)。你可能还需要与其他 UIKit 类交互才能实现所需的行为。

图 2-1 展示了一些与自定义 View Controller 直接关联的关键对象。这些对象基本上都由 View Controller 自身拥有和管理。视图（可通过 [view](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621460-view) 属性访问）是唯一必须提供的对象，不过大多数 View Controller 还会拥有一些自定义对象，用来保存它们需要显示的数据。其他对象仅在需要支持导航栏、标签栏等界面特性时才会用到，即便如此，大多数情况下默认行为已经足够。

__图 2-1__  自定义 View Controller 剖析

!

虽然 View Controller 很少单独发挥作用，但自定义 View Controller 始终应当被设计成独立的对象。换句话说，一个 View Controller 应当封装管理其视图层级中各视图所需的全部行为。你的 View Controller 应当包含它所需的数据（或者至少是对它所控制数据的引用）、显示该数据所需的视图、用于适应系统变化（例如方向变化）的逻辑，以及验证或处理用户交互所需的代码。任何用于管理视图层级或数据模型某部分的自定义对象，都应当完全由该 View Controller 创建和管理。

当你想为应用程序实现一个自定义 View Controller 时，需要使用 Xcode 来搭建源文件。大多数 iOS 项目模板都至少包含一个 View Controller 类，你也可以按需在 Xcode 中创建新的 View Controller。

对于你所创建的任何自定义 View Controller，都有几项任务是你应当始终处理的：

- 你必须配置好由 View Controller 加载的视图；参见[为 View Controller 创建视图](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzs)。
- 你必须决定 View Controller 支持哪些方向；参见[管理 View Controller 的界面方向](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzt)。
- 你必须清理由 View Controller 管理的内存；参见[高效管理内存](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzu)。

在配置 View Controller 的视图时，你可能会发现需要为这些视图定义 action 方法或 outlet。例如，如果你的视图层级中包含一个表格，你可能想把指向该表格的指针存储在一个 outlet 中，以便之后访问。类似地，如果你的视图层级中包含按钮或其他控件，你可能希望这些控件在响应用户交互时调用相应的 action 方法。在反复完善[你的 View Controller 类定义](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassDefinition.html#//apple_ref/doc/uid/TP40008195-CH6)的过程中，你可能会发现需要向 View Controller 类添加以下内容：

- 指向包含相应视图所要显示数据的对象的[成员变量](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassDefinition.html#//apple_ref/doc/uid/TP40008195-CH6)
- 指向 View Controller 必须与之交互的关键视图对象的成员变量（或 outlet）
- 执行与视图层级中按钮及其他控件相关任务的 action 方法
- 实现 View Controller 自定义行为所需的任何其他方法

以上内容是你在创建的每个自定义 View Controller 类中最有可能包含的部分。不过，你还可能为 View Controller 添加其他方法来实现特定行为。这些方法中有许多都会利用 View Controller 基础设施中提供的钩子来实现常见任务。

- 你可以在 View Controller 的视图出现或从屏幕上消失时，相应地调整视图层级或应用程序状态；参见[响应显示相关通知](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzthe)。
- 你可以配置导航控制器和标签栏控制器所使用的对象，包括：

  - 导航项（如果该控制器与导航控制器界面搭配使用）；参见[定制导航栏外观](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzt)。
  - 工具栏项（如果关联的导航控制器显示工具栏）；参见[指定工具栏项](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzsgy)。
  - 标签栏项（如果该 View Controller 与标签栏控制器界面搭配使用）；参见[创建标签栏界面](Tab%20Bar%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgiwvgvzs)。
- 你可以在界面方向变化时调整视图层级；参见[响应方向变化](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsgm)。
- 你可以实现事件处理方法，用来捕获视图及其子视图未处理的事件；参见 _iOS 事件处理指南_。
- 你可以实现视图的可编辑版本；参见[为视图启用编辑模式](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvztga)。

在一个 View Controller 对象中，对相应视图的管理分为两个不同的周期：加载周期和卸载周期。每当应用程序的某个部分向 View Controller 请求指向其视图对象的指针、而该对象当前又不在内存中时，就会触发加载周期。此时，View Controller 会把视图加载到内存中，并保存一个指向该视图的指针以供后续使用。

如果你的应用程序之后收到内存不足警告，View Controller 随后可能会尝试卸载该视图。在卸载周期中，View Controller 会尝试释放其视图对象，使 View Controller 恢复到最初没有视图的状态。如果它能够成功释放视图，View Controller 就会保持没有视图对象的状态，直到该视图再次被请求时，加载周期才会重新开始。

在加载和卸载周期中，View Controller 会完成加载和卸载视图的大部分工作。不过，如果你的 View Controller 类保存了对视图层级中各视图的引用，或者需要在加载时对视图进行额外配置，你可以[重写](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57)特定方法（下文会加以说明）来执行任何额外的任务。

加载周期中发生的步骤如下：

1. 应用程序的某个部分请求获取 View Controller 的 [view](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621460-view) 属性中的视图。
2. 如果该视图当前不在内存中，View Controller 会调用它的 [loadView](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621454-loadview) 方法。
3. `loadView` 方法会执行以下两者之一：

   - 如果你重写了这个方法，你的实现就负责创建所有必需的视图，并为 `view` 属性赋一个非 `nil` 的值。
   - 如果你没有重写这个方法，默认实现会使用 View Controller 的 [nibName](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621487-nibname) 和 [nibBundle](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621489-nibbundle) 属性，尝试从指定的 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)中加载视图。如果找不到指定的 nib 文件，它会查找名称与 View Controller 类名匹配的 nib 文件并加载该文件。
   - 如果没有可用的 nib 文件，该方法会创建一个空的 [UIView](https://developer.apple.com/documentation/uikit/uiview) 对象并赋给 `view` 属性。
4. View Controller 调用它的 [viewDidLoad](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621495-viewdidload) 方法来执行任何额外的加载时任务。

图 2-2 直观展示了加载周期，包括其中调用的几个方法。你的应用程序可以按需重写 `loadView` 和 `viewDidLoad` 方法，以实现你希望 View Controller 具备的行为。

__图 2-2__  将视图加载到内存中

!

卸载周期中发生的步骤如下：

1. 应用程序从系统收到一次内存警告。
2. 每个 View Controller 都会调用它的 [didReceiveMemoryWarning](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621409-didreceivememorywarning) 方法：

   - 如果你重写了这个方法，应当用它来释放 View Controller 对象不再需要的任何自定义数据。不应该用它来释放 View Controller 的视图。你必须在实现中的某个位置调用 `super`，以执行默认行为。
   - 默认实现只有在判断释放视图是安全的情况下才会释放视图。
3. 如果 View Controller 释放了它的视图，就会调用它的 [viewDidUnload](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621383-viewdidunload) 方法。你可以重写这个方法，为你的视图和视图层级执行任何额外的清理工作。

图 2-3 直观展示了 View Controller 的卸载周期。

__图 2-3__  从内存中卸载视图

!

自定义 View Controller 是 [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 的子类，用来呈现应用程序的内容。许多 Xcode 项目模板都自带一个可供你按需修改的自定义 View Controller 类。如果你需要创建其他自定义 View Controller，请执行以下操作：

1. 选择 File > New File，向项目中添加一个新的源文件。

   你想要创建一个新的 `UIViewController` 子类。在 New File 对话框的 Cocoa Touch Classes 部分中，有这类类的模板。
2. 给新的 View Controller 文件起一个合适的名称，并把它添加到项目中。
3. 保存源文件。

有了 View Controller 的源文件之后，你就可以实现呈现内容所需的行为了。以下各小节描述了你可以使用自定义 View Controller 执行的关键任务。有关创建 View Controller 的更多信息，参见 _[UIViewController Class Reference](https://developer.apple.com/documentation/uikit/uiviewcontroller)_。

View Controller 的主要工作是按需加载和卸载它的视图。大多数 View Controller 都从关联的 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)加载视图。使用 nib 文件的好处是，它们让你可以以图形化方式布局和配置视图，从而更轻松、更快速地调整布局。不过，如果你愿意，也可以以编程方式创建视图。

Interface Builder 提供了一种直观的方式来创建和配置 View Controller 的视图。顾名思义，Interface Builder 是一个以图形化方式（而非编程方式）构建应用程序界面的工具。使用这个应用程序时，你通过直接操作视图和控件——把它们拖入工作区、定位、调整尺寸，并使用检查器窗口修改它们的属性——来组装界面。最终的结果会保存在一个 nib 文件中，其中存储了你组装的对象集合，以及你所做的全部自定义信息。

有两种方式可以为 View Controller 配置 nib 文件：

- 创建一个 _分离式 nib 文件_，把视图单独存储在一个 nib 文件中。
- 创建一个 _整合式 nib 文件_，把视图和 View Controller 存储在同一个 nib 文件中。

在这两种方式中，使用分离式 nib 文件是迄今为止更受青睐的做法。分离式 nib 文件提供了更稳健的解决方案，尤其是在内存管理方面。在内存不足的情况下，分离式 nib 文件的内容可以按需从内存中清除，而不会影响其所属 View Controller 对象的状态。整合式 nib 文件则不然，其内容必须一直保留在内存中，直到该 nib 文件中的所有对象都不再需要为止。

创建分离式 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)的过程包含两个独立的实现步骤：

- 你必须用视图配置一个 nib 文件。
- 你必须把该 nib 文件与你的 View Controller 对象关联起来。

nib 文件本身的配置相对简单直接。如果你从零开始创建 nib 文件，应当以 Interface Builder 中的 Cocoa Touch View 模板作为起点。该模板创建的 nib 文件包含 File's Owner 占位符和一个自定义视图对象。把这个新的 nib 文件添加到你的 Xcode 项目中，然后按如下方式配置其内容：

1. 把 File's Owner 占位符的类名设置为你的 View Controller 类。

   你应该已经在 Xcode 项目中创建了这个类。对于新的 nib 文件，File's Owner 的类默认设置为 `NSObject`。（如果你正在编辑某个 Xcode 项目模板为你提供的 nib 文件，该类可能已经被设置为正确的 View Controller 类名。）
2. 确保 File's Owner 占位符的 `view` outlet 已连接到 nib 文件中的顶层 View 对象。

   这个 `view` outlet 由 `UIViewController` 类定义，并由所有 View Controller 对象继承。如果你在 File's Owner 占位符中没有看到这个 outlet，请检查你是否已把 nib 文件添加到 Xcode 项目中。把 nib 文件与 Xcode 项目关联起来，可以让 Interface Builder 自动获取该项目中各个类的信息，这对于确定这些类可用的 outlet 和 action 是必需的。

   如果你忘记连接这个 outlet，那么当 nib 文件被加载时，你的 View Controller 类的 [view](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621460-view) 属性会被设置为 `nil`，这会导致你的视图无法呈现在屏幕上。
3. 配置视图本身，并添加显示应用程序内容所需的任何子视图。
4. 保存 nib 文件。

创建好 nib 文件并将其添加到 Xcode 项目后，你需要用该 nib 文件的名称来[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)你的 View Controller 对象。如何初始化 View Controller 对象取决于你创建它的方式。如果你是以编程方式创建 View Controller，那么在初始化 View Controller 对象时，把 nib 文件的名称传给 [initWithNibName:bundle:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621359-initwithnibname) 方法。如果你是从一个单独的 nib 文件（不是包含视图的那个）加载 View Controller 对象，请使用 Interface Builder 把该 View Controller 对象的 NIB Name 属性值设置为你视图所在 nib 文件的名称。

清单 2-1 展示了如何以编程方式创建并初始化一个 View Controller 的示例。在这个例子中，自定义类使用一个同名的 nib 文件来存储它的视图。初始化 View Controller 之后，你就可以按需使用这个 View Controller，包括像示例中那样把它呈现给用户。

__清单 2-1__  以编程方式创建 View Controller 对象

```objc
- (void)displayModalView
{
   MyViewController* vc = [[[MyViewController alloc] initWithNibName:@"MyViewController"
                               bundle:nil] autorelease];
   [self presentModalViewController:vc animated:YES];
}
```

对于分离式 nib 文件，当访问 View Controller 对象的 `view` 属性、且该视图当前不在内存中时，实际加载 nib 文件的操作会自动发生。默认的 [loadView](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621454-loadview) 方法使用 [nibName](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621487-nibname) 和 [nibBundle](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621489-nibbundle) 属性来定位所需的 nib 文件，并将其内容加载到内存中。

图 2-4 展示了一个 View Controller 及其分离式 nib 文件在加载之前的运行时配置。View Controller 的 `nibName` 属性中存储着一个字符串，记录着 nib 文件的名称。这个字符串用于在应用程序的 bundle 中定位该 nib 文件。在 nib 文件内部，File's Owner 占位符代表着 View Controller 对象，用于把 View Controller 的 outlet 和 action 连接到 nib 文件中的对象。nib 文件加载完成后，View Controller 对象的 `view` 属性就会指向来自该 nib 文件的视图。

__图 2-4__  从分离式 nib 文件加载视图

!

有关如何创建 nib 文件或配置其内容的更多信息，参见 _[Interface Builder User Guide](../../Developer%20Tools/Interface%20Builder%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbu)_。有关为 View Controller 配置自定义 outlet 和 action 的信息，参见[为 View Controller 配置 Action 和 Outlet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzrge)。

如果你的应用程序只有一个屏幕，你可以把该屏幕的视图与管理它们的 View Controller 一起放在同一个 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)中。通常不建议把视图和自定义 View Controller 对象存储在同一个 nib 文件中，因为这样往往会导致系统在内存不足的情况下无法卸载视图。不过，如果视图本身永远不会被卸载，那么把它和它的 View Controller 对象放在同一个 nib 文件中或许是最合理的做法。

图 2-5 展示了一个在窗口中呈现单一屏幕的应用程序的主 nib 文件。在这个例子中，nib 文件同时包含一个自定义 View Controller 对象（`MyViewController`）以及由该 View Controller 管理的视图。请注意，在文档窗口中，视图对象嵌套在 View Controller 对象内部。以这种方式嵌套视图是更受青睐的做法，因为它让 Interface Builder 能够让视图和它的 View Controller 保持同步。

__图 2-5__  在 nib 文件中嵌入 View Controller

!

要配置图 2-5 中所示的 nib 文件，你需要执行以下操作：

1. 把一个 View Controller（`UIViewController`）对象从库中拖到你的 Interface Builder 文档窗口中。
2. 用以下方式之一，把一个通用 View 对象添加到该 View Controller 中：

   - 把视图拖到 View Controller 的工作区窗口中。
   - 把视图拖到 Interface Builder 文档窗口中的 View Controller 对象上。
3. 把一个 Image View 从库中拖到通用视图上。
4. 把一个 Table View 从库中拖到通用视图上。
5. 保存 nib 文件。

每当你向 nib 文件的顶层添加对象时，都应该始终把这些对象连接到 nib 文件其他地方的某个 outlet。就上面这个 nib 文件而言，这意味着要在你的应用程序委托对象中定义一个 outlet，并把该 outlet 连接到自定义 View Controller 对象。没有这个 outlet，你的代码在运行时就无法访问该 View Controller。此外，由于顶层对象会先被 retain 再被 autorelease，如果你没有 retain 这个对象，它就有可能在你还没来得及使用之前就被释放了。

由于 View Controller 和它的视图存储在同一个 nib 文件中，nib 文件加载到内存后，两者都可以立即使用。对于主 nib 文件而言，你通常会在应用程序委托的 [applicationDidFinishLaunching:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching) 方法中加入一些代码，把 View Controller 的视图添加到你的窗口中，具体做法参见[呈现 View Controller 的视图](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsgu)。

为了帮助你正确布局视图的内容，Interface Builder 提供了一些控件，让你可以指定视图是否带有导航栏、工具栏，或其他可能影响自定义内容位置的对象。表 2-1 列出了你可以配置的项目，以及它们对你的 View Controller 或视图产生的影响。对于分离式 nib 文件，你通过修改视图对象的属性来配置这些项目；对于整合式 nib 文件，你通过修改 View Controller 对象的属性来配置这些项目。

__表 2-1__  View Controller 的可配置项

| 可配置项 | 说明 |
| 状态栏 | 你可以通过修改 Attributes inspector 中的 Status Bar 属性，来指定状态栏是否可见以及应用程序显示哪种类型的状态栏。这个属性仅用于设计目的，目的是让你能够完整地了解视图和控件在与状态栏一起显示时的外观。Status Bar 属性的值不会保存到你的 nib 文件中。状态栏的实际样式（以及是否显示）必须由应用程序在运行时以编程方式设置。 |
| 导航栏 | 你可以通过修改 Attributes inspector 中 Top Bar 属性的值，来指定视图是否带有导航栏。这个属性仅用于设计目的，目的是让你能够完整地了解视图和控件在与导航栏一起显示时的外观。Interface Builder 让你可以配置多种不同的导航栏样式，包括带有额外提示文字空间的导航栏。Top Bar 属性的值不会保存到你的 nib 文件中。导航栏的实际样式（以及是否显示）由其所属的导航控制器控制。有关如何配置导航栏的信息，参见[定制导航栏外观](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzt)。 |
| 标签栏 | 你可以通过修改 Attributes inspector 中 Bottom Bar 属性的值，来指定视图是否带有标签栏。这个属性主要用于设计目的，目的是让你能够完整地了解视图和控件在有标签栏存在时的外观。如果你实际是在配置一个标签栏控制器，标签栏项可以被添加到与标签栏界面各个标签关联的独立 View Controller 上。有关配置标签栏控制器和标签栏项的更多信息，参见[创建标签栏界面](Tab%20Bar%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgiwvgvzs)。 |
| 工具栏项 | 要指定你的视图使用由导航控制器提供的工具栏，请把 Attributes inspector 中的 Bottom Bar 属性设置为 Toolbar。这个属性主要用于创建导航界面时的设计目的。你可以用它来查看视图和控件在有标签栏存在时的外观。如果你实际是在配置一个导航控制器，你还可以把 View Controller 工具栏所用的 bar button item 包含在你的 nib 文件中。有关在导航界面中配置工具栏的更多信息，参见[显示导航工具栏](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzu)。 |
| 标题 | 在整合式 nib 文件中，你可以通过为 Title 属性赋一个合适的值，来为你的 View Controller 指定标题。导航控制器和标签栏控制器会把这个属性的值作为显示该 View Controller 时使用的默认值。 |
| Nib 名称 | 对于嵌入在 nib 文件中的 View Controller，你使用 NIB Name 属性来指定包含该 View Controller 视图的分离式 nib 文件的名称。有关如何配置分离式 nib 文件的信息，参见[在分离式 Nib 文件中存储视图](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvztgm)。当 View Controller 在运行时被加载到内存中时，这个属性的值会被用来设置 View Controller 的 [nibName](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621487-nibname) 属性的值。 |

在 nib 文件中配置导航控制器和标签栏控制器要稍微复杂一些，具体内容将在以下位置讨论：

- 有关如何单独配置导航控制器对象的信息，参见[创建导航界面](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzsg4)。
- 有关如何单独配置标签栏控制器的信息，参见[创建标签栏界面](Tab%20Bar%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgiwvgvzs)。
- 有关如何配置导航控制器和标签栏控制器组合的信息，参见[在标签栏界面中添加导航控制器](Combined%20View%20Controller%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgqwvgvzs)。

无论你使用的是分离式还是整合式 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)，配置 View Controller 的 action 和 outlet 的方式本质上是相同的。使用 Interface Builder，你可以在界面中的视图与控件同代表你的 View Controller 的对象之间建立连接。在整合式 nib 文件中，你可以直接连接到 View Controller 对象；而在分离式 nib 文件中，你连接的是代表你 View Controller 对象的 File's Owner 占位符。

清单 2-2 展示了自定义 `MyViewController` 类的定义，其中定义了两个自定义 outlet（由 `IBOutlet` 关键字标示）和一个 action 方法（由 `IBAction` 返回类型标示）。这些 outlet 存储着指向 nib 文件中一个按钮和一个文本框的引用，而这个 action 方法则响应该按钮上的点按。

__清单 2-2__  自定义 View Controller 类的声明

```objc
@interface MyViewController : UIViewController
{
  id myButton;
  id myTextField;
}
@property (nonatomic) IBOutlet id myButton;
@property (nonatomic) IBOutlet id myTextField;

- (IBAction)myAction:(id)sender;
```

图 2-6 展示了在这样一个 `MyViewController` 类中，你需要在各个对象之间建立的连接。这个 nib 文件按照[为 View Controller 配置 Action 和 Outlet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzrge)中的说明进行配置：File's Owner 占位符的类被设置为该 View Controller 类，且 File's Owner 的 `view` outlet 已连接到顶层视图对象。这个 nib 文件还包含 `MyViewController` 类的 outlet 和 action 同相应 nib 文件对象之间的连接。

__图 2-6__  `MyViewController.nib` 的内容

!

当前面配置好的 `MyViewController` 类被创建并以模态方式呈现时，View Controller 基础设施会自动加载 nib 文件，并重新配置所有的 outlet 或 action。因此，等到视图呈现给用户时，你的 View Controller 的 outlet 和 action 都已设置完毕，可供使用。这种在运行时代码与设计时资源文件之间架起桥梁的能力，正是 nib 文件强大之处的体现之一。

如果你更愿意以编程方式创建视图，而不是使用 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)，你需要在 View Controller 的 [loadView](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621454-loadview) 方法中完成这项工作。如果你打算以编程方式创建视图，就必须[重写](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57)这个方法。你对这个方法的实现应当执行以下操作：

1. 创建一个尺寸适合屏幕的根视图对象。

   根视图充当着与你的 View Controller 关联的所有其他视图的容器。你通常会把这个视图的 frame 定义为与应用程序窗口的尺寸相匹配，而应用程序窗口本身应当铺满整个屏幕。不过，View Controller 也会按需调整 frame 的尺寸，以适应系统状态栏、导航栏或标签栏等各种视图的存在。

   你可以使用一个通用的 [UIView](https://developer.apple.com/documentation/uikit/uiview) 对象、你自定义的视图，或任何其他能够缩放以铺满屏幕的视图。
2. 创建任何额外的子视图，并把它们添加到根视图中。对于每个视图，你应当执行以下操作：

   1. 创建并初始化该视图。对于系统视图，你通常使用 [initWithFrame:](https://developer.apple.com/documentation/uikit/uiview/1622488-init) 方法来指定该视图的初始尺寸和位置。
   2. 使用 [addSubview:](https://developer.apple.com/documentation/uikit/uiview/1622616-addsubview) 方法把该视图添加到父视图中。
   3. 调用该视图的 [release](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/release) 方法来释放它。
3. 把根视图赋给你 View Controller 的 [view](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621460-view) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)。
4. 释放根视图。

在创建每个视图后不久就将其释放，这个想法听起来可能有些奇怪，但一旦你把某个视图添加到视图层级中，或保存了对它的引用，这恰恰就是你想要做的事。任何对象在创建时的初始[保留计数](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)都是 1。由于父视图会自动 retain 它的子视图，因此在子视图被添加到其父视图之后释放它是安全的。同样，用于存储根视图的 `view` 属性使用 retain 语义来防止该视图被释放。因此，释放每个视图会把所有权转移到合适的地方，并防止该对象之后发生内存泄漏。

清单 2-3 展示了示例项目 _Metronome_ 中 `MetronomeViewController` 类的 `loadView` 方法。这个方法创建了一个自定义视图，并做了一些基本设置，包括把这个自定义视图赋给 View Controller 的 `view` 属性（该属性会 retain 这个视图）。在这个例子中，View Controller 的 `metronomeView` 属性是一个额外的属性，用于存储指向该视图的指针；不过，这个属性使用赋值语义，以避免潜在的保留（retain）问题。

__清单 2-3__  在 Metronome 应用程序中以编程方式创建视图

```objc
- (void)loadView {

    self.wantsFullScreenLayout = YES;

    MetronomeView *view = [[MetronomeView alloc]
                           initWithFrame:[UIScreen mainScreen].applicationFrame];
    view.metronomeViewController = self;
    self.view = view;
    self.metronomeView = view;

    [view release];
}
```

如果你使用属性或自定义存取方法（setter method）retain 了任何视图对象，你应当始终记得实现一个 [viewDidUnload](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621383-viewdidunload) 方法，把这些属性设置为 `nil`。如果你使用 outlet 来存储对视图的引用，而这些 outlet 使用带有 retain 语义的属性或其他存取方法，这一点尤为重要。有关管理视图相关内存的更多信息，参见[高效管理内存](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzu)。

View Controller 的视图一旦被加载到内存中，就会一直保留在内存里，直到出现内存不足的情况，或者 View Controller 本身被释放（deallocate）。在内存不足的情况下，[UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 的默认行为是：如果 [view](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621460-view) 属性中存储的视图对象当前没有被使用，就释放该对象。不过，如果你的自定义 View Controller 类存储了指向视图层级中任何视图的 outlet 或指针，那么在顶层视图对象被释放时，你也必须释放这些引用。如果不这样做，会导致这些对象无法立即从内存中移除，并且如果你之后覆写了指向它们的任何指针，还可能造成内存泄漏。

有两个地方，你的 View Controller 应当始终在其中清理对视图对象的任何引用：

- [dealloc](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/dealloc) 方法
- [viewDidUnload](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621383-viewdidunload) 方法

如果你使用[声明属性（declared property）](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)来存储对视图的引用，并且该属性使用 retain 语义，那么把它赋值为 `nil` 就足以释放该视图。由于属性使用起来十分方便，因此它是迄今为止管理视图对象的首选方式。如果你不使用属性，就必须在把相应的指针值设置为 `nil` 之前，向你显式 retain 过的任何视图发送一条 `release` 消息。

有关内存管理最佳实践的信息，参见[高效管理内存](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzu)。

在 View Controller 和[内存管理](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)方面，有两个问题需要考虑：

- 如何高效地分配内存？
- 何时以及如何释放内存？

虽然内存分配的某些方面完全由你自行决定，但 [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 类中有几个方法通常都与内存管理任务有一定关联。表 2-2 列出了你在 View Controller 对象中可能进行内存分配或释放的各个位置，以及关于你在每个位置应当做些什么的信息。

__表 2-2__  分配和释放内存的位置

| 任务 | 方法 | 说明 |
| 分配 View Controller 所需的关键数据结构 | 初始化方法 | 你的自定义[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)方法（无论命名为 `init` 还是其他名称）始终负责把 View Controller 对象置于一个已知的良好状态。这包括分配确保正常运行所需的各种数据结构。 |
| 创建视图对象 | [loadView](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621454-loadview) | 只有当你打算以编程方式创建视图时，才需要重写 `loadView` 方法。如果你是从 nib 文件加载视图，你所要做的只是使用 [initWithNibName:bundle:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621359-initwithnibname) 方法，用相应的 nib 文件信息初始化你的 View Controller。 |
| 分配或加载要在视图中显示的数据 | [viewDidLoad](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621495-viewdidload) | 任何与视图对象相关联的数据都应当在 `viewDidLoad` 方法中创建或加载。等到这个方法被调用时，你的视图对象已经保证存在，并处于已知的良好状态。 |
| 释放对视图对象的引用 | [viewDidUnload](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621383-viewdidunload)  [dealloc](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/dealloc) | 如果你使用 outlet 或类中的其他成员变量 retain 了视图层级中的任何视图对象，那么当这些视图不再需要时，你必须始终释放这些 outlet。释放某个视图对象后，务必把你的 outlet 或变量设置为 `nil`，以确保安全。有关视图何时会被释放的更多信息，参见[理解视图管理周期](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzrhe)。 |
| 在视图未显示时释放不需要的数据 | [viewDidUnload](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621383-viewdidunload) | 你可以使用 `viewDidUnload` 方法来释放任何特定于视图、并且在该视图再次被加载到内存时可以轻松重新创建的数据。不过，如果重新创建这些数据可能过于耗时，你也不必在这里释放相应的数据对象。相反，你应当考虑在 `didReceiveMemoryWarning` 方法中释放这些对象。 |
| 响应内存不足通知 | [didReceiveMemoryWarning](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621409-didreceivememorywarning) | 使用这个方法来释放与你的 View Controller 关联的所有非关键性自定义数据结构。虽然你不会用这个方法来释放对视图对象的引用，但你可能会用它来释放尚未在 `viewDidUnload` 方法中释放的任何与视图相关的数据结构。（视图对象本身应当始终在 `viewDidUnload` 方法中释放。） |
| 释放 View Controller 所需的关键数据结构 | [dealloc](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/dealloc) | 使用这个方法来释放与你的 View Controller 关联的所有数据结构。如果你的 View Controller 仍有值不为 `nil` 的 outlet 或其他变量，你应当在这里释放它们。 |

基于 iOS 的设备上配备的加速度计使确定设备的当前方向成为可能。UIKit 框架会利用这一信息，在适当的时候使应用程序的用户界面方向与设备方向保持一致。虽然应用程序默认只支持纵向，但你可以按需配置 View Controller 以支持其他方向。

支持其他方向需要对你的视图以及管理这些视图的 View Controller 进行额外配置。支持多种界面方向最简单的方式是执行以下操作：

- 重写 View Controller 的 [shouldAutorotateToInterfaceOrientation:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621459-shouldautorotatetointerfaceorien) 方法，声明它支持哪些方向；参见[声明支持的界面方向](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsgi)。
- 为 View Controller 视图层级中的每个视图配置自动调整尺寸的掩码（autoresizing mask）；参见[配置视图以支持多种方向](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsgq)。

对许多应用程序而言，这两个步骤应当就已经足够了。不过，如果视图的自动调整尺寸行为无法为每种方向带来你所需要的布局，你可以重写其他 View Controller 方法，并用它们在方向变化发生时微调你的布局。[UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 类提供了一系列通知，让你能够响应方向变化的不同阶段，并按需对你的视图（或应用程序的其他部分）进行调整。这些通知的详细说明参见[响应方向变化](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsgm)。

当基于 iOS 的设备方向发生变化时，系统会发出一条 [UIDeviceOrientationDidChangeNotification](https://developer.apple.com/documentation/uikit/uidevice/1620025-orientationdidchangenotification) 通知，让任何感兴趣的对象知道该变化已经发生。默认情况下，UIKit 框架会拦截这条通知，并用它来自动更新你的界面方向。这意味着，除了少数例外情况，你基本上不需要自己处理这条通知。相反，你只需要在 View Controller 类中实现相应的方法来响应方向变化即可。

在一个 iOS 应用程序中，窗口对象承担了与切换当前方向相关的大部分工作。不过，它会与应用程序的各个 View Controller 协同工作，来决定是否应当发生方向变化，以及如果发生的话，应当调用哪些额外的方法来响应这一变化。具体来说，它只与那个根视图最近被添加到窗口中或在窗口中被呈现的 View Controller 协同工作。换句话说，窗口对象只与最前面的 View Controller 协同工作，而该 View Controller 的视图必须是通过[呈现 View Controller 的视图](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsgu)中描述的某种机制显示出来的。

实际的旋转过程会沿着两条路径之一进行，具体取决于相关 View Controller 的实现方式。最常见的路径是执行一步式旋转，但如果两步式旋转能带来更好的体验，View Controller 也可以支持它。一步式旋转过程在 iOS 3.0 及以后的版本中可用，由于它比两步式过程更高效，因此更受青睐。究竟采用哪条路径，取决于你的 View Controller 子类以及你[重写](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57)了哪些方法。如果你重写了任何与一步式过程相关的方法，窗口对象就会使用该过程；否则，它会使用两步式过程。

无论使用哪种旋转过程，View Controller 的方法都会在旋转的各个阶段被调用，让 View Controller 有机会执行额外的任务。你可以用这些方法来隐藏或显示视图、重新定位或调整视图尺寸，或者通知应用程序的其他部分方向已经发生变化。由于你的自定义方法是在旋转操作期间被调用的，你应当避免在其中执行任何耗时的操作。你还应当避免用一整套新的视图替换整个视图层级。对于为不同方向提供独特视图，有更好的做法，例如以模态方式呈现一个新的 View Controller（如[创建备用的横屏界面](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsgy)中所述）。

有关一步式和两步式旋转过程中所发生步骤序列的详细信息，参见[响应方向变化](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsgm)。

如果你的 View Controller 所管理的视图支持默认纵向以外的方向，你必须重写 `shouldAutorotateToInterfaceOrientation:` 方法，说明你的视图支持哪些方向。你应当始终在设计时就选定视图所支持的方向，并按照这些方向来编写代码。基于运行时信息动态选择要支持哪些方向，并没有什么好处。即便你这样做了，仍然要实现支持所有可能方向所需的代码，因此你不妨一开始就直接决定是否支持某个方向。

清单 2-4 展示了一个相当典型的 `shouldAutorotateToInterfaceOrientation:` 方法实现，该 View Controller 支持默认的纵向以及向左横向。你自己对这个方法的实现应当同样简单。

__清单 2-4__  实现 `shouldAutorotateToInterfaceOrientation:` 方法

```objc
- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)orientation
{
   if ((orientation == UIInterfaceOrientationPortrait) ||
       (orientation == UIInterfaceOrientationLandscapeLeft))
      return YES;

   return NO;
}
```

如果你的应用程序同时支持两种横向，可以使用 `UIInterfaceOrientationIsLandscape` 宏作为快捷方式，而不必显式地把 _orientation_ 参数与两个横向常量分别比较。UIKit 框架类似地定义了一个 `UIInterfaceOrientationIsPortrait` 宏，用于识别纵向的两种变体。

当用户界面的方向发生变化时，受影响视图的 bounds 会根据它们的自动调整尺寸掩码自动被修改。每个视图的 [autoresizingMask](https://developer.apple.com/documentation/uikit/uiview/1622559-autoresizingmask) 属性都包含一些常量，描述该视图的 bounds 相对于其 superview 应如何变化。每个视图会先调整自身的 bounds，然后再让它的每个子视图根据自身的自动调整尺寸行为来调整自己的尺寸。最终的结果是：只要你恰当地配置好视图的自动调整尺寸行为，你的视图就能自动适应方向的变化。

如果视图的自动调整尺寸行为无法提供你所需要的精确布局，你可能想通过提供自己的自定义布局代码，来替换或补充这些行为。[UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 类定义了几个在方向变化之前、期间和之后被调用的方法。你可以使用这些方法来按需修改视图的布局。

有关旋转过程中会调用哪些方法的信息，参见[响应方向变化](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsgm)。有关视图的自动调整尺寸属性及其对视图的影响的更多信息，参见 _[View Programming Guide for iOS](../View%20Programming%20Guide%20for%20iOS/About%20Windows%20and%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbt)_。

当设备的方向发生变化时，View Controller 可以通过对其视图的方向做出相应改变来响应。如果新的方向受支持，View Controller 在进行这一改变的过程中会产生一系列通知，让你的代码有机会做出响应。旋转通知可以以一步式或两步式过程发生。

你可能想要响应方向变化的原因，是为了对视图层级进行调整。例如，你可能会利用这些通知来进行以下几类改变：

- 显示或隐藏特定于某个方向的视图。
- 根据新的方向调整视图的位置或尺寸。
- 更新应用程序的其他部分，以反映方向的变化。

只要有可能，UIKit 框架就会使用一步式旋转过程来旋转你的视图。不过，它实际使用一步式还是两步式过程，取决于你自己。两步式过程会用到一些一步式过程不会用到的方法，反之亦然；如果你重写了任何一步式方法，就会使用一步式过程。如果你只重写了两步式过程所用的方法，就会使用两步式过程。以下各小节描述了与每种过程相关联的方法。你也可以在 _[UIViewController Class Reference](https://developer.apple.com/documentation/uikit/uiviewcontroller)_ 中找到有关这些方法的信息（包括它们会触发一步式还是两步式过程）。

在 iOS 3.0 及以后的版本中，你可以使用一步式旋转方法，在方向变化即将发生前以及刚发生后进行改变。在这个过程中，会发生以下事件序列：

1. 窗口检测到设备方向发生了变化。
2. 窗口寻找一个合适的 View Controller，并调用它的 [shouldAutorotateToInterfaceOrientation:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621459-shouldautorotatetointerfaceorien) 方法，以确定它是否支持新的方向。

   容器 View Controller 可能会拦截这个方法，并使用自己的启发式规则来判断是否应当发生方向变化。例如，标签栏控制器只有在其所管理的全部 View Controller 都支持新方向时，才会允许方向变化发生。
3. 如果新方向受支持，窗口会调用该 View Controller 的 [willRotateToInterfaceOrientation:duration:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621376-willrotate) 方法。

   容器 View Controller 会把这条消息转发给当前显示的自定义 View Controller。你可以在自定义 View Controller 中重写这个方法，在界面旋转之前隐藏视图或对视图布局做出其他改变。
4. 窗口调整该 View Controller 视图的 bounds。

   这会导致视图层级中的每个视图根据其自动调整尺寸掩码来调整尺寸。
5. 窗口调用该 View Controller 的 [didRotateFromInterfaceOrientation:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621492-didrotatefrominterfaceorientatio) 方法。

   容器 View Controller 会把这条消息转发给当前显示的自定义 View Controller。这标志着旋转过程的结束。你可以使用这个方法来显示视图、改变视图的布局，或对你的应用程序做出其他改变。

图 2-7 直观展示了上述步骤，同时也展示了在这个过程的各个阶段中，界面看起来会是什么样子。

__图 2-7__  处理一步式界面旋转

!

在所有版本的 iOS 中，你都可以使用两步式通知来响应界面方向的变化。在两步式过程中，会发生两次独立的旋转。第一步中，界面只旋转到目的地的一半。第二步中，旋转会从这个中间点继续旋转到最终的方向。在整个过程中，你的应用程序都会收到通知，让你能够在旋转之前、期间和之后做出响应。

两步式旋转过程中会发生以下事件序列：

1. 窗口检测到设备方向发生了变化。
2. 窗口寻找一个合适的 View Controller，并调用它的 [shouldAutorotateToInterfaceOrientation:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621459-shouldautorotatetointerfaceorien) 方法，以确定它是否支持新的方向。

   容器 View Controller 可能会拦截这个方法，并使用自己的启发式规则来判断是否应当发生方向变化。例如，标签栏控制器只有在其所管理的全部 View Controller 都支持新方向时，才会允许方向变化发生。
3. 如果新方向受支持，窗口会调用该 View Controller 的 [willRotateToInterfaceOrientation:duration:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621376-willrotate) 方法。

   容器 View Controller 会把这条消息转发给当前显示的自定义 View Controller。你可以使用这个方法，在界面旋转之前隐藏视图或对视图布局做出其他改变。
4. 窗口调用该 View Controller 的 [willAnimateFirstHalfOfRotationToInterfaceOrientation:duration:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621469-willanimatefirsthalfofrotationto) 方法。

   容器 View Controller 会把这条消息转发给当前显示的自定义 View Controller。你可以使用这个方法，在界面旋转之前隐藏视图或对视图布局做出其他改变。
5. 窗口执行前半段旋转。

   这会导致视图层级中每个视图的 bounds 根据其自动调整尺寸行为进行调整。虽然大多数旋转都是从纵向变为横向（因此旋转 45 度到达中间点），但也有可能从向左横向旋转到向右横向，或者从纵向旋转到倒转纵向。在后面这些情况下，前半段旋转会是 90 度。
6. 窗口调用该 View Controller 的 [didAnimateFirstHalfOfRotationToInterfaceOrientation:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621496-didanimatefirsthalfofrotationtoi) 方法。

   容器 View Controller 会把这条消息转发给当前显示的自定义 View Controller。
7. 窗口调用该 View Controller 的 [willAnimateSecondHalfOfRotationFromInterfaceOrientation:duration:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621509-willanimatesecondhalfofrotationf) 方法。

   容器 View Controller 会把这条消息转发给当前显示的自定义 View Controller。
8. 窗口执行后半段旋转。

   到这次旋转结束时，所有视图的自动调整尺寸行为都已应用完毕，各视图都已处于它们的“最终”位置。
9. 窗口调用该 View Controller 的 [didRotateFromInterfaceOrientation:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621492-didrotatefrominterfaceorientatio) 方法。

   容器 View Controller 会把这条消息转发给当前显示的自定义 View Controller。旋转结束后，你可以使用这个方法来显示视图、重新定位或调整视图尺寸，或做出其他改变。

图 2-8 直观展示了上述步骤，并展示了在每个步骤中，该视图在用户看来会是什么样子。

__图 2-8__  处理两步式界面旋转

!

如果你想根据设备处于纵向还是横向，以不同的方式呈现相同的数据，实现这一点的方法是使用两个独立的 View Controller。其中一个 View Controller 应当管理主方向（通常是纵向）下的数据显示，另一个则管理备用方向下的数据显示。使用两个 View Controller 比每次方向变化时都对视图层级做重大改动要更简单、更高效。它让每个 View Controller 都能专注于在一种方向下呈现数据，并据此进行相应的管理。它还免去了在 View Controller 代码中到处充斥当前方向条件判断的必要。

为了支持备用的横屏界面，你必须执行以下操作：

- 实现两个 View Controller 对象：

  - 一个只呈现纵向界面。
  - 一个只呈现横向界面。
- 注册接收 [UIDeviceOrientationDidChangeNotification](https://developer.apple.com/documentation/uikit/uidevice/1620025-orientationdidchangenotification) 通知。在你的处理方法中，根据当前设备方向来呈现或消除备用的 View Controller。

由于 View Controller 通常会在内部自行管理方向变化，你必须告诉每个 View Controller 只以一种方向显示自己。主 View Controller 的实现随后需要检测设备方向的变化，并在适当的方向变化发生时呈现备用的 View Controller。当方向恢复到主方向时，主 View Controller 随即消除备用的 View Controller。

清单 2-5 展示了你需要在一个支持纵向的主 View Controller 中实现的关键方法。作为其初始化的一部分，这个 View Controller 会注册以接收来自共享 [UIDevice](https://developer.apple.com/documentation/uikit/uidevice) 对象的方向变化通知。当这样一条通知到达时，`orientationChanged:` 方法会根据当前方向来呈现或消除横屏 View Controller。

__清单 2-5__  呈现横屏 View Controller

```objc
@implementation PortraitViewController
- (id)init
{
   self = [super initWithNibName:@"PortraitView" bundle:nil];
   if (self)
   {
       isShowingLandscapeView = NO;
       self.landscapeViewController = [[[LandscapeViewController alloc]
                            initWithNibName:@"LandscapeView" bundle:nil] autorelease];

       [[UIDevice currentDevice] beginGeneratingDeviceOrientationNotifications];
       [[NSNotificationCenter defaultCenter] addObserver:self
                                 selector:@selector(orientationChanged:)
                                 name:UIDeviceOrientationDidChangeNotification
                                 object:nil];
   }
   return self;
}

- (void)orientationChanged:(NSNotification *)notification
{
    UIDeviceOrientation deviceOrientation = [UIDevice currentDevice].orientation;
    if (UIDeviceOrientationIsLandscape(deviceOrientation) &&
        !isShowingLandscapeView)
    {
        [self presentModalViewController:self.landscapeViewController
                                animated:YES];
        isShowingLandscapeView = YES;
    }
    else if (UIDeviceOrientationIsPortrait(deviceOrientation) &&
             isShowingLandscapeView)
    {
        [self dismissModalViewControllerAnimated:YES];
        isShowingLandscapeView = NO;
    }
}
```


根据你视图的复杂程度，你可能需要编写大量代码来支持旋转，也可能完全不需要。在弄清楚你需要做什么时，可以参考以下提示来指导你编写代码。

- __在旋转过程中临时禁用事件投递。__ 为视图禁用事件投递，可以防止在方向变化进行期间执行不必要的代码。
- __保存可见的地图区域。__ 如果你的应用程序包含一个地图视图，请在旋转开始之前保存可见地图区域的值。旋转结束后，按需使用保存的值，确保显示的区域与之前大致相同。
- __对于复杂的视图层级，用快照图像替换你的视图。__ 如果为大量视图设置动画会导致性能问题，可以暂时用一个包含这些视图图像的 image view 来替换这些视图。等旋转完成后，重新装回你的视图并移除这个 image view。
- __在旋转之后重新加载任何可见表格的内容。__ 在旋转结束时强制执行一次重新加载操作，可以确保任何新露出的表格行都被恰当地填充。
- __使用旋转通知来更新应用程序的状态信息。__ 如果你的应用程序使用当前方向来决定如何呈现内容，请使用 View Controller 的旋转方法（或相应的设备方向通知）来记录这些变化，并做出任何必要的调整。

创建自定义 View Controller 对象有两种方式：以编程方式创建，或使用 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)。你应当使用哪种技术，取决于用户界面的结构。对于包含标签栏控制器和导航控制器的复杂界面，你通常会在应用程序的主 nib 文件中包含至少几个自定义 View Controller，其余的则以编程方式创建。在大多数其他情况下，你应当以编程方式创建 View Controller，并且只在需要时才创建。

要以编程方式创建自定义 View Controller，你可以使用类似下面的代码：

```objc
MyViewController* vc = [[MyViewController alloc] initWithNibName:@"MyViewController"
                             bundle:nil];
```

这样一个例子假设你的 View Controller 不执行任何重要的[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)，或者即便执行，也是在[重写](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57)版本的 [initWithNibName:bundle:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621359-initwithnibname) 方法中完成的。不过，在设计自定义 View Controller 时，一种常见的做法是定义一个或多个自定义初始化方法。这样做可以让你隐藏 View Controller 初始化中一些更为固定不变的方面（例如指定 nib 文件和 bundle 名称），转而专注于你想用来初始化该 View Controller 的数据。例如，一个接受对象数组的自定义初始化方法可能类似下面这样：

```objc
- (id)initWithData:(NSArray*)data {
    if ((self = [super initWithNibName:@"MyViewController" bundle:nil])) {
        // 用初始数据来初始化该 view controller
    }
    return self;
}
```

使用这样一个初始化方法，你创建并初始化的 View Controller 会立即处于可用状态。之后你就可以呈现这个 View Controller，或者把它添加到导航界面中。例如，要以模态方式呈现这个新的 View Controller，你可能会在当前 View Controller 上定义一个类似下面这样的方法：

```objc
- (void)presentModalViewControllerWithData:(NSArray*)data {
   MyViewController* vc = [[MyViewController alloc] initWithData:data];
   [self presentModalViewController:vc animated:YES];
}
```

当以编程方式创建 View Controller 时，在使用其视图之前，正确设置该 View Controller 视图的 frame 是你自己的责任。以编程方式创建、且从 nib 文件加载视图的 View Controller，不会尝试改变该视图的尺寸或位置。如果该 View Controller 是以模态方式呈现的，或与某个容器 View Controller 一起使用，其父级或容器 View Controller 通常会替你调整视图。但如果你自己把视图添加到一个窗口中，该视图现有的 frame 会被原样使用。如果你的应用程序带有状态栏，未能调整视图的 frame 可能会导致该视图在状态栏下方被错误放置。

使用 nib 文件创建 View Controller 的过程要稍微复杂一些，具体内容在[在同一个 Nib 文件中存储视图和 View Controller](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvztgq)中描述。有关如何在运行时显示 View Controller 视图的信息，参见[呈现 View Controller 的视图](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsgu)。

显示与某个 View Controller 关联的视图有几种选择：

- 使用 [addSubview:](https://developer.apple.com/documentation/uikit/uiview/1622616-addsubview) 方法把视图添加到窗口中，直接显示该视图。
- 使用以下技术之一间接显示该视图：

  - 使用 [presentModalViewController:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621465-presentmodalviewcontroller) 方法以模态方式呈现所属的 View Controller。
  - 把所属的 View Controller 压入某个导航控制器对象的导航栈中。
  - 把所属的 View Controller 作为标签栏界面中某个标签的根 View Controller。
  - 在 iPad 上，使用 popover 呈现该 View Controller。

清单 2-6 展示了一个直接在应用程序主窗口中显示视图的例子。在这个例子中，`viewController` 变量是一个 outlet，存储着指向从主 nib 文件加载的某个 View Controller 的指针。类似地，`window` 变量存储着指向应用程序窗口的指针。（当你使用 View-based Application 项目模板时，这段代码会自动在你的应用程序委托中为你生成。）把视图添加到窗口中会加载该视图，并使其在窗口随后显示时一并显示出来。

__清单 2-6__  将 View Controller 的视图添加到窗口

```objc
- (void)applicationDidFinishLaunching:(UIApplication *)application {
   // 此时，主 nib 文件已经加载完成。
   // 在把视图添加到窗口之前，最好先设置好它的 frame。
   [viewController.view setFrame:[[UIScreen mainScreen] applicationFrame]];

   [window addSubview:viewController.view];
   [window makeKeyAndVisible];
}
```

建议你只使用推荐的技术来显示 View Controller 的视图。为了正确地呈现和管理视图，系统会记录你直接或间接显示的每个视图（及其关联的 View Controller）。它之后会利用这些信息，向你的应用程序报告与 View Controller 相关的事件。例如，当设备方向发生变化时，窗口会利用这些信息来识别最前面的 View Controller 并通知它这一变化。如果你通过其他方式（例如把它作为子视图添加到某个其他视图中）把某个 View Controller 的视图纳入你的层级结构，系统会认为你想自己管理这个视图，因此不会向相关联的 View Controller 对象发送消息。

除了搭建应用程序的初始界面之外，大多数其他视图都是通过它们的 View Controller 对象间接呈现的。有关如何间接呈现视图的信息，请查阅以下各小节：

- 有关如何以模态方式呈现视图的信息，参见[以模态方式呈现 View Controller](Modal%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjrgewvgvzt)。
- 有关如何在导航界面中显示视图的信息，参见[修改导航栈](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzrgi)。
- 有关在标签中显示视图的信息，参见[创建标签栏界面](Tab%20Bar%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgiwvgvzs)。
- 有关使用 popover 显示视图的信息，参见[创建并呈现 Popover](iPad-Specific%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqnrnknlto)。

当某个 View Controller 视图的可见性发生变化时，该 View Controller 会调用一些内置方法，通知子类这些变化。你可以使用这些内置方法来恰当地响应可见性的变化。例如，你可以利用这些通知来改变状态栏的颜色和方向，使其与即将显示的视图的呈现样式相匹配。根据某个视图即将在屏幕上出现还是消失，View Controller 会调用不同的方法。

图 2-9 展示了当某个 View Controller 的视图被添加到窗口中时所发生的基本事件序列。（如果该视图已经在窗口中，只是当前被另一个视图遮挡，那么当这些遮挡物被移除、该视图再次显露出来时，也会发生同样的事件序列。）[viewWillAppear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621510-viewwillappear) 和 [viewDidAppear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621423-viewdidappear) 方法让子类有机会执行与视图出现相关的任何额外操作。

__图 2-9__  响应视图的出现

!

图 2-10 展示了当某个视图从其窗口中移除时所发生的基本事件序列。（当某个视图被另一个视图完全遮挡时，也会发生同样的事件序列，例如在现有 View Controller 之上呈现新的 View Controller 时就可能发生这种情况。）当 View Controller 检测到它的视图即将被移除或隐藏时，会调用 [viewWillDisappear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621485-viewwilldisappear) 和 [viewDidDisappear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621477-viewdiddisappear) 方法，让子类有机会执行任何相关任务。

__图 2-10__  响应视图的消失

!

如果你的应用程序显示状态栏，[UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 类会自动缩小它的视图，使该视图不会延伸到状态栏下方。毕竟，如果状态栏是不透明的，就没有办法看到其下方的内容或与之交互。不过，如果你的应用程序显示的是半透明状态栏，你可以把 View Controller 的 [wantsFullScreenLayout](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621390-wantsfullscreenlayout) 属性值设置为 `YES`，让你的视图可以延伸到状态栏下方。

在你想最大化可用于显示内容的空间的情况下，让内容延伸到状态栏下方会很有用。当在状态栏下方显示内容时，你应当确保把这些内容放在一个 scroll view 中，以便用户可以把它从状态栏下方滚动出来。能够滚动你的内容很重要，因为用户无法与位于状态栏或任何其他半透明视图（例如半透明的导航栏和工具栏）后面的内容进行交互。导航栏会自动为你的 scroll view 添加一个 scroll content inset（假设它是 View Controller 的根视图），以补偿导航栏的高度；否则，你必须手动修改 scroll view 的 [contentInset](https://developer.apple.com/documentation/uikit/uiscrollview/1619406-contentinset) 属性。

有关为与导航控制器搭配使用的 View Controller 采用全屏布局的更多信息，参见[为导航视图采用全屏布局](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzz)。

如果你想使用同一个 View Controller 来显示和编辑内容，可以重写 [setEditing:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621378-setediting) 方法，并用它在 View Controller 视图的显示模式和编辑模式之间切换。当这个方法被调用时，你的实现应当添加、隐藏并调整 View Controller 的各个视图，以匹配指定的模式。例如，你可能想改变视图的内容或外观，以表明该视图现在是可编辑的。如果你的 View Controller 管理着一个表格，你也可以调用该表格自身的 `setEditing:animated:` 方法，把表格切换到相应的模式。

图 2-11 展示了 Contacts 应用程序中支持就地编辑的一个视图。点按右上角的 Edit 按钮会告诉 View Controller 更新自己以进入编辑状态；Done 按钮则会让用户返回显示模式。除了修改表格之外，该视图还会改变 image view 的内容以及显示用户姓名的视图。它还会配置各个视图和 cell，使得点按它们时会编辑其内容，而不是执行其他操作。

__图 2-11__  视图的显示模式和编辑模式

!

你自己实现 `setEditing:animated:` 方法相对简单直接。你所要做的只是检查 View Controller 正要进入哪种模式，并据此调整视图的内容。

```objc
- (void)setEditing:(BOOL)flag animated:(BOOL)animated
{
    [super setEditing:flag animated:animated];
    if (flag == YES){
        // 把视图切换为编辑模式
    }
    else {
        // 如果需要则保存更改，并把视图切换为不可编辑状态
    }
}
```

导航界面是使用可编辑视图的一个常见场合。在实现导航界面时，当可编辑的 View Controller 可见时，你可以在导航栏中加入一个特殊的 Edit 按钮。（你可以通过调用 View Controller 的 [editButtonItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621471-editbuttonitem) 方法来获取这个按钮。）点按这个按钮时，它会自动在 Edit 和 Done 按钮之间切换，并以相应的值调用你 View Controller 的 `setEditing:animated:` 方法。你也可以从自己的代码中调用这个方法（或修改 View Controller 的 [editing](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621498-isediting) 属性的值）来在两种模式之间切换。

有关在导航栏中添加 Edit 按钮的更多信息，参见[使用 Edit 和 Done 按钮](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzrha)。有关如何支持表格视图编辑的更多信息，参见 _[Table View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/AboutTableViewsiPhone/AboutTableViewsiPhone.html#//apple_ref/doc/uid/TP40007451)_。

View Controller 本身是 [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder) 类的后代，因此能够处理各种各样的事件。通常情况下，当某个视图不响应给定的事件时，它会把该事件传递给它的 superview。不过，如果这个视图是由某个 View Controller 管理的，它会先把事件传递给该 View Controller 对象。这就让 View Controller 有机会吸收其视图未处理的任何事件。如果 View Controller 也不处理该事件，该事件就会像往常一样继续传递给该视图的 superview。

图 2-12 演示了事件在一个视图层级中的流动过程。假设你有一个自定义视图，嵌套在一个铺满屏幕的通用视图对象内部，而这个通用视图对象又由你的 View Controller 管理。到达你自定义视图 frame 范围内的触摸事件会被投递给该视图进行处理。如果你的视图不处理某个事件，它会被继续传递给父视图。由于这个通用视图不处理事件，它会先把这些事件传递给它的 View Controller。如果该 View Controller 也不处理这个事件，该事件就会被进一步传递给这个通用 `UIView` 对象的 superview，在这个例子中就是窗口对象。

__图 2-12__  View Controller 的响应者链

!

虽然你可能并不想在 View Controller 中专门处理触摸事件，但你可以用它来处理基于运动的事件。你也可以用它来协调第一响应者的设置和变更。有关 iOS 应用程序中事件如何分发和处理的更多信息，参见 _iOS 事件处理指南_。

虽然 View Controller 的主要职责是提供并管理其视图层级，但 View Controller 常常会与其他 View Controller 协同工作，以呈现更复杂精细的界面。例如，导航控制器管理着导航栏视图，该视图提供了一个返回按钮以及特定于当前 View Controller 的信息。至于具体内容，导航控制器则依赖于你的自定义 View Controller 来提供。标签栏控制器同样期望你的自定义 View Controller 提供与标签相关的信息。

自定义 View Controller 负责提供上层 View Controller 所需的任何特定对象。表 2-3 列出了你的 View Controller 应当准备提供的对象类型，以及需要提供这些对象的场景。如果你没有为这些属性中的任何一个指定自定义对象，View Controller 会为你提供一个合适的默认项。

__表 2-3__  自定义 View Controller 所管理的支持性对象

| 对象 | 属性 | 说明 |
| 导航工具栏项 | [toolbarItems](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621867-toolbaritems) | 与提供自定义工具栏的导航控制器搭配使用。你可以使用这个属性来指定你想在该工具栏中显示的任何项。当用户从一个屏幕切换到下一个屏幕时，与新 View Controller 关联的工具栏项会以动画方式移动到位。默认行为是不提供任何自定义工具栏项。在 iOS 3.0 及以后的版本中可用。有关配置导航工具栏的信息，参见[显示导航工具栏](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzu)。 |
| 导航栏内容 | [navigationItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621851-navigationitem) | 与导航控制器搭配使用。导航项对象提供了当你的 View Controller 显示时要在导航栏中显示的对象。你可以用它来为你的视图提供自定义标题或额外的控件。默认的导航项使用 View Controller 的标题作为导航栏的标题，且不提供任何自定义按钮。导航控制器会自动添加返回按钮。有关指定导航栏内容的信息，参见[定制导航栏外观](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzt)。 |
| 标签栏项 | [tabBarItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621175-tabbaritem) | 与标签栏控制器搭配使用。标签栏项提供了要在与你的 View Controller 关联的标签中显示的图像和文字。默认的标签栏项包含 View Controller 的标题，不包含图像。有关为 View Controller 指定标签内容的信息，参见[创建标签栏界面](Tab%20Bar%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgiwvgvzs)。 |

有关这些属性的更多信息，参见 _[UIViewController Class Reference](https://developer.apple.com/documentation/uikit/uiviewcontroller)_。

[下一页](Navigation%20Controllers.md)[上一页](View%20Controller%20Basics.md)

