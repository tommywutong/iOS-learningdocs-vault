---
title: iOS View Controller 编程指南（旧版）
apple_id: TP40011381
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerPGforiOSLegacy/TabBarControllers/TabBarControllers.html
archived_at: '2026-07-18T02:24:02.027107Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 编程指南（旧版）](About%20View%20Controllers.md)


[下一页](iPad-Specific%20Controllers.md)[上一页](Navigation%20Controllers.md)

# Tab Bar Controller

你可以使用 tab bar controller 把应用组织成一个或多个独立的操作模式。一个 tab bar controller 管理着一个自成一体的视图层级（称为标签栏界面），其内容一部分由 tab bar controller 管理的视图组成，另一部分由你提供的自定义 View Controller 管理的视图组成。

本章概述了如何在你的应用中配置和使用 tab bar controller。有关如何将 tab bar controller 与其他类型的 View Controller 对象组合使用的信息，参见[Combined View Controller Interfaces](Combined%20View%20Controller%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgqwvgvzr)。

标签栏界面适用于以下情形：你想为同一组数据提供不同的呈现视角，或者你想按功能来组织你的应用。标签栏界面的关键组成部分是位于屏幕底部的标签栏视图。这个视图用于发起应用不同模式之间的导航，还可以传达每种模式的状态信息。

标签栏界面的管理者是一个 tab bar controller 对象。tab bar controller 创建并管理标签栏视图，同时也管理着为每种模式提供内容视图的自定义 View Controller。每个自定义 View Controller 都被指定为标签栏视图中某个标签页的_根 View Controller_。当用户点按某个标签页时，tab bar controller 对象会选中该标签页，并首先显示与对应根 View Controller 关联的视图。

图 4-1 展示了 Clock 应用实现的标签栏界面。tab bar controller 拥有自己的容器视图，其中包含了所有其他视图，包括标签栏视图。自定义内容由当前选中标签页的根 View Controller 提供。

__图 4-1__  标签栏界面的视图

!

虽然标签栏视图通常是一个可自定义的对象，但当它成为标签栏界面的一部分时，就不得再对其进行修改。在标签栏界面中，标签栏视图被视为 tab bar controller 对象所拥有的私有视图层级的一部分。如果你确实需要更改当前有效的标签页列表，必须始终通过 tab bar controller 自身的方法来完成。有关如何在运行时修改标签栏界面的信息，参见[在运行时管理标签页](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgiwvgvzu)。

一个标准的标签栏界面由以下对象组成：

- 一个 [UITabBarController](https://developer.apple.com/documentation/uikit/uitabbarcontroller) 对象
- 每个标签页对应一个自定义 View Controller 对象
- 一个可选的[委托（delegate）](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)对象

图 4-2 展示了 tab bar controller 与其关联 View Controller 之间的关系。tab bar controller 的 [viewControllers](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621185-viewcontrollers) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)中的每个 View Controller 都是标签栏中对应标签页的根 View Controller。

__图 4-2__  tab bar controller 及其关联的 View Controller

!

你提供的自定义 View Controller 是标签栏界面中最重要的元素。每个 View Controller 都定义了对应标签页被选中时所显示的内容。你可以使用显示单个视图的自定义 View Controller，也可以使用 navigation controller 来支持标签页内更复杂的导航。不过，你不应该在标签页里再安装另一个 tab bar controller。

如果你在 `viewControllers` 属性中添加超过五个项，tab bar controller 会自动插入一个特殊的 View Controller（称为 _More view controller_）来处理额外项的显示。More view controller 提供了一个自定义界面，以表格形式列出其余的 View Controller，并可以扩展以容纳任意数量的 View Controller。More view controller 不能被自定义或被选中，也不会出现在 tab bar controller 管理的任何 View Controller 列表中。在大多数情况下，它会在需要时自动出现，与你的自定义内容是相互独立的。不过你可以通过访问 `UITabBarController` 的 [moreNavigationController](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621183-morenavigationcontroller) 属性来获取对它的引用。

