---
title: iOS 视图编程指南
apple_id: TP40009503
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/CreatingWindows/CreatingWindows.html
archived_at: '2026-07-18T02:24:12.002277Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS 视图编程指南](About%20Windows%20and%20Views.md)


[下一页](Views.md)[上一页](View%20and%20Window%20Architecture.md)

# 窗口

每个 iOS 应用都至少需要一个窗口（window）——即 [UIWindow](https://developer.apple.com/documentation/uikit/uiwindow) 类的一个实例——有些应用可能还不止一个。窗口对象承担着以下几项职责：

- 它承载应用的可见内容。
- 它在把触摸事件分发给视图和其他应用对象的过程中起着关键作用。
- 它与应用的 View Controller 协作，配合完成方向变化。

在 iOS 中，窗口没有标题栏、关闭按钮，也没有任何其他视觉装饰。窗口始终只是一个装载一个或多个视图的空白容器。另外，应用也不会通过显示新窗口来改变自己的内容。当你想改变所显示的内容时，改变的是窗口中最前面的那些视图。

大多数 iOS 应用在整个生命周期中只创建并使用一个窗口。这个窗口覆盖设备的整块主屏幕，并在应用生命周期的早期从应用的主 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)中加载（或以编程方式创建）。不过，如果应用支持通过外接显示屏输出视频，它可以再创建一个窗口，把内容显示到那块外接显示屏上。其他所有窗口通常由系统创建，一般是为响应某些特定事件而创建的，比如来电。

对许多应用来说，唯一一次与窗口打交道的时机就是启动时创建窗口。不过，你也可以借助应用的窗口对象完成一些与应用相关的任务：

- __用窗口对象在窗口的本地坐标系与其他坐标系之间转换点和矩形。__ 例如，如果你拿到的是一个以窗口坐标表示的值，在使用之前可能需要先把它转换到某个特定视图的坐标系中。关于如何转换坐标，请参阅[在视图层级中转换坐标](Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnjnknltima)。
- __用窗口通知来跟踪与窗口相关的变化。__ 窗口在显示或隐藏时，以及在成为或放弃主窗口（key window）状态时，都会发出通知。你可以利用这些通知在应用的其他部分执行相应操作。更多信息请参阅[监视窗口变化](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnbnknltcmy)。

你既可以用代码创建和配置应用的主窗口，也可以用 Interface Builder。无论采用哪种方式，都应该在启动时创建窗口，并保留（retain）它，同时在应用委托对象中保存一个指向它的引用。如果你的应用还要创建其他窗口，应当等到真正需要时再惰性创建。例如，如果应用支持在外接显示屏上显示内容，就应该等到显示屏接入之后再创建对应的窗口。

无论应用是被启动到前台还是后台，你都应该在启动时创建应用的主窗口。创建和配置窗口本身并不是什么昂贵的操作。不过，如果应用是直接启动到后台的，就应该避免让窗口可见，直到应用进入前台为止。

