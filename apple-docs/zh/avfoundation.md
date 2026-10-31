---
title: AVFoundation
framework: AVFoundation
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 2.2+, iPadOS 13.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation
source_url: 'https://developer.apple.com/documentation/avfoundation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation.json'
content_hash: 'sha256:135f88661d56ad84'
translated: true
---

> 导航：[技术](technologies.md)

# AVFoundation

<sub>框架</sub>

处理视听资产，控制设备相机，处理音频，并配置系统音频交互。

## 概述

AVFoundation 融合了几个主要的技术领域，共同涵盖了在 Apple 平台上检查、播放、捕捉和处理视听媒体的广泛任务。

## 主题

### 基础

- [AVFoundation 更新](updates/avfoundation.md) — 了解 AVFoundation 的重要变化。

### 通用

- [媒体资源](avfoundation/media-assets.md) — 从文件和流加载媒体资源，以检查它们的属性、轨道和内嵌元数据。
- [媒体读取与写入](avfoundation/media-reading-and-writing.md) — 从视频中读取图像、导出为其他格式，以及对媒体数据执行样本级读取和写入。
- [媒体类型与实用工具](avfoundation/media-types-and-utilities.md) — 识别 AVFoundation 支持的内容类型和文件格式。
- [视频设置](avfoundation/video-settings.md) — 使用标准的键和值常量来配置视频处理设置。
- [音频设置](avfoundation/audio-settings.md) — 使用标准的键和值常量来配置音频处理设置。

### 播放

- [媒体播放](avfoundation/media-playback.md) — 管理媒体资源和插播内容的播放，与你在界面中呈现这些内容的方式无关。
- [离线播放与存储](avfoundation/offline-playback-and-storage.md) — 将流媒体内容下载到磁盘以支持离线播放，并定义自动移除已下载资产的策略。
- [流媒体与隔空播放](avfoundation/streaming-and-airplay.md) — 使用隔空播放（AirPlay）将内容无线串流到其他设备，并处理涉及 FairPlay 保护资产的请求。
- [样本缓冲区播放](avfoundation/sample-buffer-playback.md) — 创建自定控制器来播放样本缓冲区流并同步其计时。

### 捕捉

- [捕捉设置](avfoundation/capture-setup.md) — 为媒体捕捉配置内置相机和麦克风，以及外部捕捉设备。
- [照片捕捉](avfoundation/photo-capture.md) — 捕捉高质量静态图像、实况照片以及配套的照片数据。
- [音频与视频捕捉](avfoundation/audio-and-video-capture.md) — 将音频和视频直接捕捉到媒体文件，或捕捉媒体流以直接访问媒体样本缓冲区。
- [附加数据捕捉](avfoundation/additional-data-capture.md) — 捕捉深度和元数据等附加数据，并同步来自多个输出的捕捉。

### 编辑

- [合成资源](avfoundation/composite-assets.md) — 将多个资产的轨道和轨道片段合并为一个可供播放或处理的合成资源。
- [QuickTime 影片](avfoundation/quicktime-movies.md) — 访问 QuickTime 影片文件的内容，并对其媒体轨道执行样本级编辑。
- [视频效果](avfoundation/video-effects.md) — 定义标准的视频过渡效果，将图层动画与媒体计时同步，并创建自定视频合成器。
- [音频混音](avfoundation/audio-mixing.md) — 定义如何在资产的时长内混合来自多个音轨的电平。

### 音频

- [音频播放、录制与处理](avfoundation/audio-playback-recording-and-processing.md) — 播放、录制和处理音频；配置 App 的系统音频行为。
- [语音合成](avfoundation/speech-synthesis.md) — 配置嗓音来朗读文本字符串。

### 错误

- [AVFoundationErrorDomain](avfoundation/avfoundationerrordomain.md) — AVFoundation 错误的错误域。
- [AVError](avfoundation/averror-swift.struct.md) — 一个定义框架操作可能产生的错误的结构体。

### 宏

- [宏](avfoundation/avfoundation-macros.md)
