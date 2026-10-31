---
title: 从原深感摄像头流式传输深度数据
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, Xcode 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/streaming-depth-data-from-the-truedepth-camera
source_url: 'https://developer.apple.com/documentation/avfoundation/streaming-depth-data-from-the-truedepth-camera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/streaming-depth-data-from-the-truedepth-camera.json'
content_hash: 'sha256:84df23da31dfb319'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [附加数据捕获](additional-data-capture.md)

# 从原深感摄像头流式传输深度数据

<sub>示例代码</sub>

以 2D 和 3D 形式呈现来自原深感（TrueDepth）摄像头的深度数据。

## 概述

原深感摄像头实时提供深度数据，让你能够确定某个像素距前置摄像头有多远。本示例演示了如何使用 AVFoundation 框架的捕获 API 从原深感摄像头读取数据，以及如何以直观的方式在屏幕上显示这些数据。

该示例展示了两种不同的视图：一种是通过将深度映射为颜色来区分深度值的 2D 视图，另一种是将数据渲染为点云的 3D 视图。

要在实际中查看这个示例 App，请在运行 iOS 11 或更高版本的 iOS 设备上使用 Xcode 构建并运行该项目。由于 Xcode 无法访问原深感摄像头，本示例无法在 Xcode 模拟器中构建或运行。

### 设置捕获会话

通过会话队列在单独的线程上设置 `AVCaptureSession`。在为捕获配置相机之前初始化这个会话队列，如下所示：

```swift
private let sessionQueue = DispatchQueue(label: "session queue", attributes: [], autoreleaseFrequency: .workItem)
```

`startRunning` 方法是一个阻塞调用，执行时可能需要一些时间。请将会话设置分派到会话队列，这样主队列就不会被阻塞，从而让 App 的 UI 保持响应：

```swift
sessionQueue.async {
    self.configureSession()
}
```

将相机设置为视频捕获遵循与普通视频捕获相同的许多步骤。有关配置流式传输设置的细节，请参阅[设置捕获会话](setting-up-a-capture-session.md)。

在普通设置的基础上，通过声明一个单独的输出来请求深度数据：

```swift
private let depthDataOutput = AVCaptureDepthDataOutput()
```

将这种输出类型显式添加到你的捕获会话中：

```swift
session.addOutput(depthDataOutput)
depthDataOutput.isFilteringEnabled = false
if let connection = depthDataOutput.connection(with: .depthData) {
    connection.isEnabled = true
} else {
    print("No AVCaptureConnection")
}
```

搜索具有浮点深度值的最高可用分辨率，并锁定该格式的配置。

```swift
let depthFormats = videoDevice.activeFormat.supportedDepthDataFormats
let filtered = depthFormats.filter({
    CMFormatDescriptionGetMediaSubType($0.formatDescription) == kCVPixelFormatType_DepthFloat16
})
let selectedFormat = filtered.max(by: {
    first, second in CMVideoFormatDescriptionGetDimensions(first.formatDescription).width < CMVideoFormatDescriptionGetDimensions(second.formatDescription).width
})

do {
    try videoDevice.lockForConfiguration()
    videoDevice.activeDepthDataFormat = selectedFormat
    videoDevice.unlockForConfiguration()
} catch {
    print("Could not lock device for configuration: \(error)")
    setupResult = .configurationFailed
    session.commitConfiguration()
    return
}
```

将普通的 RGB 视频数据与深度数据输出同步。`dataOutputs` 数组中的第一个输出是主输出。

```swift
outputSynchronizer = AVCaptureDataOutputSynchronizer(dataOutputs: [videoDataOutput, depthDataOutput])
outputSynchronizer!.setDelegate(self, queue: dataOutputQueue)
```

`CameraViewController` 的实现会创建并管理这个会话以与相机对接。它还包含在 2D 和 3D 两种查看模式之间切换的 UI。

### 以 2D 形式呈现深度数据

该示例使用 JET 颜色编码来区分深度值，范围从红色（近）到蓝色（远）。一个滑块控制颜色编码与实际颜色值之间的混合。触摸某个像素会显示它的深度值。

`DepthToJETConverter` 执行这一转换。它将色谱划分为直方图区间，根据从图像缓冲区获得的深度值为 Metal 纹理着色，并将该纹理渲染到预览中。

```swift
var cvTextureOut: CVMetalTexture?
CVMetalTextureCacheCreateTextureFromImage(kCFAllocatorDefault, textureCache, pixelBuffer, nil, textureFormat, width, height, 0, &cvTextureOut)
guard let cvTexture = cvTextureOut, let texture = CVMetalTextureGetTexture(cvTexture) else {
    print("Depth converter failed to create preview texture")
    CVMetalTextureCacheFlush(textureCache, 0)
    return nil
}
```

### 以 3D 形式呈现深度数据

该示例的 3D 查看器将数据渲染为点云。使用以下手势控制相机：

