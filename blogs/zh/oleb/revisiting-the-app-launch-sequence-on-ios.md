---
title: 重温 iOS 上的 App 启动序列
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/02/app-launch-sequence-ios-revisited/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b4956547f04e0bc9'
translated: true
---

> 原文：[Revisiting the App Launch Sequence on iOS](https://oleb.net/blog/2012/02/app-launch-sequence-ios-revisited/)　·　Ole Begemann

# 重温 iOS 上的 App 启动序列

2011 年 6 月，我首次撰文介绍了 [iOS 上的 App 启动序列](https://oleb.net/blog/2011/06/app-launch-sequence-ios/)，阐明了在 iOS App 启动到 [`application:didFinishLaunchingWithOptions:`](https://developer.apple.com/library/IOs/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/Reference/Reference.html#//apple_ref/doc/uid/TP40006786-CH3-SW18) 方法之间实际发生的底层过程。

自那以后，Apple 修改了其 iOS App 项目模板中的默认启动序列，因此是时候对原文章进行更新了。

# 流程图

[![Xcode 4.2 下的 App 启动序列（未使用 Storyboard）](https://oleb.net/media/xcode-4-2-app-launch-sequence.png)](https://oleb.net/media/xcode-4-2-app-launch-sequence.png)

<sub>iOS 中 Xcode 4.2 下非 storyboard App 的默认 App 启动序列流程图。你可根据 [Creative Commons 署名许可](http://creativecommons.org/licenses/by/3.0/) (CC-BY) 自由分享此图片。在使用 storyboard 的 App 中，`UIApplicationMain()` 还会额外触发加载 App 的主 Storyboard 文件，进而创建窗口和初始视图控制器（view controller）。</sub>

# `main()` 的变更

让我们看看 `main()` 函数的变化，它仍然是 App 的入口点。现在该函数如下所示：

```
int main(int argc, char *argv[])
{
    @autoreleasepool {
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([AppDelegate class]));
    }
}
```

`main()` 使用了 LLVM 3.0 引入的新 `@autoreleasepool { }` 语法，但这一更改与 App 的启动序列无关。更重要的是，对 [`UIApplicationMain()`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIKitFunctionReference/Reference/reference.html#//apple_ref/doc/uid/TP40006894-CH3-SW7) 的调用从 `UIApplicationMain(argc, argv, nil, nil);` 变为了上述形式。注意第四个参数的变化。

查阅[文档](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIKitFunctionReference/Reference/reference.html#//apple_ref/doc/uid/TP40006894-CH3-SW7)可知，`UIApplicationMain()` 的第四个参数指定了：

> 用于实例化 App 委托的类名。……如果从 App 的主 NIB 文件中加载委托对象，则指定 `nil`。

因此，我们之前的 App 委托之前在 `MainWindow.xib` 中通过 Interface Builder 创建，现在则直接由 `UIApplicationMain()` 函数创建了。^[1](#fn:1) 事实上，项目中甚至不再存在 `MainWindow.xib` 文件！

# 不再有 MainWindow.xib

在 Xcode 4.2 之前，所有默认项目模板都会创建一个 `MainWindow.xib` 文件。由于该文件在 App 的 `Info.plist` 中被指定为主 NIB 文件，`UIApplicationMain()` 函数在创建 App 的 [`UIApplication`](https://developer.apple.com/reference/uikit/uiapplication) 实例后，会立即自动加载它。

正是在这个 NIB 文件中，App 委托对象和 App 的主窗口被创建出来，并通过 Outlet 连接在一起。通常情况下，`MainWindow.xib` 还会包含 App 的根视图控制器，该控制器已连接到 App 委托类中的自定义 Outlet 以及窗口的 `rootViewController` Outlet。

由于主 NIB 文件完成了如此多的工作，默认的 `application:didFinishLaunchingWithOptions:` 方法几乎可以保持为空。它只需要将窗口显示到屏幕上：

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    // 在 App 启动后进行自定义设置的覆盖点。
    [self.window makeKeyAndVisible];
    return YES;
}
```

从 Xcode 4.2 开始，Apple 决定从 iOS 项目模板中移除主 NIB 文件。这一更改的直接原因很可能是[故事板（storyboarding）](https://developer.apple.com/library/ios/#releasenotes/Miscellaneous/RN-AdoptingStoryboards/_index.html)的引入。

Storyboard 基于视图控制器，而非视图或窗口。对于基于 storyboard 的 App 来说，坚持主 NIB 文件的概念毫无意义（而且也不可能，因为 `Info.plist` 中的 `NSMainNibFile` 和 `UIMainStoryboardFile` 键[是互斥的](https://developer.apple.com/library/ios/documentation/general/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW9)）。而仅在基于 storyboard 的 App 中放弃主 NIB 文件，却为其他 App 保留它，会导致项目模板之间产生不必要的不一致。

# `application:didFinishLaunchingWithOptions:` 中需要做更多工作

主 NIB 文件消失后，原本在 NIB 文件中执行的任务必须迁移到其他地方。我们已经看到 `UIApplicationMain()` 接管了其中一项：创建 App 委托。由于该函数现在同时控制 `UIApplication` 实例及其委托，我们也可以有把握地假设它会将委托分配给 App 实例。

在此阶段，会发送 `application:didFinishLaunchingWithOptions:` 消息。由于尚未有人创建窗口或视图控制器，该方法现在会在代码中执行这些任务，至少对于不使用 storyboard 的 App 来说是这样的：

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    // 在 App 启动后进行自定义设置的覆盖点。
    self.viewController = [[ViewController alloc] initWithNibName:@"ViewController" bundle:nil];
    self.window.rootViewController = self.viewController;
    [self.window makeKeyAndVisible];
    return YES;
}
```

如果你的 App 使用了故事板（通过在 `Info.plist` 中指定 `UIMainStoryboardFile`），那么 App 在启动时会自动加载主 Storyboard 文件，就像加载主 NIB 文件一样。它还会创建一个窗口，将 storyboard 的初始视图控制器放入其中，并将窗口显示到屏幕上。因此，我们无需在 `application:didFinishLaunchingWithOptions:` 中再做任何事：

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    // 在 App 启动后进行自定义设置的覆盖点。
    return YES;
}
```

# 代码多了一些，但更加清晰

现在，初始化（非 storyboard）App 所需的代码行数比以前多了一些，但我认为这一更改使 App 启动序列比以前清晰得多。我知道许多 iOS 开发者曾因不理解主 NIB 文件的作用而在理解启动过程时遇到困难。

我通常非常支持使用 NIB 文件 / storyboard，但在某些情况下，它们反而可能增加困惑，而不是起到帮助作用。

1. 语法 `NSStringFromClass([AppDelegate class])` 可能看起来有点奇怪。为什么 Apple 不直接在这里使用普通字符串 `@"AppDelegate"` 呢？结果是一样的。他们采用更复杂的方式可能是为了简化重构：如果你想重命名 `AppDelegate` 类，内置的重构工具会检测到它在 `main()` 中的使用并将其一并重命名。而如果它只是一个字符串，显然就无法做到这一点。[↩︎](#fnref:1)
