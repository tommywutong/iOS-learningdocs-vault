---
title: 色彩
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capture-device-color
source_url: 'https://developer.apple.com/documentation/avfoundation/capture-device-color'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capture-device-color.json'
content_hash: 'sha256:14354654cf144016'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕获设置](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# 色彩

<sub>API 集合</sub>

管理设备的 HDR 和色彩空间设置。

## 主题

### 配置 HDR 设置

- [automaticallyAdjustsVideoHDREnabled](avcapturedevice/automaticallyadjustsvideohdrenabled.md) — 一个布尔值，指示设备是否自动管理高动态范围（HDR）视频流传输的状态。
- [videoHDREnabled](avcapturedevice/isvideohdrenabled.md) — 一个布尔值，指示设备是否流式传输高动态范围视频缓冲区，也称为扩展动态范围（EDR）。

### 启用全局色调映射

- [globalToneMappingEnabled](avcapturedevice/isglobaltonemappingenabled.md) — 一个布尔值，指示设备是否应使用全局色调映射。

### 配置色彩空间设置

- [activeColorSpace](avcapturedevice/activecolorspace.md) — 当前用于捕获的活跃色彩空间。
- [AVCaptureColorSpace](avcapturecolorspace.md) — 设备可以支持的色彩空间的枚举。

## 另请参阅

### 配置相机硬件

- [- lockForConfiguration:](<avcapturedevice/lockforconfiguration().md>) — 请求独占访问以配置设备硬件属性。
- [- unlockForConfiguration](<avcapturedevice/unlockforconfiguration().md>) — 释放对设备硬件属性的独占控制。
- [subjectAreaChangeMonitoringEnabled](avcapturedevice/issubjectareachangemonitoringenabled.md) — 一个布尔值，指示设备是否监控拍摄主体区域的变化。
- [AVCaptureDeviceSubjectAreaDidChangeNotification](avcapturedevice/subjectareadidchangenotification.md) — 当捕获设备检测到视频拍摄主体区域发生显著变化时系统发布的通知。
- [格式](capture-device-formats.md) — 配置捕获格式和相机帧速率。
- [对焦](capture-device-focus.md) — 配置相机的自动对焦行为，或手动设置其镜头位置。
- [曝光](capture-device-exposure.md) — 配置相机的自动曝光行为，或手动控制其曝光设置。
- [白平衡](capture-device-white-balance.md) — 配置相机的自动白平衡行为，或手动控制白平衡设置。
- [照明](capture-device-lighting.md) — 配置设备的闪光灯、手电筒和低光设置。
- [变焦](capture-device-zoom.md) — 配置设备的变焦行为并检查硬件能力。