尽管标签栏视图是标签栏界面的关键部分，但你不能直接修改这个视图。tab bar controller 对象会根据你的自定义 View Controller 提供的 [UITabBarItem](https://developer.apple.com/documentation/uikit/uitabbaritem) 对象来组装标签栏的内容。图 4-3 展示了 iPod 应用中 tab bar controller、View Controller 和标签栏项对象之间的关系。由于 View Controller 的数量超过了可同时显示的上限，因此只有前四个 View Controller 的标签栏项会被显示出来。最后一个标签栏项由 More view controller 提供。

__图 4-3__  iPod 应用的标签栏项

!

由于标签栏项用于配置标签栏，你必须在显示标签栏界面之前配置好每个根 View Controller 的标签栏项。如果你使用 Interface Builder 来搭建界面，可以按照[使用 Nib 文件创建标签栏界面](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgiwvgvzrgq)中所述的方式指定标题和图片。如果你以编程方式创建标签栏界面，则必须按照[以编程方式创建标签栏界面](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgiwvgvzrgu)中所述，为每个 View Controller 创建一个新的 `UITabBarItem` 对象。

tab bar controller 还支持一个可选的委托对象，可用于响应标签栏的选择和自定义操作。有关如何响应委托相关消息的信息，参见[在运行时管理标签页](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgiwvgvzu)。

在创建标签栏界面之前，你需要先确定打算如何使用它。由于它会给你的数据强加一种整体组织结构，因此使用标签栏界面的合适方式只有为数不多的几种：

- 直接安装在应用的主窗口中。
- 作为 split view 界面中两个根视图之一来安装。（仅限 iPad）
- 以模态方式呈现，用于显示需要自身按模式组织的数据。
- 从 popover 中显示。（仅限 iPad）

将标签栏界面安装在应用的主窗口中，是迄今为止最常见的使用方式。在这种场景下，标签栏界面为应用的数据提供了基本的组织原则，每个标签页都会把用户引导到应用的一个独立部分。由于它提供了对整个应用的访问入口，因此必须是窗口中的根级部分。

当然，如果某个非常特殊的需求使这样做值得一试，仍然可以以模态方式呈现 tab bar controller。例如，你可以以模态方式呈现一个 tab bar controller，用来编辑某个包含若干独立选项集的复杂数据集。由于模态视图会填满全部或大部分屏幕（取决于设备），标签栏的存在只是反映了查看或编辑模态呈现数据时的可选项。不过，如果有更简单的设计方案可用，就应当避免以这种方式使用标签栏。

由于标签栏界面的每种模式都与其他模式相互独立，因此每个标签页中的根 View Controller 本质上定义了该标签页的内容。所以，你为每个标签页选择的 View Controller 应当反映该特定操作模式的需求。如果你需要呈现相对丰富的数据集，可以安装一个 navigation controller 来管理这些数据的导航。如果要呈现的数据比较简单，你可以安装一个只有单一视图的自定义 View Controller。

图 4-4 展示了 Clock 应用的几个界面。World Clock 标签页使用 navigation controller，主要是为了能够呈现编辑时钟列表所需的按钮。Stopwatch 标签页的整个界面只需要单个界面，因此使用单个 View Controller。Timer 标签页在主界面使用自定义 View Controller，并在用户点按 When Timer Ends 按钮时以模态方式呈现另一个 View Controller。

__图 4-4__  Clock 应用的标签页

!

由于 tab bar controller 处理了与呈现根 View Controller 相关的所有交互，你在管理标签页及其中的 View Controller 方面几乎不需要做什么。一旦显示出来，你的自定义 View Controller 只需专注于呈现自身的内容即可。

从 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)加载 tab bar controller 的语义与加载自定义 View Controller 略有不同。对于自定义 View Controller，你使用 nib 文件来存储与该 View Controller 关联的视图，但通常会单独创建这个 View Controller 本身——要么以编程方式创建，要么从另一个 nib 文件中加载。而 tab bar controller 则始终以编程方式创建其视图，因此没有视图需要放在单独的 nib 文件中。这种行为的一个结果是：tab bar controller 从不管理 nib 文件——换句话说，你永远不会把 tab bar controller 指定为 File's Owner 占位符。相反，唯一会将 tab bar controller 与 nib 文件混用的情形，是 tab bar controller 本身被存储在 nib 文件中的时候。因此，tab bar controller 几乎总是作为“乘客”存在于由其他对象管理的 nib 文件中。

将 tab bar controller 包含在应用的主 nib 文件中是最合理的做法。当 tab bar controller 本身为应用窗口提供主视图时，就应该这样做。虽然你也可以从主 nib 文件（或其他任何 nib 文件）中加载一个以模态方式呈现的 tab bar controller，但这样做并不理想。实际上，通常在使用它的地方以编程方式创建 tab bar controller 会更简单。

