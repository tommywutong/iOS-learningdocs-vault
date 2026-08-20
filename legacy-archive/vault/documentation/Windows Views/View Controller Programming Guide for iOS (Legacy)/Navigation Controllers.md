---
title: iOS View Controller 编程指南（旧版）
apple_id: TP40011381
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerPGforiOSLegacy/NavigationControllers/NavigationControllers.html
archived_at: '2026-07-18T02:23:54.164755Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 编程指南（旧版）](About%20View%20Controllers.md)


[下一页](Tab%20Bar%20Controllers.md)[上一页](Custom%20View%20Controllers.md)

# Navigation Controller

你可以使用 navigation controller 来管理应用程序中层级数据的呈现。一个 navigation controller 管理着一个自包含的视图层级（称为导航界面），其内容一部分由 navigation controller 直接管理的视图组成，一部分由你提供的自定义 View Controller 所管理的视图组成。每个自定义 View Controller 管理一个独立的视图层级，而 navigation controller 负责协调不同视图层级之间的导航。

虽然导航界面大部分由你的自定义内容构成，但仍有一些地方你的代码必须直接与 navigation controller 对象交互。除了告诉 navigation controller 何时显示新视图之外，你还需要负责配置导航栏——屏幕顶部提供用户在导航层级中所处位置上下文信息的那个视图。你还可以为由 navigation controller 管理的工具栏提供内容项。

本章概述了如何在应用程序中配置和使用 navigation controller。有关如何将 navigation controller 与其他类型的 View Controller 对象组合使用的信息，请参阅[组合 View Controller 界面](Combined%20View%20Controller%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgqwvgvzr)。

尽管其主要职责是管理你自定义 View Controller 的呈现，但 navigation controller 本身也负责呈现一些自定义视图。具体来说，它会呈现一个导航栏，其中包含一个返回按钮以及一些你可以自定义的按钮。在 iOS 3.0 及以后版本中，navigation controller 还可以呈现一个导航工具栏视图，并在其中填充自定义按钮；不过工具栏的显示是可选的。

图 3-1 展示了导航界面的关键视图。图中的导航视图就是保存在 navigation controller 的 [view](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621460-view) 属性中的那个视图。这是你获取并嵌入到窗口中、或通过另一个 View Controller 来呈现的视图。界面中的其他所有视图都属于本质上不透明、由 navigation controller 管理的视图层级的一部分。

__图 3-1__  导航界面的各个视图

!

