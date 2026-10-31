---
title: 评估 App 的视频色彩
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/evaluating-an-app-s-video-color
source_url: 'https://developer.apple.com/documentation/avfoundation/evaluating-an-app-s-video-color'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/evaluating-an-app-s-video-color.json'
content_hash: 'sha256:e9fb03663a0dc6c7'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体读写](media-reading-and-writing.md)

# 评估 App 的视频色彩

使用测试图样、视频测试设备和光测量仪器检查你的 App 中视频的色彩再现。

## 概述

AVFoundation 会在播放期间自动对视频应用色彩管理。ColorSync 会创建一个色彩变换，在视频的色彩空间（由媒体中的色彩标签指定）与你的显示器的特定色度和伽马特性之间提供色彩匹配。

ColorSync 使用显示器的 ICC 描述文件来获取其色度和伽马特性。然后，它使用感知渲染意图执行色彩匹配，缩放视频颜色，使其适配显示器指定的目标色域。AVFoundation 会在视频播放期间实时地对每一帧的每个像素应用这一色彩变换，确保原始视频的色彩保真度。

> [!note] 注意
> 观众通常在光线昏暗的观看环境（例如客厅）中观看基于广播标准的视频。播放期间应用的色彩管理会降低对比度，以便在更明亮的观看条件下观看视频时保持正确的色调。

### 管理色彩再现

在播放期间，色彩管理过程会更改视频文件中编码的像素值，使其在显示器上呈现得与原始内容一致。由于这种色彩管理，[数字测色计 App](https://support.apple.com/guide/digital-color-meter/welcome/mac) 报告的显示缓冲区值与视频文件中编码的实际像素不同。此外，如果两个看似相同的显示器具有不同的显示器描述文件，「数字测色计」App 可能会在它们之间报告不相等的像素值。

你可以使用多种技术来验证系统是否在你的视频中正确管理色彩：

- 使用测试图样文件来评估你的 App 或工作流的色彩特性。
- 将测试图样文件输出到矢量示波器或波形分析仪以查看视频信号。
- 将测试图样文件与光谱辐射计或色度计配合使用，以测量屏幕正面（FoS）亮度。

在播放期间对视频进行恰当的色彩管理需要：为你的内容添加标签、使用提供隐式视频色彩管理的框架，以及评估你的结果。

有关色彩标签的更多信息，请参阅[用视频色彩信息标记媒体](tagging-media-with-video-color-information.md)。

### 使用测试图样文件评估视频

使用测试图样文件来评估你的基于 AVFoundation 的 App 或工作流的色彩特性。这些文件在 Apple 设备和操作系统上显示时会产生预期的结果。在 QuickTime Player App 或其他正确支持 QuickTime 文件格式规范（QuickTime File Format Specification）的 App 或工作流中打开这些文件。使用「数字测色计」App 读取显示缓冲区的像素值。请参阅[使用 QuickTime 测试图样文件评估视频](evaluating-video-using-quicktime-test-pattern-files.md)。

### 使用矢量示波器或波形分析仪评估视频

将测试图样输出到矢量示波器或波形分析仪以分析视频信号。在矢量示波器上查看测试图样，并验证正确的色彩空间转换矩阵。在波形监视器上验证伽马、量化误差以及范围的扩展与压缩。请参阅[使用视频测试设备评估 App 的视频色彩](evaluating-an-app-s-video-color-using-video-test-equipment.md)。

### 使用光谱辐射计或色度计评估视频

将测试图样文件输出到光谱辐射计或色度计以测量屏幕正面（FoS）亮度。测量你的结果并与预期的 FoS 值进行比较。请参阅[使用光测量仪器评估 App 的视频色彩](evaluating-an-app-s-video-color-using-light-measurement-instruments.md)。

### 确保你的 App 的视频得到准确的色彩应用

要确保在播放期间对视频应用恰当的色彩管理：

- 使用与 ColorSync 集成的高级框架（例如 AVFoundation）来实现隐式色彩管理。
- 为所有视频内容添加色彩信息标签，以避免不同设备之间色彩不一致。在大多数情况下，系统会将未标记的媒体视为作者在标清（SD）色彩空间中创建的内容。请参阅[用视频色彩信息标记媒体](tagging-media-with-video-color-information.md)。
- 使用这里描述的技术评估所有结果。

## 主题

### 视频评估

- [使用 QuickTime 测试图样文件评估视频](evaluating-video-using-quicktime-test-pattern-files.md) — 使用测试图样文件检查你的 App 或工作流的色彩再现。
- [使用视频测试设备评估 App 的视频色彩](evaluating-an-app-s-video-color-using-video-test-equipment.md) — 将测试图样文件输出到矢量示波器或波形分析仪以查看视频信号。
- [使用光测量仪器评估 App 的视频色彩](evaluating-an-app-s-video-color-using-light-measurement-instruments.md) — 将测试图样文件与光谱辐射计或色度计配合使用来测量屏幕正面亮度。

## 另请参阅

### 媒体写入

- [将投影视频转换为 Apple Projected Media Profile](converting-projected-video-to-apple-projected-media-profile.md) — 将具有等距圆柱投影或半等距圆柱投影的内容转换为 APMP。
- [将并排 3D 视频转换为多视图 HEVC 和空间视频](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md) — 通过将现有的 3D HEVC 文件转换为多视图 HEVC 格式来创建适用于 visionOS 的视频内容，可选择添加空间元数据来创建空间视频。
- [向影片文件添加显示遮罩矩形元数据轨道](adding-a-display-mask-rectangle-metadata-track-to-a-movie-file.md) — 使用定时显示遮罩矩形元数据显示视频的特定区域。
- [为 HTTP 实时流写入分片 MPEG-4 文件](writing-fragmented-mpeg-4-files-for-http-live-streaming.md) — 通过将影片文件转换为一系列分片 MPEG-4 文件来创建 HTTP 实时流呈现。
- [使用空间元数据创建空间照片和视频](../imageio/creating-spatial-photos-and-videos-with-spatial-metadata.md) — 向立体照片和视频添加空间元数据，以创建可在 Apple Vision Pro 上观看的空间媒体。
- [用视频色彩信息标记媒体](tagging-media-with-video-color-information.md) — 在写入和转码媒体时检查并设置视频色彩空间信息。
- [AVOutputSettingsAssistant](avoutputsettingsassistant.md) — 一个构建音频和视频输出设置字典的对象。
- [AVAssetWriter](avassetwriter.md) — 一个将媒体数据写入容器文件的对象。
- [AVAssetWriterInput](avassetwriterinput.md) — 一个将媒体样本追加到媒体资源写入器输出文件中轨道的对象。
- [AVAssetWriterInputPixelBufferAdaptor](avassetwriterinputpixelbufferadaptor.md) — 一个将视频样本追加到媒体资源写入器输入的对象。 _(已废弃)_
- [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md) — 一个将带标签缓冲区组追加到媒体资源写入器输入的对象。 _(已废弃)_
- [AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md) — 一个将定时元数据组追加到媒体资源写入器输入的对象。 _(已废弃)_
- [AVAssetWriterInputGroup](avassetwriterinputgroup.md) — 一组带有轨道的输入，这些轨道在播放或处理时彼此互斥。