图 4-5 展示了在应用主 nib 文件中，tab bar controller 及其相关对象的典型配置。每个自定义 View Controller 都代表与某个标签页关联的根 View Controller。由于它们都是自定义 View Controller（而不是 navigation controller），每个 View Controller 都通过引用指向一个包含其视图的单独 nib 文件。虽然你也可以把自定义视图包含在主 nib 文件中，但不建议这样做。将视图存储在单独的 nib 文件中，可以让系统在需要时选择将它们从内存中清除。

__图 4-5__  包含标签栏界面的 Nib 文件

!

如果你从头开始创建 Xcode 项目，可以使用 Tab Bar Application 模板来创建。这个项目自带的主 nib 文件中包含一个已针对该项目做了最基本配置的 tab bar controller 对象。

下面的步骤展示了如何从零开始，把一个 tab bar controller 添加到应用的主 nib 文件中。如果你是从 Tab Bar Application 模板开始的，可以直接跳过前两步。

1. 从库中把一个 tab bar controller 对象拖到你的 Interface Builder 文档窗口中。

   当你把一个 tab bar controller 添加到 nib 文件中时，Interface Builder 还会添加一个标签栏视图、两个根 View Controller，以及两个标签栏项（每个 View Controller 对应一个）。你可以通过在 tab bar controller 编辑界面中选中这些对象来访问其中一些对象。在大纲模式或浏览器模式下，你也可以从文档窗口中选择任意对象。

   如果你是使用 Tab Bar Application 模板创建的项目，这一步已经替你完成了。
2. 使用 outlet 保存对 tab bar controller 的引用。

   为了在运行时访问 tab bar controller，你要么需要使用 outlet，要么必须在加载 nib 文件时显式获取该 nib 文件的顶层对象。使用 outlet 通常要简单得多。要添加一个 outlet，请在你的应用委托类的声明中添加一个类似下面这样的变量：

```objc
@interface MyAppDelegate : NSObject <UIApplicationDelegate> {
   IBOutlet UITabBarController*  myTabBarController;
}
@end
```

   添加好 outlet 定义之后，从这个 outlet 创建一个到 tab bar controller 对象的连接。

   如果你是使用 Tab Bar Application 模板创建的项目，这一步已经替你完成了。
3. 添加或删除 View Controller，以反映界面所需的标签页数量。

   嵌入在 tab bar controller 对象中的 View Controller 数量，决定了标签栏界面所显示的标签页数量。你最终的 tab bar controller 应该至少有两个 View Controller；否则，使用 tab bar controller 的必要性就值得怀疑了。从 Interface Builder 库中，你可以拖入一个 View Controller 对象（`UIViewController`）、Navigation Controller 对象（`UINavigationController`）或 Table View Controller 对象（`UITableViewController`），并将其与某个标签页关联。

   要添加一个 View Controller，可以执行以下操作之一：

   - 从库中把合适的对象拖到编辑界面中的标签栏上。
   - 从库中把对象拖到 Interface Builder 文档窗口中的 tab bar controller 上。此时窗口必须处于大纲模式。

   在为界面添加 navigation controller 或 table view controller 时，你应该从库中拖入相应的对象，或者选中 tab bar controller 并使用 Attributes 检查器配置 View Controller 的类型。这两种方式都会把正确类型的 View Controller 对象添加到你的 nib 文件中。你永远不应该通过把一个通用的 View Controller 对象拖入 nib 文件、再把它的类名改成所需的类类型，来添加 navigation controller 或 table view controller。

   要删除一个 View Controller，请在编辑界面或文档窗口中选中该 View Controller 对象，然后按 Delete 键。
4. 按照你希望它们在屏幕上出现的顺序排列这些 View Controller。

   你可以通过拖动 tab bar controller 编辑界面上显示的标签页，或者在 Interface Builder 文档窗口（仅限大纲模式）中拖动这些 View Controller，来重新排列它们（以及对应的标签页）。虽然编辑界面会显示所有标签页，但运行时只会显示五个。如果你的 tab bar controller 包含六个或更多 View Controller，最初标签栏中只会显示前四个。标签栏上的最后一个位置留给 More view controller，用来呈现其余的 View Controller。
