---
title: QuickTime 影片
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/quicktime-movies
source_url: 'https://developer.apple.com/documentation/avfoundation/quicktime-movies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/quicktime-movies.json'
content_hash: 'sha256:ad42a4263d34e7fd'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# QuickTime 影片

<sub>API 集合</sub>

访问 QuickTime 影片文件的内容，并对其媒体轨道执行样本级编辑。

## 主题

### 影片

- [AVMovie](avmovie.md) — 一个表示视听容器的对象，该容器符合 QuickTime 影片文件格式或 MPEG-4 等相关格式。
- [AVMovieTrack](avmovietrack.md) — 影片中符合 QuickTime 或 ISO 基础媒体文件格式的轨道。

### 可变影片

- [AVMutableMovie](avmutablemovie.md) — 一个表示视听容器的可变对象，该容器符合 QuickTime 影片文件格式或 MPEG-4 等相关格式。
- [AVMutableMovieTrack](avmutablemovietrack.md) — 一个符合 QuickTime 或 ISO 基础媒体文件格式的可变轨道。

### 分片影片

- [AVFragmentedMovie](avfragmentedmovie.md) — 一个表示分片影片文件的对象。
- [AVFragmentedMovieTrack](avfragmentedmovietrack.md) — 一个表示分片影片中轨道的对象。
- [AVFragmentedMovieMinder](avfragmentedmovieminder.md) — 一个检查分片影片是否追加了额外影片分片的对象。
- [AVFragmentMinding](avfragmentminding.md) — 一个定义媒体资源是否支持分片看护（fragment minding）的协议。

### 样本光标

- [AVSampleCursor](avsamplecursor.md) — 一个提供光标当前位置处媒体样本信息的对象。
- [AVSampleCursorSyncInfo](avsamplecursorsyncinfo.md) — 一个结构，描述在重新同步解码器时需要考虑的媒体样本特性。
- [AVSampleCursorDependencyInfo](avsamplecursordependencyinfo.md) — 一个用于描述媒体样本与同一样本序列中其他媒体样本之间依赖关系的值。
- [AVSampleCursorAudioDependencyInfo](avsamplecursoraudiodependencyinfo.md) — 一个描述音频样本独立可解码性的结构。
- [AVSampleCursorStorageRange](avsamplecursorstoragerange.md) — 一个指示媒体样本或其区块（chunk）的存储偏移量和长度的结构。
- [AVSampleCursorChunkInfo](avsamplecursorchunkinfo.md) — 一个提供媒体样本区块信息的值。

### 媒体数据存储

- [AVMediaDataStorage](avmediadatastorage.md) — 一个表示媒体样本数据存储文件的对象。

## 另请参阅

### 编辑

- [组合媒体资源](composite-assets.md) — 将来自多个媒体资源的轨道和轨道分段组合成一个可播放或处理的组合媒体资源。
- [视频效果](video-effects.md) — 定义标准的视频过渡效果、将图层动画与媒体时间同步，以及创建自定义视频合成器。
- [音频混音](audio-mixing.md) — 定义如何在媒体资源的时长范围内混合多个音频轨道的音量。
