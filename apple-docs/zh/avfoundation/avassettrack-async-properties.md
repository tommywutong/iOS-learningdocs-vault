---
title: AVAssetTrack
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrack-async-properties
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack-async-properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack-async-properties.json'
content_hash: 'sha256:e07ae082b067741f'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media assets](media-assets.md) · [AVPartialAsyncProperty](avpartialasyncproperty.md)

# AVAssetTrack

<sub>API 集合</sub>

asset 轨道的异步属性。

## 主题

### 加载轨道信息

- [totalSampleDataLength](avpartialasyncproperty/totalsampledatalength.md) — 该轨道所需的样本数据总字节数。
- [formatDescriptions](avpartialasyncproperty/formatdescriptions.md) — 轨道引用的媒体样本的格式描述。
- [isDecodable](avpartialasyncproperty/isdecodable.md) — 一个布尔值，指示该轨道在当前环境中是否可解码。
- [isEnabled](avpartialasyncproperty/isenabled.md) — 一个布尔值，指示该轨道是否处于启用状态。
- [isPlayable](avpartialasyncproperty/isplayable-6txa5.md) — 一个布尔值，指示该轨道在当前环境中是否可播放。
- [mediaCharacteristics](avpartialasyncproperty/mediacharacteristics.md) — 该轨道的媒体特性。
- [isSelfContained](avpartialasyncproperty/isselfcontained.md) — 一个布尔值，指示该轨道是否仅引用其容器文件内的样本数据。

### 加载时间信息

- [timeRange](avpartialasyncproperty/timerange.md) — 该轨道在 asset 整体时间线中的时间范围。
- [naturalTimeScale](avpartialasyncproperty/naturaltimescale.md) — 轨道引用的媒体的自然时间标度。
- [estimatedDataRate](avpartialasyncproperty/estimateddatarate.md) — 轨道引用的媒体的估计数据速率（以位/秒为单位）。

### 加载语言支持

- [languageCode](avpartialasyncproperty/languagecode.md) — 该轨道的语言代码。
- [extendedLanguageTag](avpartialasyncproperty/extendedlanguagetag.md) — 该轨道的语言标签。

### 加载视觉特性

- [naturalSize](avpartialasyncproperty/naturalsize.md) — 轨道引用的媒体数据的自然尺寸。
- [preferredTransform](avpartialasyncproperty/preferredtransform-90jdn.md) — 该轨道在呈现或处理期间应用于其视觉内容的变换偏好。

### 加载声音特性

- [preferredVolume](avpartialasyncproperty/preferredvolume-8q2yt.md) — 该轨道播放其声音媒体时的音量偏好。
- [hasAudioSampleDependencies](avpartialasyncproperty/hasaudiosampledependencies.md) — 一个布尔值，指示该轨道是否存在样本依赖。

### 加载基于帧的特性

- [nominalFrameRate](avpartialasyncproperty/nominalframerate.md) — 该轨道的帧率（以帧/秒为单位）。
- [minFrameDuration](avpartialasyncproperty/minframeduration.md) — 该轨道各帧的最小时长。
- [requiresFrameReordering](avpartialasyncproperty/requiresframereordering.md) — 一个布尔值，指示轨道中的样本是否可能具有不同的呈现时间戳和解码时间戳。

### 加载元数据

- [metadata](avpartialasyncproperty/metadata-6e14c.md) — 针对所有有值的元数据标识符的元数据项目数组。
- [availableMetadataFormats](avpartialasyncproperty/availablemetadataformats-5p9xg.md) — 该轨道可用的元数据格式数组。
- [commonMetadata](avpartialasyncproperty/commonmetadata-73m58.md) — 针对所有有值的常用元数据键的元数据项目数组。

### 加载轨道段

- [segments](avpartialasyncproperty/segments.md) — 从轨道的媒体样本到其时间线的时间映射。

### 加载轨道关联

- [availableTrackAssociationTypes](avpartialasyncproperty/availabletrackassociationtypes.md) — 该轨道用于与其他轨道建立关联的关联类型数组。

### 创建样本游标

- [canProvideSampleCursors](avpartialasyncproperty/canprovidesamplecursors.md) — 一个布尔值，指示该轨道能否提供样本游标实例来遍历其媒体样本并发现信息。

## 另请参阅

### 加载属性

- [AVAsset](avasset-async-properties.md) — asset 的异步属性。
- [AVURLAsset](avurlasset-async-properties.md) — URL asset 的异步属性。
- [AVFragmentedAsset](avfragmentedasset-async-properties.md) — 分片 asset 的异步属性。
- [AVMetadataItem](avmetadataitem-async-properties.md) — 元数据项目的异步属性。
- [AVComposition](avcomposition-async-properties.md) — 合成的异步属性。
- [AVMutableComposition](avmutablecomposition-async-properties.md) — 可变合成的异步属性。
- [AVMovie](avmovie-async-properties.md) — 影片的异步属性。
- [AVMutableMovie](avmutablemovie-async-properties.md) — 可变影片的异步属性。
- [AVFragmentedMovie](avfragmentedmovie-async-properties.md) — 分片影片的异步属性。