5. 为每个标签页配置根 View Controller。

   对于每个根 View Controller，你应当配置以下属性：

   - 使用 Identity 检查器设置任何自定义 View Controller 对象的类。如果根 View Controller 是一个通用的 View Controller 对象或 Table View Controller 对象，你可以把类名改成你的自定义子类。如果它是一个 Navigation Controller 对象，则不要更改类名。
   - 为该 View Controller 提供一个视图。首选的做法是把这个 View Controller 的 NIB Name 属性配置为包含该视图的 nib 文件名。虽然你也可以把视图包含在主 nib 文件中，但不建议这样做。
   - 根据需要，为该 View Controller 配置任何样式或外观信息。

   如果你为某个根 View Controller 使用了 navigation controller，请按照[从 Nib 文件加载 navigation 界面](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzsha)中所述进行配置。有关如何在 tab bar controller 中嵌入 navigation controller 的更多信息和示例，参见[向标签栏界面添加 navigation controller](Combined%20View%20Controller%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgqwvgvzs)。
6. 为每个 View Controller 配置标签栏项。

   你可以从 tab bar controller 编辑界面，或者处于大纲模式或浏览器模式下的 Interface Builder 文档窗口中选中标签栏项。使用 Interface Builder，你可以指定标签栏项的标题、图片和徽章。或者，你也可以通过在 Attributes 检查器中为 Identifier 属性赋值，把标签栏项设置为某个标准系统标签页。
7. 在你应用委托的 [applicationDidFinishLaunching:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching) 方法中，把 tab bar controller 的视图添加到你的主窗口中。

   tab bar controller 不会自动把自己安装到应用的窗口中。你必须使用类似下面这样的代码，以编程方式完成这一步：

```objc
- (void)applicationDidFinishLaunching:(UIApplication *)application {
    [window addSubview:myTabBarController.view];
}
```
8. 保存你的 nib 文件。

对于随 tab bar controller 一起添加到 nib 文件中的标签栏视图，你通常不需要再对其做任何配置。这个栏不包含任何样式选项，其余所有选项都由 tab bar controller 对象替你管理。

有关使用 Interface Builder 配置 nib 文件的更多信息，参见 _[Interface Builder User Guide](../../Developer%20Tools/Interface%20Builder%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbu)_。

如果你更喜欢以编程方式创建 tab bar controller，最合适的地方是在应用委托的 [applicationDidFinishLaunching:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching) 方法中。由于 tab bar controller 通常为应用的窗口提供根视图，你需要在启动之后、显示窗口之前立即创建它。创建标签栏界面的步骤如下：

