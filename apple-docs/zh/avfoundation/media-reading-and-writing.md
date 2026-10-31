---
title: 媒体读写
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/media-reading-and-writing
source_url: 'https://developer.apple.com/documentation/avfoundation/media-reading-and-writing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/media-reading-and-writing.json'
content_hash: 'sha256:a8fabdfc2f803a58'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 媒体读写

<sub>API 集合</sub>

从视频中读取图像、导出为其他格式，以及对媒体数据执行样本级的读取和写入。

## 主题

### 媒体导出

- [将视频导出为其他格式](exporting-video-to-alternative-formats.md) — 将现有的影片文件转换为不同的格式。
- [AVAssetExportSession](avassetexportsession.md) — 一个使用导出预设以你指定的格式导出媒体资源的对象。

### 计划导出

- [AVAssetWritingPlanner](avassetwritingplanner.md) — AVAssetWritingPlanner 编排媒体文件的增量写入。 _(beta)_
- [AVAssetWritingPlannerProgress](avassetwritingplannerprogress.md) — AVAssetWritingPlannerProgress 跟踪 AVAssetWritingPlanner 会话中每个轨道的增量写入进度。 _(beta)_
- [AVAssetTrackPlan](avassettrackplan.md) — AVAssetTrackPlan 保存有关轨道的信息，以及它在增量写入会话中应如何分段和执行。 _(beta)_
- [AVAssetVideoTrackPlan](avassetvideotrackplan.md) — AVAssetVideoTrackPlan 保存有关轨道的信息，以及它在增量写入会话中应如何分段和执行。 _(beta)_
- [AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md) — AVPlannedSegmentConfiguration 描述由 AVAssetWritingPlanner 执行的增量写入会话中计划分段的要求。从 Swift 中使用的该类型子类必须满足 Sendable 类型的要求。 _(beta)_
- [AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md) — AVPlannedVideoSegmentConfiguration 描述由 AVAssetWritingPlanner 执行的增量写入会话中计划视频分段的要求。 _(beta)_
- [AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md) — AVPlannedSegmentWritingRequest 包含来自 AVAssetWritingPlanner 的请求，要求客户端代码写入一个增量轨道分段。 _(beta)_
- [AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md) — AVPlannedVideoSegmentWritingRequest 包含来自 AVAssetWritingPlanner 的请求，要求客户端代码写入一个经过压缩的增量视频轨道分段。 _(beta)_

### 图像生成

- [从视频媒体资源创建图像](creating-images-from-a-video-asset.md) — 通过从视频的帧生成图像，显示媒体时间线上特定时间的图像。
- [AVAssetImageGenerator](avassetimagegenerator.md) — 一个从视频媒体资源生成图像的对象。

### 媒体读取

- [读取多视图 3D 视频文件](reading-multiview-3d-video-files.md) — 通过读取单独的视频帧，从多视图高效视频编码（MV-HEVC）格式文件渲染左眼和右眼的单一图像。
- [AVAssetReader](avassetreader.md) — 一个从媒体资源读取媒体数据的对象。
- [AVAssetReaderOutput](avassetreaderoutput.md) — 一个抽象类，定义了从媒体资源读取器读取媒体样本的接口。
- [AVAssetReaderTrackOutput](avassetreadertrackoutput.md) — 一个从媒体资源的单个轨道读取媒体数据的对象。
- [AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md) — 一个读取混音结果音频样本的对象，混音来自一个或多个轨道的音频。
- [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md) — 一个从媒体资源的一个或多个轨道读取合成视频帧的对象。
- [AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md) — 一个从媒体资源轨道读取样本引用的对象。
- [AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md) — 一个为媒体资源轨道创建定时元数据组对象的对象。 _(已废弃)_

### 媒体写入

- [将投影视频转换为 Apple Projected Media Profile](converting-projected-video-to-apple-projected-media-profile.md) — 将具有等距圆柱投影或半等距圆柱投影的内容转换为 APMP。
- [将并排 3D 视频转换为多视图 HEVC 和空间视频](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md) — 通过将现有的 3D HEVC 文件转换为多视图 HEVC 格式来创建适用于 visionOS 的视频内容，可选择添加空间元数据来创建空间视频。
- [向影片文件添加显示遮罩矩形元数据轨道](adding-a-display-mask-rectangle-metadata-track-to-a-movie-file.md) — 使用定时显示遮罩矩形元数据显示视频的特定区域。
- [为 HTTP 实时流写入分片 MPEG-4 文件](writing-fragmented-mpeg-4-files-for-http-live-streaming.md) — 通过将影片文件转换为一系列分片 MPEG-4 文件来创建 HTTP 实时流呈现。
- [使用空间元数据创建空间照片和视频](../imageio/creating-spatial-photos-and-videos-with-spatial-metadata.md) — 向立体照片和视频添加空间元数据，以创建可在 Apple Vision Pro 上观看的空间媒体。
- [用视频色彩信息标记媒体](tagging-media-with-video-color-information.md) — 在写入和转码媒体时检查并设置视频色彩空间信息。
- [评估 App 的视频色彩](evaluating-an-app-s-video-color.md) — 使用测试图样、视频测试设备和光测量仪器检查你的 App 中视频的色彩再现。
- [AVOutputSettingsAssistant](avoutputsettingsassistant.md) — 一个构建音频和视频输出设置字典的对象。
- [AVAssetWriter](avassetwriter.md) — 一个将媒体数据写入容器文件的对象。
- [AVAssetWriterInput](avassetwriterinput.md) — 一个将媒体样本追加到媒体资源写入器输出文件中轨道的对象。
- [AVAssetWriterInputPixelBufferAdaptor](avassetwriterinputpixelbufferadaptor.md) — 一个将视频样本追加到媒体资源写入器输入的对象。 _(已废弃)_
- [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md) — 一个将带标签缓冲区组追加到媒体资源写入器输入的对象。 _(已废弃)_
- [AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md) — 一个将定时元数据组追加到媒体资源写入器输入的对象。 _(已废弃)_
- [AVAssetWriterInputGroup](avassetwriterinputgroup.md) — 一组带有轨道的输入，这些轨道在播放或处理时彼此互斥。

### 字幕

- [字幕创作](caption-authoring.md) — 以行业标准格式创建字幕。

## 另请参阅

### 通用

- [媒体资源](media-assets.md) — 从文件和流加载媒体资源，以检查它们的属性、轨道和内嵌元数据。
- [媒体类型与实用工具](media-types-and-utilities.md) — 识别 AVFoundation 支持的内容类型和文件格式。
- [视频设置](video-settings.md) — 使用标准的键和值常量配置视频处理设置。
- [音频设置](audio-settings.md) — 使用标准的键和值常量配置音频处理设置。
