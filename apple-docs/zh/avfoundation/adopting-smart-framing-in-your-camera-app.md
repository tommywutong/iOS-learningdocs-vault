---
title: 在相机 App 中采用智能取景
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/adopting-smart-framing-in-your-camera-app
source_url: 'https://developer.apple.com/documentation/avfoundation/adopting-smart-framing-in-your-camera-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/adopting-smart-framing-in-your-camera-app.json'
content_hash: 'sha256:e346ee14b24a5683'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕获设置](capture-setup.md)

# 在相机 App 中采用智能取景

<sub>文章</sub>

通过提供自动取景建议来捕捉最佳镜头。

## 概述

智能取景（smart framing）会检测人们何时进入或离开场景，并对镜头进行取景以构成出色的照片。iPhone 17、iPhone Air 和 iPhone 17 Pro 上提供的前置超广角摄像头可在不中断相机预览的情况下动态更改宽高比。你可以通过采用 [AVCaptureSmartFramingMonitor](avcapturesmartframingmonitor.md) 来为你的 App 添加智能取景功能。

[AVCaptureSmartFramingMonitor](avcapturesmartframingmonitor.md) 类会监控受支持相机的视场，并提供宽高比和变焦系数建议，以获得更好的摄影构图。当出现最佳取景机会时，监控器会通过其 [recommendedFraming](avcapturesmartframingmonitor/recommendedframing.md) 属性提供建议。

## 寻找支持智能取景的设备

首先验证用户的设备是否支持智能取景：

```swift
func findAndConfigureSmartFramingDevice() -> AVCaptureDevice? {
    // 配置发现会话以查找前置超广角摄像头。
    let discoverySession = AVCaptureDevice.DiscoverySession(
        deviceTypes: [.builtInUltraWideCamera],
        mediaType: .video,
        position: .front
    )

    // 找到第一个匹配的设备和支持智能取景的格式。
    guard let device = discoverySession.devices.first,
          let format = device.formats.first(where: \.isSmartFramingSupported) else {
        // 如果设备没有前置超广角摄像头，则返回 nil。
        return nil
    }

    if device.activeFormat.isSmartFramingSupported {
        // 如果设备已经为智能取景配置好，则返回该设备。
        return device
    } else {
        // 否则，尝试配置该设备，如果成功则返回它。
        do {
            try device.lockForConfiguration()
            defer { device.unlockForConfiguration() }
            // 将智能取景格式设置为活跃格式。
            device.activeFormat = format
            return device
        } catch {
            return nil
        }
    }
}
```

上面的代码使用一个 [DiscoverySession](avcapturedevice/discoverysession.md) 对象来查找前置超广角摄像头，并验证它是否提供支持该功能的 [Format](avcapturedevice/format.md)。如果设备配置支持智能取景，它会返回该捕获设备。否则，它会设置 [activeFormat](avcapturedevice/activeformat.md)，然后返回配置好的设备。

## 配置智能取景监控器

找到受支持的捕获设备后，通过访问该设备关联的 [AVCaptureSmartFramingMonitor](avcapturesmartframingmonitor.md) 对象来配置其监控行为：

```swift
func configureSmartFraming() async {
    // 访问智能取景监控器（如果可用）。
    guard let monitor = currentDevice?.smartFramingMonitor else { return }
    // 启用所有受支持的取景方式。
    monitor.enabledFramings = monitor.supportedFramings
}
```

默认情况下，智能取景监控器并未配置为提供建议。在这种状态下尝试启动它会导致错误。要监控场景，请通过设置监控器的 [enabledFramings](avcapturesmartframingmonitor/enabledframings.md) 属性值，指定监控器应考虑的取景方式。上面的示例启用了监控器的全部 [supportedFramings](avcapturesmartframingmonitor/supportedframings.md)，但你可以根据 App 的需要只启用这些值的一个子集。例如，照片拍摄可以只启用 [AVCaptureAspectRatio3x4](avcapturedevice/aspectratio/ratio3x4.md) 和 [AVCaptureAspectRatio4x3](avcapturedevice/aspectratio/ratio4x3.md)，而视频拍摄则启用 [AVCaptureAspectRatio9x16](avcapturedevice/aspectratio/ratio9x16.md) 和 [AVCaptureAspectRatio16x9](avcapturedevice/aspectratio/ratio16x9.md)。

