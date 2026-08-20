---
title: iOS 多显示屏编程指南
apple_id: TP40012555
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/WindowAndScreenGuide/UsingExternalDisplay/UsingExternalDisplay.html
archived_at: '2026-07-18T02:24:16.576683Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS 多显示屏编程指南](Using%20Windows%20to%20Present%20Content%20on%20Multiple%20Displays.md)


[下一页](Document%20Revision%20History.md)[上一页](Understanding%20Windows%20and%20Screens.md)

# 在外接显示屏上呈现内容

如果你用 AirPlay 让用户把内容重定向到外接设备显示屏，你既可以把当前的应用内容镜像到第二块显示屏上，也可以在其上显示不同的内容。

在每块显示屏上呈现不同的内容，可以提升用户体验。例如，你可以在宿主设备的显示屏上呈现应用 UI，同时在外接显示屏上播放高清媒体内容。

要在外接设备显示屏上显示独立的内容，你需要遵循以下基本流程：

1. 在应用启动时，检查是否存在外接显示屏，并注册屏幕连接和断开通知。
2. 当外接显示屏可用时——无论是在应用启动时还是在应用运行期间——为它创建并配置一个窗口。
3. 把该窗口与相应的屏幕对象关联起来，显示这第二个窗口，并像平常那样更新它。

在显示了独立内容之后，若要重新启用镜像，只需把你创建的窗口从相应的屏幕对象上移除即可。

你可以在应用启动时通过检查窗口的 `UIScreen` 对象的 `screens` 数组，判断是否存在第二块显示屏。通常 `screens` 数组只包含一个屏幕对象，因为这个对象代表宿主 iOS 设备的显示屏。如果用户连接了外接设备，该数组就会多出一个代表外接显示屏的屏幕对象。支持连接外接显示屏的 iOS 设备包括配备 Retina 显示屏的 iPhone 和 iPod touch 设备以及 iPad。较老的设备——例如 iPhone 3GS——不支持外接显示屏。

清单 2-1 展示了一个在应用启动时检查是否存在外接显示屏的方法。如果第二块显示屏可用，它就为其创建一个窗口。

__清单 2-1__  检查是否存在外接显示屏

```objc
- (void)checkForExistingScreenAndInitializeIfPresent
{
    if ([[UIScreen screens] count] > 1)
    {
        // 获取代表外接显示屏的屏幕对象。
        UIScreen *secondScreen = [[UIScreen screens] objectAtIndex:1];
        // 获取该屏幕的 bounds，以便创建尺寸正确的窗口。
        CGRect screenBounds = secondScreen.bounds;

        self.secondWindow = [[UIWindow alloc] initWithFrame:screenBounds];
        self.secondWindow.screen = secondScreen;

        // 设置要显示的初始内容……
        // 显示该窗口。
        self.secondWindow.hidden = NO;
    }
}
```


当用户连接或断开显示屏时，系统会向你的应用发送相应的通知。这类通知对于优雅地处理外接显示屏的变化至关重要。你应该利用这些通知更新应用状态，并创建或销毁与外接显示屏关联的窗口。

关于连接和断开通知，最需要记住的一点是：它们可能在任何时刻到来，甚至在你的应用于后台被挂起时也会到来。由于你无法预测这些通知何时到达，最好从一个在应用整个运行期间都会存在的对象（例如你的 app delegate）中观察它们。如果你的应用被挂起，这些通知会被排入队列，直到应用退出挂起状态并开始在前台或后台运行。

清单 2-2 展示了注册这些通知的一种方式。（处理这些通知的代码见[处理连接与断开通知](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdknjvfvbuqmznknlte)。）

__清单 2-2__  注册屏幕连接和断开通知

```objc
- (void)setUpScreenConnectionNotificationHandlers
{
    NSNotificationCenter *center = [NSNotificationCenter defaultCenter];

    [center addObserver:self selector:@selector(handleScreenDidConnectNotification:)
            name:UIScreenDidConnectNotification object:nil];
    [center addObserver:self selector:@selector(handleScreenDidDisconnectNotification:)
            name:UIScreenDidDisconnectNotification object:nil];
}
```


