---
title: 将投影视频转换为 Apple Projected Media Profile
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 26.0+, Xcode 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/converting-projected-video-to-apple-projected-media-profile
source_url: 'https://developer.apple.com/documentation/avfoundation/converting-projected-video-to-apple-projected-media-profile'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/converting-projected-video-to-apple-projected-media-profile.json'
content_hash: 'sha256:c7bb4cd9ea00fe44'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体读取与写入](media-reading-and-writing.md)

# 将投影视频转换为 Apple Projected Media Profile

<sub>示例代码</sub>

将等距圆柱投影或半等距圆柱投影的内容转换为 APMP。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC25 场次 297：[Learn about the Apple Projected Media Profile](https://developer.apple.com/videos/play/wwdc2025/297)。

### 配置示例代码项目

本 App 接受一个单目或立体（帧打包）左右并排或上下叠放的立体输入视频文件路径，作为唯一的命令行实参。要在 Xcode 中运行该 App，请点击 Run 按钮以转换项目内附的左右并排帧打包立体 180 度示例资源（`Lighthouse_sbs.mp4`），或者依次选择 Product \> Scheme \> Edit Scheme，并在 Run 构建方案操作的 Arguments 选项卡中编辑指向你的文件的路径。

要向输出文件添加投影媒体元数据，请传入以下两个选项之一：

- **`--autoDetect`（或 `-a`）** — 检查来源文件中是否存在与 APMP 兼容的球形元数据。
- **`--projectionKind <projection_kind>`（或 `-p`）** — 指定投影类型，可以是 `equirectangular` 或 `halfequirectangular`。

其他选项：

- **`--viewPackingKind <view_packing_kind>`（或 `-v`）** — 手动指定帧打包模式，可以是 `sidebyside` 或 `overunder`。如果你指定了 `--autoDetect` 选项，App 会忽略此选项。
- **`--baseline`（或 `-b`）** — 以毫米为单位指定基线（例如 `--baseline 64.0` 表示 64 毫米基线）。
- **`--fov`（或 `-f`）** — 以度为单位指定水平视场角（例如 `--fov 80.0` 表示 80 度视场角）。

默认情况下，项目的方案会从 Xcode 项目文件夹加载名为 `Lighthouse_sbs.mp4` 的左右并排视频。

## 另请参阅

### 媒体写入

- [将左右并排 3D 视频转换为多视图 HEVC 和空间视频](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md) — 将现有的 3D HEVC 文件转换为多视图 HEVC 格式来创建 visionOS 视频内容，并可选择添加空间元数据以创建空间视频。
- [向影片文件添加显示遮罩矩形元数据轨道](adding-a-display-mask-rectangle-metadata-track-to-a-movie-file.md) — 使用定时显示遮罩矩形元数据来显示视频的特定区域。
- [为 HTTP Live Streaming 写入分段 MPEG-4 文件](writing-fragmented-mpeg-4-files-for-http-live-streaming.md) — 通过将影片文件转换为一系列分段 MPEG-4 文件来创建 HTTP Live Streaming 呈现。
- [使用空间元数据创建空间照片和视频](../imageio/creating-spatial-photos-and-videos-with-spatial-metadata.md) — 向立体照片和视频添加空间元数据，以创建可在 Apple Vision Pro 上观看的空间媒体。
- [为媒体标记视频颜色信息](tagging-media-with-video-color-information.md) — 在写入和转码媒体时检查并设置视频色彩空间信息。
- [评估 App 的视频色彩](evaluating-an-app-s-video-color.md) — 使用测试图案、视频测试设备和测光仪器检查 App 中视频的颜色再现。
- [AVOutputSettingsAssistant](avoutputsettingsassistant.md) — 一个构建音频和视频输出设置字典的对象。
- [AVAssetWriter](avassetwriter.md) — 一个将媒体数据写入容器文件的对象。
- [AVAssetWriterInput](avassetwriterinput.md) — 一个将媒体样本追加到资源写入器输出文件中轨道的对象。
- [AVAssetWriterInputPixelBufferAdaptor](avassetwriterinputpixelbufferadaptor.md) — 一个将视频样本追加到资源写入器输入的对象。_(已废弃)_
- [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md) — 一个将带标记缓冲区组追加到资源写入器输入的对象。_(已废弃)_
- [AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md) — 一个将定时元数据组追加到资源写入器输入的对象。_(已废弃)_
- [AVAssetWriterInputGroup](avassetwriterinputgroup.md) — 一组输入，其轨道在播放或处理时彼此互斥。

## 下载

- [ConvertingProjectedVideoToAppleProjectedMediaProfile.zip](https://docs-assets.developer.apple.com/published/6a11c3cf4e6d/ConvertingProjectedVideoToAppleProjectedMediaProfile.zip)
