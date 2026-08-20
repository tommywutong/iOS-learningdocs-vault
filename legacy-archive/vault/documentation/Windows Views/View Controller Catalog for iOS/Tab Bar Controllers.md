---
title: iOS View Controller 一览
apple_id: TP40011313
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-11-15'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerCatalog/Chapters/TabBarControllers.html
archived_at: '2026-07-18T02:23:26.205992Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 一览](About%20View%20Controllers.md)


[下一页](Page%20View%20Controllers.md)[上一页](Navigation%20Controllers.md)

# Tab Bar Controller

你可以用 tab bar controller 把 app 组织成一种或多种彼此独立的操作模式。tab bar controller 的视图层级是自包含的，它由 tab bar controller 直接管理的视图和你所提供的内容 View Controller 管理的视图共同组成。每个内容 View Controller 管理一套独立的视图层级，而 tab bar controller 负责协调这些视图层级之间的导航。

本章介绍如何在 app 中配置和使用 tab bar controller。要了解可以怎样把 tab bar controller 与其他类型的 View Controller 对象组合起来，请参阅[组合式 View Controller 界面](Combined%20View%20Controller%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqnrnknltc)。

如果你想为同一组数据提供不同的观察角度，或者想按功能划分来组织 app，标签栏界面就很有用。标签栏界面的关键组成部分，是屏幕底部的那个标签栏视图。用户通过它在 app 的不同模式之间导航，它同时也能传达每种模式的状态信息。

标签栏界面的管理者是 tab bar controller 对象。tab bar controller 创建并管理标签栏视图，同时也管理为每种模式提供内容视图的那些 View Controller。每个内容 View Controller 都被指定为标签栏视图中某一个标签页的 View Controller。当用户点按某个标签页时，tab bar controller 对象会选中该标签页，并显示与对应内容 View Controller 关联的视图。

图 2-1 展示了 Clock app 实现的标签栏界面。tab bar controller 有自己的容器视图，它包含了其他所有视图，标签栏视图也在其中。自定义内容则由当前选中标签页的 View Controller 提供。

__图 2-1__  标签栏界面中的各个视图

!

当标签栏视图是标签栏界面的一部分时，绝不能对它进行修改。在标签栏界面中，标签栏视图被视为 tab bar controller 对象所拥有的私有视图层级的一部分。如果你确实需要更改活动标签页的列表，必须始终通过 tab bar controller 自身的方法来完成。要了解如何在运行时修改标签栏界面，请参阅[在运行时管理标签页](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmznknlti)。

一个标准的标签栏界面由以下对象组成：

- 一个 [UITabBarController](https://developer.apple.com/documentation/uikit/uitabbarcontroller) 对象
- 每个标签页各对应一个内容 View Controller 对象
- 一个可选的[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)对象

图 2-2 展示了 tab bar controller 与其关联的各个 View Controller 之间的关系。tab bar controller 的 [viewControllers](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621185-viewcontrollers) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)中的每个 View Controller，都对应标签栏中的一个标签页。

__图 2-2__  tab bar controller 及其关联的 View Controller

!

如果你往 `viewControllers` 属性中添加了超过五个项，tab bar controller 会自动插入一个特殊的 View Controller（称为 _More View Controller_）来负责显示多出来的那些项。More View Controller 提供了一个自定义界面，用一个表格列出多余的 View Controller，这个表格可以容纳任意数量的 View Controller。More View Controller 不能被自定义，也不能被选中，并且不会出现在 tab bar controller 管理的任何 View Controller 列表中。它会在需要时自动出现，与你的自定义内容彼此独立。不过，你可以通过访问 `UITabBarController` 的 [moreNavigationController](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621183-morenavigationcontroller) 属性获取它的引用。

