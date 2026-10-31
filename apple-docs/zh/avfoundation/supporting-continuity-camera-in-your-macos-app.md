---
title: 在 macOS App 中支持连续互通相机
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 13.0+, Xcode 16.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/supporting-continuity-camera-in-your-macos-app
source_url: 'https://developer.apple.com/documentation/avfoundation/supporting-continuity-camera-in-your-macos-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/supporting-continuity-camera-in-your-macos-app.json'
content_hash: 'sha256:d8f749c652dc5499'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕捉设置](capture-setup.md)

# 在 macOS App 中支持连续互通相机

<sub>示例代码</sub>

使用 iPhone 相机作为外部捕捉设备，实现高质量的照片和视频捕捉。

## 概述

连续互通相机（Continuity Camera）将 iPhone 设备的相机和图像信号处理能力带到 Mac 上。它让你可以使用 iPhone 的后置广角相机，在 macOS App 中支持高质量的照片和视频捕捉。连续互通相机还将舞台居中（Center Stage）、人像模式和录音室灯光（Studio Light）等高级功能带给所有 Mac 设备。在 App 中采用此功能的一个重要部分是支持自动相机选择。

从 macOS 13 开始，操作系统会记住它偏好的用于捕捉的相机。它的偏好基于多种因素，包括捕捉质量、设备摆放位置和用户偏好。App 观察系统偏好相机的状态，并随该值的变化自动更新其相机选择。

示例 App 向你展示如何访问 iPhone 的相机和麦克风、采用自动相机选择，以及控制和观察系统视频效果的状态。