## 监控取景建议

配置好智能取景监控器后，它就可以开始生成取景建议了。要响应新的建议，请按如下所示对监控器的 [recommendedFraming](avcapturesmartframingmonitor/recommendedframing.md) 属性进行键值观察：

```swift
func startMonitoring() async {
    // 如果监控器不存在或当前正在监控，则提前返回。
    guard let monitor = currentDevice?.smartFramingMonitor, !monitor.isMonitoring else { return }

    // 对监控器的取景建议变化进行键值观察。
    framingObservation = monitor.observe(\.recommendedFraming, options: [.new]) { [weak self] monitor, change in
        // 访问推荐的取景方式。
        guard let self, let framing = monitor.recommendedFraming else { return }
        // 使用最新建议配置设备。
        Task { await self.applyRecommendedFraming(framing) }
    }

    do {
        // 开始监控取景建议。
        try monitor.startMonitoring()
    } catch {
        logger.error("Unable to start monitoring: \(error)")
    }
}
```

这个代码示例配置了一个观察者来响应新的取景建议。当它观察到新值时，会调用一个方法将该取景应用于捕获设备。配置好观察者后，示例调用监控器的 [- startMonitoringWithError:](<avcapturesmartframingmonitor/startmonitoring().md>) 方法来生成取景建议。

要停用智能取景、让人们可以手动为镜头取景，请使你的键值观察失效，并调用监控器的 [- stopMonitoring](<avcapturesmartframingmonitor/stopmonitoring().md>) 方法，如下所示：

```swift
func stopMonitoring() async {
    // 停止对监控器的键值观察。
    framingObservation?.invalidate()
    framingObservation = nil

    guard let monitor = currentDevice?.smartFramingMonitor else { return }
    // 停止监控智能取景建议。
    monitor.stopMonitoring()
}
```

调用这个方法会让监控器停止生成建议，直到你重新开始监控。

> [!note] 注意
> 你可以独立于捕获会话启动和停止智能取景监控器，这让你能够在不中断视频流的情况下切换该功能的状态。

## 应用取景建议

当监控器生成新的取景建议时，按如下方式设置设备的动态宽高比和视频变焦系数来应用它们：

```swift
private func applyRecommendedFraming(_ framing: AVCaptureFraming) async {
    guard let device = currentDevice else { return }
    do {
        // 请求对设备的独占控制。
        try device.lockForConfiguration()
        do {
            // 设置推荐的宽高比和变焦系数。
            try await device.setDynamicAspectRatio(framing.aspectRatio)
            device.videoZoomFactor = CGFloat(framing.zoomFactor)
        } catch {
            logger.error("Failed to set aspect ratio: \(error)")
        }
        // 释放对设备的独占控制。
        device.unlockForConfiguration()
    } catch {
        logger.error("Failed to lock device for configuration: \(error)")
    }
}
```

应用宽高比和变焦系数的先后顺序会影响视觉过渡效果。先应用宽高比更改，再更新变焦系数，可以在不同取景之间提供平滑的过渡。

## 另请参阅

### 捕获设备

- [选择捕获设备](choosing-a-capture-device.md) — 选择前置或后置摄像头，或使用原深感摄像头、双摄像头等高级特性。
- [AVCaptureDevice](avcapturedevice.md) — 一个表示相机或麦克风等硬件或虚拟捕获设备的对象。
- [AVCaptureDeviceInput](avcapturedeviceinput.md) — 一个将来自捕获设备的媒体输入提供给捕获会话的对象。
- [AVContinuityDevice](avcontinuitydevice.md) — 一个表示附近的物理 iOS 设备的类，可提供对其相机和麦克风的访问。
- [AVExternalStorageDevice](avexternalstoragedevice.md) — 表示存储媒体资产的物理外部存储设备。
- [AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md) — 在外部存储设备连接到系统和从系统断开时通知你的 App。
