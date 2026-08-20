---
title: 管理网络活动指示器
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2009/09/managing-the-network-activity-indicator/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:91e39d34c4be4108'
translated: true
---

> 原文：[管理网络活动指示器](https://oleb.net/blog/2009/09/managing-the-network-activity-indicator/)　·　Ole Begemann

# 管理网络活动指示器

iPhone 开发者应当使用 iPhone 状态栏中的小型网络活动指示器（network activity indicator），在 App 访问网络时告知用户。显示或隐藏该指示器很简单：

```
[[UIApplication sharedApplication] setNetworkActivityIndicatorVisible:YES];
```

大多数人大概会从自己的视图控制器中调用此方法。但当你需要同时处理多个访问网络的任务和（或）多个同时活跃的视图控制器时，这种方法就行不通了。例如，你可能正在后台运行一个 HTTP 请求来从 Web 服务下载数据，同时使用一个 `MKMapView` 实例，每当用户将地图移动到新位置时它都会访问网络。

如果在这些情况下从多个方法直接访问 `networkActivityIndicatorVisible` 属性，你很可能会在第一个任务完成后就隐藏指示器，即便你的 App 仍在继续访问网络。你需要实现一个计数器，记录网络活动指示器被显示和隐藏的次数，从而正确管理它。如果你的代码分散在多个视图控制器中，这就更加麻烦了。

这个问题诚然只是可用性中的一个微小方面，但解决方案是如此简单而优雅，以至于我认为即使你的 App 没有处理多个并发的网络活动任务，也值得去做。

由于网络活动指示器显示在你的 App 窗口之外，管理它的合理位置不是视图控制器，而是应用委托。我在我的应用委托中编写了一个简短方法，它使用一个静态变量来跟踪指示器被要求显示或隐藏的次数：

```
- (void)setNetworkActivityIndicatorVisible:(BOOL)setVisible {
    static NSInteger NumberOfCallsToSetVisible = 0;
    if (setVisible)
        NumberOfCallsToSetVisible++;
    else
        NumberOfCallsToSetVisible--;

    // 此断言有助于发现网络活动指示器管理中的编程错误。
    // 由于 NumberOfCallsToSetVisible 为负数并非致命错误，
    // 在生产代码中可能应将其移除。
    NSAssert(NumberOfCallsToSetVisible >= 0, @"Network Activity Indicator was asked to hide more often than shown");

    // 只要静态计数器大于 0，就显示指示器。
    [[UIApplication sharedApplication] setNetworkActivityIndicatorVisible:(NumberOfCallsToSetVisible > 0)];
}
```

此方法单独负责实际调用 `UIApplication` 实例来显示或隐藏指示器。所有视图控制器改为调用应用委托上的此方法：

```
[(MyAppDelegate *)[[UIApplication sharedApplication] delegate] setNetworkActivityIndicatorVisible:YES];
```
