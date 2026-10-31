---
title: 为你的内容实现简单增强缓冲
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/implementing-simple-enhanced-buffering-for-your-content
source_url: 'https://developer.apple.com/documentation/avfoundation/implementing-simple-enhanced-buffering-for-your-content'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/implementing-simple-enhanced-buffering-for-your-content.json'
content_hash: 'sha256:1028f49a60f7bfa1'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [流媒体与隔空播放](streaming-and-airplay.md)

# 为你的内容实现简单增强缓冲

<sub>文章</sub>

将你的 App 配置为使用简单增强缓冲，以更快的速度将内容流传输到支持隔空播放的设备和受支持的 CarPlay 车辆。

## 概述

[AVPlayer](avplayer.md) 和 [AVQueuePlayer](avqueueplayer.md) 类是为你的内容配合 AirPlay 2 实现增强缓冲的最简单方式。

要实现简单增强缓冲，请完成以下步骤。

1. 创建一个播放器。

```swift
let player = AVQueuePlayer()
```

1. 确定一个指向你想要播放的本地或云端内容的 URL。
2. 用该 URL 创建一个 [AVAsset](avasset.md) 实例，然后用该媒体资源创建一个 [AVPlayerItem](avplayeritem.md) 实例。

```swift
let url = URL(string: "http://www.examplecontenturl.com")!
let asset = AVAsset(url: url)
let item = AVPlayerItem(asset: asset)
```

1. 将播放器条目交给播放器。

```swift
player.insert(item, after: nil)
```

1. 开始播放。

```swift
player.play()
```

## 另请参阅

### 缓冲播放

- [为你的内容实现灵活增强缓冲](implementing-flexible-enhanced-buffering-for-your-content.md) — 将你的 App 配置为使用灵活增强缓冲，以更快的速度将内容流传输到支持隔空播放的设备和受支持的 CarPlay 车辆。
- [为长篇视频 App 集成隔空播放](integrating-airplay-for-long-form-video-apps.md) — 通过为长篇视频播放准备好路由系统，集成隔空播放特性并实现专门的外部播放体验。
