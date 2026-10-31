---
title: 对焦
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capture-device-focus
source_url: 'https://developer.apple.com/documentation/avfoundation/capture-device-focus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capture-device-focus.json'
content_hash: 'sha256:88359fc666abe15c'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Capture setup](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# 对焦

<sub>API 集合</sub>

配置相机的自动对焦行为，或手动设置其镜头位置。

## 主题

### 配置自动对焦

- [- isFocusModeSupported:](<avcapturedevice/isfocusmodesupported(__).md>) — 返回一个布尔值，指示设备是否支持指定的对焦模式。
- [focusMode](avcapturedevice/focusmode-swift.property.md) — 采集设备的对焦模式。
- [FocusMode](avcapturedevice/focusmode-swift.enum.md) — 指定采集设备对焦模式的常量。
- [smoothAutoFocusSupported](avcapturedevice/issmoothautofocussupported.md) — 一个布尔值，指示设备是否支持平滑自动对焦。
- [smoothAutoFocusEnabled](avcapturedevice/issmoothautofocusenabled.md) — 一个布尔值，指示设备上的平滑自动对焦是否处于启用状态。
- [faceDrivenAutoFocusEnabled](avcapturedevice/isfacedrivenautofocusenabled.md) — 一个布尔值，指示设备是否启用了人脸驱动的自动对焦。
- [automaticallyAdjustsFaceDrivenAutoFocusEnabled](avcapturedevice/automaticallyadjustsfacedrivenautofocusenabled.md) — 一个布尔值，指示设备是否自动调整人脸驱动的自动对焦。
- [autoFocusRangeRestrictionSupported](avcapturedevice/isautofocusrangerestrictionsupported.md) — 一个布尔值，指示设备是否支持对焦范围限制。
- [autoFocusRangeRestriction](avcapturedevice/autofocusrangerestriction-swift.property.md) — 一个控制自动对焦允许范围的值。
- [AutoFocusRangeRestriction](avcapturedevice/autofocusrangerestriction-swift.enum.md) — 指定采集设备自动对焦范围的常量。

### 设置对焦兴趣点

- [focusPointOfInterestSupported](avcapturedevice/isfocuspointofinterestsupported.md) — 一个布尔值，指示设备是否支持对焦兴趣点。
- [focusPointOfInterest](avcapturedevice/focuspointofinterest.md) — 对焦的兴趣点。

### 设置对焦兴趣矩形

- [focusRectOfInterestSupported](avcapturedevice/isfocusrectofinterestsupported.md) — 接收者是否支持对焦兴趣矩形。
- [focusRectOfInterest](avcapturedevice/focusrectofinterest.md) — 设备当前的对焦兴趣矩形（如果有）。
- [minFocusRectOfInterestSize](avcapturedevice/minfocusrectofinterestsize.md) — 指定兴趣矩形时可以使用的最小尺寸。
- [- defaultRectForFocusPointOfInterest:](<avcapturedevice/defaultrectforfocuspoint(ofinterest_).md>) — 针对给定对焦兴趣点所使用的默认兴趣矩形。

### 监视对焦变化

- [adjustingFocus](avcapturedevice/isadjustingfocus.md) — 一个布尔值，指示设备当前是否正在调整其焦点设置。

### 手动设置对焦

- [lockingFocusWithCustomLensPositionSupported](avcapturedevice/islockingfocuswithcustomlenspositionsupported.md) — 一个布尔值，指示设备是否支持把对焦锁定到特定的镜头位置。
- [lensPosition](avcapturedevice/lensposition.md) — 镜头当前的对焦位置。
- [AVCaptureLensPositionCurrent](avcapturedevice/currentlensposition.md) — 表示当前镜头位置的常量。
- [- setFocusModeLockedWithLensPosition:completionHandler:](<avcapturedevice/setfocusmodelocked(lensposition_completionhandler_).md>) — 把镜头位置锁定在指定值，并把对焦模式设置为锁定状态。

### 检查对焦距离

- [minimumFocusDistance](avcapturedevice/minimumfocusdistance.md) — 采集设备的最小对焦距离（以毫米为单位）。

## 另请参阅

### 配置相机硬件

- [- lockForConfiguration:](<avcapturedevice/lockforconfiguration().md>) — 请求独占访问以配置设备硬件属性。
- [- unlockForConfiguration](<avcapturedevice/unlockforconfiguration().md>) — 释放对设备硬件属性的独占控制。
- [subjectAreaChangeMonitoringEnabled](avcapturedevice/issubjectareachangemonitoringenabled.md) — 一个布尔值，指示设备是否监视拍摄主体区域的变化。
- [AVCaptureDeviceSubjectAreaDidChangeNotification](avcapturedevice/subjectareadidchangenotification.md) — 当采集设备检测到视频主体区域发生重大变化时系统发布的公告。
- [Formats](capture-device-formats.md) — 配置采集格式和相机帧率。
- [Exposure](capture-device-exposure.md) — 配置相机的自动曝光行为，或手动控制其曝光设置。
- [White balance](capture-device-white-balance.md) — 配置相机的自动白平衡行为，或手动控制白平衡设置。
- [Lighting](capture-device-lighting.md) — 配置设备的闪光灯、手电筒和低光设置。
- [Color](capture-device-color.md) — 管理设备的 HDR 和色彩空间设置。
- [Zoom](capture-device-zoom.md) — 配置设备的变焦行为并检查硬件能力。
