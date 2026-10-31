---
title: 控制播放器的播放行为
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/controlling-the-transport-behavior-of-a-player
source_url: 'https://developer.apple.com/documentation/avfoundation/controlling-the-transport-behavior-of-a-player'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/controlling-the-transport-behavior-of-a-player.json'
content_hash: 'sha256:9ed7f86cd84e0d68'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体播放](media-playback.md)

# 控制播放器的播放行为

<sub>文章</sub>

播放、暂停媒体呈现，并在其中跳转。

## 概述

AVFoundation 为播放媒体资产提供了全面的支持，包括本地和远程的基于文件的媒体，以及通过 HTTP 实时流传输的媒体。该框架使用 [AVAsset](avasset.md) 类为媒体资产建模，无论媒体的类型或位置如何，它都提供一个一致的接口来加载和检查你的媒体。使用 [AVPlayer](avplayer.md) 对象以 [AVPlayerItem](avplayeritem.md) 对象的形式播放媒体资产，这些对象为资产的动态状态（例如其 [- currentTime](<avplayeritem/currenttime().md>)）建模。

了解如何有效使用 [AVPlayer](avplayer.md)，对于构建自定义播放器 UI 或需要以编程方式控制播放的人来说至关重要。

### 观察播放就绪状态

当你创建一个播放器条目时，它的初始状态为 [AVPlayerItemStatusUnknown](avplayeritem/status-swift.enum/unknown.md)，这意味着系统尚未尝试加载其媒体以供播放。只有当你将该条目与一个 [AVPlayer](avplayer.md) 对象关联时，系统才会开始加载资产的媒体。

要知道播放器条目何时可以播放，请观察其 [status](avplayeritem/status-swift.property.md) 属性的值。在调用播放器的 [- replaceCurrentItemWithPlayerItem:](<avplayer/replacecurrentitem(with_).md>) 方法之前添加这个观察，因为将播放器条目与播放器相关联就是系统开始加载该条目媒体的信号：

```swift
var statusObservation: NSKeyValueObservation?

func playMedia(at url: URL) {
    let asset = AVAsset(url: url)
    let playerItem = AVPlayerItem(
        asset: asset,
        automaticallyLoadedAssetKeys: [.tracks, .duration, .commonMetadata]
    )
    // 在与播放器关联之前对 status 属性进行键值观察。
    statusObservation = playerItem.observe(\.status, options: [.new, .initial]) { [weak self] item, _ in
        guard let self else { return }
        Task { @MainActor in
            switch item.status {
            case .readyToPlay:
                // 可以播放。呈现播放 UI。
            case .failed:
                // 加载媒体时发生了失败。
            default:
                break
            }
        }
    }
    // 将该条目设置为播放器的当前条目。
    player.replaceCurrentItem(with: playerItem)
}
```

当播放器条目达到 [AVPlayerItemStatusReadyToPlay](avplayeritem/status-swift.enum/readytoplay.md) 状态时，呈现或启用你的播放 UI。如果发生失败，则在播放器中显示相应的状态。

### 控制播放速率

播放器提供 [- play](<avplayer/play().md>) 和 [- pause](<avplayer/pause().md>) 方法作为控制其播放速率的主要手段。当播放器条目可以播放时，调用播放器的 [- play](<avplayer/play().md>) 方法，请求以 [defaultRate](avplayer/defaultrate.md)（初始值为 `1.0`，即自然速率）开始播放。默认情况下，播放器会自动等待，直到有足够的媒体数据可用才开始播放，以尽量减少停顿。你可以通过观察播放器的 [timeControlStatus](avplayer/timecontrolstatus-swift.property.md) 值来确定它处于暂停、等待播放还是正在播放状态：

```swift
var isPlaying = false
var timeControlObservation: NSKeyValueObservation?

private func observePlayingState() {
    timeControlObservation = player.observe(\.timeControlStatus, options: [.new, .initial]) { [weak self] player, _ in
        guard let self else { return }
        Task { @MainActor in
            self.isPlaying = player.timeControlStatus == .playing
        }
    }
}
```

