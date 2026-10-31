---
title: 补光
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capture-device-lighting
source_url: 'https://developer.apple.com/documentation/avfoundation/capture-device-lighting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capture-device-lighting.json'
content_hash: 'sha256:c28e00c43cf20deb'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕捉设置](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# 补光

<sub>API 集合</sub>

配置设备的闪光灯、手电筒和低光设置。

## 主题

### 配置闪光灯设置

- [hasFlash](avcapturedevice/hasflash.md) — 一个布尔值，指示捕捉设备是否有闪光灯。
- [flashAvailable](avcapturedevice/isflashavailable.md) — 一个布尔值，指示闪光灯当前是否可用。
- [flashActive](avcapturedevice/isflashactive.md) — 一个布尔值，指示闪光灯当前是否处于活动状态。_(已废弃)_
- [flashMode](avcapturedevice/flashmode-swift.property.md) — 设备当前的闪光灯模式。_(已废弃)_
- [- isFlashModeSupported:](<avcapturedevice/isflashmodesupported(__).md>) — 返回一个布尔值，指示设备是否支持给定的闪光灯模式。_(已废弃)_
- [FlashMode](avcapturedevice/flashmode-swift.enum.md) — 指定捕捉设备闪光灯模式的常量。

### 配置手电筒设置

- [hasTorch](avcapturedevice/hastorch.md) — 一个布尔值，指定捕捉设备是否有手电筒。
- [torchAvailable](avcapturedevice/istorchavailable.md) — 一个布尔值，指示手电筒当前是否可用。
- [torchActive](avcapturedevice/istorchactive.md) — 一个布尔值，指示设备的手电筒当前是否处于活动状态。
- [torchLevel](avcapturedevice/torchlevel.md) — 当前的手电筒亮度级别。
- [torchMode](avcapturedevice/torchmode-swift.property.md) — 当前的手电筒模式。
- [TorchMode](avcapturedevice/torchmode-swift.enum.md) — 用于指定捕捉设备手电筒模式的常量。
- [- isTorchModeSupported:](<avcapturedevice/istorchmodesupported(__).md>) — 返回一个布尔值，指示设备是否支持指定的手电筒模式。
- [- setTorchModeOnWithLevel:error:](<avcapturedevice/settorchmodeon(level_).md>) — 在手电筒模式下设置照明级别。
- [AVCaptureMaxAvailableTorchLevel](avcapturedevice/maxavailabletorchlevel.md) — 一个常量，指示将手电筒设置为最大级别。

### 配置低光设置

- [lowLightBoostSupported](avcapturedevice/islowlightboostsupported.md) — 一个布尔值，指示捕捉设备是否支持在低光条件下增强图像。
- [lowLightBoostEnabled](avcapturedevice/islowlightboostenabled.md) — 一个布尔值，指示捕捉设备的低光增强功能是否处于启用状态。
- [automaticallyEnablesLowLightBoostWhenAvailable](avcapturedevice/automaticallyenableslowlightboostwhenavailable.md) — 一个布尔值，指示捕捉设备是否会在必要时自动切换到低光增强模式。

## 另请参阅

### 配置相机硬件

- [- lockForConfiguration:](<avcapturedevice/lockforconfiguration().md>) — 请求独占访问以配置设备硬件属性。
- [- unlockForConfiguration](<avcapturedevice/unlockforconfiguration().md>) — 释放对设备硬件属性的独占控制。
- [subjectAreaChangeMonitoringEnabled](avcapturedevice/issubjectareachangemonitoringenabled.md) — 一个布尔值，指示设备是否监控被摄主体区域的变化。
- [AVCaptureDeviceSubjectAreaDidChangeNotification](avcapturedevice/subjectareadidchangenotification.md) — 当捕捉设备检测到视频被摄主体区域发生重大变化时系统发布的通知。
- [格式](capture-device-formats.md) — 配置捕捉格式和相机帧率。
- [对焦](capture-device-focus.md) — 配置相机的自动对焦行为，或手动设置其镜头位置。
- [曝光](capture-device-exposure.md) — 配置相机的自动曝光行为，或手动控制其曝光设置。
- [白平衡](capture-device-white-balance.md) — 配置相机的自动白平衡行为，或手动控制白平衡设置。
- [颜色](capture-device-color.md) — 管理设备的 HDR 和色彩空间设置。
- [变焦](capture-device-zoom.md) — 配置设备变焦行为并检查硬件能力。
