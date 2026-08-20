---
title: iOS 上的 App 启动序列
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/06/app-launch-sequence-ios/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:15f92b7b9e1174b8'
translated: true
---

> 原文：[The App Launch Sequence on iOS](https://oleb.net/blog/2011/06/app-launch-sequence-ios/)　·　Ole Begemann

# iOS 上的 App 启动序列

**更新于 2012 年 2 月 9 日：** Apple 在 Xcode 4.2 的默认项目模板中对 App 启动序列做了一些更改。因此，[我在一篇新文章中重新探讨了这个主题](https://oleb.net/blog/2012/02/app-launch-sequence-ios-revisited/)。请参阅新文章以获取最新信息。

我注意到许多初学 iOS 开发者将 iOS App 的启动过程视为某种神秘事件。不知何故，有人向我们的 App 委托发送了一条 `application:didFinishLaunchingWithOptions:` 消息，这似乎是我们第一次有机会注入自己的代码。但我们的 App 是如何到达那里的呢？

# 始于 `main()`

每个 C 程序的执行都从一个名为 `main()` 的函数开始，由于 Objective-C 是 C 的严格超集，因此对于 Objective-C 程序也必须如此。如果你从默认模板之一创建一个新的 iOS 项目，Xcode 会将这个函数放在一个名为 `main.m` 的单独文件中，该文件位于 _Supporting Files_ 组中。通常，你不需要查看该文件，但我们来看一下。这是 `main()` 的完整代码：

```
int main(int argc, char *argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    int retVal = UIApplicationMain(argc, argv, nil, nil);
    [pool release];
    return retVal;
}
```

函数的参数 `argc` 和 `argv` 包含有关启动时传递给可执行文件的命令行参数的信息。在本次讨论中我们可以安全地忽略它们。让我们看看这个函数做了什么，看起来非常简单：

1. 它创建了一个自动释放池（autorelease pool），因为在每个 Cocoa App 中必须始终存在一个（否则，`autorelease` 调用会失败）。
2. 它调用了一个名为 `UIApplicationMain()` 的函数。我们将在下面深入探讨它。
3. 它排空了刚刚创建的自动释放池。
4. 它将 `UIApplicationMain()` 的返回值返回给调用者（即启动可执行文件的 shell）。

当 (Objective-)C 程序执行到 `main()` 的末尾时，它就结束了。所以这看起来确实是一个非常短的程序。尽管如此，所有 iOS App 都是这样工作的，所以秘密一定在于 `UIApplicationMain()` 函数。只要它返回，我们的程序就会立即结束。

# `UIApplicationMain()`

查看 `UIApplicationMain()` 的文档，我们发现：

> 此函数从主类（principal class）实例化 App 对象，并从给定类实例化委托（如果有），并为 App 设置委托。它还设置了主事件循环，包括 App 的运行循环（run loop），并开始处理事件。如果 App 的 `Info.plist` 文件通过包含 `NSMainNibFile` 键和一个有效的 nib 文件名称作为值来指定要加载的主 nib 文件，则此函数会加载该 nib 文件。
>
> 尽管声明了返回类型，但此函数从不返回。

让我们逐步分析这一点：

[![iOS 4 上的 App 启动序列](https://oleb.net/media/ios-4-app-launch-flow.png)](https://oleb.net/media/ios-4-app-launch-flow.png)

<sub>iOS 4 上的 App 启动序列流程图。欢迎在 [Creative Commons Attribution 许可协议](http://creativecommons.org/licenses/by/3.0/) (CC-BY) 下分享此图片。</sub>

1. 首先，该函数创建主 App 对象（流程图中的第 3 步）。如果你将 `nil` 指定为 `UIApplicationMain()` 的第三个参数（默认值），它将在此步骤中创建一个 `UIApplication` 的实例。这通常就是你想要的。但是，如果你需要派生子类（subclass）`UIApplication`（例如，在 `sendEvent:` 中覆盖其事件处理），则必须将子类的名称以字符串形式传递给 `UIApplicationMain()`。
2. 然后，该函数查看其第四个参数。如果它非 nil，则将其解释为 App 委托类的名称，实例化该类的对象，并将其指定为 App 对象的 `delegate`。不过，第四个参数的默认值是 `nil`，这表示 App 委托将在主 NIB 文件中创建。
3. 接下来，`UIApplicationMain()` 加载并解析你的 App 的 `Info.plist`（第 4 步）。如果其中包含一个名为 "Main nib file base name" (`NSMainNibFile`) 的键，该函数还将加载其中指定的 NIB 文件（第 5 步）。
4. 默认情况下，主 NIB 文件名为 `MainWindow.nib`。它至少包含一个表示 App 委托的对象，连接到 File's Owner 的 `delegate` 出口（outlet）（第 6 步），以及一个将用作 App 主窗口（window）的 `UIWindow` 对象，连接到 App 委托的一个出口。如果你使用了基于视图控制器（view controller）的 App 模板，NIB 文件还将包含你的 App 的根视图控制器（root view controller），以及可能的一个或多个子视图控制器。

  值得一提的是，这是基于 UIKit 的 App 模板（基于窗口、基于视图、基于导览、基于标签页等）之间唯一显著不同的步骤。如果你从一个基于视图的 App 开始，后来想要引入一个导览控制器（navigation controller），则无需启动新项目：只需替换主 NIB 文件中的根视图控制器，并调整 App 委托中的一两行代码即可。我注意到许多 iOS 平台新手在这个问题上挣扎，并认为不同的项目模板之间存在巨大差异。事实并非如此。
5. 现在，`UIApplicationMain()` 创建了 App 的运行循环，`UIApplication` 实例使用它来处理事件，例如触摸事件或网络事件（第 7 步）。运行循环基本上是一个无限循环，导致 `UIApplicationMain()` 永不返回。
6. 在 App 对象处理第一个事件之前，它最终会向 App 委托发送著名的 `application:didFinishLaunchingWithOptions:` 消息，使我们有机会执行自己的设置（第 8 步）。我们在此至少要做的，是通过向主窗口发送 `makeKeyAndVisible` 消息将其显示在屏幕上。

# 入口点

你看，这里并没有什么神秘之处。除了 `application:didFinishLaunchingWithOptions:` 之外，在启动序列期间还有几个自定义代码的入口点（通常都不需要）：

- 直接在 `main()` 中，在调用 `UIApplicationMain()` 之前。
- 自定义 `UIApplication` 子类的 `init` 方法。
- 如果 App 委托是从 NIB 文件创建的（默认情况），那么是在其 `initWithCoder:` 或 `awakeFromNib` 方法中。
- App 委托类或自定义 `UIApplication` 子类的 `+initialize` 方法。任何类在从程序内部接收第一条消息之前，都会收到 `+initialize` 消息。

请注意，此序列仅在 App 实际**启动**时发生。如果 App 已在运行，并且只是从后台被带回前台，则这些都不会发生。
