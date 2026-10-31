---
title: 创建无缝的多视图播放体验
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, Xcode 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/creating-a-seamless-multiview-playback-experience
source_url: 'https://developer.apple.com/documentation/avfoundation/creating-a-seamless-multiview-playback-experience'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/creating-a-seamless-multiview-playback-experience.json'
content_hash: 'sha256:e1f03c6f197bafbb'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体播放](media-playback.md)

# 创建无缝的多视图播放体验

<sub>示例代码</sub>

使用 AVFoundation 和 AVRouting 框架构建高级的多视图播放体验。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC25 场次 302：[Create a seamless multiview playback experience](https://developer.apple.com/videos/play/wwdc2025/302)。

### 配置示例代码项目

要运行本示例，你需要：

- 一台运行 iOS 26 或更高版本的 iOS 设备，或者
- 一台运行 tvOS 26 或更高版本的 tvOS 设备

## 另请参阅

### 播放控制

- [在 SwiftUI 中观察播放状态](observing-playback-state-in-swiftui.md) — 让你的用户界面与播放对象的状态变化保持同步。
- [控制播放器的播放行为](controlling-the-transport-behavior-of-a-player.md) — 播放、暂停媒体呈现，并在其中跳转。
- [AVPlayer](avplayer.md) — 一个提供控制播放器播放行为的界面的对象。
- [AVPlayerItem](avplayeritem.md) — 一个为资产在播放期间的时间和呈现状态建模的对象。
- [AVPlayerItemTrack](avplayeritemtrack.md) — 一个表示资产轨道在播放期间的呈现状态的对象。
- [AVQueuePlayer](avqueueplayer.md) — 一个按顺序播放多个播放器条目的对象。
- [AVPlayerLooper](avplayerlooper.md) — 一个使用队列播放器循环播放媒体内容的对象。

## 下载

- [CreatingASeamlessMultiviewPlaybackExperience.zip](https://docs-assets.developer.apple.com/published/4bd19326ff2f/CreatingASeamlessMultiviewPlaybackExperience.zip)