虽然导航栏和工具栏都是可定制的视图，但你绝不能直接修改导航层级中的这些视图。定制这些视图的唯一方式是通过 [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) 和 [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 类的特定接口。关于如何定制导航栏内容的信息，请参阅[定制导航栏的外观](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzt)。关于如何在导航界面中显示和配置自定义工具栏项的信息，请参阅[显示导航工具栏](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzu)。

navigation controller 使用多个对象来实现导航界面。其中一部分对象由你负责提供，其余的则由 navigation controller 自身创建。具体来说，你负责为 View Controller 提供你想要呈现的自定义内容。如果你想要响应来自 navigation controller 的通知，还可以提供一个[委托（delegate）对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)。不过，navigation controller 会创建导航界面所需的其他视图（例如导航栏和工具栏），并负责管理这些视图。图 3-2 展示了 navigation controller 与这些关键对象之间的关系。

__图 3-2__  navigation controller 管理的对象

!

除了修改外观的某些方面之外，你不应修改与 navigation controller 关联的导航栏或工具栏对象。navigation controller 是唯一负责配置和显示它们的对象。此外，navigation controller 对象会自动将自己指定为其 [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar) 对象的委托，并阻止其他对象改变这一关系。

你可以放心修改的对象包括委托，以及导航栈中的其他 View Controller。_导航栈_ 是由 navigation controller 管理的一个后进先出的自定义 View Controller 对象集合。添加到栈中的第一个条目会成为 _根 View Controller_，并且永远不能被移除。其他条目可以使用 [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) 类的方法添加到栈中。

图 3-3 展示了 navigation controller 与导航栈上对象之间的相关关系。需要注意的是，[topViewController](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621849-topviewcontroller) 和 [visibleViewController](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621862-visibleviewcontroller) 属性中的对象未必相同。如果你从栈顶对象以模态方式呈现一个 View Controller，`topViewController` 属性不会改变，但 `visibleViewController` 属性中的对象会改变。具体来说，`visibleViewController` 属性的值会变化，以反映所呈现的那个模态 View Controller。

__图 3-3__  导航栈

!

你的主要职责是根据用户操作将新的 View Controller 压入栈中。你压入导航栈的每个 View Controller 都负责呈现应用程序数据的某一部分。通常情况下，当用户在当前可见视图中选择一个条目时，你会创建一个新的 View Controller 对象，把所选条目的数据赋给它，然后将这个新的 View Controller 压入栈中。这就是你向用户呈现所选数据的方式。例如，当用户选择一个相册时，Photos 应用会压入一个显示该相册中照片的 View Controller。在大多数情况下，你不需要以编程方式从栈中弹出 View Controller。相反，navigation controller 会在导航栏上提供一个返回按钮，点按该按钮就会自动弹出栈顶的 View Controller。

关于如何定制导航栏的更多信息，请参阅[定制导航栏的外观](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzt)。关于将 View Controller 压入导航栈（以及之后将其移除）的信息，请参阅[修改导航栈](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzrgi)。关于如何定制工具栏内容的信息，请参阅[显示导航工具栏](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzu)。

当你想要呈现的信息按层级组织时，就应该使用导航界面。通常，你会使用 navigation controller 来管理层级数据的呈现，但你也可以用它来管理多级编辑，或者其他需要多个连续屏幕的界面。

在创建导航界面之前，你需要先决定打算如何使用它。以下是你可能在应用程序中安装导航界面的几个场景：

- 直接安装在应用程序的主窗口中。
- 作为 tab bar 界面中某个标签页的根 View Controller 安装。
- 作为 split view 界面中两个根 View Controller 之一安装。（仅限 iPad）
- 以模态方式呈现，或者以其他方式将其用作一个独立的 View Controller，按需显示和关闭。
- 从 popover 中显示。（仅限 iPad）

在前三种场景中，navigation controller 提供了基本界面中至关重要的一部分，并且会一直存在直到应用程序退出。然而，后两种场景反映的是 navigation controller 更为临时性的用法，在这种情况下，使用 navigation controller 的过程与使用其他模态和自定义 View Controller 的过程是一样的。唯一的区别是，navigation controller 仍然会提供单个自定义 View Controller 所不具备的额外导航功能。尽管接下来的小节主要关注如何创建更为永久性的导航界面类型，但大多数定制步骤和一般性信息适用于所有 navigation controller，无论你打算如何使用它们。

实现导航界面时，你必须做的关键事情之一是决定在每个阶段打算呈现什么数据。每个导航界面都至少有一级数据，代表根级数据，这是界面的起点。例如，Photos 应用在其数据层级的根级显示可用相册的列表。选择一个相册后，会显示该相册中的照片，选择一张照片则会显示该照片的放大版本。

对于数据层级中的每一级，你都必须提供一个自定义 View Controller 对象，来管理和呈现该级别的数据。如果多个级别的呈现方式本质上相同，你可以按需重用同一个 View Controller 类。不过，在运行时你仍然必须创建该类的独立实例，并分别配置每个实例来管理各自的数据集。例如，Photos 应用有三种不同的呈现类型，因此它需要三个独立的 View Controller 对象，如图 3-4 所示。

__图 3-4__  为每一级数据定义 View Controller

!

除了管理叶子数据的 View Controller 之外，每个自定义 View Controller 都必须提供一种方式，让用户能够导航到数据层级的下一级。显示条目列表的 View Controller 可以利用某个表格单元格上的点按来显示下一级数据。例如，当用户从顶层列表中选择一个相册时，Photos 应用会创建一个新的相册 View Controller。这个新的 View Controller 会用足够的相册信息进行初始化，以便呈现相关照片。

如果你的应用程序数据结构高度规整，从一个级别到下一个级别的推进方式是已知的，那么在每个级别定义 View Controller（以及它们之间的关系）应该相对简单。（Photos 应用总是先显示相册，然后是相册内容，然后是单张照片。）但如果你的应用程序会根据当前级别所选条目的不同而以不同方式呈现数据，你可能需要在数据模型中使用额外信息来决定如何呈现该数据。你可以利用这些信息来决定是使用不同的 View Controller 类，还是定制单个 View Controller 类的呈现样式。例如，在 iPod 应用中按作曲者查看歌曲时，会根据该作曲者的歌曲是否来自同一张专辑还是来自多张不同专辑，来显示专辑列表或歌曲列表。不过在这两种情况下，数据都是以表格形式呈现的列表；因此，你可以使用同一个 View Controller，只需为每种数据类型提供不同的表格单元格即可。

关于定义自定义 View Controller 的一般信息和指导，请参阅[自定义 View Controller](Custom%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzr)。

虽然 Interface Builder 支持在 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)中包含 navigation controller 对象，但其语义与自定义 View Controller 略有不同。对于自定义 View Controller，你使用 nib 文件来存储与该 View Controller 关联的视图，但通常会单独创建 View Controller 本身——要么以编程方式创建，要么从另一个 nib 文件中加载。然而，对于 navigation controller，其视图总是以编程方式创建的，因此没有视图需要放入单独的 nib 文件中。这种行为的一个后果是，navigation controller 从不管理 nib 文件——换句话说，你永远不会将 navigation controller 指定给 File's Owner 占位符。相反，唯一会将 navigation controller 与 nib 文件混用的情况，是 navigation controller 本身被存储在 nib 文件中的时候。因此，navigation controller 几乎总是作为乘客存在于由其他对象管理的 nib 文件中。

将 navigation controller 包含在应用程序的主 nib 文件中是最合理的做法。当 navigation controller 本身为应用程序窗口提供主视图时，或者当 navigation controller 为 tab bar 界面提供根视图时，你就会这样做。虽然你也可以从主 nib 文件（或其他任何 nib 文件）加载独立呈现或模态呈现的 navigation controller，但这样做并不是最佳选择。在这些场景下，通常在使用点以编程方式创建 navigation controller 会更简单。

图 3-5 展示了一个应用程序主 nib 文件的配置，该应用程序在其主窗口中显示导航界面。这个 nib 文件包含窗口对象、navigation controller，以及导航界面的根 View Controller（它被嵌入在 navigation controller 本身之中）。（根 View Controller 所管理的视图通常不需要放在同一个 nib 文件中，本例中将其放在了一个单独的 nib 文件中展示。）

