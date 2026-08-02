---
title: iOS View Controller 一览
apple_id: TP40011313
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-11-15'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerCatalog/Chapters/SplitViewControllers.html
archived_at: '2026-07-18T02:23:24.432380Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 一览](About%20View%20Controllers.md)


[下一页](Popovers.md)[上一页](Page%20View%20Controllers.md)

# Split View Controller

[UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) 类是一个容器 View Controller，负责管理两个信息面板。第一个面板宽度固定为 320 点，高度与可见窗口的高度一致。第二个面板填满剩余的空间。图 4-1 展示了一个 split view controller 界面。

__图 4-1__  split view 界面

!!

split view 界面各面板中的内容，由你提供的 [View Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) 负责管理。由于这些面板装的是应用特有的内容，两个 View Controller 之间的交互要由你自己来管理。不过，旋转以及其他与系统相关的行为则由 split view controller 自己处理。

split view controller 必须始终是你所创建的任何界面的根。换句话说，你必须始终把 [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) 对象的视图安装为应用窗口的根视图。随后，split view 界面的各个面板中可以包含 navigation controller、tab bar controller，或者实现你的界面所需的任何其他类型的 View Controller。split view controller 不能以模态方式呈现。

把 split view controller 集成到应用中最简单的办法，是从一个新工程开始。Xcode 中的 Split View-based Application 模板为构建包含 split view controller 的界面提供了很好的起点。实现 split view 界面所需的一切都已经准备好了。你要做的只是修改 View Controller 数组，让它呈现你的内容。修改这些 View Controller 的过程，与 iPhone 应用中所用的过程几乎完全相同。唯一的区别是，现在你有更多屏幕空间可用来显示详情相关的内容。当然，你也可以把 split view controller 集成到已有的界面中。

如果你正在创建新的 Xcode 工程，Master-Detail Application 模板会在 storyboard 中给你一个 split view，并把它设为第一个场景。

要把 split view controller 添加到已有的 app 中：

1. 打开应用的主 storyboard。
2. 从库中拖出一个 split view controller。

   Interface Builder 会创建一个 split view controller、一个 navigation controller 和一个 View Controller，并在它们之间建立关系。这些关系把新创建的 View Controller 标识为 split view controller 的左侧面板和右侧面板。
3. 在 Attributes 检查器中勾选 Is Initial View Controller 选项，把它作为第一个 View Controller 显示（或者用其他方式在你的用户界面中呈现该 View Controller）。

你嵌入 split view 中的这两个 View Controller 的内容由你自己负责。配置这两个 View Controller 的方式，与配置应用中其他任何 View Controller 完全一样。例如，对于嵌入其中的 navigation controller 和 tab bar controller，你可能需要指定额外的 View Controller 信息。

要以编程方式创建 split view controller，先创建 [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) 类的一个新实例，然后把 [View Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) 赋给它的两个属性。由于它的内容是根据你提供的 View Controller 动态构建的，创建 split view controller 时你不必指定 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)。因此，你直接用 `init` 方法[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)它就行。清单 4-1 展示了如何在启动时创建并配置一个 split view 界面。你需要把第一个和第二个 View Controller 换成呈现你应用内容的那些 View Controller 对象。这里假定 `window` 变量是一个 [outlet](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Outlet.html#//apple_ref/doc/uid/TP40009071-CH4)，指向从应用主 nib 文件中加载的[窗口](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Window.html#//apple_ref/doc/uid/TP40009071-CH6)。

__清单 4-1__  以编程方式创建 split view controller

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
   MyFirstViewController* firstVC = [[MyFirstViewController alloc] init];
   MySecondViewController* secondVC = [[MySecondViewController alloc] init];

   UISplitViewController* splitVC = [[UISplitViewController alloc] init];
   splitVC.viewControllers = [NSArray arrayWithObjects:firstVC, secondVC, nil];

    window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    window.rootViewController = splitVC;
   [window makeKeyAndVisible];

   return YES;
}
```


split view controller 依靠它所包含的两个 View Controller 来决定支持哪些方向。只有当两个被包含的 View Controller 都支持某个方向时，它才支持该方向。即便其中一个被包含的 View Controller 当前并未显示，它也必须支持该方向。当方向发生变化时，split view controller 会自动处理大部分旋转行为。

在横屏方向下，split view controller 会把两个面板并排显示，中间用一条细分隔线隔开。在竖屏方向下，split view controller 要么同时显示两个面板，要么只显示第二个（也就是较大的那个）面板，并提供一个工具栏按钮，用来以 popover 的形式显示第一个面板；具体是哪种行为，取决于 [splitViewController:shouldHideViewController:inOrientation:](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623174-splitviewcontroller) [委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)方法返回的值。

[下一页](Popovers.md)[上一页](Page%20View%20Controllers.md)

