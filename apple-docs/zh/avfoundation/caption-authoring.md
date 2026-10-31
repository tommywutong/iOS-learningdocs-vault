---
title: 字幕创作
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/caption-authoring
source_url: 'https://developer.apple.com/documentation/avfoundation/caption-authoring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/caption-authoring.json'
content_hash: 'sha256:c724d946b3bf2142'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体读写](media-reading-and-writing.md)

# 字幕创作

<sub>API 集合</sub>

以行业标准格式创建字幕。

## 主题

### 字幕

- [AVCaption](avcaption.md) — 一个表示要在某个时间范围内呈现的文本的对象。
- [AVMutableCaption](avmutablecaption.md) — 一个用于创建新字幕的可变字幕子类。

### 区域

- [AVCaptionRegion](avcaptionregion.md) — 一个表示系统呈现字幕所在区域的对象。
- [AVMutableCaptionRegion](avmutablecaptionregion.md) — 一个用于创建新字幕区域的可变字幕区域子类。

### 分组

- [AVCaptionGroup](avcaptiongroup.md) — 一个表示在时间上相交的零个或多个字幕的对象。
- [AVCaptionGrouper](avcaptiongrouper.md) — 一个分析字幕对象在时间上的重叠情况，为每段并发字幕创建字幕分组的对象。

### 呈现

- [AVCaptionRenderer](avcaptionrenderer.md) — 一个渲染字幕以在特定时间显示的对象。

### 读取与写入

- [AVAssetReaderOutputCaptionAdaptor](avassetreaderoutputcaptionadaptor.md) — 一个从包含定时文本的媒体资源轨道读取字幕组对象的对象。 _(已废弃)_
- [AVAssetWriterInputCaptionAdaptor](avassetwriterinputcaptionadaptor.md) — 一个将字幕追加到媒体资源写入器输入的对象。 _(已废弃)_

### 转换与验证

- [AVCaptionSettingsKey](avcaptionsettingskey.md) — 一个定义字典键以配置字幕转换器和验证器的结构。
- [AVCaptionFormatConformer](avcaptionformatconformer.md) — 一个将规范字幕转换为特定格式的对象。
- [AVCaptionConversionValidator](avcaptionconversionvalidator.md) — 一个为转换操作验证字幕的对象。