__图 3-5__  包含导航界面的 nib 文件

!

由于 navigation controller 是以编程方式创建其视图的，你无法使用 Interface Builder 将该视图安装到窗口中。相反，你还必须以编程方式将该视图添加到窗口中。如果窗口和 navigation controller 本身都在某个 nib 文件中，那么你必须记得保存对这些对象的引用，以便之后能够访问它们。

要在 nib 文件中配置一个 navigation controller，你需要执行以下操作：

1. 从库中把一个 navigation controller 对象拖到你的 Interface Builder 文档窗口中。

   当你添加一个 navigation controller 时，Interface Builder 还会添加一个导航栏、一个内嵌的根 View Controller 对象，以及一个供你的根 View Controller 使用的 navigation item。你可以通过在 navigation controller 编辑界面中选中这些对象来访问其中一部分。你也可以在大纲和浏览器模式下，从文档窗口中选中任意一个对象。
2. 使用 outlet 保存对该 navigation controller 的引用。

   为了在运行时访问 navigation controller，你要么需要使用 outlet，要么必须在加载 nib 文件时显式获取该 nib 文件的顶层对象。使用 outlet 通常要简单得多。要添加一个 outlet，请在应用程序委托类的声明中添加一个类似下面这样的变量：

```objc
@interface MyAppDelegate : NSObject <UIApplicationDelegate> {
   IBOutlet UINavigationController*  myNavigationController;
}
@end
```

   添加好 outlet 定义之后，在 Interface Builder 中从该 outlet 创建一个到 navigation controller 对象的连接。
3. 将根 View Controller 的类设置为你 Xcode 项目中的某个自定义类。

   你选择的这个类应当负责显示导航层级中最高层级的数据。如果存在多个数据级别，你的 View Controller 类所呈现的视图应当包含用于导航到下一级数据的控件。有关如何设计 View Controller 的信息，请参阅[为导航界面定义自定义 View Controller](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvztgi)。
4. 为你的根 View Controller 配置视图。

   你可以将视图放在同一个 nib 文件中，也可以将其存储在不同的 nib 文件中。推荐使用不同的 nib 文件，因为这样系统就可以在内存不足时选择将该视图从内存中移除。

   要指定单独的 nib 文件，请将根 View Controller 的 NIB Name 属性设置为你的 nib 文件名。要将视图包含在与 navigation controller 相同的 nib 文件中，请把你的视图对象拖到 navigation controller 编辑界面中。
5. 在应用程序委托的 [applicationDidFinishLaunching:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching) 方法中，将 navigation controller 的视图添加到你的主窗口中。

   navigation controller 不会自动将自己安装到应用程序的窗口中。你必须以编程方式完成这一步，代码类似下面这样：

```objc
- (void)applicationDidFinishLaunching:(UIApplication *)application {
    [window addSubview:myNavigationController.view];
}
```
6. 保存你的 nib 文件。

除了配置根 View Controller 对象之外，你还可以使用检查器（inspector）来更改 Interface Builder 所创建的 navigation item 和导航栏的属性。对于导航栏，你可以更改一些基本的样式属性。对于 navigation item，你可以指定自定义的标题和提示文本。如果你没有为 navigation item 指定自定义字符串，Interface Builder 会使用自定义 View Controller 的 title 属性中的字符串。

navigation controller 的编辑界面提供了一种便捷的方式来编辑导航栏的配置。要向导航栏添加额外的按钮或视图，请将库中相应的对象拖到编辑界面中的导航栏上。这样做会把相应的对象添加到根 View Controller 的 navigation item 中。然后你就可以像配置其他 Interface Builder 对象一样配置你拖入的这些条目。例如，你可以将 navigation item 中的按钮连接到 View Controller 的动作方法，以便在运行时便于处理用户的点按操作。

关于如何使用 Interface Builder 配置 nib 文件内容（包括如何将视图和其他控件连接到动作方法）的信息，请参阅 _[Interface Builder User Guide](../../Developer%20Tools/Interface%20Builder%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbu)_。

如果你更倾向于以编程方式创建 navigation controller，可以在代码中任何合适的位置这样做。例如，如果 navigation controller 为应用程序窗口提供根视图，你可以在应用程序[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)的 [applicationDidFinishLaunching:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching) 方法中创建该 navigation controller。

在其他一些情况下，以编程方式创建 View Controller 可能更为合适。例如，如果你打算以模态方式呈现导航界面，通常在使用点创建 navigation controller 对象、呈现它，并在不再需要时释放它，会更简单。从 nib 文件加载这样的 View Controller 需要加载 nib 文件的额外开销，并且可能要求你把指向该 navigation controller 对象的指针保存的时间超出必要的长度。

[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) navigation controller 时，你必须执行以下操作：

1. 为导航界面创建根 View Controller。

   该对象是导航栈中的顶层 View Controller。显示其视图时，导航栏不会显示返回按钮，并且该 View Controller 无法从导航栈中弹出。
2. 创建 navigation controller，使用 [initWithRootViewController:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621858-initwithrootviewcontroller) 方法对其进行[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)。
3. 将 navigation controller 的视图添加到你的窗口中（或以其他方式在你的界面中呈现它）。

