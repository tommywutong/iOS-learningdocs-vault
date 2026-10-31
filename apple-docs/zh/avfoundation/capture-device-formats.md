---
title: 格式
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capture-device-formats
source_url: 'https://developer.apple.com/documentation/avfoundation/capture-device-formats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capture-device-formats.json'
content_hash: 'sha256:8b8253bb943e4768'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕捉设置](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# 格式

<sub>API 集合</sub>

配置捕捉格式和相机帧率。

## 概述

下面的代码示例展示了如何选择 iOS 设备上可实现的最高帧率：

```swift
func configureCameraForHighestFrameRate(device: AVCaptureDevice) {
    
    var bestFormat: AVCaptureDevice.Format?
    var bestFrameRateRange: AVFrameRateRange?

    for format in device.formats {
        for range in format.videoSupportedFrameRateRanges {
            if range.maxFrameRate > bestFrameRateRange?.maxFrameRate ?? 0 {
                bestFormat = format
                bestFrameRateRange = range
            }
        }
    }
    
    if let bestFormat = bestFormat, 
       let bestFrameRateRange = bestFrameRateRange {
        do {
            try device.lockForConfiguration()
            
            // 设置设备的当前格式。
            device.activeFormat = bestFormat
            
            // 设置设备的最小/最大帧时长。
            let duration = bestFrameRateRange.minFrameDuration
            device.activeVideoMinFrameDuration = duration
            device.activeVideoMaxFrameDuration = duration
            
            device.unlockForConfiguration()
        } catch {
            // 处理错误。
        }
    }
}
```

大多数常见的捕捉设置配置都可以通过 [AVCaptureSession](avcapturesession.md) 对象及其可用的预设来完成。不过，在 iOS 设备上，某些专门的选项（例如高帧率）需要直接在 [AVCaptureDevice](avcapturedevice.md) 实例上设置捕捉格式。

> [!note] 注意
> 在 iOS 中，直接配置捕捉设备的 [activeFormat](avcapturedevice/activeformat.md) 属性会将捕捉会话的预设更改为 [AVCaptureSessionPresetInputPriority](avcapturesession/preset/inputpriority.md)。做出此更改后，当你调用 [- startRunning](<avcapturesession/startrunning().md>) 方法，或在更改会话拓扑后调用 [- commitConfiguration](<avcapturesession/commitconfiguration().md>) 方法时，捕捉会话将不再自动配置捕捉格式。
>
> 在 macOS 中，做出更改后捕捉会话仍会自动配置捕捉格式。要在 macOS 中防止捕捉格式被自动更改，请遵循 [- lockForConfiguration:](<avcapturedevice/lockforconfiguration().md>) 方法下所列的建议。

## 主题

### 配置捕捉格式

- [formats](avcapturedevice/formats.md) — 设备支持的捕捉格式。
- [activeFormat](avcapturedevice/activeformat.md) — 设备正在使用的捕捉格式。
- [activeDepthDataFormat](avcapturedevice/activedepthdataformat.md) — 捕捉设备当前活跃的深度数据格式。
- [Format](avcapturedevice/format.md) — 一个定义捕捉设备所支持的媒体格式和捕捉设置的类。

### 配置帧时长

- [activeVideoMinFrameDuration](avcapturedevice/activevideominframeduration.md) — 当前活跃的最小帧时长。
- [activeVideoMaxFrameDuration](avcapturedevice/activevideomaxframeduration.md) — 当前活跃的最大帧时长。
- [activeDepthDataMinFrameDuration](avcapturedevice/activedepthdataminframeduration.md) — 深度数据的最小帧时长。

## 另请参阅

### 配置相机硬件

- [- lockForConfiguration:](<avcapturedevice/lockforconfiguration().md>) — 请求独占访问以配置设备硬件属性。
- [- unlockForConfiguration](<avcapturedevice/unlockforconfiguration().md>) — 释放对设备硬件属性的独占控制。
- [subjectAreaChangeMonitoringEnabled](avcapturedevice/issubjectareachangemonitoringenabled.md) — 一个布尔值，指示设备是否监控被摄主体区域的变化。
- [AVCaptureDeviceSubjectAreaDidChangeNotification](avcapturedevice/subjectareadidchangenotification.md) — 当捕捉设备检测到视频被摄主体区域发生重大变化时系统发布的通知。
- [对焦](capture-device-focus.md) — 配置相机的自动对焦行为，或手动设置其镜头位置。
- [曝光](capture-device-exposure.md) — 配置相机的自动曝光行为，或手动控制其曝光设置。
- [白平衡](capture-device-white-balance.md) — 配置相机的自动白平衡行为，或手动控制白平衡设置。
- [补光](capture-device-lighting.md) — 配置设备的闪光灯、手电筒和低光设置。
- [颜色](capture-device-color.md) — 管理设备的 HDR 和色彩空间设置。
- [变焦](capture-device-zoom.md) — 配置设备变焦行为并检查硬件能力。
