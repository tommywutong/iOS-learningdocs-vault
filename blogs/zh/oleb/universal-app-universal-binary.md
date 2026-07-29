---
title: 'Universal App ≠ Universal Binary'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/04/universal-app-is-not-a-universal-binary/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:573c018ce4eb5c84'
translated: true
---

> 原文：[Universal App != Universal Binary](https://oleb.net/blog/2010/04/universal-app-is-not-a-universal-binary/)　·　Ole Begemann

# Universal App ≠ Universal Binary

当 Apple 开始谈论构建可同时在 iPhone 和 iPad 上运行的 [universal app](http://developer.apple.com/iphone/library/documentation/General/Conceptual/iPadProgrammingGuide/StartingYourProject/StartingYourProject.html#//apple_ref/doc/uid/TP40009370-CH9-SW2) 时，我立刻想到了作为 PowerPC 到 Intel 过渡基石的 [universal binary](http://www.apple.com/universal/)。我原本以为一款可在 iPhone 和 iPad 上运行的 universal app 在技术上与 universal binary 完全相同，但事实上并非如此。

虽然 PowerPC 和 Intel 平台是完全不同且互不兼容的架构，但 iPhone 和 iPad 都基于 ARM 架构。这意味着，与 PowerPC/Intel 的 universal binary 不同，iPhone OS 意义上的 universal app 并不需要包含两个独立的二进制文件。毕竟，所有设备都能运行相同的代码。而 Apple 正是这样做的。Universal app 只是一个“普通”的 iPhone OS App，在其 `Info.plist` 中添加了一些特殊键值。

这对开发者的影响是：由于两个版本运行相同的二进制文件，你不能使用条件编译指令（`#if ... #else ... #endif`）来为 iPhone 和 iPad 生成不同的代码。所有设备类型相关的分支判断都必须在运行时进行。[Apple 建议我们使用新的 `UI_USER_INTERFACE_IDIOM()` 宏来实现这一点](http://developer.apple.com/iphone/library/documentation/General/Conceptual/iPadProgrammingGuide/StartingYourProject/StartingYourProject.html#//apple_ref/doc/uid/TP40009370-CH9-SW11)：

```
if (UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPad)
{
    // The device is an iPad running iPhone 3.2 or later.
}
else
{
    // The device is an iPhone or iPod touch.
}
```

这个方法效果很好。你将项目的 Base SDK 设置为 iPhone OS 3.2，将 Deployment Target 设置为 3.0 或 3.1，就可以为 iPad 设备或 iPad 模拟器（运行 3.2）或 iPhone 设备（运行 3.0/3.1）构建并运行这段代码。注意：你无法再在模拟器中测试 App 的 iPhone 版本。原因是，如果运行的是 universal application，3.2 模拟器默认会进入 iPad 模式。而且你无法再为 3.1 模拟器构建 App，因为 3.1 SDK 不认识 `UI_USER_INTERFACE_IDIOM` 符号。

为了解决这个问题，我们需要使用一个条件编译块。[Jeff LaMarche 几天前撰文介绍了这种方法](https://iphonedevelopment.blogspot.com/2010/04/few-more-notes-on-creating-universal.html)，我这里把他的方案稍作修改后重新发布，因为我认为他的代码中存在一个 bug（[请参阅我在他文章下的评论](https://iphonedevelopment.blogspot.com/2010/04/few-more-notes-on-creating-universal.html?showComment=1270580224919#c7696767908654355678)）：

```
#if __IPHONE_OS_VERSION_MAX_ALLOWED >= 30200
    if (UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPad)
    {
        // The device is an iPad running iPhone 3.2 or later.
    }
    else
#endif
    {
        // The device is an iPhone or iPod touch.
    }
```

[![Picture Effects 在 iPhone 模拟器 3.1 中运行](https://oleb.net/media/picture-effects-iphone-simulator-3-1-screenshot.png)](https://oleb.net/media/picture-effects-iphone-simulator-3-1-screenshot.png)

<sub>我的 universal app Picture Effects 在 iPhone 模拟器 3.1 中运行。</sub>

[![Picture Effects 在 iPad 模拟器 3.2 上运行](https://oleb.net/media/ipad-device-screenshot-4.jpg)](https://oleb.net/media/ipad-device-screenshot-4.jpg)

<sub>Picture Effects 在 iPad 模拟器 3.2 上运行。</sub>

**2010 年 4 月 9 日更新：** Chris 在评论中让我准备一个 universal app 的起始点。没问题：[UniversalViewBasedApp.zip](https://oleb.net/media/UniversalViewBasedApp.zip) 是一个非常简单的 App，可在 iPhone 和 iPad 上运行。它包含 iPhone 和 iPad 的独立 NIB 文件，两个版本都使用相同的视图控制器代码。要了解系统如何知道在哪个平台上加载哪些 NIB 文件，请参见 `Info.plist` 中的 `NSMainNibFile` 和 `NSMainNibFile~ipad` 键值。以下是我创建该 App 的方法：

- 使用 Xcode 内置的项目模板，为 iPhone 创建一个标准的基于视图的 App。
- 选择 `Project > Upgrade Target for iPad...`，并选择创建 Universal app 的选项。
- 在 Interface Builder 中打开 MainViewController.xib，选择 `File > Create iPad Version`，将生成的 NIB 文件保存为 MainViewController-iPad.xib，并将其添加到你的项目中。
- 在 MainWindow-iPad.xib 中，将 MainViewController 的 NIB 名称属性设置为 MainViewController-iPad。

**2010 年 4 月 13 日更新：** Jim Dovey [发现了另一种无需添加条件编译指令的解决方案](https://quatermain.tumblr.com/post/517122761/running-universal-ipad-iphone-apps-in-the-simulator)：首先为 3.2 模拟器 SDK 构建你的 App，然后将目标切换为 3.0 模拟器 SDK，然后运行（不要构建）。

**2010 年 5 月 5 日更新：** 来自 [Ryan Stubblefield](http://www.ryanstubblefield.net/) 的消息：

> 我创建了一个 universal app 模板，它使用最简单且精确的设备检测方法，并正确使用合适的 app delegate，全部通过代码实现，没有使用 NIB 文件。我发现所有使用 NIB 的 universal app 参考方案都不符合我的要求。universal app 模板项目的直接下载链接是：
> 
> [clean_universal_app_template.zip](https://github.com/ryanscott/rcloudlib/raw/1b6cc34f586eaf8206619542ff7a4f89cb991607/Samples/clean_universal_app_template.zip)
> 
> 我已将该项目包含在 [我的 iPhone 实用工具库的 GitHub 仓库](https://github.com/ryanscott/rcloudlib) 中。
> 
> 这是一个非常轻量级的库，包含了我发现的最有用的类扩展（class extension），以及一些自定义控制（custom control）和几个示例 App 模板。我鼓励你来看看。欢迎使用和贡献。