创建好 navigation controller 之后，你就可以按需使用它了。例如，你可以将它的视图添加到窗口中，用它来初始化另一个 View Controller，或者以模态方式呈现它。

清单 3-1 展示了 `applicationDidFinishLaunching:` 方法的一个简单实现，该方法创建了一个 navigation controller 并将其添加到应用程序的主窗口中。`navigationController` 和 `window` 变量是应用程序委托的成员变量，`MyRootViewController` 类是一个自定义 View Controller 类。当本示例中的窗口显示时，导航界面会呈现该导航界面中根 View Controller 的视图。

__清单 3-1__  以编程方式创建 navigation controller

```objc
- (void)applicationDidFinishLaunching:(UIApplication *)application
{
    UIViewController *rootController = [[MyRootViewController alloc] init];
    navigationController = [[UINavigationController alloc]
                                initWithRootViewController:rootController];
    [rootController release];

    window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    [window addSubview:navigationController.view];
    [window makeKeyAndVisible];
}
```


通常情况下，导航界面会在导航栏底部与工具栏或 tab bar 顶部之间的空隙中显示你的自定义内容（参见[图 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzrgm)）。不过，View Controller 也可以要求以全屏布局显示其视图。在全屏布局中，内容视图会被配置为按需下叠在导航栏、状态栏和工具栏之下。这样可以为用户最大化可见内容的数量，适用于照片展示等你可能需要更多空间的场合。

在决定一个视图是否应当被调整为填满整个屏幕或大部分屏幕时，navigation controller 会考虑多个因素，包括以下几项：

- 底层窗口（或父视图）的大小是否填满了整个屏幕边界？
- 导航栏是否被配置为半透明？
- 导航工具栏（如果使用的话）是否被配置为半透明？
- 底层 View Controller 的 [wantsFullScreenLayout](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621390-wantsfullscreenlayout) 属性是否被设置为 `YES`？

以上每个因素都会被用来决定自定义视图的最终大小。前面列表中各项的顺序也反映了各个因素被考虑时的优先级。窗口大小是第一个限制因素；如果应用程序的主窗口（对于以模态方式呈现的 View Controller 而言，则是其所在的父视图）没有横跨整个屏幕，那么其中包含的视图也不可能做到这一点。同样，如果导航栏或工具栏可见但不是半透明的，那么即便 View Controller 希望以全屏布局显示其视图也无济于事。navigation controller 绝不会在不透明的导航栏下方显示内容。

如果你正在创建一个导航界面，并希望你的自定义内容横跨大部分或全部屏幕，可以执行以下步骤：

