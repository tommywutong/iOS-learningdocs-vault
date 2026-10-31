---
title: 组合媒体资源
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/composite-assets
source_url: 'https://developer.apple.com/documentation/avfoundation/composite-assets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/composite-assets.json'
content_hash: 'sha256:408ad4a188699d93'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 组合媒体资源

<sub>API 集合</sub>

将来自多个媒体资源的轨道和轨道分段组合成一个可播放或处理的组合媒体资源。

## 主题

### 组合

- [AVComposition](avcomposition.md) — 一个将来自多个媒体资源的媒体组合并编排为单一组合媒体资源的对象，可供播放或处理。
- [AVCompositionTrack](avcompositiontrack.md) — 组合中呈现单一类型媒体的轨道。
- [AVCompositionTrackSegment](avcompositiontracksegment.md) — 一种轨道分段，将来自源媒体轨道的时间映射到组合轨道。

### 可变组合

- [AVMutableComposition](avmutablecomposition.md) — 一个用于从现有媒体资源创建新组合的对象。
- [AVMutableCompositionTrack](avmutablecompositiontrack.md) — 组合中的可变轨道，用于插入、移除和缩放轨道分段，而不会影响它们的底层表示。

## 另请参阅

### 编辑

- [QuickTime 影片](quicktime-movies.md) — 访问 QuickTime 影片文件的内容，并对其媒体轨道执行样本级编辑。
- [视频效果](video-effects.md) — 定义标准的视频过渡效果、将图层动画与媒体时间同步，以及创建自定义视频合成器。
- [音频混音](audio-mixing.md) — 定义如何在媒体资源的时长范围内混合多个音频轨道的音量。
