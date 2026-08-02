---
title: iOS View Controller 编程指南（旧版）
apple_id: TP40011381
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerPGforiOSLegacy/iPadControllers/iPadControllers.html
archived_at: '2026-07-18T02:24:07.803718Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 编程指南（旧版）](About%20View%20Controllers.md)


[下一页](Modal%20View%20Controllers.md)[上一页](Tab%20Bar%20Controllers.md)

# iPad 专用控制器

由于 iPad 与 iPhone、iPod touch 设备的外形规格不同，它还拥有几个专门用于在该外形规格下呈现内容的特殊控制器对象。我们鼓励 iPad 应用的开发者尽可能使用这些控制器。不过，如果你在开发一个通用应用，请务必注意，当应用运行在 iPhone 或 iPod touch 上时，不要创建和使用这些控制器。

[UIPopoverController](https://developer.apple.com/documentation/uikit/uipopovercontroller) 类本身并不是一个 View Controller，但它负责管理 View Controller 的呈现。你可以使用一个 popover 控制器对象，通过 _popover_ 来呈现内容——popover 是悬浮在应用窗口之上的一层视觉层。popover 提供了一种轻量级的方式来向用户呈现信息或从用户那里收集信息，常见的使用场景包括：

- 显示屏幕上某个对象的相关信息。
- 管理经常访问的工具或配置选项
- 呈现一系列可对某个视图内对象执行的操作列表
- 当设备处于竖屏方向时，呈现 split view controller 中的一个面板

对于上述场景，使用 popover 比使用模态视图更不显突兀、也更省事。在 iPad 应用中，模态视图应当只保留给那些需要用户明确接受或取消某个操作或信息的场景。例如，你可以使用模态视图向用户索要密码，以授权访问应用的其余部分。在大多数其他情况下，应当改用 popover。popover 的优势在于它不会覆盖整个屏幕，只需在 popover 视图之外轻点一下即可将其消除。因此，在不需要用户与你的内容进行交互、但需要为用户提供信息或附加功能的场景中，popover 是一个绝佳的选择。

图 5-1 展示了一个使用 popover 显示 split view 界面中某个面板的示例。在 popover 中选择一出戏剧后，应用的主视图会显示该剧目的相关信息。（关于创建 split view 界面的更多信息，请参阅 [Split View Controller](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqnrnknlte)。）

__图 5-1__  使用 popover 显示主面板

!!

popover 的内容来自你所提供的 [view controller 对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11)。popover 能够呈现大多数类型的 View Controller，包括自定义 View Controller、table view controller、navigation controller，乃至 tab bar controller。当你准备好在 popover 中呈现该 View Controller 时，请执行以下步骤：

1. [创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) [UIPopoverController](https://developer.apple.com/documentation/uikit/uipopovercontroller) 类的一个实例，并用你的 View Controller 对象对其进行[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)。
2. 指定 popover 的大小，你可以通过以下两种方式之一来实现：

   - 为你想在 popover 中显示的 View Controller 的 [contentSizeForViewInPopover](https://developer.apple.com/documentation/uikit/uiviewcontroller/1619323-contentsizeforviewinpopover) 属性赋值。
   - 为 popover 控制器自身的 [popoverContentSize](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624667-contentsize) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)赋值。
3. （可选）为 popover 指定一个[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)。关于委托职责的更多信息，请参阅[容器 View Controller](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmznknlte)。
4. 呈现该 popover。

呈现 popover 时，你需要将它与用户界面的某个特定部分关联起来。popover 通常与工具栏按钮相关联，因此 [presentPopoverFromBarButtonItem:permittedArrowDirections:animated:](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624668-presentpopoverfrombarbuttonitem) 方法是从应用工具栏呈现 popover 的一种便捷方式。你也可以使用 [presentPopoverFromRect:inView:permittedArrowDirections:animated:](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624660-present) 方法，将 popover 与视图中的某个特定部分相关联。

popover 通常会从被呈现的 View Controller 的 [contentSizeForViewInPopover](https://developer.apple.com/documentation/uikit/uiviewcontroller/1619323-contentsizeforviewinpopover) 属性中获取其初始大小。该属性存储的默认大小为宽 320 像素、高 1100 像素。你可以通过为 `contentSizeForViewInPopover` 属性赋一个新值来自定义这个默认值。你也可以为 popover 控制器自身的 `popoverContentSize` 属性赋值。如果你更改了 popover 所显示的 View Controller，那么你在 `popoverContentSize` 属性中设置的任何自定义尺寸信息都会被新 View Controller 的尺寸取代。当 popover 处于可见状态时，对内容 View Controller 或其尺寸所做的更改都会自动带有动画效果。你也可以使用 [setPopoverContentSize:animated:](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624670-setpopovercontentsize) 方法来更改尺寸（可以选择是否带动画）。

清单 5-1 展示了一个简单的[动作方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/TargetAction.html#//apple_ref/doc/uid/TP40009071-CH3)，用于响应用户对工具栏按钮的轻点操作并呈现一个 popover。该 popover 存储在一个属性中（由所属类定义），该属性对 popover 对象进行了保留（retain）。popover 的大小被设置为该 View Controller 视图的大小，但二者并不需要保持一致。当然，如果二者不一致，你就必须使用一个 scroll view，以确保用户能够看到 popover 的全部内容。

__清单 5-1__  呈现一个 popover

```objc
- (IBAction)toolbarItemTapped:(id)sender
{
   MyCustomViewController* content = [[MyCustomViewController alloc] init];
   UIPopoverController* aPopover = [[UIPopoverController alloc]
        initWithContentViewController:content];
   aPopover.delegate = self;
   [content release];

   // 将 popover 存储在自定义属性中，供以后使用。
   self.popoverController = aPopover;
   [aPopover release];

   [self.popoverController presentPopoverFromBarButtonItem:sender
        permittedArrowDirections:UIPopoverArrowDirectionAny animated:YES];
}
```

当用户在 popover 视图之外轻点时，popover 会自动被消除。在 popover 内部轻点不会导致其自动被消除，但你可以使用 [dismissPopoverAnimated:](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624662-dismisspopoveranimated) 方法以编程方式消除它。当用户在你的 View Controller 内容中选择了某个项目，或执行了某个理应移除该 popover 的操作时，你可能就需要这样做。如果你要以编程方式消除 popover，就需要把该 popover 控制器对象的引用存储在你的 View Controller 能够访问到的地方。系统并不会提供当前活跃 popover 控制器的引用。

当 popover 因用户在其视图之外轻点而被消除时，popover 会自动通知其[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)这一动作。如果你提供了委托，就可以借助该对象阻止 popover 被消除，或在其被消除时执行额外的操作。[popoverControllerShouldDismissPopover:](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624661-popovercontrollershoulddismisspo) 委托方法让你可以控制是否真的要消除该 popover。如果你的委托没有实现这个方法，或者你的实现返回 `YES`，控制器就会消除该 popover，并向委托发送一条 [popoverControllerDidDismissPopover:](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624671-popovercontrollerdiddismisspopov) 消息。

在大多数情况下，你根本不需要重写 `popoverControllerShouldDismissPopover:` 方法。该方法是为消除 popover 可能给应用带来问题的场景而提供的。不过，与其在这个方法中返回 `NO`，不如干脆避免那些需要让 popover 一直存活的设计。例如，更好的做法可能是以模态方式呈现你的内容，强制用户输入所需的信息，或者接受、取消这些更改。

当你的委托的 `popoverControllerDidDismissPopover:` 方法被调用时，该 popover 本身已经从屏幕上移除。此时，如果你不打算再次使用它，就可以放心地释放该 popover 控制器。你也可以借助这条消息来刷新用户界面或更新应用的状态。

在为应用编写与 popover 相关的代码时，请考虑以下几点：

- 以编程方式消除 popover 需要一个指向该 popover 控制器的指针。获取这样一个指针的唯一方式，就是自己把它存储起来，通常存储在内容 [View Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) 中。这样可以确保内容 View Controller 能够在响应适当的用户操作时消除该 popover。
- popover 控制器可以被重用，因此应当缓存 popover 控制器，而不是每次都从头创建新的。popover 控制器非常灵活，因此你每次使用时都可以指定不同的 View Controller 和配置选项。
- 呈现 popover 时，应尽可能为允许的箭头方向指定 [UIPopoverArrowDirectionAny](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/uipopoverarrowdirectionany) 常量。指定这个常量能让 UIKit 在定位和调整 popover 大小时拥有最大的灵活性。如果你指定了一组有限的允许箭头方向，popover 控制器在显示之前可能不得不缩小你的 popover 尺寸。

[UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) 类是一个容器 View Controller，用于管理两个信息面板。第一个面板的宽度固定为 320 点，高度与可见窗口高度一致。第二个面板则填满剩余空间。在横屏方向下，split view controller 会把这两个面板并排呈现，中间用一条细分隔线隔开。在竖屏方向下，split view controller 只显示第二个、较大的面板，并提供一个工具栏按钮，用于以 popover 的形式显示第一个面板，如图 5-2 所示

__图 5-2__  split view 界面

!

split view 界面的各个面板中包含的内容由你所提供的 [View Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) 负责管理。由于这些面板包含的是应用特有的内容，两个 View Controller 之间的交互需要由你自己来管理。不过，旋转以及其他与系统相关的行为则由 split view controller 自身来管理。

split view controller 必须始终是你所创建的任何界面的根。换句话说，你必须始终把 [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) 对象的视图安装为应用窗口的根视图。此后，你的 split view 界面的各个面板中就可以包含 navigation controller、tab bar controller，或者实现你的界面所需的任何其他类型的 View Controller。

将 split view controller 整合到应用中最简单的方式，就是从一个新项目开始。Xcode 中的 Split View-based Application 模板为搭建包含 split view controller 的界面提供了一个良好的起点。实现该 split view 界面所需的一切都已经提供好了。你只需修改 View Controller 数组，以呈现你的自定义内容即可。修改这些 View Controller 的过程与 iPhone 应用中所用的过程几乎完全相同。唯一的区别在于，现在你有了更多的屏幕空间来显示详情相关的内容。不过，你也可以按照 [More view controller](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmznknltk) 中的说明，把 split view controller 整合到现有的界面中。

如果你不想以 Split View-based Application 模板项目为起点，仍然可以把一个 split [View Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) 添加到你的用户界面中。Interface Builder 的库中包含一个 split view controller 对象，你可以把它添加到现有的 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)中。添加 split view controller 时，你通常会把它添加到应用的主 nib 文件中。这是因为 split view 通常会被插入作为应用[窗口](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Window.html#//apple_ref/doc/uid/TP40009071-CH6)的顶层视图，因此需要在启动时被加载。

要将 split view controller 添加到应用的主 nib 文件中：

1. 打开应用的主 nib 文件。
2. 把一个 split view controller 对象拖到 nib 文件窗口中。

   该 split view controller 对象已包含两个面板通用的 View Controller。
3. 在应用的[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)中为该 split view controller 添加一个[出口（outlet）](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Outlet.html#//apple_ref/doc/uid/TP40009071-CH4)，并把该出口连接到这个 split view controller 对象。
4. 在应用委托的 [application:didFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 方法中，把该 split view controller 的视图安装为窗口的主视图：

```objc
[window addSubview:mySplitViewController.view];
```
5. 对于 split view controller 所包含的每个 View Controller：

   - 使用 Identity inspector 设置该 View Controller 的类名。
   - 在 Attributes inspector 中，设置包含该 View Controller 视图的 nib 文件名称。

你嵌入到 split view 中的这两个 View Controller 的内容由你自己负责。配置这些 View Controller 的方式，与配置应用中任何其他 View Controller 完全相同。在应用的主 nib 文件中，你只需要设置好类名和 nib 名称。其余的配置则取决于 View Controller 的类型。例如，对于 navigation controller 和 tab bar controller，你可能还需要指定额外的 View Controller 信息。

要以编程方式创建 split view controller，请创建一个 [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) 类的新实例，并为它的两个属性分别赋值 [View Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11)。由于其内容是根据你所提供的 View Controller 即时构建的，因此创建 split view controller 时不必指定 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)。因此，你只需使用 `init` 方法对其进行[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)即可。清单 5-2 展示了如何在启动时创建并配置一个 split view 界面的示例。你需要把第一个和第二个 View Controller 替换成呈现你应用内容的自定义 View Controller 对象。这里假定 `window` 变量是一个指向应用主 nib 文件中所加载[窗口](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Window.html#//apple_ref/doc/uid/TP40009071-CH6)的[出口](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Outlet.html#//apple_ref/doc/uid/TP40009071-CH4)。

__清单 5-2__  以编程方式创建 split view controller

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
   MyFirstViewController* firstVC = [[[MyFirstViewController alloc]
                     initWithNibName:@"FirstNib" bundle:nil] autorelease];
   MySecondViewController* secondVC = [[[MySecondViewController alloc]
                     initWithNibName:@"SecondNib" bundle:nil] autorelease];

   UISplitViewController* splitVC = [[UISplitViewController alloc] init];
   splitVC.viewControllers = [NSArray arrayWithObjects:firstVC, secondVC, nil];

   [window addSubview:splitVC.view];
   [window makeKeyAndVisible];

   return YES;
}
```


split [View Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) 依赖其所包含的两个 View Controller 来决定是否应当进行界面方向的更改。如果其中一个或两个 View Controller 都不支持新的方向，就不会发生任何更改。即使是在竖屏模式下——此时第一个 View Controller 并未显示——这一点同样成立。因此，你必须为这两个 View Controller 都重写 [shouldAutorotateToInterfaceOrientation:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621459-shouldautorotatetointerfaceorien) 方法，并对所有支持的方向返回 `YES`。

方向发生变化时，split view controller 会自动处理大部分旋转相关的行为。具体来说，当旋转到竖屏方向时，split view controller 会自动隐藏其 [viewControllers](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623181-viewcontrollers) 数组中的第一个 View Controller；旋转到横屏方向时，则会重新显示它。

如果你想在竖屏方向下也显示第一个 View Controller，可以借助一个[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)对象来实现。当旋转到竖屏方向时，split view controller 会为其委托提供一个按钮，轻点该按钮即可在 popover 中显示第一个面板。你的应用要做的，只是在委托的 [splitViewController:willHideViewController:withBarButtonItem:forPopoverController:](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623175-splitviewcontroller) 方法中把这个按钮添加到应用的工具栏上，并在 [splitViewController:willShowViewController:invalidatingBarButtonItem:](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623202-splitviewcontroller) 方法中移除该按钮。清单 5-3 展示了 Split-View based application 模板所提供的这些方法的实现。这些方法由详情 View Controller 实现，该 View Controller 管理着 split view controller 第二个面板的内容。

__清单 5-3__  响应 split view 方向变化，添加和移除工具栏按钮

```objc
// 旋转到竖屏方向时调用。
- (void)splitViewController: (UISplitViewController*)svc willHideViewController:(UIViewController *)aViewController withBarButtonItem:(UIBarButtonItem*)barButtonItem forPopoverController: (UIPopoverController*)pc 
{
    barButtonItem.title = @"Root List";
    NSMutableArray *items = [[toolbar items] mutableCopy];
    [items insertObject:barButtonItem atIndex:0];
    [toolbar setItems:items animated:YES];
    [items release];
    self.popoverController = pc;
}

// 当视图在 split view 中重新显示时调用，此时按钮和 popover 控制器都将失效。
- (void)splitViewController: (UISplitViewController*)svc willShowViewController:(UIViewController *)aViewController invalidatingBarButtonItem:(UIBarButtonItem *)barButtonItem {

    NSMutableArray *items = [[toolbar items] mutableCopy];
    [items removeObjectAtIndex:0];
    [toolbar setItems:items animated:YES];
    [items release];
    self.popoverController = nil;
}
```

[下一页](Modal%20View%20Controllers.md)[上一页](Tab%20Bar%20Controllers.md)