1. [创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)一个新的 [UITabBarController](https://developer.apple.com/documentation/uikit/uitabbarcontroller) 对象。
2. 为每个标签页创建一个自定义根 View Controller 对象。
3. 把这些根 View Controller 添加到一个数组中，并将该数组赋值给 tab bar controller 的 [viewControllers](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621185-viewcontrollers) 属性。
4. 把 tab bar controller 的视图添加到应用的主窗口中。

清单 4-1 展示了在应用主窗口中创建并安装一个 tab bar controller 界面所需的基本代码。这个示例只创建了两个标签页，但你可以按需创建更多标签页，方法是创建更多 View Controller 对象并把它们添加到 `controllers` 数组中。你需要把自定义 View Controller 名称 `MyViewController` 和 `MyOtherViewController` 替换成你自己应用中的类。

__清单 4-1__  从零开始创建 tab bar controller

```objc
- (void)applicationDidFinishLaunching:(UIApplication *)application {
   tabBarController = [[UITabBarController alloc] init];

   MyViewController* vc1 = [[MyViewController alloc] init];
   MyOtherViewController* vc2 = [[MyOtherViewController alloc] init];

   NSArray* controllers = [NSArray arrayWithObjects:vc1, vc2, nil];
   tabBarController.viewControllers = controllers;

   // 把 tab bar controller 当前的视图添加为窗口的子视图
   [window addSubview:tabBarController.view];
}
```


对于标签栏界面中的每个根 View Controller，你都必须提供一个 [UITabBarItem](https://developer.apple.com/documentation/uikit/uitabbaritem) 对象，用来显示对应标签页中的图片和文字。你可以在显示标签栏界面之前的任意时刻，把标签栏项与你的 View Controller 关联起来。具体做法是把标签栏项赋值给对应 View Controller 的 [tabBarItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621175-tabbaritem) 属性。创建标签栏项的理想时机是在 View Controller 自身的初始化过程中，但这通常只对自定义 View Controller 可行。你也可以先创建并初始化 View Controller 对象，再创建标签栏项，然后再建立关联，这样同样简单。

清单 4-2 展示了如何为一个自定义 View Controller 创建标签栏项的示例。由于它与一个自定义 View Controller 相关联，因此该 View Controller 会在自身初始化过程中创建这个标签栏项。在这个示例中，标签栏项既包含一张自定义图片（存储在应用的 bundle 中），也包含一个自定义标题字符串。

__清单 4-2__  创建 View Controller 的标签栏项

```objc
- (id)init {
   if (self = [super initWithNibName:@"MyViewController" bundle:nil]) {
      self.title = @"My View Controller";

      UIImage* anImage = [UIImage imageNamed:@"MyViewControllerImage.png"];
      UITabBarItem* theItem = [[UITabBarItem alloc] initWithTitle:@"Home" image:anImage tag:0];
      self.tabBarItem = theItem;
      [theItem release];
   }
   return self;
}
```

如果你是从 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)加载标签栏界面，也可以使用 Interface Builder 来创建标签栏项。有关在 nib 文件中包含 tab bar controller（及标签栏项）的更多信息，参见[使用 Nib 文件创建标签栏界面](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgiwvgvzrgq)。

创建好标签栏界面之后，有几种方式可以对其进行修改，并响应应用中的变化。你可以添加和移除标签页，或者使用[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)，根据动态条件阻止某些标签页被选中。你还可以为单个标签页添加徽章，以引起用户对该标签页的注意。以下各节将展示如何在你的应用中运用这些功能。

如果你标签栏界面中的标签页数量可能会动态变化，你可以在运行时按需做出相应的更改。在运行时更改标签页的方式，与在创建时指定标签页的方式相同，都是把合适的一组 View Controller 赋值给你的 tab bar controller。如果你添加或移除标签页的操作可能会被用户看到，可以使用 [setViewControllers:animated:](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621177-setviewcontrollers) 方法为标签页的变化添加动画效果。

清单 4-3 展示了一个方法，它会在用户点按同一标签页中某个特定按钮时，移除当前选中的标签页。这个方法由该标签页的根 View Controller 实现。如果你想移除一个不再需要的标签页，可以在自己的代码中使用类似的方法。例如，你可以用它来移除一个包含某些只需录入一次的用户专属数据的标签页。

__清单 4-3__  移除当前标签页

```objc
- (IBAction)processUserInformation:(id)sender
{
   // 调用某个特定于应用的方法来校验用户数据。
   // 如果这个自定义方法返回 YES，就移除该标签页。
   if ([self userDataIsValid])
   {
      NSMutableArray* newArray = [NSMutableArray arrayWithArray:self.tabBarController.viewControllers];
      [newArray removeObject:self];

      [self.tabBarController setViewControllers:newArray animated:YES];
   }
}
```


如果你需要阻止用户选择某个标签页，可以通过提供一个[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)，并在该对象上实现 [tabBarController:shouldSelectViewController:](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621166-tabbarcontroller) 方法来实现。阻止选择标签页应仅在临时情形下使用，比如某个标签页暂时没有任何内容时。例如，如果你的应用要求用户提供某些特定信息（比如登录名和密码），你可以禁用除提示用户输入所需信息之外的所有标签页。清单 4-4 展示了这样一个方法的示例。`hasValidLogin` 方法是一个你需要自行实现的自定义方法，用来校验所提供的信息。

__清单 4-4__  阻止选择标签页

```objc
- (BOOL)tabBarController:(UITabBarController *)aTabBar
         shouldSelectViewController:(UIViewController *)viewController
{
   if (![self hasValidLogin] && (viewController != [aTabBar.viewControllers objectAtIndex:0]) )
   {
      // 禁用除第一个标签页外的所有标签页。
      return NO;
   }

   return YES;
}
```


标签栏上可能发生两类由用户发起的更改：

- 用户可以选择某个标签页。
- 用户可以重新排列标签页。

这两类更改都会上报给 tab bar controller 的[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)——一个遵循 [UITabBarControllerDelegate](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate) [协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)的对象。你可以提供一个委托来追踪用户的更改，并相应地更新应用的状态信息。不过，你不应该利用这些通知来执行本应由被隐藏和显示的 View Controller 自己处理的工作。例如，你不应该在 tab bar controller 的委托里去改变状态栏的外观，使其匹配当前选中视图的样式。这类视觉上的变化最好交由你的自定义 View Controller 来处理。

有关 `UITabBarControllerDelegate` 协议方法及其用法的更多信息，参见 _[UITabBarControllerDelegate Protocol Reference](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate)_。

More view controller 内置了让用户修改标签栏中所显示项的支持。对于标签页很多的应用来说，这项支持让用户可以自行挑选哪些界面便于直接访问，哪些界面需要额外的导航才能到达。图 4-6 左侧展示了 iPod 应用所显示的 More 选择界面。当用户点按该界面左上角的 Edit 按钮时，More controller 会自动显示右侧所示的配置界面。在这个界面上，用户可以通过把新的项拖入标签栏来替换其内容。

__图 4-6__  配置 iPod 应用的标签栏

!

虽然在大多数情况下，让用户能够重新排列标签页是个好主意，但在某些情形下，你可能不希望用户从标签栏中移除特定的标签页，或者把特定的标签页放到标签栏上。在这些情形下，你可以把一个 View Controller 对象数组赋值给 [customizableViewControllers](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621184-customizableviewcontrollers) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)。这个数组应当只包含允许被重新排列的那部分 View Controller。不在这个数组中的 View Controller 不会显示在配置界面上，如果它们已经存在于标签栏中，也无法被移除。

