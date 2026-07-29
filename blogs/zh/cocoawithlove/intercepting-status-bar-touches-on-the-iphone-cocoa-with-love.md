---
title: '拦截 iPhone 状态栏触摸 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/05/intercepting-status-bar-touches-on.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:028de792d2351f43'
translated: true
---

> 原文：[Intercepting status bar touches on the iPhone | Cocoa with Love](https://www.cocoawithlove.com/2009/05/intercepting-status-bar-touches-on.html)　·　Cocoa with Love (Matt Gallagher)

你可以配置你的 iPhone App，使得触摸状态栏时，能让 `UIScrollView` 滚动到顶部。我会向你展示如何拦截这一触摸事件，以便将状态栏触摸用于其他用途。示例 App 会显示一个隐藏的抽屉（drawer），当你点击状态栏时，它会从状态栏下方滑出。

## 状态栏中的触摸

iPhone 上一个不太为人知的用户界面特性是，触摸状态栏通常会使得主 `UIScrollView` 滚动到顶部，为快速回到长文稿的顶部提供了一种便捷方式。

当且仅当一个 `UIScrollView` 的 `scrollsToTop` 属性返回 `YES`（默认值为 `YES`）时，此功能会在你的 App 中生效。如果有多个 `UIScrollView` 对该属性返回 `YES`（或者 `UIScrollView` 的 `delegate` 在 `scrollViewWillScrollToTop:` 中返回 `NO`），那么滚动到顶部的功能就会被禁用。

以上就是常规功能，但我们如何实现不同的功能呢？

## HiddenDrawer 示例 App

![](https://www.cocoawithlove.com/assets/objc-era/hidden_drawer_screenshots.png)

这些截图展示了 HiddenDrawer 示例 App。当在左侧点击状态栏时，隐藏的抽屉会从状态栏下方动画弹出，呈现出右侧所示的状态。

## 窃取状态栏触摸事件

示例 App 中最棘手的部分是如何检测状态栏中的触摸。

通过在 `UITableView` 上实现自定义的 `setContentOffset:animated:` 方法并在其中设置断点，你可以在调试器的调用栈中看到 `UIApplication` 的 `sendEvent:` 方法会因状态栏触摸而被调用，所以我们就从这里开始。

### CustomApplication

重写 `UIApplication` 的情况极为罕见，因此我会解释如何使其生效。一旦创建了 `UIApplication` 的子类，你需要告诉程序使用这个子类。在 Cocoa Senior（Mac OS X）中，你需要在 Info.plist 文件中指定 App 的子类。在 Cocoa Touch 中，你需要在 `main.m` 文件中的 `UIApplicationMain` 函数里按名称指定自定义的 App 子类：

```objc
int retVal = UIApplicationMain(argc, argv, @"CustomApplication", nil);
```

### sendEvent:

我们在 `CustomApplication` 中唯一需要重写的方法是 `sendEvent:`。难点在于从 `UIEvent` 中判断哪些事件是状态栏触摸事件——不幸的是，对于状态栏触摸，`allTouches` 方法返回的是空数组。

因此，我们转而深入访问私有的 `GSEvent`。

我之前在[在 iPhone 上合成触摸事件](https://www.cocoawithlove.com/2008/10/synthesizing-touch-event-on-iphone.html)一文中访问过 `GSEvent`。在那篇文章中，我创建了一个 `PublicEvent` 类和一个伪造的 `GSEventProxy` 类来访问所需字段。这次，我将采用不同的方法，直接跳转到我需要的数据。

```objc
- (void)sendEvent:(UIEvent *)anEvent
{
    #define GS_EVENT_TYPE_OFFSET 2
    #define GS_EVENT_X_OFFSET 6
    #define GS_EVENT_Y_OFFSET 7
    #define STATUS_BAR_TOUCH_DOWN 1015
    
    // 从 UIEvent 遍历到 GSEvent 再到类型
    int *eventMemory = (int *)[anEvent performSelector:@selector(_gsEvent)];
    int eventType = eventMemory[GS_EVENT_TYPE_OFFSET];

    // 根据事件类型查找状态栏触摸
    if (eventType == STATUS_BAR_TOUCH_DOWN)
    {
        // 接下来的 6 行不是必需的，但如果你想知道触摸坐标在哪里，
        // 它们就在这里：
        int xMemory = eventMemory[GS_EVENT_X_OFFSET];
        int yMemory = eventMemory[GS_EVENT_Y_OFFSET];

        typedef union {int intValue; float floatValue;} Int2Float;
        float x = ((Int2Float)xMemory).floatValue;
        float y = ((Int2Float)yMemory).floatValue;

        NSLog(@"Status bar down at %f, %f", x, y);
        
        // 向 delegate 发送消息以处理操作
        [(HiddenDrawerAppDelegate *)self.delegate toggleDrawer];
    }
    else
    {
        [super sendEvent:anEvent];
    }
}
```

你可能好奇 `OFFSET` 值从何而来。答案是，我在故意触发状态栏及其他触摸事件的同时，花了些时间盯着 `GSEvent` 对象中的原始内存值——仅此而已。这种方法既棘手又不可靠。即便它在 iPhoneSDK3.0 上能工作，也纯属运气。

我在这里还使用了一个 `union`。这是因为我是以 `int` 类型逐步读取内存，而在 C 语言中，直接将 `int` 转换为 `float` 会引发数值转换（我需要的是重新解释，而非数值转换）。

我还选择阻止状态栏触摸事件通过常规路径传递到 `UITableView`。如果你想重新启用此行为，可以将 `[super sendEvent:anEvent];` 这行代码从 `else` 块中取出，放到主方法体中。

## 抽屉的动画

上述 `sendEvent:` 实现调用了 App 的 `delegate` 上的 `toggleDrawer` 方法。

所需要做的就是将抽屉的视图动画移入，并将表格视图下推：

```objc
drawerController = [[HiddenDrawerViewController alloc] init];

// 将抽屉放置在状态栏下方
CGRect drawerFrame = drawerController.view.frame;
CGRect statusBarFrame = [[UIApplication sharedApplication] statusBarFrame];
drawerFrame.origin.x = statusBarFrame.origin.x;
drawerFrame.size.width = statusBarFrame.size.width;
drawerFrame.origin.y = statusBarFrame.origin.y + statusBarFrame.size.height;

// 动画中将抽屉上移自身高度
drawerFrame.origin.y -= drawerFrame.size.height;

// 安放抽屉并添加到窗口
drawerController.view.frame = drawerFrame;
[window addSubview:drawerController.view];

// 启动动画
[UIView beginAnimations:nil context:nil];

// 将表格下移
CGRect tableFrame = viewController.view.frame;
tableFrame.origin.y += drawerFrame.size.height;
viewController.view.frame = tableFrame;

// 将抽屉下移
drawerFrame.origin.y += drawerFrame.size.height;
drawerController.view.frame = drawerFrame;

// 提交动画
[UIView commitAnimations];
```

如果你下载整个项目，你会看到还有一个向上动画并移除的分支，当 `drawerController` 已存在时会被执行。

## 结论

> 你可以下载 [HiddenDrawer 示例项目](https://www.cocoawithlove.com/assets/objc-era/HiddenDrawer.zip) (30kB) 来查看整个 App 的运行效果。

状态栏下方的隐藏抽屉并非每个 iPhone App 都必备，但它那种晦涩、隐秘的特性吸引了我。

通过 `GSEvent` 中的 `type` 字段来确定我们想要哪个 `UIEvent` 的方法有点不太可靠。Apple 随时可以更改 `GSEvent` 的结构，这可能会导致你的 App 行为异常或崩溃，因此这类代码需要在每个 iPhone OS 版本上进行测试，以确保其仍然能够工作。
