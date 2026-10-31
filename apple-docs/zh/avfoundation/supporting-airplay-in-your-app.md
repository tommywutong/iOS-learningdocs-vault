---
title: 在你的 App 中支持隔空播放
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/supporting-airplay-in-your-app
source_url: 'https://developer.apple.com/documentation/avfoundation/supporting-airplay-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/supporting-airplay-in-your-app.json'
content_hash: 'sha256:de372381e77b32de'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [流媒体与隔空播放](streaming-and-airplay.md)

# 在你的 App 中支持隔空播放

<sub>文章</sub>

设置你的 App 使用隔空播放（AirPlay）以无线方式发送内容。

## 概述

隔空播放让你能够以无线方式将内容从 Apple 设备发送到 Apple TV 或支持隔空播放的扬声器。隔空播放为无线音频分发提供了增强支持，包括将内容发送到多个支持隔空播放的扬声器的能力。

### 确定 App 播放的音频类型

在 iOS、tvOS 和 watchOS 上，将你的音频会话的路由共享策略设置为 `.longForm`。长篇音频（long-form audio）是指系统声音以外的任何音频，例如音乐、有声书或播客。这一设置标识了 App 播放的音频类型，如下例所示。

```swift
let audioSession = AVAudioSession.sharedInstance()
try audioSession.setCategory(.playback, 
                             mode: .default, 
                             policy: .longFormAudio)
```

### 添加隔空播放选择器

将 [AVRoutePickerView](../avkit/avroutepickerview.md) 添加到你的视图层级结构中，以便在你的 App 中包含一个隔空播放选择器。该选择器向用户提供一份可用于你的 App 的潜在隔空播放设备列表。要控制何时显示该选择器，请使用 [AVRouteDetector](avroutedetector.md) 来识别路由探测器的状态。

### 添加媒体播放器

通过 Media Player 集成使用 API 来自定你的隔空播放采用方式。如果你使用 [MPRemoteCommandCenter](../mediaplayer/mpremotecommandcenter.md)，你可以接收远程命令。如果你使用 [MPNowPlayingInfoCenter](../mediaplayer/mpnowplayinginfocenter.md)，你可以将正在设备上播放的轨道的元数据告知系统。

### 为快速流传输配置 App

采用以下两组播放 API 之一，以利用隔空播放中增强的缓冲能力：

- 对于简单增强缓冲，使用 [AVPlayer](avplayer.md) 或 [AVQueuePlayer](avqueueplayer.md)。这非常适合视频内容。更多信息请参阅[为你的内容实现简单增强缓冲](implementing-simple-enhanced-buffering-for-your-content.md)。
- 若要在增强缓冲方面获得更大的灵活性，请使用 [AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md) 和 [AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md)。对于需要对 I/O 进行控制、对媒体数据执行预处理，或拥有 [AVPlayer](avplayer.md) 不支持的 DRM 模型的 App，这个选项更为合适。更多信息请参阅[为你的内容实现灵活增强缓冲](implementing-flexible-enhanced-buffering-for-your-content.md)。
