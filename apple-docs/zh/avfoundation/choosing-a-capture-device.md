---
title: 选择捕捉设备
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/choosing-a-capture-device
source_url: 'https://developer.apple.com/documentation/avfoundation/choosing-a-capture-device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/choosing-a-capture-device.json'
content_hash: 'sha256:8e95d42313d471f3'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕捉设置](capture-setup.md)

# 选择捕捉设备

<sub>文章</sub>

选择前置或后置相机，或使用 TrueDepth 相机、双相机等高级功能。

## 概述

设备为捕捉照片和视频提供了许多选项，包括前置和后置相机、双相机以及 TrueDepth 相机。自动选择合适的相机，或提供用于选择相机的用户界面，是开发任何具备相机功能的 App 的重要部分。

AVFoundation 提供两条选择相机设备的主要途径：[+ defaultDeviceWithDeviceType:mediaType:position:](<avcapturedevice/default(__for_position_).md>) 方法和 [DiscoverySession](avcapturedevice/discoverysession.md) 类。

### 快速选择默认设备

如果你明确知道自己要找的是哪种捕捉设备，请使用 [AVCaptureDevice](avcapturedevice.md) 的某个便捷方法来选择默认设备。例如，下面的代码会选择可用的最佳后置相机：在支持的设备上选择双相机，在单相机设备上选择单（广角）相机。

```swift
if let device = AVCaptureDevice.default(.builtInDualCamera,
                                        for: .video, position: .back) {
    return device
} else if let device = AVCaptureDevice.default(.builtInWideAngleCamera,
                                               for: .video, position: .back) {
    return device
} else {
    fatalError("Missing expected back camera device.")
}
```

### 使用发现会话对设备排序和筛选

要查看符合特定条件的全部设备集合，以便用自己的逻辑选择其中之一，请使用 [DiscoverySession](avcapturedevice/discoverysession.md) 类。首先，为你需要的设备类型创建一个发现会话：

```swift
let discoverySession = AVCaptureDevice.DiscoverySession(deviceTypes:
    [.builtInTrueDepthCamera, .builtInDualCamera, .builtInWideAngleCamera],
    mediaType: .video, position: .unspecified)
```

然后，读取发现会话的 [devices](avcapturedevice/discoverysession/devices.md) 列表来找到匹配的设备，并选择一个适合你需求的设备。发现会话会根据你请求的设备类型自动对其 [devices](avcapturedevice/discoverysession/devices.md) 列表排序，因此你可以利用数组顺序找到具备某些特征的最佳设备。例如，由于上面显示的发现会话先搜索具备深度能力的设备、再搜索广角相机，且允许任意设备位置，因此其设备列表中第一个匹配指定位置的项目就是该位置的最佳深度捕捉设备（或后备设备）：

```swift
func bestDevice(in position: AVCaptureDevice.Position) -> AVCaptureDevice {
    let devices = self.discoverySession.devices
    guard !devices.isEmpty else { fatalError("Missing capture devices.")}

    return devices.first(where: { device in device.position == position })!
}
```

## 另请参阅

### 捕捉设备

- [在相机 App 中采用智能取景](adopting-smart-framing-in-your-camera-app.md) — 通过提供自动取景建议来捕捉最佳镜头。
- [AVCaptureDevice](avcapturedevice.md) — 一个表示硬件或虚拟捕捉设备（如相机或麦克风）的对象。
- [AVCaptureDeviceInput](avcapturedeviceinput.md) — 一个将来自捕捉设备的媒体输入提供给捕捉会话的对象。
- [AVContinuityDevice](avcontinuitydevice.md) — 一个类，表示附近的一台实体 iOS 设备，可提供对其相机和麦克风的访问。
- [AVExternalStorageDevice](avexternalstoragedevice.md) — 表示一台存储媒体资产的实体外部存储设备。
- [AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md) — 在外部存储设备连接到系统或从系统断开连接时通知你的 App。
