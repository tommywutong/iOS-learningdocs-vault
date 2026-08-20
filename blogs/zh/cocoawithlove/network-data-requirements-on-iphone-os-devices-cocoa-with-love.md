---
title: iPhone OS 设备网络数据要求 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/04/network-data-requirements-on-iphone-os.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:5850a3c623ffe15e'
translated: true
---

> 原文：[Network data requirements on iPhone OS devices | Cocoa with Love](https://www.cocoawithlove.com/2010/04/network-data-requirements-on-iphone-os.html)　·　Cocoa with Love (Matt Gallagher)

如果你的 iPhone OS App 大量使用网络，那么你的 App 还需要一些额外设置，才能确保网络正常工作，并且 Apple 会批准你的 App。这些要求并非总是显而易见（有些在文档中有所记载，另一些则只在文档中有所暗示）。我想把它们分享出来，让你可以避免网络中断和 App Store 不必要的拒绝。

## Info.plist 设置

如果你的 iPhone/iPad/iPod Touch App 使用了 WiFi 网络连接，你应该在 App 的 Info.plist 中启用 `UIRequiresPersistentWiFi`（Application uses Wi-Fi）。如果没有此项设置，设备会在 5–30 分钟后将 WiFi 连接置于休眠状态。

我在[之前的文章](https://www.cocoawithlove.com/2009/08/control-and-configuration-of.html)中提到过这个设置，但我认为值得重复，因为它是一个容易被忽略的标志，如果未设置，会导致意外的网络中断。

还有其他 Info.plist 设置，包括 `UIRequireDeviceCapabilities`（Required device capabilities）值 "wifi"，你可以选择启用它，但目前看来它似乎没有任何效果。

## Reachability

如果你的 App 仅运行于 WiFi 或仅运行于 3G，那么你需要测试这一情况，并在使用了错误网络时向用户显示错误。这是 Apple 强制执行的可用性要求，如果不遵守，你的 App 将被拒绝。

Apple 提供了 [Reachability 示例 App](http://developer.apple.com/iphone/library/samplecode/Reachability/Introduction/Intro.html) 来演示如何测试网络可用性。在内部，该类使用了 `SCNetworkReachability` API，但从该示例程序中借用整个 `Reachability` 类并调用以下代码会更容易：

```objc
if ([[Reachability reachabilityForLocalWiFi] currentReachabilityStatus] == ReachableViaWiFi)
{
    // 执行需要本地 WiFi 连接的操作
}
else
{
    // 给出需要本地 WiFi 的提示
}
```

关于此的一个快速警告：设备从睡眠中唤醒后，WiFi 连接可能需要 10 秒或更长时间才能唤醒。如果 WiFi 不可用，你可能需要设置一个定时器，在接下来的 5–10 秒内重试，然后再显示错误。

## 3G 数据节流

如果你的 App 通过 3G 持续使用数据，你需要对该数据进行节流，而不是持续使用最大可用带宽。

这是什么意思？举个例子：我为某个客户编写了一款 App，它将音乐曲目下载到手机上，然后从本地存储的缓存中播放这些曲目。曲目的下载没有速度限制，Apple 最初因 App 过度使用 3G 而拒绝了它。

这个准则有些模糊。Apple 没有给出 App 应限制的具体数据速率。我确实想知道，他们是否没有意识到音频并非实际流式传输，而是在渐进式下载（progressive download）。

无论如何，以 128kbps 的速率对下载进行节流后，App 获得了批准。

你如何对下载进行节流？使用 `NSURLConnection` 无法做到。

我采用了以下原始但易于实现的方法。首先，我从 `NSURLConnection` 切换到了 `CFReadStream`。然后，在 `ReadStreamCallback` 中，我跟踪了一个小时间窗口内下载的数据，如果下载的数据超出了该窗口的配额，只需将 `CFReadStreamRef` 从运行循环（run loop）中移除，并安排一个定时器，在窗口配额期结束时将其放回：

```objc
CFReadStreamUnscheduleFromRunLoop(
    downloadStream,
    CFRunLoopGetCurrent(),
    kCFRunLoopCommonModes);

NSTimeInterval delay =
    THROTTLE_WINDOW_DURATION * 
    (totalDataDownloaded - startOfThrottleWindow) / THROTTLE_WINDOW_QUOTA;
throttleTimer =
    [NSTimer
        scheduledTimerWithTimeInterval:delay
        target:self
        selector:@selector(continueDownload)
        userInfo:nil
        repeats:NO];
```

在 `continueDownload` 的实现中，我使用 `CFReadStreamScheduleWithRunLoop` 重新安排下载。

通过将 `CFReadStreamRef` 从运行循环中移除，它不会被处理，连接也就被节流了。当它再次低于配额时，将其放回运行循环。

## 3G 视频的渐进式下载限制

这个限制非常简单：如果你正在播放通过 3G 网络下载的 MP4/MOV，其时长必须短于 10 分钟，并且数据速率低于 5 分钟内 5MB（大约 192kbps）。Apple 已经开始拒绝明显超出这些规定限制的 App。

解决办法是，你应该将此类 App 转换为新的 HTTP 视频流方法，该方法可以在 3G 上提供更灵敏的性能。

## HTTP 流式视频 64kbps 流

关于 HTTP 流式视频，Apple 还增加了一项新要求：任何计划用于 3G 的 HTTP 视频流都必须提供至少一个质量在 64kbps 或以下的流。

Apple 建议你提供纯音频流来满足此要求。就个人而言，如果你能找到一种方法也挤进视频，那么每秒 4 帧仍然比没有好。iPhone 不太喜欢以低于约 2.5fps 的帧率播放视频，所以你不能比这个再低太多。

## 结论

使用移动、低功耗或 3G 网络设备有很多小怪癖（quirks），这些怪癖在模拟器上测试期间或在办公 WiFi 上短暂测试期间不一定会出现。

Apple 还增加了很多关于你如何使用 3G 的限制。这些都不是他们强硬的措施——看起来他们确实只是想确保连接到 3G 的 App 能在真实世界的情况下正常工作——但这确实产生了一系列你需要满足的额外要求。

我希望其中一些要点对你有用。此页面上的每个示例都代表了我必须在 App 中修复的一个点（有时是在 beta 阶段，但有时是在 App Store 提审期间或向客户发布之后）。越早越好——最好在开始之前就知道。