> [!note] 注意
> 本示例代码项目关联 WWDC22 场次 [10018: Bring Continuity Camera to your macOS app](https://developer.apple.com/wwdc22/10018)

### 配置示例代码项目

要运行此示例 App，你需要：

- 一台运行 macOS 13 beta 或更高版本的 Mac。
- 一台运行 iOS 16 beta 或更高版本的 iPhone。
- Xcode 14 beta 或更高版本。
- 两台设备都必须登录使用双重认证的 Apple ID 账户。

通过 USB 将 iPhone 连接到 Mac。首次运行本示例时，系统会提示你授予 App 访问相机和麦克风的权限。你必须允许示例 App 访问这两者，它才能正常工作。

### 配置设备发现

App 执行初始设置时，会配置两个 [DiscoverySession](avcapturedevice/discoverysession.md) 实例：一个用于发现视频设备，另一个用于发现音频设备。它用一个包含内置设备以及 [AVCaptureDeviceTypeExternalUnknown](avcapturedevice/devicetype-swift.struct/externalunknown.md) 设备的设备列表来初始化每个发现会话。指定外部未知设备类型使发现会话能够找到兼容的 iPhone 相机和麦克风，以及其他厂商的支持捕捉设备。

```swift
// 观察设备相机。指定 `.externalUnknown` 以将 iPhone 相机作为 `AVCaptureDevice` 访问。
videoDiscoverySession = AVCaptureDevice.DiscoverySession(deviceTypes: [.builtInWideAngleCamera, .externalUnknown],
                                                         mediaType: .video,
                                                         position: .unspecified)
// 观察设备麦克风。指定 `.externalUnknown` 以将 iPhone 麦克风作为 `AVCaptureDevice` 访问。
audioDiscoverySession = AVCaptureDevice.DiscoverySession(deviceTypes: [.builtInMicrophone, .externalUnknown],
                                                         mediaType: .audio,
                                                         position: .unspecified)
```

App 观察每个发现会话的 [devices](avcapturedevice/discoverysession/devices.md) 数组的状态，当设备连接到系统或从系统断开时，它会更新其在用户界面中呈现的设备列表。

### 设置初始视频设备选择

示例 App 默认启用自动相机选择，因此在执行初始捕捉会话配置时，它使用系统偏好的相机作为其默认相机设备，如下所示。

```swift
private var defaultVideoCaptureDevice: AVCaptureDevice {
    get throws {
        // 访问系统偏好的相机。
        if let device = AVCaptureDevice.systemPreferredCamera {
            return device
        } else {
            // 主机系统上没有可用相机。
            throw Error.noVideoDeviceAvailable
        }
    }
}
```

[AVCaptureDevice](avcapturedevice.md) 的 [systemPreferredCamera](avcapturedevice/systempreferredcamera.md) 属性提供一个可选的捕捉设备值。但是，除非主机系统既无内置设备也无已连接设备，否则它总是提供一个有效的捕捉设备。

### 响应系统偏好相机变化

系统偏好相机会根据设备可用性和用户相机选择而变化。示例 App 提供一个 `PreferredCameraObserver` 对象，对 `systemPreferredCamera` 属性进行键值观察以监控变化。当它观察到该值变化时，会按如下方式更新其 `@Published` 属性值的状态。

```swift
class PreferredCameraObserver: NSObject, ObservableObject {
    
    private let systemPreferredKeyPath = "systemPreferredCamera"
    
    @Published private(set) var systemPreferredCamera: AVCaptureDevice?
    
    override init() {
        super.init()
        // 对 `AVCaptureDevice` 上的 `systemPreferredCamera` 类属性进行键值观察。
        AVCaptureDevice.self.addObserver(self, forKeyPath: systemPreferredKeyPath, options: [.new], context: nil)
    }
    
    override func observeValue(forKeyPath keyPath: String?, of object: Any?, change: [NSKeyValueChangeKey: Any]?, context: UnsafeMutableRawPointer?) {
        switch keyPath {
        case systemPreferredKeyPath:
            // 更新观察者的系统偏好相机值。
            systemPreferredCamera = change?[.newKey] as? AVCaptureDevice
        default:
            super.observeValue(forKeyPath: keyPath, of: object, change: change, context: context)
        }
    }
}
```

如果 App 启用了自动相机选择，那么当它观察到系统偏好相机发生变化时，会自动切换到新设备。

```swift
// 当系统偏好相机变化时，App 调用此方法。
private func systemPreferredCameraChanged(to captureDevice: AVCaptureDevice) async {
    
    // 如果 SPC 因设备断开连接而变化，则将 App 重置为
    // 其默认设备选择。
    guard isActiveVideoInputDeviceConnected else {
        resetToDefaultDevices()
        return
    }
    
    // 如果「自动相机选择」复选框处于启用状态，
    // 则自动选择新的捕捉设备。
    if isAutomaticCameraSelectionEnabled {
        await selectCaptureDevice(captureDevice)
    }
}
```

### 更新用户偏好的相机选择

当 App 选择新设备时，它会从会话中移除旧的设备输入，尝试为新设备添加输入，如果成功，则按如下所示更新相应活跃输入设备的状态。

```swift
// 从会话中移除当前输入。
session.removeInput(currentInput)

// 尝试将新设备添加到捕捉会话。
let newInput = try addInput(for: device)

// 相机
if mediaType == .video {
    activeVideoInput = newInput
    if isUserSelection {
        // 如果设备变化是由用户选择引起的，则设置 UPC 值，
        // 这会更新系统偏好相机的状态。
        AVCaptureDevice.userPreferredCamera = device
    }
}
// 麦克风
else {
    activeAudioInput = newInput
}
```

对于相机设备，如果选择请求来自用户输入，App 还会更新 [userPreferredCamera](avcapturedevice/userpreferredcamera.md) 的状态，这会跨 App 重启和设备重启持久化用户的偏好相机选择。

> [!note] 注意
> 设置用户偏好相机也会更新 [systemPreferredCamera][7] 属性的值。

### 支持系统视频效果

当 App 选定的相机发生变化时，系统会评估新捕捉设备的 [activeFormat](avcapturedevice/activeformat.md) 以确定它是否支持舞台居中。如果支持，App 会启用舞台居中复选框，让你可以更改其值。切换该功能的状态会将 [centerStageControlMode](avcapturedevice/centerstagecontrolmode-swift.type.property.md) 设置为 [AVCaptureCenterStageControlModeCooperative](avcapturedevice/centerstagecontrolmode-swift.enum/cooperative.md) 并更新其启用状态。

```swift
@Published var isCenterStageEnabled = false {
    didSet {
        guard isCenterStageEnabled != AVCaptureDevice.isCenterStageEnabled else { return }
        AVCaptureDevice.centerStageControlMode = .cooperative
        AVCaptureDevice.isCenterStageEnabled = isCenterStageEnabled
    }
}
```

你还可以在控制中心启用舞台居中，以及人像模式和录音室灯光等视频效果。由于每个效果的启用状态都可能从外部发生变化，App 还会对这些效果的状态进行键值观察。与观察系统偏好相机的变化类似，App 会对 [centerStageEnabled](avcapturedevice/iscenterstageenabled.md)、[portraitEffectEnabled](avcapturedevice/isportraiteffectenabled.md) 和 [studioLightEnabled](avcapturedevice/isstudiolightenabled.md) 属性的状态进行键值观察，并随着值的变化更新用户界面状态。

```swift
AVCaptureDevice.self.addObserver(self, forKeyPath: centerStageKeyPath, options: [.new], context: nil)
AVCaptureDevice.self.addObserver(self, forKeyPath: portraitEffectKeyPath, options: [.new], context: nil)
AVCaptureDevice.self.addObserver(self, forKeyPath: studioLightKeyPath, options: [.new], context: nil)
```

## 另请参阅

### 连续互通相机

- [在 tvOS App 中支持连续互通相机](../avkit/supporting-continuity-camera-in-your-tvos-app.md) — 通过连接 iPhone 或 iPad 作为连续互通设备，在你的 Apple TV App 中捕捉高质量的照片、视频和音频。
- [AVCaptureDeskViewApplication](avcapturedeskviewapplication.md) — 一个以编程方式呈现桌面视图（Desk View）的对象。

## 下载

- [SupportingContinuityCameraInYourMacOSApp.zip](https://docs-assets.developer.apple.com/published/5e4b3abd4b85/SupportingContinuityCameraInYourMacOSApp.zip)
