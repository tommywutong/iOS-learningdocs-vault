---
title: 曝光
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capture-device-exposure
source_url: 'https://developer.apple.com/documentation/avfoundation/capture-device-exposure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capture-device-exposure.json'
content_hash: 'sha256:6c60e75c45f2341a'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Capture setup](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# 曝光

<sub>API 集合</sub>

配置相机的自动曝光行为，或手动控制其曝光设置。

## 主题

### 管理曝光模式

- [- isExposureModeSupported:](<avcapturedevice/isexposuremodesupported(__).md>) — 返回一个布尔值，指示设备是否支持指定的曝光模式。
- [exposureMode](avcapturedevice/exposuremode-swift.property.md) — 设备的曝光模式。
- [ExposureMode](avcapturedevice/exposuremode-swift.enum.md) — 指定采集设备曝光模式的常量。

### 设置曝光兴趣点

- [exposurePointOfInterestSupported](avcapturedevice/isexposurepointofinterestsupported.md) — 一个布尔值，指示设备是否支持曝光兴趣点。
- [exposurePointOfInterest](avcapturedevice/exposurepointofinterest.md) — 曝光的兴趣点。

### 设置曝光兴趣矩形

- [exposureRectOfInterestSupported](avcapturedevice/isexposurerectofinterestsupported.md) — 设备是否支持曝光兴趣矩形。
- [exposureRectOfInterest](avcapturedevice/exposurerectofinterest.md) — 设备当前的曝光兴趣矩形（如果有）。
- [minExposureRectOfInterestSize](avcapturedevice/minexposurerectofinterestsize.md) — 指定兴趣矩形时可以使用的最小尺寸。
- [- defaultRectForExposurePointOfInterest:](<avcapturedevice/defaultrectforexposurepoint(ofinterest_).md>) — 针对给定曝光兴趣点所使用的默认兴趣矩形。

### 配置人脸驱动的自动曝光

- [faceDrivenAutoExposureEnabled](avcapturedevice/isfacedrivenautoexposureenabled.md) — 一个布尔值，指示设备是否启用了人脸驱动的自动曝光。
- [automaticallyAdjustsFaceDrivenAutoExposureEnabled](avcapturedevice/automaticallyadjustsfacedrivenautoexposureenabled.md) — 一个布尔值，指示设备是否自动调整人脸驱动的自动曝光。

### 监视曝光变化

- [adjustingExposure](avcapturedevice/isadjustingexposure.md) — 一个布尔值，指示设备当前是否正在调整其曝光设置。

### 调整曝光补偿

- [exposureTargetOffset](avcapturedevice/exposuretargetoffset.md) — 测得的曝光级别相对目标曝光值的偏移量，以曝光值（EV）为单位。
- [exposureTargetBias](avcapturedevice/exposuretargetbias.md) — 要应用于目标曝光值的偏置，以曝光值（EV）为单位。
- [minExposureTargetBias](avcapturedevice/minexposuretargetbias.md) — 支持的曝光偏置最小值，以曝光值（EV）为单位。
- [maxExposureTargetBias](avcapturedevice/maxexposuretargetbias.md) — 支持的曝光偏置最大值，以曝光值（EV）为单位。
- [AVCaptureExposureTargetBiasCurrent](avcapturedevice/currentexposuretargetbias.md) — 表示当前曝光偏置值的特殊常量。
- [- setExposureTargetBias:completionHandler:](<avcapturedevice/setexposuretargetbias(__completionhandler_).md>) — 设置要应用于目标曝光值的偏置。

### 手动配置曝光

- [- setExposureModeCustomWithDuration:ISO:completionHandler:](<avcapturedevice/setexposuremodecustom(duration_iso_completionhandler_).md>) — 把曝光模式设置为自定状态，并将曝光时长和 ISO 锁定为显式值。
- [exposureDuration](avcapturedevice/exposureduration.md) — 曝光进行的时长。
- [ISO](avcapturedevice/iso.md) — 当前的曝光 ISO 值。
- [lensAperture](avcapturedevice/lensaperture.md) — 镜头光圈的大小。
- [activeMaxExposureDuration](avcapturedevice/activemaxexposureduration.md) — 自动曝光算法定义的最大曝光时长（以秒为单位）。

## 另请参阅

### 配置相机硬件

- [- lockForConfiguration:](<avcapturedevice/lockforconfiguration().md>) — 请求独占访问以配置设备硬件属性。
- [- unlockForConfiguration](<avcapturedevice/unlockforconfiguration().md>) — 释放对设备硬件属性的独占控制。
- [subjectAreaChangeMonitoringEnabled](avcapturedevice/issubjectareachangemonitoringenabled.md) — 一个布尔值，指示设备是否监视拍摄主体区域的变化。
- [AVCaptureDeviceSubjectAreaDidChangeNotification](avcapturedevice/subjectareadidchangenotification.md) — 当采集设备检测到视频主体区域发生重大变化时系统发布的公告。
- [Formats](capture-device-formats.md) — 配置采集格式和相机帧率。
- [Focus](capture-device-focus.md) — 配置相机的自动对焦行为，或手动设置其镜头位置。
- [White balance](capture-device-white-balance.md) — 配置相机的自动白平衡行为，或手动控制白平衡设置。
- [Lighting](capture-device-lighting.md) — 配置设备的闪光灯、手电筒和低光设置。
- [Color](capture-device-color.md) — 管理设备的 HDR 和色彩空间设置。
- [Zoom](capture-device-zoom.md) — 配置设备的变焦行为并检查硬件能力。
