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
doc_path: /documentation/avfoundation/avasset-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset-deprecated-symbols.json'
content_hash: 'sha256:7b3c08d57bed415a'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media assets](media-assets.md) · [AVAsset](avasset.md)

# 已废弃符号

<sub>API 集合</sub>

查看不受支持的符号及其替代方案。

## 概述

[AVAsset](avasset.md) 不支持使用其可能阻塞调用线程的同步属性存取方法。作为替代，请使用 [load(_:isolation:)](<avasynchronouskeyvalueloading/load(__isolation_).md>) 方法异步加载 [AVAsyncProperty](avasyncproperty.md) 值。

## 主题

### 访问时长与时间信息

- [duration](avasset/duration.md) — 一个时间值，指示该 asset 的时长。 _(已废弃)_
- [providesPreciseDurationAndTiming](avasset/providesprecisedurationandtiming.md) — 一个布尔值，指示该 asset 是否提供精确的时长和时间信息。 _(已废弃)_
- [minimumTimeOffsetFromLive](avasset/minimumtimeoffsetfromlive.md) — 一个时间值，指示播放跟随最新直播流内容的紧密程度。 _(已废弃)_

### 访问轨道

- [tracks](avasset/tracks.md) — 该 asset 包含的轨道。 _(已废弃)_
- [- trackWithTrackID:](<avasset/track(withtrackid_).md>) — 返回包含指定标识符的轨道。 _(已废弃)_
- [- tracksWithMediaType:](<avasset/tracks(withmediatype_).md>) — 返回包含指定类型媒体的轨道。 _(已废弃)_
- [- tracksWithMediaCharacteristic:](<avasset/tracks(withmediacharacteristic_).md>) — 返回与指定媒体特性匹配的 asset 轨道数组。 _(已废弃)_
- [- unusedTrackID](<avasset/unusedtrackid().md>) — 返回一个该 asset 中没有其他轨道使用的标识符。 _(已废弃)_

### 访问轨道组

- [trackGroups](avasset/trackgroups.md) — 该 asset 包含的轨道组。 _(已废弃)_

### 访问元数据

- [metadata](avasset/metadata.md) — 针对所有有可用值的元数据标识符的元数据项目数组。 _(已废弃)_
- [commonMetadata](avasset/commonmetadata.md) — 该 asset 针对提供值的常用元数据标识符所包含的元数据项目。 _(已废弃)_
- [availableMetadataFormats](avasset/availablemetadataformats.md) — 该 asset 包含的元数据格式。 _(已废弃)_
- [- metadataForFormat:](<avasset/metadata(forformat_).md>) — 从具有指定格式的容器返回一个元数据项目数组。 _(已废弃)_
- [creationDate](avasset/creationdate.md) — 一个指示该 asset 创建日期的元数据项目。 _(已废弃)_
- [lyrics](avasset/lyrics.md) — 以适合当前语言环境的语言表示的该 asset 的歌词。 _(已废弃)_

### 访问适用性

- [playable](avasset/isplayable.md) — 一个布尔值，指示该 asset 是否包含可播放的内容。 _(已废弃)_
- [exportable](avasset/isexportable.md) — 一个布尔值，指示你是否可以使用导出会话导出该 asset。 _(已废弃)_
- [readable](avasset/isreadable.md) — 一个布尔值，指示你是否可以使用 asset 读取器提取该 asset 的媒体数据。 _(已废弃)_
- [composable](avasset/iscomposable.md) — 一个布尔值，指示你是否可以将该 asset 用作合成轨道的一个片段。 _(已废弃)_
- [compatibleWithAirPlayVideo](avasset/iscompatiblewithairplayvideo.md) — 一个布尔值，指示该 asset 是否与 AirPlay 视频兼容。 _(已废弃)_
- [compatibleWithSavedPhotosAlbum](avasset/iscompatiblewithsavedphotosalbum.md) — 一个布尔值，指示你是否可以将该 asset 写入“已存储的照片”相册。 _(已废弃)_

### 访问 asset 偏好设置

- [preferredRate](avasset/preferredrate.md) — 该 asset 播放其媒体时的速率偏好。 _(已废弃)_
- [preferredVolume](avasset/preferredvolume.md) — 该 asset 播放其声音媒体时的音量偏好。 _(已废弃)_
- [preferredTransform](avasset/preferredtransform.md) — 该 asset 在呈现或处理期间应用于其视觉内容的变换偏好。 _(已废弃)_
- [preferredDisplayCriteria](avasset/preferreddisplaycriteria.md) — 该 asset 为其内容的最佳播放而设的显示模式偏好。 _(已废弃)_
- [preferredMediaSelection](avasset/preferredmediaselection.md) — 该 asset 的媒体选择组的默认媒体选择。 _(已废弃)_

### 访问媒体选择

- [allMediaSelections](avasset/allmediaselections.md) — 该 asset 可用的媒体选择数组。 _(已废弃)_
- [availableMediaCharacteristicsWithMediaSelectionOptions](avasset/availablemediacharacteristicswithmediaselectionoptions.md) — 有可用媒体选择选项的媒体特性数组。 _(已废弃)_
- [- mediaSelectionGroupForMediaCharacteristic:](<avasset/mediaselectiongroup(formediacharacteristic_).md>) — 返回一个媒体选择组，其中包含一个或多个具有指定媒体特性的选项。 _(已废弃)_

### 访问章节元数据

- [availableChapterLocales](avasset/availablechapterlocales.md) — 该 asset 章节元数据的语言环境。 _(已废弃)_
- [- chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:](<avasset/chaptermetadatagroups(withtitlelocale_containingitemswithcommonkeys_).md>) — 返回一个章节数组，其中包含指定标题语言环境和常用键。 _(已废弃)_
- [- chapterMetadataGroupsBestMatchingPreferredLanguages:](<avasset/chaptermetadatagroups(bestmatchingpreferredlanguages_).md>) — 返回一个章节数组，其语言环境与首选语言列表最匹配。 _(已废弃)_

### 访问内容保护

- [hasProtectedContent](avasset/hasprotectedcontent.md) — 一个布尔值，指示该 asset 是否包含受保护的内容。 _(已废弃)_

### 访问分片支持

- [canContainFragments](avasset/cancontainfragments.md) — 一个布尔值，指示你是否可以通过分片扩展该 asset。 _(已废弃)_
- [containsFragments](avasset/containsfragments.md) — 一个布尔值，指示是否至少有一个影片分片扩展了该 asset。 _(已废弃)_
- [overallDurationHint](avasset/overalldurationhint.md) — 当前存在或将来可能存在的分片的总时长。 _(已废弃)_

### 检查视觉特性

- [naturalSize](avasset/naturalsize.md) — 该 asset 视觉部分的编码或创作尺寸。 _(已废弃)_