- 捏合缩放。
- 拖移以让相机围绕中心移动。
- 双指旋转以转动相机角度。
- 连按两下屏幕以重置初始位置。

该示例将 3D 点云实现为 `PointCloudMetalView`。它使用 Metal 顶点着色器来控制几何形状，并使用 Metal 片元着色器为各个顶点着色，同时保持深度纹理和颜色纹理相互独立：

```objective-c
CVMetalTextureCacheRef _depthTextureCache;
CVMetalTextureCacheRef _colorTextureCache;
```

深度帧的深度图为 Metal 视图的深度纹理提供了基础：

```objective-c
CVPixelBufferRef depthFrame = depthData.depthDataMap;
CVMetalTextureRef cvDepthTexture = nullptr;
if (kCVReturnSuccess != CVMetalTextureCacheCreateTextureFromImage(kCFAllocatorDefault,
                        _depthTextureCache,
                        depthFrame,
                        nil,
                        MTLPixelFormatR16Float,
                        CVPixelBufferGetWidth(depthFrame),
                        CVPixelBufferGetHeight(depthFrame),
                        0,
                        &cvDepthTexture)) {
    NSLog(@"Failed to create depth texture");
    CVPixelBufferRelease(colorFrame);
    return;
}

id<MTLTexture> depthTexture = CVMetalTextureGetTexture(cvDepthTexture);
```

RGB 图像为 Metal 视图的颜色纹理提供了基础：

```objective-c
CVMetalTextureRef cvColorTexture = nullptr;
if (kCVReturnSuccess != CVMetalTextureCacheCreateTextureFromImage(kCFAllocatorDefault,
                        _colorTextureCache,
                        colorFrame,
                        nil,
                        MTLPixelFormatBGRA8Unorm,
                        CVPixelBufferGetWidth(colorFrame),
                        CVPixelBufferGetHeight(colorFrame),
                        0,
                        &cvColorTexture)) {
    NSLog(@"Failed to create color texture");
    CVPixelBufferRelease(colorFrame);
    return;
}

id<MTLTexture> colorTexture = CVMetalTextureGetTexture(cvColorTexture);
```

### 跟踪热状态

处理来自实时流的深度数据可能会导致设备发热。密切关注热状态，以便在超过危险阈值时提醒用户。

```swift
@objc
func thermalStateChanged(notification: NSNotification) {
    if let processInfo = notification.object as? ProcessInfo {
        showThermalState(state: processInfo.thermalState)
    }
}

func showThermalState(state: ProcessInfo.ThermalState) {
    DispatchQueue.main.async {
        var thermalStateString = "UNKNOWN"
        if state == .nominal {
            thermalStateString = "NOMINAL"
        } else if state == .fair {
            thermalStateString = "FAIR"
        } else if state == .serious {
            thermalStateString = "SERIOUS"
        } else if state == .critical {
            thermalStateString = "CRITICAL"
        }
        
        let message = NSLocalizedString("Thermal state: \(thermalStateString)", comment: "Alert message when thermal state has changed")
        let alertController = UIAlertController(title: "TrueDepthStreamer", message: message, preferredStyle: .alert)
        alertController.addAction(UIAlertAction(title: NSLocalizedString("OK", comment: "Alert OK button"), style: .cancel, handler: nil))
        self.present(alertController, animated: true, completion: nil)
    }
}
```

## 另请参阅

### 深度数据拍摄

- [拍摄带深度信息的照片](capturing-photos-with-depth.md) — 在拍摄照片的同时获取深度图，以创建类似系统相机人像模式的效果（在兼容设备上）。
- [手动创建辅助深度数据](creating-auxiliary-depth-data-manually.md) — 生成一张深度图像并将其附加到你自己的图像上。
- [使用 LiDAR 摄像头拍摄深度](capturing-depth-using-the-lidar-camera.md) — 在支持的设备上访问 LiDAR 摄像头以捕获精确的深度数据。
- [AVCamFilter：为捕获流应用滤镜](avcamfilter-applying-filters-to-a-capture-stream.md) — 以玫瑰色滤镜和深度效果渲染捕获流。
- [利用原深感摄像头数据增强实时视频](enhancing-live-video-by-leveraging-truedepth-camera-data.md) — 为从前置原深感摄像头流式传输的实时捕获画面应用你自己的背景。
- [AVCaptureDepthDataOutput](avcapturedepthdataoutput.md) — 一种在兼容相机设备上记录场景深度信息的捕获输出。
- [AVDepthData](avdepthdata.md) — 由兼容相机设备捕获的逐像素距离或视差信息的容器。
- [AVCameraCalibrationData](avcameracalibrationdata.md) — 关于用于捕获图像和深度数据的相机特性的信息。

## 下载

- [StreamingDepthDataFromTheTrueDepthCamera.zip](https://docs-assets.developer.apple.com/published/1bc13e22cdde/StreamingDepthDataFromTheTrueDepthCamera.zip)
