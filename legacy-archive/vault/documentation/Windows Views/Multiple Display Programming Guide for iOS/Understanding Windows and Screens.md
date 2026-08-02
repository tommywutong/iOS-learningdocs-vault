---
title: iOS 多显示屏编程指南
apple_id: TP40012555
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/WindowAndScreenGuide/WindowScreenRolesinApp/WindowScreenRolesinApp.html
archived_at: '2026-07-18T02:24:16.735859Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS 多显示屏编程指南](Using%20Windows%20to%20Present%20Content%20on%20Multiple%20Displays.md)


[下一页](Presenting%20Content%20on%20an%20External%20Display.md)[上一页](Using%20Windows%20to%20Present%20Content%20on%20Multiple%20Displays.md)

# 理解窗口与屏幕

窗口（window）负责应用用户界面的整体呈现。窗口与视图（以及拥有这些视图的 view controller）协作，管理与可见视图层级的交互以及对该层级的变更。

每个应用都有一个窗口，用于在 iOS 设备的显示屏上显示应用的用户界面。如果设备连接了外接显示屏（external display），应用可以创建第二个窗口，把内容也呈现到那块显示屏上。

在 iOS 应用中，窗口扮演的角色与 Mac 应用中的窗口截然不同。在 iOS 中，窗口没有标题栏、关闭按钮，也没有任何其他视觉装饰。用户看不到、关不掉、也移动不了 iOS 应用的窗口。而且，iOS 应用不会像 Mac 应用惯常做的那样，通过打开另一个窗口来显示新内容，而是改变自己窗口内部的视图。