用 Interface Builder 创建应用的主窗口非常简单，因为 Xcode 的工程模板已经替你做好了。每个新建的 Xcode 应用工程都包含一个主 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)（名字通常是 `MainWindow.xib` 或类似的变体），其中就包含应用的主窗口。此外，这些模板还在应用委托对象中为该窗口定义了一个 [outlet](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Outlet.html#//apple_ref/doc/uid/TP40009071-CH4)。你可以通过这个 outlet 在代码中访问窗口对象。

如果你是在改造一个已有工程来使用 Interface Builder，那么用 Interface Builder 创建窗口只需把一个窗口对象拖进 nib 文件即可。当然，你还应该完成以下工作：

- 为了在运行时访问该窗口，你应该[把窗口连接到一个 outlet](https://developer.apple.com/library/archive/recipes/XcodeRecipes/Connecting_an_Outlet/OutletConnection.html#//apple_ref/doc/uid/TP40009043-CH8)上，这个 outlet 通常定义在应用委托或该 nib 文件的 File's Owner 中。
- 如果你的改造计划中包括把新的 nib 文件设为应用的主 nib 文件，那么还必须把应用 `Info.plist` 文件中的 `NSMainNibFile` 键设为该 nib 文件的名字。修改这个键的值可以确保在应用委托的 [application:didFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 方法被调用之前，nib 文件已经加载完毕、可供使用。

关于创建和配置 nib 文件的更多信息，请参阅 _[Interface Builder 用户指南](../../Developer%20Tools/Interface%20Builder%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbu)_。关于如何在运行时把 nib 文件加载进应用，请参阅 _[资源编程指南](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_ 中的 [Nib 文件](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/CocoaNibs/CocoaNibs.html#//apple_ref/doc/uid/10000051i-CH4)。

如果你更愿意用代码创建应用的主窗口，那么可以在应用委托的 [application:didFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 方法中写入类似下面的代码：

```objc
self.window = [[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease];
```

在上面的例子中，假定 `self.window` 是应用委托中的一个[声明属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)，且配置为保留（retain）窗口对象。如果你创建的是用于外接显示屏的窗口，就应该把它赋给另一个变量，并且需要指定代表那块显示屏的非主 [UIScreen](https://developer.apple.com/documentation/uikit/uiscreen) 对象的 bounds。

创建窗口时，你应该始终把窗口的尺寸设为屏幕的完整 bounds。不要为了给状态栏或其他元素让位而缩小窗口的尺寸。反正状态栏总是浮在窗口之上，所以唯一需要为状态栏让位而缩小的，是你放进窗口里的那个视图。而且如果你使用了 View Controller，View Controller 会自动处理视图的尺寸问题。

每个窗口通常只有一个根视图对象（由对应的 View Controller 管理），其中包含了表示你的内容的所有其他视图。使用单一根视图可以简化界面切换的过程；要显示新内容，你只需替换根视图即可。要把一个视图装进窗口，请使用 [addSubview:](https://developer.apple.com/documentation/uikit/uiview/1622616-addsubview) 方法。例如，要装入一个由 View Controller 管理的视图，你可以使用类似下面的代码：

```objc
[window addSubview:viewController.view];
```

除了上面的代码，你也可以在 nib 文件中配置窗口的 [rootViewController](https://developer.apple.com/documentation/uikit/uiwindow/1621581-rootviewcontroller) 属性。这个属性提供了一种便捷的方式，让你用 nib 文件而不是代码来配置窗口的根视图。如果窗口从 nib 文件加载时该属性已被设置，UIKit 会自动把关联 View Controller 的视图装为窗口的根视图。这个属性仅用于装入根视图，窗口不会用它来与 View Controller 通信。

窗口的根视图可以是任意你想用的视图。取决于你的界面设计，根视图可以是一个通用的 [UIView](https://developer.apple.com/documentation/uikit/uiview) 对象，充当一个或多个子视图的容器；也可以是一个标准的系统视图；还可以是你自定义的视图。常被用作根视图的标准系统视图包括滚动视图、表视图和图像视图。

配置窗口的根视图时，你需要负责设置它在窗口中的初始大小和位置。对于不含状态栏、或显示半透明状态栏的应用，把视图尺寸设为与窗口一致即可。对于显示不透明状态栏的应用，则要把视图放到状态栏下方，并相应缩小其尺寸。从视图高度中减去状态栏高度，可以避免视图顶部被遮挡。

每个 `UIWindow` 对象都有一个可配置的 [windowLevel](https://developer.apple.com/documentation/uikit/uiwindow/1621593-windowlevel) 属性，用于决定该窗口相对于其他窗口的位置。多数情况下，你都不需要改变应用窗口的层级。新窗口在创建时会自动被指定为普通窗口层级。普通窗口层级表示该窗口呈现的是与应用相关的内容。更高的窗口层级则留给那些需要浮在应用内容之上的信息，比如系统状态栏或警告消息。虽然你也可以自己把窗口指定到这些层级，但当你使用特定接口时，系统通常会替你完成这件事。例如，当你显示或隐藏状态栏、或者显示一个警告视图时，系统会自动创建显示这些内容所需的窗口。

如果你想跟踪应用内窗口的出现与消失，可以使用下面这些与窗口相关的通知：

- [UIWindowDidBecomeVisibleNotification](https://developer.apple.com/documentation/uikit/uiwindow/1621621-didbecomevisiblenotification)
- [UIWindowDidBecomeHiddenNotification](https://developer.apple.com/documentation/uikit/uiwindow/1621617-didbecomehiddennotification)
- [UIWindowDidBecomeKeyNotification](https://developer.apple.com/documentation/uikit/uiwindowdidbecomekeynotification)
- [UIWindowDidResignKeyNotification](https://developer.apple.com/documentation/uikit/uiwindow/1621591-didresignkeynotification)

这些通知是为响应应用窗口的编程式变化而发出的。也就是说，当应用显示或隐藏某个窗口时，就会相应地发出 `UIWindowDidBecomeVisibleNotification` 和 `UIWindowDidBecomeHiddenNotification` 通知。当应用进入后台执行状态时，这些通知不会发出。尽管应用处于后台时窗口并没有显示在屏幕上，但在应用自身的语境中，它仍被视为可见的。

`UIWindowDidBecomeKeyNotification` 和 `UIWindowDidResignKeyNotification` 通知可以帮助应用跟踪哪个窗口是_主窗口（key window）_——也就是当前正在接收键盘事件和其他非触摸类事件的窗口。触摸事件会被分发给触摸发生所在的窗口，而那些没有关联坐标值的事件则会被分发给应用的主窗口。同一时刻只能有一个窗口是主窗口。

要在外接显示屏上显示内容，你必须为应用再创建一个窗口，并把它与代表该外接显示屏的屏幕对象关联起来。新窗口默认通常关联到主屏幕。修改窗口所关联的屏幕对象，会让该窗口的内容被重定向到对应的显示屏上。一旦窗口与正确的屏幕关联好，你就可以像对待应用主屏幕那样，往里面添加视图并把它显示出来。

[UIScreen](https://developer.apple.com/documentation/uikit/uiscreen) 类维护着一份代表可用硬件显示屏的屏幕对象列表。通常，任何 iOS 设备都只有一个代表主显示屏的屏幕对象，但支持连接外接显示屏的设备可以多出一个屏幕对象。支持外接显示屏的设备包括配备 Retina 显示屏的 iPhone 和 iPod touch，以及 iPad。较旧的设备（如 iPhone 3GS）不支持外接显示屏。

后面几节会详细介绍在外接显示屏上显示内容的流程。不过，下面这几个步骤概括了基本过程：

1. 在应用启动时，注册屏幕连接和断开通知。
2. 当需要在外接显示屏上显示内容时，创建并配置一个窗口。

   - 使用 `UIScreen` 的 [screens](https://developer.apple.com/documentation/uikit/uiscreen/1617812-screens) 属性获取外接显示屏对应的屏幕对象。
   - 创建一个 [UIWindow](https://developer.apple.com/documentation/uikit/uiwindow) 对象，并把它的尺寸设为适合该屏幕（或适合你的内容）的大小。
   - 把外接显示屏的 `UIScreen` 对象赋给窗口的 [screen](https://developer.apple.com/documentation/uikit/uiwindow/1621597-screen) 属性。
   - 按内容需要调整屏幕对象的分辨率。
   - 往窗口中添加所需的视图。
3. 显示该窗口，并像平常一样更新它。

屏幕连接和断开通知对于优雅地处理外接显示屏的变化至关重要。当用户接入或拔掉一块显示屏时，系统会向你的应用发送相应的通知。你应该利用这些通知来更新应用状态，并创建或释放与外接显示屏关联的窗口。

关于连接和断开通知，有一点很重要：它们随时可能到来，甚至在你的应用于后台挂起时也会到来。因此，最好由一个在应用整个运行期间都存在的对象来观察这些通知，比如你的应用委托。如果应用处于挂起状态，这些通知会被排队，直到应用退出挂起状态并开始在前台或后台运行时才会送达。

清单 2-1 展示了注册连接和断开通知所用的代码。这个方法由应用委托在初始化时调用，不过你也可以在应用的其他地方注册这些通知。处理方法的实现见[清单 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnbnknltcni)。

__清单 2-1__  注册屏幕连接和断开通知

```objc
- (void)setupScreenConnectionNotificationHandlers
{
    NSNotificationCenter* center = [NSNotificationCenter defaultCenter];

    [center addObserver:self selector:@selector(handleScreenConnectNotification:)
            name:UIScreenDidConnectNotification object:nil];
    [center addObserver:self selector:@selector(handleScreenDisconnectNotification:)
            name:UIScreenDidDisconnectNotification object:nil];
}
```

如果设备接入外接显示屏时你的应用正处于活跃状态，它就应该为那块显示屏创建第二个窗口，并往里面填一些内容。这些内容不必是你最终想要呈现的内容。例如，如果应用还没准备好使用这块额外的屏幕，可以用第二个窗口显示一些占位内容。如果你没有为该屏幕创建窗口，或者创建了窗口却没有把它显示出来，外接显示屏上就会显示一片黑色。

清单 2-2 展示了如何创建一个次要窗口并往里面填充内容。在这个例子中，应用是在接收屏幕连接通知的处理方法中创建窗口的。（关于注册连接和断开通知的信息，请参阅[清单 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnbnknltcna)。）连接通知的处理方法创建了一个次要窗口，把它与新接入的屏幕关联起来，并调用应用主 View Controller 的一个方法，往窗口中添加内容并显示出来。断开通知的处理方法则释放该窗口，并通知主 View Controller，以便它相应地调整自己的呈现内容。

__清单 2-2__  处理连接和断开通知

```objc
- (void)handleScreenConnectNotification:(NSNotification*)aNotification
{
    UIScreen*    newScreen = [aNotification object];
    CGRect        screenBounds = newScreen.bounds;

    if (!_secondWindow)
    {
        _secondWindow = [[UIWindow alloc] initWithFrame:screenBounds];
        _secondWindow.screen = newScreen;

        // 设置该窗口的初始 UI。
        [viewController displaySelectionInSecondaryWindow:_secondWindow];
    }
}

- (void)handleScreenDisconnectNotification:(NSNotification*)aNotification
{
    if (_secondWindow)
    {
        // 先隐藏窗口，然后删除它。
        _secondWindow.hidden = YES;
        [_secondWindow release];
        _secondWindow = nil;

        // 根据这里显示的内容更新主屏幕。
        [viewController displaySelectionOnMainScreen];
    }

}
```


要在外接屏幕上显示窗口，你必须把它与正确的屏幕对象关联起来。这个过程包括找到合适的 [UIScreen](https://developer.apple.com/documentation/uikit/uiscreen) 对象，并把它赋给窗口的 [screen](https://developer.apple.com/documentation/uikit/uiwindow/1621597-screen) 属性。你可以通过 `UIScreen` 的 [screens](https://developer.apple.com/documentation/uikit/uiscreen/1617812-screens) 类方法获取屏幕对象列表。该方法返回的数组中总是至少包含一个代表主屏幕的对象。如果还存在第二个对象，那它代表的就是已连接的外接显示屏。

清单 2-3 展示了一个在应用启动时调用的方法，用于检查是否已经接入了外接显示屏。如果已接入，该方法就创建一个窗口，把它与外接显示屏关联起来，并在显示窗口前添加一些占位内容。在这个例子中，占位内容是一个白色背景，加上一个提示“无内容可显示”的标签。为了显示窗口，这个方法改变的是窗口的 [hidden](https://developer.apple.com/documentation/uikit/uiview/1622585-hidden) 属性的值，而不是调用 `makeKeyAndVisible`。之所以这样做，是因为这个窗口只包含静态内容，并不用于处理事件。

__清单 2-3__  为外接显示屏配置窗口

```objc
- (void)checkForExistingScreenAndInitializeIfPresent
{
    if ([[UIScreen screens] count] > 1)
    {
        // 把窗口与第二块屏幕关联起来。
        // 主屏幕始终位于索引 0。
        UIScreen*    secondScreen = [[UIScreen screens] objectAtIndex:1];
        CGRect        screenBounds = secondScreen.bounds;

        _secondWindow = [[UIWindow alloc] initWithFrame:screenBounds];
        _secondWindow.screen = secondScreen;

        // 为窗口添加一个白色背景
        UIView*            whiteField = [[UIView alloc] initWithFrame:screenBounds];
        whiteField.backgroundColor = [UIColor whiteColor];

        [_secondWindow addSubview:whiteField];
        [whiteField release];

        // 让标签在视图中居中。
        NSString*    noContentString = [NSString stringWithFormat:@"<no content>"];
        CGSize        stringSize = [noContentString sizeWithFont:[UIFont systemFontOfSize:18]];

        CGRect        labelSize = CGRectMake((screenBounds.size.width - stringSize.width) / 2.0,
                                    (screenBounds.size.height - stringSize.height) / 2.0,
                                    stringSize.width, stringSize.height);

        UILabel*    noContentLabel = [[UILabel alloc] initWithFrame:labelSize];
        noContentLabel.text = noContentString;
        noContentLabel.font = [UIFont systemFontOfSize:18];
        [whiteField addSubview:noContentLabel];

        // 把窗口显示出来。
        _secondWindow.hidden = NO;
    }
}
```

外接屏幕上的窗口一旦显示出来，你的应用就可以像更新其他任何窗口一样更新它了。你可以按需添加和移除子视图、修改子视图的内容、为视图的变化添加动画，以及在需要时让它们的内容失效。

取决于你的内容，你可能想在把窗口与屏幕关联之前先改变屏幕模式。许多屏幕支持多种分辨率，其中一些使用不同的像素宽高比。屏幕对象默认使用最常见的屏幕模式，但你可以把它改成更适合你的内容的模式。例如，如果你正在用 OpenGL ES 实现一款游戏，而纹理是按 640 x 480 像素的屏幕设计的，那么对于默认分辨率更高的屏幕，你可能就需要改变其屏幕模式。

如果你打算使用非默认的屏幕模式，应该在把屏幕与窗口关联之前，就把该模式应用到 `UIScreen` 对象上。[UIScreenMode](https://developer.apple.com/documentation/uikit/uiscreenmode) 类定义了单个屏幕模式的各项特性。你可以通过屏幕的 [availableModes](https://developer.apple.com/documentation/uikit/uiscreen/1617839-availablemodes) 属性获取它所支持的模式列表，并遍历这个列表，找到符合你需求的那一个。

关于屏幕模式的更多信息，请参阅 _[UIScreenMode 类参考](https://developer.apple.com/documentation/uikit/uiscreenmode)_。

[下一页](Views.md)[上一页](View%20and%20Window%20Architecture.md)