1. 将自定义视图的 frame 配置为填满屏幕边界。

   请确保同时也配置好视图的自动调整大小（autoresizing）属性。这些属性可以确保当你的视图需要调整大小时，其内容会相应地进行调整。或者，当视图被调整大小时，你也可以调用视图的 [setNeedsLayout](https://developer.apple.com/documentation/uikit/uiview/1622601-setneedslayout) 方法，以表明其子视图的位置应当被调整。
2. 将 navigation controller 的 [translucent](https://developer.apple.com/documentation/uikit/uinavigationbar/1624928-istranslucent) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)设置为 `YES`。这样可以让你的内容下叠在导航栏之下。
3. 要下叠在状态栏之下，请将 View Controller 的 [wantsFullScreenLayout](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621390-wantsfullscreenlayout) 属性设置为 `YES`。（导航栏必须是半透明的，这个属性才会生效。）
4. 要下叠在可选的工具栏之下，请将工具栏的 [translucent](https://developer.apple.com/documentation/uikit/uitoolbar/1618001-istranslucent) 属性设置为 `YES`。

呈现导航界面时，你所添加导航视图的那个窗口或视图，其大小也必须相应地调整。如果你的应用程序使用 navigation controller 作为主要界面，那么主窗口的大小应当与屏幕尺寸相匹配。换句话说，你应当将其大小设置为与 `UIScreen` 类的 [bounds](https://developer.apple.com/documentation/uikit/uiscreen/1617838-bounds) 属性相匹配（而不是 `applicationFrame` 属性）。事实上，对于导航界面来说，在所有情况下都以全屏边界创建窗口通常是更好的做法，因为无论如何 navigation controller 都会自动调整其视图的大小以适应状态栏。

如果你正在以模态方式呈现一个 navigation controller，那么该 navigation controller 所呈现的内容会受到执行呈现操作的那个 View Controller 的限制。如果那个 View Controller 不希望下叠在状态栏之下，那么以模态方式呈现的 navigation controller 同样也不会被允许下叠在状态栏之下。换句话说，父视图始终对其以模态方式呈现的视图的显示方式有一定的影响力。

关于如何配置界面以支持全屏布局的更多信息，请参阅[为自定义视图采用全屏布局](Custom%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsha)。

虽然 navigation controller 负责管理导航栈，但你需要负责创建驻留在该栈上的对象。在初始化 navigation controller 对象时，你必须提供一个自定义 View Controller，用于显示数据层级的根内容。这个根 View Controller 始终位于导航栈的底部，永远不能被移除。在此之后，你可以以编程方式或响应用户交互来添加或移除其他 View Controller。要添加和移除这些 View Controller，你需要使用 [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) 类的方法。

navigation controller 提供了几种管理导航栈内容的选项。这些选项涵盖了你在应用程序中可能遇到的各种场景。表 3-1 列出了这些场景以及你应如何应对。

__表 3-1__  管理导航栈的选项

| 场景 | 说明 |
| --- | --- |
| 显示层级数据的下一级。 | 当用户选择栈顶 View Controller 所显示的某个条目时，你可以使用 [pushViewController:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621887-pushviewcontroller) 方法将一个新的 View Controller 压入导航栈。这个新的 View Controller 负责呈现所选条目的内容。 |
| 在层级中返回上一级。 | navigation controller 通常会提供一个返回按钮，用来将栈顶的 View Controller 从栈中移除并返回上一屏。你也可以使用 [popViewControllerAnimated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621886-popviewcontroller) 方法以编程方式移除栈顶的 View Controller。 |
| 将导航栈恢复到之前的状态。 | 当应用程序启动时，你可以使用 [setViewControllers:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621861-setviewcontrollers) 方法将 navigation controller 恢复到之前的状态。例如，你可以使用这个方法把用户带回上次退出应用程序时正在查看的那一屏。  为了将应用程序恢复到之前的状态，你必须先保存足够的状态信息，以便重新创建所需的 View Controller。当用户退出你的应用程序时，你需要保存一些标记或其他信息，用来指明用户在数据层级中所处的位置。在下一次启动时，你就可以读取这些状态信息，并用它在调用 `setViewControllers:animated:` 方法之前重新创建所需的 View Controller。 |
| 将用户带回根 View Controller。 | 要返回到导航界面的最顶层，请使用 [popToRootViewControllerAnimated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621855-poptorootviewcontrolleranimated) 方法。这个方法会从导航栈中移除除根 View Controller 之外的所有 View Controller。 |
| 在层级中返回任意数量的级别。 | 要一次性返回多个级别，请使用 [popToViewController:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621871-poptoviewcontroller) 方法。在你使用 navigation controller 来管理自定义内容的编辑（而不是以模态方式呈现内容）的场合，你可能会用到这个方法。如果用户在你压入了多个编辑屏幕之后决定取消操作，你可以使用这个方法一次性移除所有的编辑屏幕，而不必逐个移除。 |
| 跳转到数据层级中的任意位置。 | 你可以使用 [setViewControllers:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621861-setviewcontrollers) 无缝跳转到数据层级中的任意位置。虽然在数据层级中随意跳转并不是一个好主意（因为它可能造成混淆），但使用这个方法来提供一条返回根 View Controller 的路径，是实现这一点的最佳方式。 |

当你为 View Controller 的压入或弹出添加动画时，navigation controller 会自动创建最合理的动画。例如，如果你使用 `popToViewController:animated:` 方法从栈中弹出多个 View Controller，navigation controller 只会为栈顶的 View Controller 使用动画。所有其他中间的 View Controller 都会在没有动画的情况下被移除。如果你使用动画来压入或弹出某个条目，你必须等到该动画完成之后，才能尝试压入或弹出另一个 View Controller。

随着导航栈发生变化，navigation controller 会向其[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)发送相应的消息。具体来说，每当你压入或弹出一个 View Controller 时，navigation controller 都会向受影响的 View Controller 发送消息。图 3-6 展示了压入或弹出操作期间所发生的事件顺序，以及在每个阶段发送给你自定义对象的相应消息。图中的新 View Controller 指的是即将成为栈顶 View Controller 的那个 View Controller。

__图 3-6__  栈变化期间发送的消息

!

你可以使用 navigation controller 委托的方法来更新导航界面的状态，并修改应用程序的数据模型。例如，如果你正在使用导航界面来支持内容的编辑，你可能会使用 [navigationController:willShowViewController:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621878-navigationcontroller) 方法，在相应的 View Controller 被关闭之前保存任何更改。但是，你不应使用这些方法来修改你的视图或视图层级。这类更改应当由你的自定义 View Controller 来处理。

导航栏是一个容器视图，用于管理导航界面中常见的各种控件。虽然它本质上只是一个视图对象，但当由相应的 navigation controller 对象管理时，导航栏会承担一种特殊的角色。为了保证一致性，并减少构建导航界面所需的工作量，每个 navigation controller 对象都会创建自己的导航栏，并承担管理该导航栏内容的大部分职责。在需要时，navigation controller 会与其他对象（比如你的自定义 View Controller）交互，以协助完成这一过程。

由于管理导航栏是 navigation controller 的职责，直接修改导航栏本身在很大程度上是被禁止的。尽管如此，你仍然有许多方式可以按需定制导航栏。以下小节将说明导航栏的结构，以及你该如何为应用程序定制导航栏。

导航栏的结构在许多方面都与 navigation controller 的结构类似。与 navigation controller 一样，导航栏也是一个容器，其内容由其他对象提供。就导航栏而言，内容由一个或多个 [UINavigationItem](https://developer.apple.com/documentation/uikit/uinavigationitem) 对象提供，这些对象使用一种称为 _navigation item 栈_ 的栈数据结构来存储。每个 navigation item 都提供了一整套要在导航栏中显示的视图和内容。与 navigation controller 不同的是，导航栏是一个实际存在的视图对象，可以被嵌入到其他视图内部。

图 3-7 展示了运行时与导航栏相关的一些关键对象。导航栏的所有者（无论是 navigation controller 还是你的自定义代码）负责按需将条目压入栈中并从栈中弹出。为了提供正确的导航，导航栏会维护指向栈中特定对象的指针。虽然导航栏的大部分内容都取自栈顶的 navigation item，但导航栏也会维护一个指向 back item 的指针，以便能够创建一个带有前一个条目标题的返回按钮。

__图 3-7__  与导航栏相关联的对象

!

在导航界面中使用时，导航栏栈的内容总是与父级 navigation controller 栈的内容一一对应。换句话说，对于导航栈中的每个 View Controller，在导航栏的 navigation item 栈上都会有一个位于相同位置的对应 navigation item。这种一一对应关系的原因在于，每个 View Controller 实际上都提供了自己的 navigation item。

导航栏有三个用于放置条目的主要位置：左侧、右侧和中间。表 3-2 列出了用于配置这三个位置各自的 [UINavigationItem](https://developer.apple.com/documentation/uikit/uinavigationitem) 类[属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)。在配置一个用于 navigation controller 的 navigation item 时，请注意某些位置上的自定义控件可能会被忽略，而改用预期的控件。每个位置的说明都包含了你的自定义对象将如何被使用的信息。

__表 3-2__  导航栏上的条目位置

| 位置 | 属性 | 说明 |
| --- | --- | --- |
| 左侧 | [backBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624958-backbarbuttonitem)  [leftBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624936-leftbarbuttonitem) | 在导航界面中，navigation controller 默认会在左侧位置指定一个返回按钮。要获取 navigation controller 提供的默认返回按钮，请获取 `backBarButtonItem` 属性的值。  要为左侧位置指定一个自定义按钮或视图，从而替换默认的返回按钮，请将一个 [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem) 对象赋给 `leftBarButtonItem` 属性。 |
| 中间 | [titleView](https://developer.apple.com/documentation/uikit/uinavigationitem/1624935-titleview) | 在导航界面中，navigation controller 默认会显示一个带有 View Controller 标题的自定义视图。你可以按需将其替换为你选择的自定义视图。  如果你没有提供自定义标题视图，导航栏会显示一个带有适当标题字符串的自定义视图。该标题字符串默认取自 navigation item，如果 navigation item 没有提供合适的标题，则取自 View Controller 本身。 |
| 右侧 | [rightBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624957-rightbarbuttonitem) | 该位置默认是空的，通常用于放置编辑或修改当前屏幕的按钮。你也可以通过将视图包装在 `UIBarButtonItem` 对象中，把自定义视图放置在这里。 |

图 3-8 展示了导航界面中导航栏内容的组装方式。与当前 View Controller 关联的 navigation item 提供导航栏中间和右侧位置的内容。前一个 View Controller 的 navigation item 提供左侧位置的内容。虽然左侧和右侧的条目都要求你指定一个 [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem) 对象，但如图所示，你可以把一个视图包装在栏按钮项中。如果你没有提供自定义标题视图，navigation item 会使用当前 View Controller 的标题为你创建一个。

__图 3-8__  导航栏结构

!

与 navigation controller 配合使用时，你应当始终使用 `UINavigationController` 的 [setNavigationBarHidden:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621885-setnavigationbarhidden) 方法来显示和隐藏导航栏。你绝不能通过直接修改 `UINavigationBar` 对象的 [hidden](https://developer.apple.com/documentation/uikit/uiview/1622585-hidden) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)来隐藏导航栏。除了显示或隐藏导航栏之外，使用 navigation controller 的方法还能免费获得更为复杂精细的行为。具体来说，如果某个 View Controller 在其 [viewWillAppear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621510-viewwillappear) 方法中显示或隐藏导航栏，navigation controller 会让导航栏出现或消失的动画与新 View Controller 的出现保持同步。

由于用户需要依靠导航栏上的返回按钮来导航回上一屏，因此在没有给用户提供其他返回上一屏方式的情况下，你绝不应隐藏导航栏。提供导航支持最常见的方式是拦截触摸事件，并利用它们来切换导航栏的可见性。例如，Photos 应用在全屏显示单张图片时就是这样做的。你也可以检测滑动手势，并利用它们将当前的 View Controller 从栈中弹出，但这种手势的可发现性不如直接切换导航栏可见性那么好。

在导航界面中，navigation controller 拥有其 [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar) 对象，并负责管理它。不允许更改该导航栏对象，也不允许直接修改其 bounds、frame 或 alpha 值。不过，有几个[属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)是允许修改的，包括以下几个：

- [barStyle](https://developer.apple.com/documentation/uikit/uinavigationbar/1624955-barstyle) 属性
- [translucent](https://developer.apple.com/documentation/uikit/uinavigationbar/1624928-istranslucent) 属性
- [tintColor](https://developer.apple.com/documentation/uikit/uinavigationbar/1624937-tintcolor) 属性

图 3-9 展示了 `barStyle` 和 `translucent` 属性如何影响导航栏的外观。对于半透明样式，值得注意的是，如果底层 View Controller 的主视图是一个 scroll view，导航栏会自动调整内容内边距（content inset）值，以便让内容能够滚动到导航栏下方。对于其他类型的视图，导航栏不会做这种调整。

__图 3-9__  导航栏样式

!

如果你想要显示或隐藏整个导航栏，同样应当使用 navigation controller 的 [setNavigationBarHidden:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621885-setnavigationbarhidden) 方法，而不要直接修改导航栏。关于显示和隐藏导航栏的更多信息，请参阅[显示和隐藏导航栏](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzrgu)。

要为特定的 View Controller 定制导航栏的外观，请修改其关联的 [UINavigationItem](https://developer.apple.com/documentation/uikit/uinavigationitem) 对象的属性。你可以通过 View Controller 的 [navigationItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621851-navigationitem) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)获取它的 navigation item。View Controller 在你请求之前不会创建其 navigation item，因此只有当你打算把该 View Controller 安装到导航界面中时，才应该请求这个对象。

如果你选择不修改 View Controller 的 navigation item，navigation item 会提供一整套默认对象，这在许多情况下已经够用了。当然，你所做的任何定制都会优先于这些默认对象。

对于栈顶的 View Controller，导航栏左侧显示的条目是按以下规则确定的：

- 如果你为栈顶 View Controller 的 navigation item 的 [leftBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624936-leftbarbuttonitem) 属性指定了一个自定义栏按钮项，该条目具有最高优先级。
- 如果你没有提供自定义栏按钮项，而导航栈中低一级的 View Controller 的 navigation item 在其 [backBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624958-backbarbuttonitem) 属性中有一个有效的条目，导航栏会显示那个条目。
- 如果这两个 View Controller 都没有指定栏按钮项，则使用默认的返回按钮，其标题被设置为前一个 View Controller（即导航栈中低一级的 View Controller）的 title 属性的值。（如果栈顶的 View Controller 就是根 View Controller，则不显示默认的返回按钮。）

对于栈顶的 View Controller，导航栏中间显示的条目是按以下规则确定的：

- 如果你为栈顶 View Controller 的 navigation item 的 [titleView](https://developer.apple.com/documentation/uikit/uinavigationitem/1624935-titleview) 属性指定了一个自定义视图，导航栏会显示该视图。
- 如果没有设置自定义标题视图，导航栏会显示一个包含 View Controller 标题的自定义视图。这个视图所用的字符串取自该 View Controller 的 navigation item 的 [title](https://developer.apple.com/documentation/uikit/uinavigationitem/1624965-title) 属性。如果该属性的值为 `nil`，则使用 View Controller 本身 [title](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621364-title) 属性中的字符串。

对于栈顶的 View Controller，导航栏右侧显示的条目是按以下规则确定的：

- 如果新的栈顶 View Controller 有自定义的右侧栏按钮项，则会显示该条目。要指定自定义的右侧栏按钮项，请设置 navigation item 的 [rightBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624957-rightbarbuttonitem) 属性。
- 如果没有指定自定义的右侧栏按钮项，导航栏的右侧将不显示任何内容。

要在导航栏控件上方添加一些自定义提示文本，请为 navigation item 的 [prompt](https://developer.apple.com/documentation/uikit/uinavigationitem/1624930-prompt) 属性赋值。

图 3-10 展示了几种不同的导航栏配置，其中包括几个使用了自定义视图和提示文本的例子。图中的导航栏取自示例项目 _[NavBar: Customizing UINavigationBar's appearance](../../../samplecode/NavBar-%20Customizing%20UINavigationBar%27s%20appearance/NavBar-%20Customizing%20UINavigationBar%27s%20appearance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonbrha)_。

__图 3-10__  导航栏中的自定义按钮

!

清单 3-2 展示了 NavBar 应用程序中创建图 3-10 里第三个导航栏所需的代码，该导航栏包含一个带有自定义视图的右侧栏按钮项。由于它位于导航栏的右侧位置，你必须先用 [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem) 对象包装这个自定义视图，然后再将其赋给 `rightBarButtonItem` 属性。

__清单 3-2__  创建自定义的栏按钮项

```objc
// View 3 - 带有视图的自定义右侧栏按钮
UISegmentedControl *segmentedControl = [[UISegmentedControl alloc] initWithItems:
                                      [NSArray arrayWithObjects:
                                          [UIImage imageNamed:@"up.png"],
                                          [UIImage imageNamed:@"down.png"],
                                          nil]];

[segmentedControl addTarget:self action:@selector(segmentAction:) forControlEvents:UIControlEventValueChanged];
segmentedControl.frame = CGRectMake(0, 0, 90, kCustomButtonHeight);
segmentedControl.segmentedControlStyle = UISegmentedControlStyleBar;
segmentedControl.momentary = YES;

defaultTintColor = [segmentedControl.tintColor retain];    // 保留以便之后使用

UIBarButtonItem *segmentBarItem = [[UIBarButtonItem alloc] initWithCustomView:segmentedControl];
[segmentedControl release];

self.navigationItem.rightBarButtonItem = segmentBarItem;
[segmentBarItem release];
```

以编程方式配置 View Controller 的 navigation item 是大多数应用程序中最常见的做法。虽然你也可以使用 Interface Builder 创建栏按钮项，但以编程方式创建它们通常要简单得多。你应当在 View Controller 的 [viewDidLoad](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621495-viewdidload) 方法中创建这些条目。

支持就地编辑的视图可以在其导航栏中包含一种特殊类型的按钮，让用户能够在显示模式和编辑模式之间来回切换。`UIViewController` 的 [editButtonItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621471-editbuttonitem) 方法会返回一个预先配置好的按钮，按下该按钮会在 Edit 按钮和 Done 按钮之间切换，并以合适的值调用 View Controller 的 [setEditing:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621378-setediting) 方法。要将该按钮添加到 View Controller 的导航栏中，你可以使用类似下面这样的代码：

```objc
myViewController.navigationItem.rightBarButtonItem = [myViewController editButtonItem];
```

如果你在导航栏中包含了这个按钮，还必须重写 View Controller 的 `setEditing:animated:` 方法，并用它来调整你的视图层级。关于实现这个方法的更多信息，请参阅[为视图启用编辑模式](Custom%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvztga)。

在 iOS 3.0 及以后版本中，导航界面可以显示一个工具栏，并用当前可见的 View Controller 所提供的条目填充它。工具栏本身由 navigation controller 对象管理。之所以需要在这一层级支持工具栏，是为了在各屏幕之间创建流畅的过渡。当导航栈上的栈顶 View Controller 发生变化时，navigation controller 会为不同的工具栏条目集之间的切换添加动画。在你想要为特定 View Controller 切换工具栏可见性的情况下，它也会创建流畅的动画。

要为导航界面配置工具栏，你必须执行以下操作：

- 将 navigation controller 对象的 [toolbarHidden](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621875-toolbarhidden) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)设置为 `NO`，以显示工具栏。
- 按照[指定工具栏条目](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzsgy)中的说明，将一个包含 `UIBarButtonItem` 对象的数组赋给每个自定义 View Controller 的 [toolbarItems](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621867-toolbaritems) 属性。

  如果你不想为某个特定的 View Controller 显示工具栏，可以按照[显示和隐藏工具栏](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzsgu)中的说明隐藏工具栏。

图 3-11 展示了一个示例，说明你与自定义 View Controller 关联的对象是如何反映在工具栏中的。条目在工具栏中的显示顺序与它们在数组中提供的顺序一致。该数组可以包含各种类型的栏按钮项，包括固定和可伸缩的间距条目、系统按钮条目，或你提供的任何自定义按钮条目。在这个例子中，这五个条目都是来自 Mail 应用的按钮条目。

__图 3-11__  导航界面中的工具栏项

!

配置栏按钮项时，请始终记得为按钮关联合适的目标和动作。目标和动作信息就是你用来响应工具栏上点按操作的机制。在大多数情况下，目标应当是 View Controller 本身，因为它负责提供这些工具栏条目。

图 3-12 展示了一个在工具栏中间放置了一个分段控件的示例工具栏，清单 3-3 展示了配置这样一个工具栏所需的代码。你会在 View Controller 中实现这个方法，并在[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)时调用它。

__图 3-12__  工具栏中居中的分段控件

!

__清单 3-3__  配置带有居中分段控件的工具栏

```objc
- (void)configureToolbarItems
{
   UIBarButtonItem *flexibleSpaceButtonItem = [[UIBarButtonItem alloc]
                        initWithBarButtonSystemItem:UIBarButtonSystemItemFlexibleSpace
                        target:nil action:nil];

   // 创建并配置分段控件
   UISegmentedControl *sortToggle = [[UISegmentedControl alloc]
                        initWithItems:[NSArray arrayWithObjects:@"Ascending",
                                        @"Descending", nil]];
   sortToggle.segmentedControlStyle = UISegmentedControlStyleBar;
   sortToggle.selectedSegmentIndex = 0;
   [sortToggle addTarget:self action:@selector(toggleSorting:)
               forControlEvents:UIControlEventValueChanged];

   // 为分段控件创建栏按钮项
   UIBarButtonItem *sortToggleButtonItem = [[UIBarButtonItem alloc]
                                    initWithCustomView:sortToggle];
   [sortToggle release];

   // 设置我们的工具栏条目
   self.toolbarItems = [NSArray arrayWithObjects:
                         flexibleSpaceButtonItem,
                         sortToggleButtonItem,
                         flexibleSpaceButtonItem,
                         nil];

   [sortToggleButtonItem release];
   [flexibleSpaceButtonItem release];
}
```

除了在初始化期间设置工具栏条目之外，View Controller 还可以使用 [setToolbarItems:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621874-settoolbaritems) 方法动态地更改其现有的工具栏条目集。这个方法适用于你想要根据其他用户操作更新工具栏命令的场景。例如，你可以用它来实现一组层级化的工具栏条目，即点按工具栏上的某个按钮会显示一组相关的子按钮。

要为某个特定的 View Controller 隐藏工具栏，请将该 View Controller 的 [hidesBottomBarWhenPushed](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621863-hidesbottombarwhenpushed) 属性设置为 `YES`。当 navigation controller 遇到一个该属性被设置为 `YES` 的 View Controller 时，每当该 View Controller 被压入导航栈（或从导航栈移除）时，它都会生成相应的过渡动画。

如果你想要有时（但不是一直）隐藏工具栏，可以随时调用 navigation controller 的 [setToolbarHidden:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621888-settoolbarhidden) 方法。使用这个方法的一种常见做法是将其与调用 `setNavigationBarHidden:animated:` 方法结合起来，从而创建一个临时的全屏视图。例如，Photos 应用在全屏显示单张照片、且用户点按屏幕时，会切换这两个栏的可见性。

[下一页](Tab%20Bar%20Controllers.md)[上一页](Custom%20View%20Controllers.md)