窗口对象——也就是 [UIWindow](https://developer.apple.com/documentation/uikit/uiwindow) 的实例——承担着几项重要职责：

- 它容纳应用的可见内容。
- 它在向你的视图以及其他应用对象派发触摸事件的过程中扮演关键角色。
- 它与应用的 view controller 协作，处理方向变化。

大多数情况下，你无需做任何事情，应用的窗口就能履行这些职责。如果你使用 storyboard 创建应用的用户界面，那么唯一需要显式创建窗口对象的理由，就是为了支持外接设备显示屏。

一个窗口有唯一的根 view controller 对象，其中包含表示你的内容的所有其他视图。使用单一的根 view controller 简化了修改界面的过程，因为要显示新内容，你只需把旧的根 view controller 替换成新的即可。把根视图装入窗口最简单的办法，就是使用 storyboard 定义应用的用户界面（要了解 storyboard 如何帮你定义 UI，请参阅 [Xcode 与 storyboard 可以创建、配置并加载你的窗口](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdknjvfvbuqnbnknltc)）。

你可以用任何你想用的 view controller 作为窗口的根 view controller。视你的界面设计而定，根 view controller 可以是一个充当一个或多个视图容器的通用 `UIViewController` 对象，可以是标准的 UIKit view controller，也可以是你自己定义的自定义 view controller。常被用作根 view controller 的标准 UIKit 对象包括 navigation、tab bar 和 split view controller。

当你设置根 view controller 时，窗口会把该 view controller 的视图添加到窗口中，并为其设定合适的尺寸。窗口依据若干因素来确定视图的正确尺寸——例如状态栏是否可见、当前的设备方向，以及该视图是否应该全屏显示。

当一个窗口正在接收键盘事件以及与触摸无关的事件时，它被视为主窗口（key window）。触摸事件会被派发到触摸发生的那个窗口，而没有关联坐标值的事件则会被派发到主窗口。同一时刻只能有一个窗口是主窗口。

大多数时候，应用窗口就是主窗口。由于 iOS 使用单独的窗口来显示警告视图和输入辅助视图，这些窗口也可以成为主窗口。例如，当警告视图或输入辅助视图中有一个文本字段、且用户正在其中输入时，包含该输入视图的窗口就是主窗口。

当你为应用创建窗口时，`UIWindow` 类会自动把它指定到所谓的_普通窗口层级_（normal window level），这是呈现应用相关内容的窗口应该使用的层级。这个层级由 [windowLevel](https://developer.apple.com/documentation/uikit/uiwindow/1621593-windowlevel) 属性设置，描述了窗口在 z 轴上相对于其他窗口的位置。虽然你可以把应用相关的窗口重新配置成显示在其他层级上，但你不应该有这种需要。

除了用于呈现应用相关内容的窗口之外，还有一些更高层级的窗口，用于显示需要浮动在应用内容之上的信息，例如系统状态栏和警告框。

`UIWindow` 类的 [screen](https://developer.apple.com/documentation/uikit/uiwindow/1621597-screen) 属性代表窗口当前显示所在的那块具体设备显示屏。该属性包含一个屏幕（screen）对象——也就是 [UIScreen](https://developer.apple.com/documentation/uikit/uiscreen) 的实例——其中包含关于设备显示屏的信息，例如它的 bounds、模式和亮度。

屏幕对象还包含若干通知，你可以监听它们以获知设备显示屏的变化。例如，你可以注册在设备显示屏连接或断开时、以及显示屏的模式或亮度值发生变化时发送的通知。

iOS 定义了若干通知，用于表示窗口对象和屏幕对象的变化。总的来说，这些通知对支持外接显示屏的应用最为有用。

除了表示键盘何时可见的通知（例如 `UIKeyboardDidShowNotification`）之外，`UIWindow` 还定义了以下通知：

- `UIWindowDidBecomeVisibleNotification`
- `UIWindowDidBecomeHiddenNotification`
- `UIWindowDidBecomeKeyNotification`
- `UIWindowDidResignKeyNotification`

`UIWindow` 的这些通知是为响应应用窗口的程序化变更而派发的。例如，当你的应用显示或隐藏某个窗口时，就会相应地派发 `UIWindowDidBecomeVisibleNotification` 和 `UIWindowDidBecomeHiddenNotification` 通知。注意，当你的应用转入后台时并不会派发这些通知：尽管应用处于后台时窗口并未显示在屏幕上，但在应用自身的语境中，它仍被视为可见。

大多数应用无需关注 `UIWindowDidBecomeVisibleNotification` 和 `UIWindowDidBecomeHiddenNotification` 通知，因为一个应用拥有多个窗口的情况很少见。

`UIWindowDidBecomeKeyNotification` 和 `UIWindowDidResignKeyNotification` 通知可以帮你跟踪应用窗口何时成为主窗口。如果你要显示输入辅助视图来获取用户输入，可能就需要知道窗口何时成为主窗口。

总的来说，除非你需要支持外接设备显示屏，否则你几乎永远不必访问应用的窗口对象或屏幕对象。在应用启动之后——窗口已被创建、加载并配置完毕——你可能想对窗口做的事情只有寥寥几件：

- __用窗口对象在窗口的本地坐标系与其他坐标系之间转换点和矩形。__ 例如，如果你有一个以窗口坐标表示的值，在使用它之前，你可能想先把它转换到某个特定视图的坐标系。有关如何转换坐标的信息，请参阅 [Converting Coordinates in the View Hierarchy](../View%20Programming%20Guide%20for%20iOS/Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnjnknltima)。
- __用窗口通知跟踪与窗口相关的变化。__ 窗口在被显示或隐藏、以及接受或放弃主窗口状态时会产生通知。你可以利用这些通知在应用的其他部分执行相应操作。更多信息请参阅[窗口通知帮助你监控变化](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdknjvfvbuqnbnknlte)。

类似地，你想要访问屏幕对象的理由也只有少数几个。其中一个理由是调整宿主设备显示屏的亮度。例如，你可以用 `brightness` 属性让用户能够设置自己 iOS 设备显示屏的亮度。你还可以用 `wantsSoftwareDimming` 属性表明你的应用需要比设备最低亮度更暗的亮度级别。（注意，开启 `wantsSoftwareDimming` 可能带来性能影响，因为变暗是通过软件实现的。）

最后，你可能想用 `UIScreen` 的 [displayLinkWithTarget:selector:](https://developer.apple.com/documentation/uikit/uiscreen/1617820-displaylink) 方法创建一个 Core Animation 显示链接对象，把你的绘制与显示屏的刷新率同步。要进一步了解如何用显示链接对象搭建动画循环，请参阅 [Rendering Using an Animation Loop](../../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/Drawing%20to%20Other%20Rendering%20Destinations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojtfvbuqmjqgmwvgvzsga)。注意，你可以使用 GLKit API 自动设置显示链接。要进一步了解 GLKit 框架，请参阅 _[GLKit Framework Reference](https://developer.apple.com/documentation/glkit)_。

当你基于某个 Xcode 模板创建新的 iOS 应用工程，并使用 storyboard 设计用户界面时，你无需显式地创建、配置或加载应用的窗口。

当你为应用创建了主 storyboard 文件，并在[信息属性列表文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/InfoPlist.html#//apple_ref/doc/uid/TP40008195-CH61)中把它标识为主 storyboard 时，iOS 会为你完成若干设置工作。具体来说，在启动时 iOS 会：

- 实例化一个窗口。
- 加载主 storyboard 并实例化其初始 view controller。
- 把这个新的 view controller 赋给窗口的 `rootViewController` 属性，然后让窗口可见。

在初始 view controller 显示之前，你的 app delegate 会被调用，让你有机会配置这个 view controller。

你应该尽可能使用 storyboard 来指定应用的用户界面（iOS 5.0 之前的版本不支持 storyboard）。如果你选择用 nib 文件而不是 storyboard 来创建应用的 UI，你多半仍然不需要创建窗口对象，因为大多数 Xcode 模板已经为你创建好了一个。（如果你确实要把一个窗口对象拖入 Interface Builder 文件，务必设置它的 Full Screen at Launch 属性，以确保窗口的尺寸适配目标设备。）

如果你用 nib 文件而不是 storyboard 来创建应用的 UI，就需要确保主 nib 文件的内容在启动时被装入窗口。要把主 nib 文件的内容装入窗口，你可以在 [application:willFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623032-application) 方法中添加类似下面这样的代码：

```objc
window.rootViewController = myViewController;
```

在少数情况下，你可能想以编程方式创建应用的窗口。你可以用类似下面这样的代码，以编程方式创建窗口、装入根 view controller，并让窗口可见：

```objc
- (BOOL)application:(UIApplication *)application willFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
   UIWindow *window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
   myViewController = [[MyViewController alloc] init];
   window.rootViewController = myViewController;
   [window makeKeyAndVisible];
   return YES;
}
```

[下一页](Presenting%20Content%20on%20an%20External%20Display.md)[上一页](Using%20Windows%20to%20Present%20Content%20on%20Multiple%20Displays.md)