你在自定义通知处理方法中收到的通知对象，就是代表外接显示屏的屏幕对象。和应用启动时一样，你需要确定新屏幕的 bounds，以便创建并初始化尺寸正确的窗口。然后把窗口的 `screen` 属性设为这个新的屏幕对象，并把窗口的 `hidden` 属性设为 `NO`，如清单 2-3 所示。

__清单 2-3__  处理屏幕连接和断开通知

```objc
- (void)handleScreenDidConnectNotification:(NSNotification*)aNotification
{
    UIScreen *newScreen = [aNotification object];
    CGRect screenBounds = newScreen.bounds;

    if (!self.secondWindow)
    {
        self.secondWindow = [[UIWindow alloc] initWithFrame:screenBounds];
        self.secondWindow.screen = newScreen;

        // 为该窗口设置初始 UI。
    }
}

- (void)handleScreenDidDisconnectNotification:(NSNotification*)aNotification
{
    if (self.secondWindow)
    {
        // 先隐藏，然后删除该窗口。
        self.secondWindow.hidden = YES;
        self.secondWindow = nil;

    }

}
```


许多显示屏支持多种分辨率，其中有些使用不同的像素长宽比。`UIScreen` 对象默认使用显示屏的首选屏幕模式，而且应尽可能使用这个模式。你可以通过 `UIScreen` 对象的 [preferredMode](https://developer.apple.com/documentation/uikit/uiscreen/1617823-preferredmode) 属性获取显示屏的首选模式。

注意，无论采用哪种屏幕模式，你的应用都需要应对用一台设备的资源生成第二块屏幕内容所带来的性能影响。例如，你可能需要通过测试找出一个最佳帧率，使内容能够在两块屏幕上渲染而不掉帧、不卡顿。

在某些情况下，你可能想在把窗口与显示屏关联之前，先把显示屏的屏幕模式改成更适合你内容的模式。例如，如果你正在用 OpenGL ES 实现一款游戏，而你的纹理是为 640 x 480 像素的屏幕设计的，你就可能想改变那些默认分辨率更高的显示屏的屏幕模式。在改变屏幕模式之前，请确认你的内容被放大之后用户体验仍然可以接受。

如果你打算使用非默认的屏幕模式，应该在把屏幕与窗口关联之前，先把该模式应用到 `UIScreen` 对象上。[UIScreenMode](https://developer.apple.com/documentation/uikit/uiscreenmode) 类定义了单个屏幕模式的属性。你可以从屏幕对象的 [availableModes](https://developer.apple.com/documentation/uikit/uiscreen/1617839-availablemodes) 属性获取它所支持的模式列表，并遍历该列表找出符合你需求的那一个。

有关屏幕模式的更多信息，请参阅 _[UIScreenMode Class Reference](https://developer.apple.com/documentation/uikit/uiscreenmode)_。

除了屏幕模式之外，`UIScreen` 对象还包含 [overscanCompensation](https://developer.apple.com/documentation/uikit/uiscreen/1617818-overscancompensation) 属性，必要时你可以用它来调整外接显示屏的过扫描补偿（overscan compensation）。过扫描（overscanning）这种做法源自阴极射线管显示器。由于技术上的限制，老式 CRT 会把输入画面扫描到显像管边缘之外，从而显示出一幅被裁切的图像。虽然这些限制如今已经解决，许多广播机构和显示器制造商却仍然按存在过扫描来预期。使用 `overscanCompensation` 属性的默认值——也就是 `UIScreenOverscanCompensationScale`——时，iOS 在检测到外接显示屏存在过扫描时会对你的内容做相应的缩放。

在少数情况下，你可能想为 `overscanCompensation` 属性使用其他值，但这样做总会带来更多需要你自己完成的工作。例如，如果你使用 `UIScreenOverscanCompensationInsetBounds`，就必须做好应对非标准显示屏尺寸的 bounds 的准备。

[下一页](Document%20Revision%20History.md)[上一页](Understanding%20Windows%20and%20Screens.md)

