---
title: AVAsset
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avasset-async-properties
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset-async-properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset-async-properties.json'
content_hash: 'sha256:bfa7354340e584f0'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media assets](media-assets.md) · [AVPartialAsyncProperty](avpartialasyncproperty.md)

# AVAsset

<sub>API 集合</sub>

asset 的异步属性。

## 主题

### 加载时长与时间信息

- [duration](avpartialasyncproperty/duration.md) — 一个表示该 asset 时长的时间值。
- [providesPreciseDurationAndTiming](avpartialasyncproperty/providesprecisedurationandtiming.md) — 一个布尔值，指示该 asset 是否提供精确的时长和时间信息。
- [minimumTimeOffsetFromLive](avpartialasyncproperty/minimumtimeoffsetfromlive.md) — 一个时间值，指示播放跟随最新直播流内容的紧密程度。

### 加载轨道

- [tracks](avpartialasyncproperty/tracks-48zyw.md) — 一个 asset 包含的媒体轨道。

### 加载轨道组

- [trackGroups](avpartialasyncproperty/trackgroups.md) — 该 asset 包含的轨道组。

### 加载元数据

- [metadata](avpartialasyncproperty/metadata-16qej.md) — 一个 asset 针对所有元数据标识符所包含的元数据项目。
- [commonMetadata](avpartialasyncproperty/commonmetadata-3j3n4.md) — 一个 asset 针对常用元数据标识符所包含的元数据项目。
- [availableMetadataFormats](avpartialasyncproperty/availablemetadataformats-4yiq8.md) — 一个 asset 包含的元数据格式。
- [creationDate](avpartialasyncproperty/creationdate.md) — 一个指示 asset 创建日期的元数据项目。
- [lyrics](avpartialasyncproperty/lyrics.md) — 以适合当前语言环境的语言表示的该 asset 的歌词。

### 加载适用性

- [isPlayable](avpartialasyncproperty/isplayable-45h5v.md) — 一个布尔值，指示 asset 是否包含可播放的内容。
- [isExportable](avpartialasyncproperty/isexportable.md) — 一个布尔值，指示你是否可以使用导出会话导出 asset。
- [isReadable](avpartialasyncproperty/isreadable.md) — 一个布尔值，指示你是否可以使用 asset 读取器提取该 asset 的媒体数据。
- [isComposable](avpartialasyncproperty/iscomposable.md) — 一个布尔值，指示你是否可以在媒体合成中使用该 asset。
- [isCompatibleWithSavedPhotosAlbum](avpartialasyncproperty/iscompatiblewithsavedphotosalbum.md) — 一个布尔值，指示你是否可以将该 asset 写入“已存储的照片”相册。
- [isCompatibleWithAirPlayVideo](avpartialasyncproperty/iscompatiblewithairplayvideo.md) — 一个布尔值，指示该 asset 是否与 AirPlay 视频兼容。

### 加载 asset 偏好设置

- [preferredRate](avpartialasyncproperty/preferredrate.md) — 该 asset 播放其媒体时的速率偏好。
- [preferredTransform](avpartialasyncproperty/preferredtransform-80d13.md) — 该 asset 在呈现或处理期间应用于其视觉内容的变换偏好。
- [preferredVolume](avpartialasyncproperty/preferredvolume-20mb3.md) — 该 asset 播放其声音媒体时的音量偏好。
- [preferredDisplayCriteria](avpartialasyncproperty/preferreddisplaycriteria.md) — 该 asset 为其内容的最佳播放而设的显示模式偏好。

### 加载媒体选择

- [allMediaSelections](avpartialasyncproperty/allmediaselections.md) — 一个 asset 可用的媒体选择。
- [preferredMediaSelection](avpartialasyncproperty/preferredmediaselection.md) — 一个 asset 的媒体选择组的默认媒体选择。
- [availableMediaCharacteristicsWithMediaSelectionOptions](avpartialasyncproperty/availablemediacharacteristicswithmediaselectionoptions.md) — 提供媒体选择选项的媒体特性。

### 加载章节元数据

- [availableChapterLocales](avpartialasyncproperty/availablechapterlocales.md) — 一个 asset 章节元数据的语言环境。

### 加载内容保护

- [hasProtectedContent](avpartialasyncproperty/hasprotectedcontent.md) — 一个布尔值，指示该 asset 是否包含受保护的内容。

### 加载分片支持

- [canContainFragments](avpartialasyncproperty/cancontainfragments.md) — 一个布尔值，指示你是否可以通过分片扩展该 asset。
- [containsFragments](avpartialasyncproperty/containsfragments.md) — 一个布尔值，指示是否至少有一个影片分片扩展了该 asset。
- [overallDurationHint](avpartialasyncproperty/overalldurationhint.md) — 对当前存在或将来可能存在的分片总时长的提示。

## 另请参阅

### 加载属性

- [AVAssetTrack](avassettrack-async-properties.md) — asset 轨道的异步属性。
- [AVURLAsset](avurlasset-async-properties.md) — URL asset 的异步属性。
- [AVFragmentedAsset](avfragmentedasset-async-properties.md) — 分片 asset 的异步属性。
- [AVMetadataItem](avmetadataitem-async-properties.md) — 元数据项目的异步属性。
- [AVComposition](avcomposition-async-properties.md) — 合成的异步属性。
- [AVMutableComposition](avmutablecomposition-async-properties.md) — 可变合成的异步属性。
- [AVMovie](avmovie-async-properties.md) — 影片的异步属性。
- [AVMutableMovie](avmutablemovie-async-properties.md) — 可变影片的异步属性。
- [AVFragmentedMovie](avfragmentedmovie-async-properties.md) — 分片影片的异步属性。
