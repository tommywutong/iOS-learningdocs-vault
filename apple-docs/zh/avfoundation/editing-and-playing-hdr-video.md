---
title: 编辑和播放 HDR 视频
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, Xcode 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/editing-and-playing-hdr-video
source_url: 'https://developer.apple.com/documentation/avfoundation/editing-and-playing-hdr-video'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/editing-and-playing-hdr-video.json'
content_hash: 'sha256:74e325aa75d67a60'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [视频效果](video-effects.md)

# 编辑和播放 HDR 视频

<sub>示例代码</sub>

使用 AVFoundation 的 HDR 编辑和播放能力，在你的 App 中支持高动态范围（HDR）视频内容。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC20 场次 [10009: Edit and Play Back HDR Video with AVFoundation](https://developer.apple.com/videos/play/wwdc2020/10009/)。

## 另请参阅

### 内置视频合成

- [调试 AVFoundation 音频混音、组合与视频合成](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md) — 解决创建组合、视频合成和音频混音时的常见问题。
- [AVVideoComposition](avvideocomposition.md) — 一个描述如何在特定时间点合成视频帧的对象。
- [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md) — 合成器执行的一个操作。
- [AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md) — 一个用于修改合成中给定轨道所应用的变换、裁剪和不透明度渐变的对象。
- [AVMutableVideoComposition](avmutablevideocomposition.md) — 可变的视频合成子类。 _(已废弃)_
- [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md) — 可变的视频合成指令子类。 _(已废弃)_
- [AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md) — 一个用于修改可变合成中给定轨道所应用的变换、裁剪和不透明度渐变的对象。 _(已废弃)_

## 下载

- [EditingAndPlayingHDRVideo.zip](https://docs-assets.developer.apple.com/published/690ad4b1d285/EditingAndPlayingHDRVideo.zip)
