---
title: 视频效果
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/video-effects
source_url: 'https://developer.apple.com/documentation/avfoundation/video-effects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/video-effects.json'
content_hash: 'sha256:71be0d410e8281f3'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 视频效果

<sub>API 集合</sub>

定义标准的视频过渡效果、将图层动画与媒体时间同步，以及创建自定义视频合成器。

## 主题

### Core Animation 集成

- [AVVideoCompositionCoreAnimationTool](avvideocompositioncoreanimationtool.md) — 一个用于将 Core Animation 纳入视频合成的对象。

### 内置视频合成

- [编辑和播放 HDR 视频](editing-and-playing-hdr-video.md) — 使用 AVFoundation 的 HDR 编辑和播放能力，在你的 App 中支持高动态范围（HDR）视频内容。
- [调试 AVFoundation 音频混音、组合与视频合成](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md) — 解决创建组合、视频合成和音频混音时的常见问题。
- [AVVideoComposition](avvideocomposition.md) — 一个描述如何在特定时间点合成视频帧的对象。
- [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md) — 合成器执行的一个操作。
- [AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md) — 一个用于修改合成中给定轨道所应用的变换、裁剪和不透明度渐变的对象。
- [AVMutableVideoComposition](avmutablevideocomposition.md) — 可变的视频合成子类。 _(已废弃)_
- [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md) — 可变的视频合成指令子类。 _(已废弃)_
- [AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md) — 一个用于修改可变合成中给定轨道所应用的变换、裁剪和不透明度渐变的对象。 _(已废弃)_

### 自定义视频合成

- [使用自定义视频合成器处理空间视频](processing-spatial-video-with-a-custom-video-compositor.md) — 创建一个自定义视频合成器，用于编辑空间视频以供播放和导出。
- [AVVideoCompositing](avvideocompositing.md) — 一个定义自定义视频合成器必须实现的方法的协议。

## 另请参阅

### 编辑

- [组合媒体资源](composite-assets.md) — 将来自多个媒体资源的轨道和轨道分段组合成一个可播放或处理的组合媒体资源。
- [QuickTime 影片](quicktime-movies.md) — 访问 QuickTime 影片文件的内容，并对其媒体轨道执行样本级编辑。
- [音频混音](audio-mixing.md) — 定义如何在媒体资源的时长范围内混合多个音频轨道的音量。
