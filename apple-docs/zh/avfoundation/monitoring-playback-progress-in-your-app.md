---
title: 在你的 App 中监视播放进度
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/monitoring-playback-progress-in-your-app
source_url: 'https://developer.apple.com/documentation/avfoundation/monitoring-playback-progress-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/monitoring-playback-progress-in-your-app.json'
content_hash: 'sha256:8374b893f72695b3'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media playback](media-playback.md)

# 在你的 App 中监视播放进度

<sub>文章</sub>

观察媒体 asset 的播放，以更新你 App 的用户界面状态。

## 概述

媒体播放类 App 通常需要监视播放进度，以驱动播放器 UI 的状态或执行其他操作。监视这种状态所需的时间精度高于键值观察能提供的水平，因此 [AVPlayer](avplayer.md) 提供了专门用于观察播放时间的 API。本文介绍如何按固定时间间隔或在播放跨越特定时间边界时观察这种状态。

### 按固定时间间隔观察当前播放时间

观察播放器当前时间最常见的方式是按固定时间间隔观察。当你要驱动播放器用户界面中时间显示的状态时，这种方式非常有用。

要按固定时间间隔观察播放器的当前时间，调用它的 [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<avplayer/addperiodictimeobserver(forinterval_queue_using_).md>) 方法。该方法接受一个表示观察时间间隔的 [CMTime](../coremedia/cmtime.md) 值、一个串行派发队列，以及播放器按指定时间间隔调用的回调。下面的示例添加了一个观察器，播放器在正常播放期间每半秒调用它一次：

```swift
@Published private(set) var duration: TimeInterval = 0.0
@Published private(set) var currentTime: TimeInterval = 0.0

private let player = AVPlayer()
private var timeObserver: Any?

/// Adds an observer of the player timing.
private func addPeriodicTimeObserver() {
    // Create a 0.5 second interval time.
    let interval = CMTime(value: 1, timescale: 2)
    timeObserver = player.addPeriodicTimeObserver(forInterval: interval,
                                                  queue: .main) { [weak self] time in
        guard let self else { return }
        // Update the published currentTime and duration values.
        currentTime = time.seconds
        duration = player.currentItem?.duration.seconds ?? 0.0
    }
}

/// Removes the time observer from the player.
private func removePeriodicTimeObserver() {
    guard let timeObserver else { return }
    player.removeTimeObserver(timeObserver)
    self.timeObserver = nil
}
```

在完成状态监视后，务必把对播放器 [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<avplayer/addperiodictimeobserver(forinterval_queue_using_).md>) 方法的调用与对 [- removeTimeObserver:](<avplayer/removetimeobserver(__).md>) 的调用配对使用。不遵守这条规则会导致未定义行为。

### 观察媒体呈现中特定时间的播放

另一种观察播放器的方式，是在播放跨越特定时间边界时进行观察。你可以在这些时间点过去时更新你的播放器 UI 或执行其他操作。

要让播放器在跨越媒体时间线中的特定点时通知你的 App，调用播放器的 [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<avplayer/addboundarytimeobserver(fortimes_queue_using_).md>) 方法。该方法接受一个由 [NSValue](../foundation/nsvalue.md) 对象组成的数组（其中包装着定义边界时间的 [CMTime](../coremedia/cmtime.md) 值）、一个串行派发队列，以及一个回调闭包。下面的示例展示如何为播放的每个四分之一处定义边界时间：

```swift
/// Adds an observer of the player traversing specific times during standard playback.
private func addBoundaryTimeObserver() async throws {
    
    // Asynchronously load the duration of the asset.
    let duration = try await asset.load(.duration)
    
    // Divide the asset's duration into quarters.
    let quarterDuration = CMTimeMultiplyByRatio(duration,
                                                multiplier: 1,
                                                divisor: 4)
    
    var currentTime = CMTime.zero
    var times = [NSValue]()
    
    // Calculate boundary times.
    while currentTime < duration {
        currentTime = currentTime + quarterDuration
        times.append(NSValue(time:currentTime))
    }
    
    timeObserver = player.addBoundaryTimeObserver(forTimes: times,
                                                  queue: .main) { [weak self] in
        // Update the percentage complete in the user interface.
    }
}
```

无论你添加的是周期时间观察器还是边界时间观察器，都需要在完成时调用 [- removeTimeObserver:](<avplayer/removetimeobserver(__).md>) 来移除观察。

## 另请参阅

### 呈现

- [使用带 alpha 通道的 HEVC 视频](using-hevc-video-with-alpha.md) — 播放、写入和导出带 alpha 通道的 HEVC 视频，为你的视频处理添加叠层效果。
- [AVPlayerLayer](avplayerlayer.md) — 一个呈现播放器对象视觉内容的对象。
- [AVSynchronizedLayer](avsynchronizedlayer.md) — 一种 Core Animation 图层，它的时间源自一个 player item，让你可以让图层动画与媒体播放保持同步。