标签栏界面中某个标签页的外观通常不会发生变化，除非它被选中。不过，如果你想引起用户对某个特定标签页的注意——比如该标签页上有新内容需要用户查看——可以通过徽章来实现。

徽章是显示在标签页角落的一个红色小标记，里面是你提供的一些自定义文字。徽章通常包含数值，反映该标签页上可查看的新项数量，但你也可以指定非常简短的字符串。图 4-7 展示了 Phone 应用中各标签页的徽章。

__图 4-7__  标签栏项的徽章

!

要为某个标签页分配徽章，需要为对应标签栏项的 [badgeValue](https://developer.apple.com/documentation/uikit/uitabbaritem/1617065-badgevalue) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)赋一个非 nil 的值。例如，一个在徽章中显示新项数量的 View Controller，可能会使用类似下面的代码来生成徽章的值。（注意，示例中的 `numberOfNewItems` 属性是该 View Controller 实现的一个虚构属性，用来追踪新项的数量。要在你自己的代码中实现这个示例，你需要把对该属性的引用替换为来自你自己 View Controller 的合适值。）

```objc
if (self.numberOfNewItems == 0)
   self.tabBarItem.badgeValue = nil;
else
   self.tabBarItem.badgeValue = [NSString stringWithFormat:@"%d", self.numberOfNewItems];
```

何时显示徽章的值以及在合适的时机更新该值，由你自行决定。不过，如果你的 View Controller 包含一个持有此类值的属性（比如前面示例中虚构的 `numberOfNewItems` 属性），你可以使用 KVO 通知来检测该值的变化，并相应地更新徽章。有关设置和处理 KVO 通知的信息，参见 _[Key-Value Observing Programming Guide](../../Cocoa/Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_。

tab bar controller 默认支持竖屏方向，除非所有根 View Controller 都支持横屏方向，否则不会旋转到横屏方向。当设备方向发生变化时，tab bar controller 会查询其 View Controller 数组。只要其中任何一个不支持该方向，tab bar controller 就不会改变自身的方向。

tab bar controller 对全屏布局的支持方式，与大多数其他 controller 不同。如果你希望自定义 View Controller 的视图延伸到状态栏或 navigation bar（如果存在）下方，仍然可以把该 View Controller 的 [wantsFullScreenLayout](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621390-wantsfullscreenlayout) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)设置为 `YES`。然而，把这个属性设置为 `YES` 并不会让视图延伸到标签栏视图下方。tab bar controller 总是会调整你的视图大小，防止它延伸到标签栏下方。

有关自定义视图全屏布局的更多信息，参见[为自定义视图采用全屏布局](Custom%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsha)。

[下一页](iPad-Specific%20Controllers.md)[上一页](Navigation%20Controllers.md)