你不能直接修改标签栏视图。tab bar controller 对象会根据内容 View Controller 提供的 [UITabBarItem](https://developer.apple.com/documentation/uikit/uitabbaritem) 对象来组装标签栏的内容。图 2-3 展示了 iPod app 中 tab bar controller、View Controller 和标签栏项对象三者之间的关系。由于 View Controller 的数量超过了一次能显示的上限，标签栏中只显示了前四个 View Controller 的标签栏项，最后一个标签栏项则由 More View Controller 提供。

__图 2-3__  iPod app 的标签栏项

!

由于标签栏是靠标签栏项来配置的，你必须在显示标签栏界面之前先配置好每个 View Controller 的标签栏项。如果你使用 Interface Builder 搭建界面，可以按[使用 storyboard 创建标签栏界面](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmznknltq)中的说明指定标题和图像。如果你以编程方式创建标签栏界面，则必须为每个内容 View Controller 创建一个新的 `UITabBarItem` 对象，具体做法见[以编程方式创建标签栏界面](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmznknltcni)。

tab bar controller 还支持一个可选的委托对象，可用来响应标签栏的选中和自定义操作。要了解如何响应与委托相关的消息，请参阅[在运行时管理标签页](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmznknlti)。

在创建标签栏界面之前，你需要先想清楚打算怎样使用它。由于标签栏界面会给你的数据强加一种全局性的组织方式，因此只应按以下这几种特定方式使用它：

- 直接安装为窗口的根 View Controller。
- 安装为 split view 界面中的两个 View Controller 之一。（仅限 iPad）
- 从另一个 View Controller 中以模态方式呈现。
- 在 popover 中显示。（仅限 iPad）

把标签栏界面装到 app 的主窗口里，是迄今为止最常见的用法。在这种场景下，标签栏界面为 app 的数据提供了根本性的组织原则，每个标签页把用户引向 app 的一个不同部分。你可以单独使用 tab bar controller，也可以把它与其他 View Controller 结合起来构建更复杂的界面。更多信息请参阅[组合式 View Controller 界面](Combined%20View%20Controller%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqnrnknltc)。

如果有非常特殊的需求确实值得这么做，也可以以模态方式呈现 tab bar controller。例如，你可以模态呈现一个 tab bar controller，用来编辑某个包含若干组不同选项的复杂数据集。由于模态视图会占满整个屏幕或屏幕的大部分（取决于设备），此时标签栏所体现的只是查看或编辑这份模态呈现数据时可用的几种选择。如果有更简单的设计方案可选，就不要这样使用标签栏。

由于标签栏界面中的每种模式都与其他模式相互独立，因此每个标签页的 View Controller 定义了该标签页的内容。这样一来，你为每个标签页选择的 View Controller 应当契合该操作模式的具体需要。如果需要呈现比较丰富的数据集，可以装入一个 navigation controller 来管理这些数据的导航；如果要呈现的数据比较简单，装入一个只有单个视图的内容 View Controller 就够了。

图 2-4 展示了 Clock app 的几个屏幕。World Clock 标签页使用了 navigation controller，主要是为了能显示编辑时钟列表所需的按钮。Stopwatch 标签页的整个界面只需要一个屏幕，因此只用了一个 View Controller。Timer 标签页的主屏幕使用了自定义 View Controller，当用户点按 When Timer Ends 按钮时，还会以模态方式呈现另一个 View Controller。

__图 2-4__  Clock app 的各个标签页

!

tab bar controller 会处理与呈现内容 View Controller 相关的全部交互，因此在管理标签页及其中的 View Controller 方面，你几乎不需要做什么。一旦显示出来，你的内容 View Controller 只需专注于呈现自己的内容即可。

要了解定义自定义 View Controller 的一般信息和指导，请参阅 _[View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_ 中的 Creating Custom Content View Controllers。

如果你正在新建 Xcode 工程，Tabbed Application 模板会在 storyboard 中为你生成一个 tab bar controller，并把它设为第一个场景。

要在 storyboard 中创建 tab bar controller，请执行以下操作：

1. 从库中拖出一个 tab bar controller。
2. Interface Builder 会创建一个 tab bar controller 和两个 View Controller，并在它们之间建立关系。这些关系把新建的两个 View Controller 分别标识为 tab bar controller 某一个标签页的 View Controller。
3. 在 Attributes 检查器中勾选 Is Initial View Controller 选项，把它显示为第一个 View Controller（或者用其他方式在你的用户界面中呈现该 View Controller）。

如果你更愿意以编程方式创建 tab bar controller，最合适的位置是应用程序委托的 [applicationDidFinishLaunching:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching) 方法。由于 tab bar controller 通常提供 app 窗口的根视图，你需要在启动之后、显示窗口之前立即创建它。创建标签栏界面的步骤如下：

1. [创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)一个新的 [UITabBarController](https://developer.apple.com/documentation/uikit/uitabbarcontroller) 对象。
2. 为每个标签页创建一个内容 View Controller。
3. 把这些 View Controller 放进一个数组，并把该数组赋给 tab bar controller 的 [viewControllers](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621185-viewcontrollers) 属性。
4. 把 tab bar controller 设为窗口的根 View Controller（或者用其他方式在你的界面中呈现它）。

清单 2-1 展示了在 app 主窗口中创建并安装标签栏界面所需的基本代码。这个例子只创建了两个标签页，但你可以创建更多 View Controller 对象并把它们加入 `controllers` 数组，从而创建任意数量的标签页。你需要把自定义 View Controller 名称 `MyViewController` 和 `MyOtherViewController` 替换成你自己 app 中的类。

__清单 2-1__  从零创建 tab bar controller

```objc
- (void)applicationDidFinishLaunching:(UIApplication *)application {
   tabBarController = [[UITabBarController alloc] init];

   MyViewController* vc1 = [[MyViewController alloc] init];
   MyOtherViewController* vc2 = [[MyOtherViewController alloc] init];

   NSArray* controllers = [NSArray arrayWithObjects:vc1, vc2, nil];
   tabBarController.viewControllers = controllers;

    window.rootViewController = tabBarController;
}
```


对于标签栏界面中的每个内容 View Controller，你都必须提供一个 [UITabBarItem](https://developer.apple.com/documentation/uikit/uitabbaritem) 对象，其中包含要在对应标签页中显示的图像和文本。你可以在显示标签栏界面之前的任意时刻把标签栏项与 View Controller 关联起来，做法是把标签栏项赋给对应 View Controller 的 [tabBarItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621175-tabbaritem) 属性。推荐在 View Controller 自身的初始化过程中创建标签栏项，不过这通常只对自定义 View Controller 可行。你也可以先创建并初始化 View Controller 对象，再创建标签栏项，然后建立二者的关联。

清单 2-2 展示了如何为一个自定义 View Controller 创建标签栏项。由于标签栏项是与自定义 View Controller 关联的，因此该 View Controller 在自己的初始化过程中就把标签栏项创建好了。在这个例子中，标签栏项既包含一张自定义图像（存放在应用程序包中），也包含一个自定义标题字符串。

__清单 2-2__  创建 View Controller 的标签栏项

```objc
UIImage* anImage = [UIImage imageNamed:@"MyViewControllerImage.png"];
UITabBarItem* theItem = [[UITabBarItem alloc] initWithTitle:@"Home" image:anImage tag:0];
```


创建好标签栏界面之后，有几种方式可以修改它并响应 app 中的变化。你可以添加和移除标签页，也可以用一个[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)根据动态条件阻止某些标签页被选中。你还可以给单个标签页添加徽标（badge），以引起用户对该标签页的注意。

如果标签栏界面中标签页的数量可以动态变化，你可以按需在运行时做出相应修改。在运行时更改标签页的方式，与创建时指定标签页的方式相同：把合适的一组 View Controller 赋给你的 tab bar controller。如果添加或移除标签页的过程可能被用户看到，可以用 [setViewControllers:animated:](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621177-setviewcontrollers) 方法为标签页的变化加上动画。

清单 2-3 展示了一个方法，它在用户点按同一标签页中的某个特定按钮时移除当前选中的标签页。这个方法由该标签页的 View Controller 实现。如果你想移除一个不再需要的标签页，可以在自己的代码中使用类似的做法。例如，你可以用它移除某个只需输入一次的用户专属数据所在的标签页。

__清单 2-3__  移除当前标签页

```objc
- (IBAction)processUserInformation:(id)sender
{
   // 调用某个 app 专用的方法来校验用户数据。
   // 如果该自定义方法返回 YES，就移除这个标签页。
   if ([self userDataIsValid])
   {
      NSMutableArray* newArray = [NSMutableArray arrayWithArray:self.tabBarController.viewControllers];
      [newArray removeObject:self];

      [self.tabBarController setViewControllers:newArray animated:YES];
   }
}
```


如果你需要阻止用户选中某个标签页，可以提供一个[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)，并在该对象上实现 [tabBarController:shouldSelectViewController:](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621166-tabbarcontroller) 方法。阻止标签页被选中只应是临时性的，比如某个标签页暂时没有任何内容时。举例来说，如果你的 app 要求用户提供某些特定信息（例如登录名和密码），你可以禁用除提示用户输入所需信息的那个标签页之外的所有标签页。清单 2-4 展示了这样一个方法大致的样子。其中 `hasValidLogin` 是需要你自己实现的自定义方法，用来校验用户提供的信息。

__清单 2-4__  阻止标签页被选中

```objc
- (BOOL)tabBarController:(UITabBarController *)aTabBar
         shouldSelectViewController:(UIViewController *)viewController
{
   if (![self hasValidLogin] && (viewController != [aTabBar.viewControllers objectAtIndex:0]) )
   {
      // 除第一个标签页外，其余全部禁用。
      return NO;
   }

   return YES;
}
```


标签栏上可能发生两类由用户发起的变更：

- 用户可以选中某个标签页。
- 用户可以重新排列标签页。

这两类变更都会报告给 tab bar controller 的[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)，也就是一个遵循 [UITabBarControllerDelegate](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate) [协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)的对象。你可以提供一个委托来跟踪用户所做的更改，并相应地更新 app 的状态信息。不过，不应该用这些通知去做那些本该由被隐藏和被显示的 View Controller 处理的工作。例如，你不应该用 tab bar controller 的委托去改变状态栏的外观，好让它匹配当前选中视图的风格。这类视觉上的变化，最好交给你的内容 View Controller 来处理。

要进一步了解 `UITabBarControllerDelegate` 协议的各个方法及其用法，请参阅 _[UITabBarControllerDelegate Protocol Reference](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate)_。

More View Controller 内置了让用户修改标签栏中所显示项的能力。对于标签页很多的 app，这项能力让用户可以自行挑选哪些屏幕可以直接访问、哪些需要多走几步导航才能到达。图 2-5 左侧展示的是 iPod app 显示的 More 选择屏幕。当用户点按该屏幕左上角的 Edit 按钮时，More 控制器会自动显示右侧那个配置屏幕。在这个屏幕上，用户可以把新的项拖到标签栏上，以替换标签栏中原有的内容。

__图 2-5__  配置 iPod app 的标签栏

!

多数情况下，让用户重新排列标签页是个不错的做法，但有时你可能不希望用户把某些特定标签页从标签栏中移除，或者不希望某些特定标签页被放到标签栏上。这种情况下，你可以给 [customizableViewControllers](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621184-customizableviewcontrollers) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)赋一个 View Controller 对象数组。这个数组应当只包含允许重新排列的那部分 View Controller。不在该数组中的 View Controller 不会出现在配置屏幕上；如果它们已经在标签栏上，也无法被移除。

标签栏界面中标签页的外观通常不会变化，除非它被选中。如果你想让用户注意到某个特定标签页——比如该标签页上有新内容需要用户查看——可以使用徽标。

徽标是显示在标签页角上的一个红色小标记，里面是你提供的自定义文本。徽标通常包含一个数值，反映该标签页上有多少条新内容，不过你也可以指定很短的字符串。图 2-6 展示了 Phone app 中各标签页的徽标。

__图 2-6__  标签栏项上的徽标

!

要给某个标签页设置徽标，请把一个非 nil 的值赋给对应标签栏项的 [badgeValue](https://developer.apple.com/documentation/uikit/uitabbaritem/1617065-badgevalue) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)。清单 2-5 展示了一个在徽标中显示新内容数量的 View Controller 可能会如何设置徽标值。

__清单 2-5__  设置标签页的徽标

```objc
if (numberOfNewItems == 0)
   self.tabBarItem.badgeValue = nil;
else
   self.tabBarItem.badgeValue = [NSString stringWithFormat:@"%d", numberOfNewItems];
```

何时显示徽标值、何时更新徽标值，都由你自己决定。不过，如果你的 View Controller 中有一个保存该数值的属性，可以利用键值观察（KVO）通知检测该值的变化，并相应地更新徽标。要了解如何设置和处理 KVO 通知，请参阅 _[键值观察编程指南](../../Cocoa/Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_。

tab bar controller 默认支持竖屏方向；除非它包含的所有 View Controller 都支持横屏方向，否则不会旋转到横屏。当设备方向发生变化时，tab bar controller 会查询自己的 View Controller 数组；只要其中有任何一个不支持该方向，tab bar controller 就不会改变自身的方向。

tab bar controller 对全屏布局的支持方式与大多数其他控制器不同。如果你希望内容 View Controller 的视图延伸到状态栏或导航栏（如果有的话）下方，仍然可以把它的 [wantsFullScreenLayout](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621390-wantsfullscreenlayout) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)设为 `YES`。不过，把这个属性设为 `YES` 并不会让视图延伸到标签栏视图下方。tab bar controller 总是会调整你的视图大小，以防止它被标签栏遮挡。

要进一步了解自定义视图的全屏布局，请参阅 _[View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_ 中的 Creating Custom Content View Controllers。

[下一页](Page%20View%20Controllers.md)[上一页](Navigation%20Controllers.md)

