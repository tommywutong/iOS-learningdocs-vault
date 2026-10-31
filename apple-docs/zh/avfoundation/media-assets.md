---
title: 媒体资源
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/media-assets
source_url: 'https://developer.apple.com/documentation/avfoundation/media-assets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/media-assets.json'
content_hash: 'sha256:6f88d0064b2fb40b'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 媒体资源

<sub>API 集合</sub>

从文件和流加载媒体资源，以检查它们的属性、轨道和内嵌元数据。

## 主题

### 基础

- [异步加载媒体数据](loading-media-data-asynchronously.md) — 使用语言级并发特性高效加载媒体数据，构建响应迅速的 App。

### 资源

- [AVAsset](avasset.md) — 一个为定时视听媒体建模的对象。
- [AVURLAsset](avurlasset.md) — 表示位于本地或远程 URL 处媒体的一种资源。
- [AVAssetTrack](avassettrack.md) — 一个为资源包含的媒体轨道建模的对象。
- [AVAssetTrackSegment](avassettracksegment.md) — 一个表示资源轨道时间范围片段的对象。
- [AVAssetTrackGroup](avassettrackgroup.md) — 资源中一组相关的轨道。

### 元数据

- [检索媒体元数据](retrieving-media-metadata.md) — 为媒体资源及其轨道加载描述性元数据。
- [AVMetadataItem](avmetadataitem.md) — 视听资产或其某个轨道的元数据项。
- [AVMutableMetadataItem](avmutablemetadataitem.md) — 视听资产或其某个轨道的可变元数据项。
- [AVMetadataIdentifier](avmetadataidentifier.md) — 一个为元数据格式定义标识符的结构体。
- [AVMetadataKey](avmetadatakey.md) — 一个定义元数据键的结构体。
- [AVMetadataKeySpace](avmetadatakeyspace.md) — 一个定义元数据键空间的结构体。
- [AVMetadataExtraAttributeKey](avmetadataextraattributekey.md) — 一个为额外元数据属性定义键的结构体。
- [AVMetadataFormat](avmetadataformat.md) — 一个定义元数据格式的结构体。
- [AVMetadataItemFilter](avmetadataitemfilter.md) — 一个从元数据项中筛选选定信息的对象。

### 属性加载

- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md) — 一个定义异步加载媒体数据接口的协议。
- [AVAsyncProperty](avasyncproperty.md) — 一种约束其类型和值的异步属性。
- [AVPartialAsyncProperty](avpartialasyncproperty.md) — 一种约束其类型的异步属性。
- [AVAnyAsyncProperty](avanyasyncproperty.md) — 异步属性的基类。

### 分段资源

- [AVFragmentedAsset](avfragmentedasset.md) — 一种资源，其时长可由系统扩展，而无需修改其现有媒体数据。
- [AVFragmentedAssetTrack](avfragmentedassettrack.md) — 一个提供轨道级接口以检查分段资源媒体轨道的对象。
- [AVFragmentedAssetMinder](avfragmentedassetminder.md) — 一个定期检查系统是否向分段资源添加新片段的对象。
- [AVFragmentMinding](avfragmentminding.md) — 一个定义资源是否支持片段关注（fragment minding）的协议。

## 另请参阅

### 通用

- [媒体读取与写入](media-reading-and-writing.md) — 从视频中读取图像、导出为其他格式，以及对媒体数据执行样本级读取和写入。
- [媒体类型与实用工具](media-types-and-utilities.md) — 识别 AVFoundation 支持的内容类型和文件格式。
- [视频设置](video-settings.md) — 使用标准的键和值常量来配置视频处理设置。
- [音频设置](audio-settings.md) — 使用标准的键和值常量来配置音频处理设置。
