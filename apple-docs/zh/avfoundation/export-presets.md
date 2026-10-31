---
title: 导出预设
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/export-presets
source_url: 'https://developer.apple.com/documentation/avfoundation/export-presets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/export-presets.json'
content_hash: 'sha256:c862816395769928'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media reading and writing](media-reading-and-writing.md) · [AVAssetExportSession](avassetexportsession.md)

# 导出预设

<sub>API 集合</sub>

配置导出会话以标准尺寸和格式输出媒体。

## 概述

使用预设名称常量来初始化一个 [AVAssetExportSession](avassetexportsession.md) 实例。

## 主题

### 质量预设

- [AVAssetExportPresetLowQuality](avassetexportpresetlowquality.md) — 用于导出低质量影片文件的预设。
- [AVAssetExportPresetMediumQuality](avassetexportpresetmediumquality.md) — 用于导出中等质量影片文件的预设。
- [AVAssetExportPresetHighestQuality](avassetexportpresethighestquality.md) — 用于导出高质量影片文件的预设。
- [AVAssetExportPresetHEVCHighestQuality](avassetexportpresethevchighestquality.md) — 用于以最高可用视频质量和 HEVC 视频压缩导出的预设。
- [AVAssetExportPresetHEVCHighestQualityWithAlpha](avassetexportpresethevchighestqualitywithalpha.md) — 用于以最高可用视频质量、HEVC 视频压缩和 alpha 通道导出的预设。

### 尺寸预设

- [AVAssetExportPreset640x480](avassetexportpreset640x480.md) — 用于导出包含 H.264 视频和 AAC 音频的 640 x 480 影片的预设。
- [AVAssetExportPreset960x540](avassetexportpreset960x540.md) — 用于导出包含 H.264 视频和 AAC 音频的 960 x 540 影片的预设。
- [AVAssetExportPreset1280x720](avassetexportpreset1280x720.md) — 用于导出包含 H.264 视频和 AAC 音频的 1280 x 720 影片的预设。
- [AVAssetExportPreset1920x1080](avassetexportpreset1920x1080.md) — 用于导出包含 H.264 视频和 AAC 音频的 1920 x 1080 影片的预设。
- [AVAssetExportPreset3840x2160](avassetexportpreset3840x2160.md) — 用于导出包含 H.264 视频和 AAC 音频的 3840 x 2160 影片的预设。

### HEVC 尺寸预设

- [AVAssetExportPresetHEVC1920x1080](avassetexportpresethevc1920x1080.md) — 用于导出包含 HEVC 视频和 AAC 音频的 1920 x 1080 影片的预设。
- [AVAssetExportPresetHEVC3840x2160](avassetexportpresethevc3840x2160.md) — 用于导出包含 HEVC 视频和 AAC 音频的 3840 x 2160 影片的预设。
- [AVAssetExportPresetHEVC1920x1080WithAlpha](avassetexportpresethevc1920x1080withalpha.md) — 用于导出包含带 alpha 通道的 HEVC 视频和 AAC 音频的 1920 x 1080 影片的预设。
- [AVAssetExportPresetHEVC3840x2160WithAlpha](avassetexportpresethevc3840x2160withalpha.md) — 用于导出包含带 alpha 通道的 HEVC 视频和 AAC 音频的 3840 x 2160 影片的预设。
- [AVAssetExportPresetHEVC4320x2160](avassetexportpresethevc4320x2160.md)
- [AVAssetExportPresetHEVC7680x4320](avassetexportpresethevc7680x4320.md) — 用于导出包含 HEVC 视频和 AAC 音频的 7680 x 4320 影片的预设。

### MV-HEVC 预设

- [AVAssetExportPresetMVHEVC960x960](avassetexportpresetmvhevc960x960.md) — 用于导出包含 MV-HEVC 视频和 AAC 音频的 960 x 960 影片的预设。
- [AVAssetExportPresetMVHEVC1440x1440](avassetexportpresetmvhevc1440x1440.md) — 用于导出包含 MV-HEVC 视频和 AAC 音频的 1440 x 1440 影片的预设。
- [AVAssetExportPresetMVHEVC4320x4320](avassetexportpresetmvhevc4320x4320.md)
- [AVAssetExportPresetMVHEVC7680x7680](avassetexportpresetmvhevc7680x7680.md)

### M4V 预设

- [AVAssetExportPresetAppleM4V480pSD](avassetexportpresetapplem4v480psd.md) — 用于导出适合在 Apple 设备上播放的 480p 标准清晰度格式的预设。
- [AVAssetExportPresetAppleM4V720pHD](avassetexportpresetapplem4v720phd.md) — 用于导出适合在 Apple 设备上播放的 720p 高清晰度格式的预设。
- [AVAssetExportPresetAppleM4V1080pHD](avassetexportpresetapplem4v1080phd.md) — 用于导出适合在 Apple 设备上播放的 1080p 高清晰度格式的预设。
- [AVAssetExportPresetAppleM4ViPod](avassetexportpresetapplem4vipod.md) — 用于导出适合在 iPod 上播放的格式的预设。
- [AVAssetExportPresetAppleM4VAppleTV](avassetexportpresetapplem4vappletv.md) — 用于导出适合在 Apple TV 上播放的格式的预设。
- [AVAssetExportPresetAppleM4VCellular](avassetexportpresetapplem4vcellular.md) — 用于导出适合在通过蜂窝网络流式传输时于 Apple 设备上播放的格式的预设。
- [AVAssetExportPresetAppleM4VWiFi](avassetexportpresetapplem4vwifi.md) — 用于导出适合在通过 WiFi 网络流式传输时于 Apple 设备上播放的格式的预设。

### Apple ProRes 预设

- [AVAssetExportPresetAppleProRes422LPCM](avassetexportpresetappleprores422lpcm.md) — 用于导出带 Apple ProRes 422 视频和 LPCM 音频的 QuickTime 影片的预设。
- [AVAssetExportPresetAppleProRes4444LPCM](avassetexportpresetappleprores4444lpcm.md) — 用于导出带 Apple ProRes 4444 视频和 LPCM 音频的 QuickTime 影片的预设。

### 直通预设

- [AVAssetExportPresetPassthrough](avassetexportpresetpassthrough.md) — 在无其他限制的情况下，用于按 asset 当前格式导出的预设。

### 纯音频预设

- [AVAssetExportPresetAppleM4A](avassetexportpresetapplem4a.md) — 用于导出带有相应 iTunes 无缝播放数据的纯音频 MPEG 4 Audio 文件的预设。

## 另请参阅

### 创建导出会话

- [- initWithAsset:presetName:](<avassetexportsession/init(asset_presetname_).md>) — 使用预设配置创建一个导出会话。
