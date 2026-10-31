---
title: macOS 捕获特性
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/macos-capture-features
source_url: 'https://developer.apple.com/documentation/avfoundation/macos-capture-features'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/macos-capture-features.json'
content_hash: 'sha256:e9f92d7cecb46ff1'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕获设置](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# macOS 捕获特性

<sub>API 集合</sub>

控制 macOS 中捕获硬件的播放行为和输入源。

## 主题

### 控制播放行为

- [transportControlsSupported](avcapturedevice/transportcontrolssupported.md) — 一个布尔值，指示设备是否支持播放控制命令。
- [transportControlsPlaybackMode](avcapturedevice/transportcontrolsplaybackmode-swift.property.md) — 当前的播放模式。
- [- setTransportControlsPlaybackMode:speed:](<avcapturedevice/settransportcontrolsplaybackmode(__speed_).md>) — 设置播放控制的播放模式和速度。
- [TransportControlsPlaybackMode](avcapturedevice/transportcontrolsplaybackmode-swift.enum.md) — 指示播放控制当前播放模式（如果有的话）的常量。
- [transportControlsSpeed](avcapturedevice/transportcontrolsspeed-swift.property.md) — 当前的播放速度。
- [TransportControlsSpeed](avcapturedevice/transportcontrolsspeed-swift.typealias.md) — 一个指定播放控制速度的常量。

### 配置输入源

- [inputSources](avcapturedevice/inputsources.md) — 设备支持的输入源数组。
- [activeInputSource](avcapturedevice/activeinputsource.md) — 设备当前活跃的输入源。
- [InputSource](avcapturedevice/inputsource.md) — 捕获设备上一个独特的输入源。

### 访问关联设备

- [linkedDevices](avcapturedevice/linkeddevices.md) — 与某设备物理关联的捕获设备数组。
