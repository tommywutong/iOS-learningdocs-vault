---
title: 在 SwiftUI 中观察播放状态
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/observing-playback-state-in-swiftui
source_url: 'https://developer.apple.com/documentation/avfoundation/observing-playback-state-in-swiftui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/observing-playback-state-in-swiftui.json'
content_hash: 'sha256:5ecece3e062090dc'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media playback](media-playback.md)

# 在 SwiftUI 中观察播放状态

<sub>文章</sub>

让你的用户界面与来自播放对象的状态变化保持同步。

## 概述

构建自定媒体播放器时的一项核心任务，是观察播放对象的状态以确定它们是否已就绪可播放，并跟踪其他重要的生命周期事件。你通常的做法是使用键值观察（key-value observing），但从 iOS 26、tvOS 26、macOS 26 和 visionOS 26 开始，AVFoundation 提供了一种基于 [Observation](../observation.md) 框架的监视播放状态的新方式。AVFoundation 让其核心播放类型遵循 [Observable](../observation/observable.md) 协议来支持该框架。这意味着你可以使用 [AVPlayer](avplayer.md) 或 [AVQueuePlayer](avqueueplayer.md)，连同它们关联的 [AVPlayerItem](avplayeritem.md) 和 [AVPlayerItemTrack](avplayeritemtrack.md) 对象，直接在 SwiftUI 视图中驱动状态变化。

## 选择加入播放观察

AVFoundation 支持用 Observation 监视播放状态，但默认不启用该功能。你需要通过把 [AVPlayer](avplayer.md) 类的 `isObservationEnabled` 属性设置为 `true` 来选择加入这种行为。

```swift
// Opt-in to observing with the Observation framework.
AVPlayer.isObservationEnabled = true
```

请在 App 生命周期的早期执行这个选择加入操作，例如在你的主 [App](../swiftui/app.md) 结构中，或在 [UIApplicationDelegate](../uikit/uiapplicationdelegate.md) 中（混合使用 UIKit 和 SwiftUI 的 App）。这个设置对整个 App 全局生效，并且必须在创建播放对象_之前_设置。在创建这些对象之后尝试更改它的值，会导致 AVFoundation 抛出异常。

## 存储播放状态

你在 App 中使用一个 SwiftUI [State](../swiftui/state.md) 变量来定义单一的事实来源。当 SwiftUI 创建视图时，这个属性包装器总是会把它的默认值实例化一次。在用它存储播放对象时——无论是直接存储，还是作为自定 `@Observable` 模型对象的一部分——请使用 [task(name:priority:file:line:_:)](<../swiftui/view/task(name_priority_file_line___).md>) 修饰符推迟这些对象的创建，以避免性能问题或其他潜在的副作用。例如，在一个简单的播放场景中，你可以定义一个状态变量来持有播放器对象，并像下面这样初始化它：

```swift
struct PlayerView: View {
    let url: URL
    // Don't create the player directly to avoid performance issues or other side effects.
    @State private var player: AVPlayer?
    
    var body: some View {
        ZStack {
            if let player {
                VideoView(player: player)
                TransportView(player: player)
            } else {
                LoadingView()
            }
        }
        // Use the task modifier to defer creating the player to ensure
        // SwiftUI creates it only once when it first presents the view.
        .task {
            player = AVPlayer(url: url)
        }
    }
}
```

使用 task 修饰符能确保 SwiftUI 在首次呈现该视图时只初始化一次播放器对象。

## 观察状态变化

由于这些播放对象遵循 [Observable](../observation/observable.md) 协议，你可以像使用任何其他 `@Observable` 对象那样，在 SwiftUI 视图中直接使用它们。例如，你可以把一个播放器实例传给某个视图，让该视图随着播放状态的变化自动重绘自身。

```swift
struct TransportView: View {
    
    // A player object passed from the view that owns the player reference.
    let player: AVPlayer
    
    // Observe the time control status property to determine whether playback is active.
    private var isPlaying: Bool {
        player.timeControlStatus == .playing
    }
    
    var body: some View {
        // A button that toggles the state of playback.
        Button {
            if isPlaying {
                player.pause()
            } else {
                player.play()
            }
        } label: {
            Image(systemName: isPlaying ? "pause.fill" : "play.fill")
        }
        // Observe the player item's status property to determine when to enable the button.
        .disabled(player.currentItem?.status != .readyToPlay)
    }
}
```

传输控制视图定义了一个 `isPlaying` 属性，它使用播放器对象的 [timeControlStatus](avplayer/timecontrolstatus-swift.property.md) 属性来判断是否正在播放媒体。它用这个属性驱动按钮呈现方式和行为的变化。该视图还观察当前的 player item，只有当 item 的 [status](avplayeritem/status-swift.property.md) 表明它已就绪可播放时才启用按钮。

> [!note] 注意
> 你可以使用 Observation 监视一般的状态属性，例如播放器的 [currentItem](avplayer/currentitem.md) 或 [rate](avplayer/rate.md)，但它不适合观察连续的状态变化，例如当前播放时间。对于这种用途，请改用专门的周期时间和边界时间观察方法。更多信息参见[在你的 App 中监视播放进度](monitoring-playback-progress-in-your-app.md)。

## 另请参阅

### 播放控制

- [控制播放器的传输行为](controlling-the-transport-behavior-of-a-player.md) — 播放、暂停媒体呈现并拖动浏览。
- [创建无缝的多视图播放体验](creating-a-seamless-multiview-playback-experience.md) — 使用 AVFoundation 和 AVRouting 框架构建高级的多视图播放体验。
- [AVPlayer](avplayer.md) — 一个提供控制播放器传输行为之接口的对象。
- [AVPlayerItem](avplayeritem.md) — 一个为播放期间 asset 的时间与呈现状态建模的对象。
- [AVPlayerItemTrack](avplayeritemtrack.md) — 一个表示播放期间 asset 轨道呈现状态的对象。
- [AVQueuePlayer](avqueueplayer.md) — 一个依次播放多个 player item 的对象。
- [AVPlayerLooper](avplayerlooper.md) — 一个使用队列播放器循环播放媒体内容的对象。
