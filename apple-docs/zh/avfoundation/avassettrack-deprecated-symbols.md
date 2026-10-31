---
title: 已废弃符号
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrack-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack-deprecated-symbols.json'
content_hash: 'sha256:d4324580c143d85d'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media assets](media-assets.md) · [AVAssetTrack](avassettrack.md)

# 已废弃符号

<sub>API 集合</sub>

查看不受支持的符号及其替代方案。

## 概述

[AVAssetTrack](avassettrack.md) 不支持使用其可能阻塞调用线程的同步属性存取方法。作为替代，请使用 [load(_:isolation:)](<avasynchronouskeyvalueloading/load(__isolation_).md>) 方法异步加载 [AVAsyncProperty](avasyncproperty.md) 值。

## 主题

### 访问轨道信息

- [formatDescriptions](avassettrack/formatdescriptions.md) — 轨道引用的媒体样本的格式描述。 _(已废弃)_
- [playable](avassettrack/isplayable.md) — 一个布尔值，指示该轨道在当前环境中是否可播放。 _(已废弃)_
- [decodable](avassettrack/isdecodable.md) — 一个布尔值，指示该轨道在当前环境中是否可解码。 _(已废弃)_
- [enabled](avassettrack/isenabled.md) — 一个布尔值，指示该轨道是否被其容器启用。 _(已废弃)_
- [selfContained](avassettrack/isselfcontained.md) — 一个布尔值，指示该轨道是否仅引用其容器文件内的样本数据。 _(已废弃)_
- [totalSampleDataLength](avassettrack/totalsampledatalength.md) — 该轨道所需的样本数据总字节数。 _(已废弃)_
- [- hasMediaCharacteristic:](<avassettrack/hasmediacharacteristic(__).md>) — 返回一个布尔值，指示该轨道是否引用具有指定媒体特性的媒体。 _(已废弃)_

### 访问时间信息

- [timeRange](avassettrack/timerange.md) — 该轨道在 asset 整体时间线中的时间范围。 _(已废弃)_
- [naturalTimeScale](avassettrack/naturaltimescale.md) — 轨道引用的媒体的自然时间标度。 _(已废弃)_
- [estimatedDataRate](avassettrack/estimateddatarate.md) — 轨道引用的媒体的估计数据速率（以位/秒为单位）。 _(已废弃)_

### 访问语言支持

- [languageCode](avassettrack/languagecode.md) — 该轨道的语言代码。 _(已废弃)_
- [extendedLanguageTag](avassettrack/extendedlanguagetag.md) — 该轨道的语言标签。 _(已废弃)_

### 访问视觉特性

- [naturalSize](avassettrack/naturalsize.md) — 轨道引用的媒体数据的自然尺寸。 _(已废弃)_
- [preferredTransform](avassettrack/preferredtransform.md) — 该轨道在呈现或处理期间应用于其视觉内容的变换偏好。 _(已废弃)_

### 访问声音特性

- [preferredVolume](avassettrack/preferredvolume.md) — 该轨道播放其声音媒体时的音量偏好。 _(已废弃)_
- [hasAudioSampleDependencies](avassettrack/hasaudiosampledependencies.md) — 一个布尔值，指示该轨道是否存在样本依赖。 _(已废弃)_

### 访问基于帧的特性

- [nominalFrameRate](avassettrack/nominalframerate.md) — 该轨道的帧率（以帧/秒为单位）。 _(已废弃)_
- [minFrameDuration](avassettrack/minframeduration.md) — 该轨道各帧的最小时长。 _(已废弃)_
- [requiresFrameReordering](avassettrack/requiresframereordering.md) — 一个布尔值，指示轨道中的样本是否可能具有不同的呈现时间戳和解码时间戳。 _(已废弃)_

### 访问元数据

- [metadata](avassettrack/metadata.md) — 针对所有有值的元数据标识符的元数据项目数组。 _(已废弃)_
- [commonMetadata](avassettrack/commonmetadata.md) — 针对所有有值的常用元数据键的元数据项目数组。 _(已废弃)_
- [availableMetadataFormats](avassettrack/availablemetadataformats.md) — 该轨道可用的元数据格式数组。 _(已废弃)_
- [- metadataForFormat:](<avassettrack/metadata(forformat_).md>) — 返回轨道针对指定格式所包含的元数据项目。 _(已废弃)_

### 访问轨道段

- [segments](avassettrack/segments.md) — 从轨道的媒体样本到其时间线的时间映射。 _(已废弃)_
- [- segmentForTrackTime:](<avassettrack/segment(fortracktime_).md>) — 检索一个目标时间范围包含指定轨道时间或与之最接近的轨道段。 _(已废弃)_
- [- samplePresentationTimeForTrackTime:](<avassettrack/samplepresentationtime(fortracktime_).md>) — 通过相应的时间映射转换指定的轨道时间，并返回得到的样本呈现时间。 _(已废弃)_

### 访问轨道关联

- [availableTrackAssociationTypes](avassettrack/availabletrackassociationtypes.md) — 该轨道用于与其他轨道建立关联的关联类型数组。 _(已废弃)_
- [- associatedTracksOfType:](<avassettrack/associatedtracks(oftype_).md>) — 返回具有指定关联类型的关联轨道数组。 _(已废弃)_

### 创建样本游标

- [canProvideSampleCursors](avassettrack/canprovidesamplecursors.md) — 一个布尔值，指示该轨道能否提供样本游标实例来遍历其媒体样本并发现信息。 _(已废弃)_
