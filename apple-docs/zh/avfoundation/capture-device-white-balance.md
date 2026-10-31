---
title: 白平衡
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capture-device-white-balance
source_url: 'https://developer.apple.com/documentation/avfoundation/capture-device-white-balance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capture-device-white-balance.json'
content_hash: 'sha256:c42fbb74b271ce5e'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕捉设置](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# 白平衡

<sub>API 集合</sub>

配置相机的自动白平衡行为，或手动控制白平衡设置。

## 主题

### 配置自动白平衡

- [- isWhiteBalanceModeSupported:](<avcapturedevice/iswhitebalancemodesupported(__).md>) — 返回一个布尔值，指示设备是否支持指定的白平衡模式。
- [whiteBalanceMode](avcapturedevice/whitebalancemode-swift.property.md) — 当前的白平衡模式。
- [WhiteBalanceMode](avcapturedevice/whitebalancemode-swift.enum.md) — 用于指定捕捉设备白平衡模式的常量。

### 监控白平衡变化

- [adjustingWhiteBalance](avcapturedevice/isadjustingwhitebalance.md) — 一个布尔值，指示设备当前是否正在调整白平衡。

### 检查增益级别

- [deviceWhiteBalanceGains](avcapturedevice/devicewhitebalancegains.md) — 当前使用的设备专属 RGB 白平衡增益值。
- [grayWorldDeviceWhiteBalanceGains](avcapturedevice/grayworlddevicewhitebalancegains.md) — 实现中性灰白点所需的当前设备专属白平衡值。
- [maxWhiteBalanceGain](avcapturedevice/maxwhitebalancegain.md) — 可为颜色通道设置的最大支持值。

### 执行转换

- [- chromaticityValuesForDeviceWhiteBalanceGains:](<avcapturedevice/chromaticityvalues(for_).md>) — 将设备专属的白平衡 RGB 增益值转换为与设备无关的色度值。
- [- temperatureAndTintValuesForDeviceWhiteBalanceGains:](<avcapturedevice/temperatureandtintvalues(for_).md>) — 将设备专属的白平衡 RGB 增益值转换为与设备无关的色温和色调值。
- [- deviceWhiteBalanceGainsForChromaticityValues:](<avcapturedevice/devicewhitebalancegains(for_)-9gdtw.md>) — 将与设备无关的色度值转换为设备专属的白平衡 RGB 增益值。
- [- deviceWhiteBalanceGainsForTemperatureAndTintValues:](<avcapturedevice/devicewhitebalancegains(for_)-3wtsa.md>) — 将与设备无关的色温和色调值转换为设备专属的白平衡 RGB 增益值。
- [WhiteBalanceGains](avcapturedevice/whitebalancegains.md) — 一个定义 RGB 白平衡增益值的结构体。
- [WhiteBalanceChromaticityValues](avcapturedevice/whitebalancechromaticityvalues.md) — 一个定义 CIE 1931 xy 色度值的结构体。
- [WhiteBalanceTemperatureAndTintValues](avcapturedevice/whitebalancetemperatureandtintvalues.md) — 一个定义与白平衡颜色相关的色温和色调值的结构体。

### 手动设置白平衡

- [lockingWhiteBalanceWithCustomDeviceGainsSupported](avcapturedevice/islockingwhitebalancewithcustomdevicegainssupported.md) — 一个布尔值，指示设备是否支持将白平衡锁定为特定增益值。
- [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:](<avcapturedevice/setwhitebalancemodelocked(with_completionhandler_).md>) — 使用指定的白平衡增益将白平衡设置为锁定模式。
- [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceTemperatureAndTintValues:completionHandler:](<avcapturedevice/setwhitebalancemodelocked(whitebalancetemperatureandtintvalues_handler_).md>) — 使用显式的色温和色调值将白平衡设置为锁定模式。

## 另请参阅

### 配置相机硬件

- [- lockForConfiguration:](<avcapturedevice/lockforconfiguration().md>) — 请求独占访问以配置设备硬件属性。
- [- unlockForConfiguration](<avcapturedevice/unlockforconfiguration().md>) — 释放对设备硬件属性的独占控制。
- [subjectAreaChangeMonitoringEnabled](avcapturedevice/issubjectareachangemonitoringenabled.md) — 一个布尔值，指示设备是否监控被摄主体区域的变化。
- [AVCaptureDeviceSubjectAreaDidChangeNotification](avcapturedevice/subjectareadidchangenotification.md) — 当捕捉设备检测到视频被摄主体区域发生重大变化时系统发布的通知。
- [格式](capture-device-formats.md) — 配置捕捉格式和相机帧率。
- [对焦](capture-device-focus.md) — 配置相机的自动对焦行为，或手动设置其镜头位置。
- [曝光](capture-device-exposure.md) — 配置相机的自动曝光行为，或手动控制其曝光设置。
- [补光](capture-device-lighting.md) — 配置设备的闪光灯、手电筒和低光设置。
- [颜色](capture-device-color.md) — 管理设备的 HDR 和色彩空间设置。
- [变焦](capture-device-zoom.md) — 配置设备变焦行为并检查硬件能力。
