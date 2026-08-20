---
title: 为 HTTP Live Streaming 编写分片 MPEG-4 文件
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 11.0+, Xcode 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/writing-fragmented-mpeg-4-files-for-http-live-streaming
source_url: 'https://developer.apple.com/documentation/avfoundation/writing-fragmented-mpeg-4-files-for-http-live-streaming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/writing-fragmented-mpeg-4-files-for-http-live-streaming.json'
content_hash: 'sha256:4b73c6caf3b0fa78'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体读写](media-reading-and-writing.md)

# 为 HTTP Live Streaming 编写分片 MPEG-4 文件

<sub>示例代码</sub>

通过将影片文件转换为一系列分片 MPEG-4（fragmented MPEG-4）文件，创建 HTTP 实时流传输（HTTP Live Streaming）呈现方式。

## 概述

> [!note] 注意
> 本示例代码项目与 WWDC20 讲座 [10011：使用 AVAssetWriter 创作分片 MPEG-4](https://developer.apple.com/videos/play/wwdc2020/10011) 相关。

### 配置示例代码项目

在 Xcode 中运行示例代码项目之前：

1. 编辑名为 `fmp4Writer` 的共享方案。
2. 打开“运行”（Run）操作。
3. 将 _\<指向磁盘上影片文件的路径\>_ 参数替换为你本地硬盘上影片文件的路径。
4. 将 _\<指向输出目录的路径\>_ 参数替换为你期望的输出目录；例如 `~/Desktop/fmp4writer/`。

## 另请参阅

### 媒体写入

- [将投影视频转换为 Apple 投影媒体配置文件](converting-projected-video-to-apple-projected-media-profile.md) — 将等距柱状或半等距柱状投影的内容转换为 APMP。
- [将并排 3D 视频转换为多视图 HEVC 和空间视频](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md) — 通过将现有的 3D HEVC 文件转换为多视图 HEVC 格式，并可选地添加空间元数据以创建空间视频，为 visionOS 制作视频内容。
- [向影片文件添加显示遮罩矩形元数据轨道](adding-a-display-mask-rectangle-metadata-track-to-a-movie-file.md) — 使用定时显示遮罩矩形元数据显示视频的特定区域。
- [使用空间元数据创建空间照片和视频](../imageio/creating-spatial-photos-and-videos-with-spatial-metadata.md) — 向立体照片和视频添加空间元数据，以创建可在 Apple Vision Pro 上观看的空间媒体。
- [使用视频色彩信息标记媒体](tagging-media-with-video-color-information.md) — 在写入和转码媒体时检查并设置视频色彩空间信息。
- [评估 App 的视频色彩](evaluating-an-app-s-video-color.md) — 使用测试图案、视频测试设备和光照测量仪器检查 App 中视频的色彩再现。
- [AVOutputSettingsAssistant](avoutputsettingsassistant.md) — 一个构建音频和视频输出设置字典的对象。
- [AVAssetWriter](avassetwriter.md) — 一个将媒体数据写入容器文件的对象。
- [AVAssetWriterInput](avassetwriterinput.md) — 一个将媒体样本追加到 asset writer 的输出文件中的轨道的对象。
- [AVAssetWriterInputPixelBufferAdaptor](avassetwriterinputpixelbufferadaptor.md) — 一个将视频样本追加到 asset writer 输入的对象。_(已废弃)_
- [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md) — 一个将标记的缓冲区组追加到 asset writer 输入的对象。_(已废弃)_
- [AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md) — 一个将定时元数据组追加到 asset writer 输入的对象。_(已废弃)_
- [AVAssetWriterInputGroup](avassetwriterinputgroup.md) — 一组输入，其轨道在播放或处理时互斥。

## 下载

- [WritingFragmentedMPEG4FilesForHTTPLiveStreaming.zip](https://docs-assets.developer.apple.com/published/454a64e24941/WritingFragmentedMPEG4FilesForHTTPLiveStreaming.zip)
