---
title: 变焦
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capture-device-zoom
source_url: 'https://developer.apple.com/documentation/avfoundation/capture-device-zoom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capture-device-zoom.json'
content_hash: 'sha256:50b1464c5e2ba9e1'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕捉设置](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# 变焦

<sub>API 集合</sub>

配置设备变焦行为并检查硬件能力。

## 主题

### 调整变焦

- [videoZoomFactor](avcapturedevice/videozoomfactor.md) — 一个控制设备所捕捉图像裁剪和放大的值。
- [- rampToVideoZoomFactor:withRate:](<avcapturedevice/ramp(tovideozoomfactor_withrate_).md>) — 开始从当前变焦系数到另一变焦系数的平滑过渡。
- [- cancelVideoZoomRamp](<avcapturedevice/cancelvideozoomramp().md>) — 平滑地结束进行中的变焦过渡。

### 观察变焦

- [rampingVideoZoom](avcapturedevice/isrampingvideozoom.md) — 一个布尔值，指示变焦过渡是否正在进行。

### 检查变焦系数

- [minAvailableVideoZoomFactor](avcapturedevice/minavailablevideozoomfactor.md) — 当前捕捉配置允许的最小变焦系数。
- [maxAvailableVideoZoomFactor](avcapturedevice/maxavailablevideozoomfactor.md) — 当前捕捉配置允许的最大变焦系数。
- [virtualDeviceSwitchOverVideoZoomFactors](avcapturedevice/virtualdeviceswitchovervideozoomfactors.md) — 一个视频变焦系数数组，当达到或超过这些系数时，虚拟设备（如双相机）可能会切换到其下一个组成设备。
- [dualCameraSwitchOverVideoZoomFactor](avcapturedevice/dualcameraswitchovervideozoomfactor.md) — 双相机设备可在相机之间自动切换的视频变焦系数。_(已废弃)_
- [displayVideoZoomFactorMultiplier](avcapturedevice/displayvideozoomfactormultiplier.md) — 在用户界面中显示变焦信息时使用的视频变焦系数乘数。

### 启用几何畸变校正

- [geometricDistortionCorrectionSupported](avcapturedevice/isgeometricdistortioncorrectionsupported.md) — 一个布尔值，指示此设备是否支持几何畸变校正。
- [geometricDistortionCorrectionEnabled](avcapturedevice/isgeometricdistortioncorrectionenabled.md) — 一个布尔值，指示此设备是否已启用几何畸变校正。

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
- [补光](capture-device-lighting.md) — 配置设备的闪光灯、手电筒和低光设置。
- [颜色](capture-device-color.md) — 管理设备的 HDR 和色彩空间设置。
