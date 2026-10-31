---
title: 在 tvOS 中支持遥控器交互
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [tvOS 16.0+, Xcode 14.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/supporting-remote-interactions-in-tvos
source_url: 'https://developer.apple.com/documentation/avfoundation/supporting-remote-interactions-in-tvos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/supporting-remote-interactions-in-tvos.json'
content_hash: 'sha256:0f3eab0f1ffe1446'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体播放](media-playback.md)

# 在 tvOS 中支持遥控器交互

<sub>示例代码</sub>

通过采用相关方式，设置你的 App 以在各种场景下支持遥控命令和事件。

## 概述

本示例代码项目演示了如何实现对遥控器和系统控制发送到 Apple TV 的各类命令的支持。

本项目分为四个部分。第一部分演示如何使用 [AVPlayerViewController](../avkit/avplayerviewcontroller.md) 提供的系统播放器为你的 App 添加原生媒体播放能力。它还展示了如何使用 [MPRemoteCommandCenter](../mediaplayer/mpremotecommandcenter.md) 在系统播放器中支持额外的命令，以及如何使用 [AVPlayerViewControllerDelegate](../avkit/avplayerviewcontrollerdelegate.md) 来自定播放器所接收命令的行为。

在大多数情况下，使用系统播放器都是很好的选择。但是，如果你需要实现一个具有自定义 UI 的播放器，你还需要实现对系统播放器所支持的全部命令的支持。第二部分展示了具体做法：使用 `MPRemoteCommandCenter` 和手势识别器。它还演示了如何处理接收到的远程事件并更新「正在播放」信息显示。

第三部分显示一个将遥控命令以可视化的方式呈现的屏幕，随播放器接收命令而更新。第四部分展示如何在显示频道和节目的指南中翻页浏览内容。

### 在系统播放器中支持额外的命令

通过使用 `AVPlayerViewController`，你可以自动获得对播放和导览媒体的大多数控制的支持。要提供对额外遥控事件（例如上一曲和下一曲命令）的支持，请使用共享的 `MPRemoteCommandCenter` 对象。在下面的示例中，`additionalRemoteCommands` 包含在遥控命令中心注册的上一曲和下一曲命令，而 `handleCommand(_:)` 会为它接收到的命令执行相应的操作。

```swift
private func setupAdditionalRemoteCommands() {
    additionalRemoteCommands.forEach { [weak self] remoteCommand in
        guard let self = self else { return }
        // 在添加新目标之前先移除每个目标。
        remoteCommand.mediaRemoteCommand.removeTarget(nil)
        remoteCommand.mediaRemoteCommand.addTarget { _ in
            self.handleCommand(remoteCommand)
        }
    }
}
```

你还可以通过遵循 `AVPlayerViewControllerDelegate` 来自定 `AVPlayerViewController` 原生支持的命令的行为。例如，下面的代码将 `skipToPreviousChannel` 事件映射到 `channelDown` 操作：

```swift
func playerViewController(_ playerViewController: AVPlayerViewController,
                          skipToPreviousChannel completion: @escaping (Bool) -> Void) {
    channelDown()
    completion(true)
}
```

### 在自定义播放器中支持所有命令并更新「正在播放」信息

当你创建自定义播放器时，请使用 `MPRemoteCommandCenter` 来实现对遥控器可以发送给它的全套命令和事件的支持。下面的示例展示了如何自定更改播放速率以及向后或向前跳过这些行为。它还展示了如何添加目标来处理所有其他受支持的命令：

```swift
for supportedCommand in supportedRemoteCommands {
    switch supportedCommand {
        // 为需要它们的命令定义速率和间隔。
    case .changePlaybackRate:
        let allSupportedRates = rewindSupportedRates + fastForwardSupportedRates
        commandCenter
            .changePlaybackRateCommand
            .supportedPlaybackRates = allSupportedRates.map {
                $0 as NSNumber
            }

    case .skipBackward:
        commandCenter
            .skipBackwardCommand
            .preferredIntervals = [skipInterval as NSNumber]

    case .skipForward:
        commandCenter
            .skipForwardCommand
            .preferredIntervals = [skipInterval as NSNumber]

    default:
        break
    }

    // Remove each target before you add a new one.
    supportedCommand.mediaRemoteCommand.removeTarget(nil)
    supportedCommand.mediaRemoteCommand.addTarget {
        self.handle(command: supportedCommand, withCommandEvent: $0)
    }
}
```

此外，这一部分还演示了如何使用默认的 [MPNowPlayingInfoCenter](../mediaplayer/mpnowplayinginfocenter.md) 对象来更新「正在播放」信息：

```swift
var nowPlayingInfo = [String: Any]()

nowPlayingInfo[MPMediaItemPropertyTitle] = currentProgram.title
nowPlayingInfo[MPMediaItemPropertyPlaybackDuration] = currentItem.duration.seconds
nowPlayingInfo[MPNowPlayingInfoPropertyIsLiveStream] = currentProgram.isLive
nowPlayingInfo[MPNowPlayingInfoPropertyAssetURL] = currentProgram.playlistURL
nowPlayingInfo[MPNowPlayingInfoPropertyPlaybackRate] = self.player.rate
nowPlayingInfo[MPNowPlayingInfoPropertyDefaultPlaybackRate] = self.defaultPlaybackRate
nowPlayingInfo[MPNowPlayingInfoPropertyElapsedPlaybackTime] = self.player.currentTime().seconds

// 设置任何适用于你的应用程序的其他属性。

MPNowPlayingInfoCenter.default().nowPlayingInfo = nowPlayingInfo
```

### 呈现接收到的远程事件

本项目的第三部分包含一个屏幕，它以可视化的方式显示用户与遥控器交互的反馈。它通过将视图控制器从遥控器接收到的远程事件上报给视图来实现，以便视图让相应的单元格闪烁：

```swift
private func reportRemoteEvent(_ remoteEvent: RemoteEvent,
                               withState state: UIGestureRecognizer.State? = nil) {
    guard let remoteEventsView = self.view as? RemoteEventsView else { return }
    remoteEventsView.remoteEventReceived(remoteEvent, withState: state)
}
```

### 在指南中翻页浏览内容

如果你的 App 显示一个列出频道及其相应节目的指南，本项目的第四部分展示了如何响应遥控命令对内容进行翻页，例如在频道向上按键时滚动到上一页：

```swift
@objc private func channelUpPressed() {
    // 由于单元格高度是固定的，`indexPathsForVisibleItems`
    // 在任一时刻屏幕上最多只有 14 个条目。
    guard let targetItemInPreviousPageSectionIdx = collectionView
        .indexPathsForVisibleItems.sorted().first?.section else { return }

    // 在每个分页分区中，频道单元格始终是条目 0，节目
    // 单元格从 1 开始。
    let firstProgramItemIdx = 1
    let targetItemIdx = currentlyFocusedIndexPath?.item ?? firstProgramItemIdx
    channelUpDownTargetIndexPath = IndexPath(
        item: targetItemIdx,
        section: targetItemInPreviousPageSectionIdx
    )
    // 频道向上按键时滚动到上一页。
    channelUpDownScrollDirection = .up

    setNeedsFocusUpdate()
    updateFocusIfNeeded()
}
```

## 下载

- [SupportingRemoteInteractionsInTvOS.zip](https://docs-assets.developer.apple.com/published/684fd81a8996/SupportingRemoteInteractionsInTvOS.zip)