通过观察 [AVPlayerRateDidChangeNotification](avplayer/ratedidchangenotification.md) 类型的通知来观察 [rate](avplayer/rate.md) 属性的变化。观察这个通知与对 [rate](avplayer/rate.md) 属性进行键值观察类似，但会提供关于速率变化原因的额外信息。使用 [AVPlayerRateDidChangeReasonKey](avplayer/ratedidchangereasonkey.md) 常量从通知的 [userInfo](../foundation/notification/userinfo.md) 字典中获取原因：

```swift
// 异步观察播放速率的变化。
private func observeRateChanges() async {
    let name = AVPlayer.rateDidChangeNotification
    for await notification in NotificationCenter.default.notifications(named: name) {
        guard let reason = notification.userInfo?[AVPlayer.rateDidChangeReasonKey] as? AVPlayer.RateDidChangeReason else {
            continue
        }
        switch reason {
        case .appBackgrounded:
            // The app transitioned to the background.
        case .audioSessionInterrupted:
            // The system interrupts the app’s audio session.
        case .setRateCalled:
            // The app set the player’s rate.
        case .setRateFailed:
            // An attempt to change the player’s rate failed.
        default:
            break
        }
    }
}
```

### 在媒体时间线上跳转

你可以使用 [AVPlayer](avplayer.md) 和 [AVPlayerItem](avplayeritem.md) 的方法以多种方式在媒体时间线上跳转。最常见的方式是使用播放器的 [- seekToTime:](<avplayer/seek(to_)-87h2r.md>) 方法，并向它传递一个目标 [CMTime](../coremedia/cmtime.md) 值。在异步上下文中调用这个方法：

```swift
// 处理来自用户界面的时间更新请求。
func seek(to timeInterval: TimeInterval) async {
    // 为传入的时间间隔创建一个 CMTime 值。
    let time = CMTime(seconds: timeInterval, preferredTimescale: 600)
    await avPlayer.seek(to: time)
}
```

你可以只调用这个方法一次来跳转到目标位置，但也可以连续调用它，例如在使用 [Slider](../swiftui/slider.md) 视图时。

[- seekToTime:](<avplayer/seek(to_)-87h2r.md>) 方法是在你的呈现中快速跳转的便捷方式，但它以速度为先，而不是以精度为先。这意味着播放器实际跳转到的时间可能与请求的时间略有差异。如果你需要实现精确的跳转行为，请使用 [- seekToTime:toleranceBefore:toleranceAfter:](<avplayer/seek(to_tolerancebefore_toleranceafter_).md>) 方法，它可以让你指明与目标时间之间可容忍的偏差量（之前和之后）。例如，如果你需要提供样本级精确的跳转行为，请将容差值指定为零：

```swift
// 精确跳转到指定时间。
await avPlayer.seek(to: time, toleranceBefore: .zero, toleranceAfter: .zero)
```

## 另请参阅

### 播放控制

- [在 SwiftUI 中观察播放状态](observing-playback-state-in-swiftui.md) — 让你的用户界面与播放对象的状态变化保持同步。
- [创建无缝的多视图播放体验](creating-a-seamless-multiview-playback-experience.md) — 使用 AVFoundation 和 AVRouting 框架构建高级的多视图播放体验。
- [AVPlayer](avplayer.md) — 一个提供控制播放器播放行为的界面的对象。
- [AVPlayerItem](avplayeritem.md) — 一个为资产在播放期间的时间和呈现状态建模的对象。
- [AVPlayerItemTrack](avplayeritemtrack.md) — 一个表示资产轨道在播放期间的呈现状态的对象。
- [AVQueuePlayer](avqueueplayer.md) — 一个按顺序播放多个播放器条目的对象。
- [AVPlayerLooper](avplayerlooper.md) — 一个使用队列播放器循环播放媒体内容的对象。
