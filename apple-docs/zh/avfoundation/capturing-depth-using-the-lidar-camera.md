---
title: 使用 LiDAR 相机捕捉深度数据
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.6+, iPadOS 15.6+, Mac Catalyst 15.6+, Xcode 16.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capturing-depth-using-the-lidar-camera
source_url: 'https://developer.apple.com/documentation/avfoundation/capturing-depth-using-the-lidar-camera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capturing-depth-using-the-lidar-camera.json'
content_hash: 'sha256:18236db2add702f6'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [附加数据捕捉](additional-data-capture.md)

# 使用 LiDAR 相机捕捉深度数据

<sub>示例代码</sub>

在支持的设备上访问 LiDAR 相机，以捕捉精确的深度数据。

## 概述

AVFoundation 在 iOS 11 中引入了针对照片和视频的深度数据捕捉。它提供的数据适用于许多 App，但可能无法满足需要更高精度深度的 App。从 iOS 15.4 开始，你可以在支持的硬件上访问 LiDAR 相机，它提供的高精度深度数据适用于房间扫描和测量等使用场景。

本示例代码项目展示如何从 LiDAR 相机捕捉并渲染深度数据。它以流模式启动，演示如何捕捉同步的视频和深度数据。当你轻点屏幕左上角的相机按钮时，App 切换到照片模式，说明如何捕捉带深度数据的照片。在两种模式下，App 都会提供多种基于 Metal 的深度数据和图像数据可视化。

### 配置示例代码项目

在提供 LiDAR 相机的设备上运行本示例代码，例如：

- iPhone 12 Pro 或更新机型
- iPad Pro 11 英寸（第 3 代）或更新机型
- iPad Pro 12.9 英寸（第 5 代）或更新机型

### 配置 LiDAR 相机

示例 App 的 `CameraController` 类提供配置和管理捕捉会话、并处理新视频和深度数据交付的代码。它的配置始于检索 LiDAR 相机。它调用捕捉设备的 [+ defaultDeviceWithDeviceType:mediaType:position:](<avcapturedevice/default(__for_position_).md>) 类方法，并传入 iOS 15.4 及更高版本中提供的新 [AVCaptureDeviceTypeBuiltInLiDARDepthCamera](avcapturedevice/devicetype-swift.struct/builtinlidardepthcamera.md) 设备类型。

```swift
// 查找 LiDAR 相机。
guard let device = AVCaptureDevice.default(.builtInLiDARDepthCamera, for: .video, position: .back) else {
    throw ConfigurationError.lidarDeviceUnavailable
}
```

检索到设备后，App 为它配置特定的视频和深度格式。它向设备查询其支持的格式，并找到符合示例 App 首选宽度、支持深度捕捉的最佳非合并（nonbinned）全范围 YUV 颜色格式。最后，它按以下代码示例在设备上设置当前格式：

```swift
// 找到一种以 App 自定 Metal 视图所需的格式输出视频数据的匹配项。
guard let format = (device.formats.last { format in
    format.formatDescription.dimensions.width == preferredWidthResolution &&
    format.formatDescription.mediaSubType.rawValue == kCVPixelFormatType_420YpCbCr8BiPlanarFullRange &&
    !format.isVideoBinned &&
    !format.supportedDepthDataFormats.isEmpty
}) else {
    throw ConfigurationError.requiredFormatUnavailable
}

// 找到一种以 App 自定 Metal 视图所需的格式输出深度数据的匹配项。
guard let depthFormat = (format.supportedDepthDataFormats.last { depthFormat in
    depthFormat.formatDescription.mediaSubType.rawValue == kCVPixelFormatType_DepthFloat16
}) else {
    throw ConfigurationError.requiredFormatUnavailable
}

// 开始设备配置。
try device.lockForConfiguration()

// 配置设备和深度格式。
device.activeFormat = format
device.activeDepthDataFormat = depthFormat

// 完成设备配置。
device.unlockForConfiguration()
```

### 配置捕捉输出

App 在流模式或照片模式下运行。为了启用流输出，它会创建 [AVCaptureVideoDataOutput](avcapturevideodataoutput.md) 和 [AVCaptureDepthDataOutput](avcapturedepthdataoutput.md) 的实例，分别用于捕捉视频样本缓冲区和深度数据。它按如下方式配置它们：

```swift
// 创建一个输出视频样本缓冲区的对象。
videoDataOutput = AVCaptureVideoDataOutput()
captureSession.addOutput(videoDataOutput)

// 创建一个输出深度数据的对象。
depthDataOutput = AVCaptureDepthDataOutput()
depthDataOutput.isFilteringEnabled = isFilteringEnabled
captureSession.addOutput(depthDataOutput)

// 创建一个同步深度数据和视频数据交付的对象。
outputVideoSync = AVCaptureDataOutputSynchronizer(dataOutputs: [depthDataOutput, videoDataOutput])
outputVideoSync.setDelegate(self, queue: videoQueue)
```

由于视频和深度数据来自不同的输出对象，示例使用一个 [AVCaptureDataOutputSynchronizer](avcapturedataoutputsynchronizer.md) 将两个输出的交付同步到单一回调。`CameraController` 类采用同步器的 [AVCaptureDataOutputSynchronizerDelegate](avcapturedataoutputsynchronizerdelegate.md) 协议，并响应新视频和深度数据的交付。

为处理照片捕捉，App 还会创建一个 [AVCapturePhotoOutput](avcapturephotooutput.md) 实例。它将该输出优化为高质量捕捉，并将其添加到捕捉会话。

```swift
// 创建一个输出照片的对象。
photoOutput = AVCapturePhotoOutput()
photoOutput.maxPhotoQualityPrioritization = .quality
captureSession.addOutput(photoOutput)

// 在将输出添加到捕捉会话之后，启用深度数据交付。
photoOutput.isDepthDataDeliveryEnabled = true
```

在将输出添加到会话后，它会启用深度数据交付，从而适当地配置捕捉管线。只有在将输出添加到捕捉会话之后才能启用深度交付，因为该输出需要先确定管线配置能否交付深度数据。

### 捕捉同步的视频和深度数据

按要求配置好捕捉会话的输入和输出后，App 就可以开始捕捉数据了。App 以流模式启动，使用视频数据输出、深度数据输出和一个 `AVCaptureDataOutputSynchronizer` 来同步它们的数据交付。App 采用同步器的委托协议，并实现其 [- dataOutputSynchronizer:didOutputSynchronizedDataCollection:](<avcapturedataoutputsynchronizerdelegate/dataoutputsynchronizer(__didoutput_).md>) 方法来处理交付，如下例所示：

```swift
func dataOutputSynchronizer(_ synchronizer: AVCaptureDataOutputSynchronizer,
                            didOutput synchronizedDataCollection: AVCaptureSynchronizedDataCollection) {
    // 检索同步的深度和样本缓冲区容器对象。
    guard let syncedDepthData = synchronizedDataCollection.synchronizedData(for: depthDataOutput) as? AVCaptureSynchronizedDepthData,
          let syncedVideoData = synchronizedDataCollection.synchronizedData(for: videoDataOutput) as? AVCaptureSynchronizedSampleBufferData else { return }
    
    guard let pixelBuffer = syncedVideoData.sampleBuffer.imageBuffer,
          let cameraCalibrationData = syncedDepthData.depthData.cameraCalibrationData else { return }
    
    // 打包捕捉到的数据。
    let data = CameraCapturedData(depth: syncedDepthData.depthData.depthDataMap.texture(withFormat: .r16Float, planeIndex: 0, addToCache: textureCache),
                                  colorY: pixelBuffer.texture(withFormat: .r8Unorm, planeIndex: 0, addToCache: textureCache),
                                  colorCbCr: pixelBuffer.texture(withFormat: .rg8Unorm, planeIndex: 1, addToCache: textureCache),
                                  cameraIntrinsics: cameraCalibrationData.intrinsicMatrix,
                                  cameraReferenceDimensions: cameraCalibrationData.intrinsicMatrixReferenceDimensions)
    
    delegate?.onNewData(capturedData: data)
}
```

App 从 [AVCaptureSynchronizedDataCollection](avcapturesynchronizeddatacollection.md) 中检索存储同步数据的容器对象。然后，它解包底层的视频像素缓冲区和深度数据，并打包它们供 App 的 Metal 视图显示。

### 捕捉照片和深度数据

当你轻点用户界面左上角的相机按钮时，App 会切换到照片模式。此时，App 会调用它的 `capturePhoto()` 方法，该方法创建一个照片设置对象、在其上请求深度数据交付，并发起照片捕捉。

```swift
func capturePhoto() {
    var photoSettings: AVCapturePhotoSettings
    if  photoOutput.availablePhotoPixelFormatTypes.contains(kCVPixelFormatType_420YpCbCr8BiPlanarFullRange) {
        photoSettings = AVCapturePhotoSettings(format: [
            kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_420YpCbCr8BiPlanarFullRange
        ])
    } else {
        photoSettings = AVCapturePhotoSettings()
    }
    
    // 在这次照片捕捉中捕捉深度数据。
    photoSettings.isDepthDataDeliveryEnabled = true
    photoOutput.capturePhoto(with: photoSettings, delegate: self)
}
```

当框架完成照片捕捉后，它会调用照片输出的委托方法，并传入包含图像和深度数据的 [AVCapturePhoto](avcapturephoto.md) 对象。示例从照片中检索数据，停止数据流直到用户返回流模式，然后像视频的情形一样，将捕捉到的数据打包交付给 App 的用户界面层。

```swift
func photoOutput(_ output: AVCapturePhotoOutput, didFinishProcessingPhoto photo: AVCapturePhoto, error: Error?) {
    
    // 检索图像和深度数据。
    guard let pixelBuffer = photo.pixelBuffer,
          let depthData = photo.depthData,
          let cameraCalibrationData = depthData.cameraCalibrationData else { return }
    
    // 停止数据流，直到用户返回流模式。
    stopStream()
    
    // 将深度数据转换为预期的格式。
    let convertedDepth = depthData.converting(toDepthDataType: kCVPixelFormatType_DepthFloat16)
    
    // 打包捕捉到的数据。
    let data = CameraCapturedData(depth: convertedDepth.depthDataMap.texture(withFormat: .r16Float, planeIndex: 0, addToCache: textureCache),
                                  colorY: pixelBuffer.texture(withFormat: .r8Unorm, planeIndex: 0, addToCache: textureCache),
                                  colorCbCr: pixelBuffer.texture(withFormat: .rg8Unorm, planeIndex: 1, addToCache: textureCache),
                                  cameraIntrinsics: cameraCalibrationData.intrinsicMatrix,
                                  cameraReferenceDimensions: cameraCalibrationData.intrinsicMatrixReferenceDimensions)
    
    delegate?.onNewPhotoData(capturedData: data)
}
```

## 另请参阅

### 深度数据捕捉

- [捕捉带深度的照片](capturing-photos-with-depth.md) — 获取带深度图的照片，以创建类似系统相机人像模式的效果（在兼容设备上）。
- [手动创建辅助深度数据](creating-auxiliary-depth-data-manually.md) — 生成深度图像并将其附加到你自己的图像上。
- [AVCamFilter：为捕捉流应用滤镜](avcamfilter-applying-filters-to-a-capture-stream.md) — 以玫瑰色滤镜和深度效果渲染捕捉流。
- [从 TrueDepth 相机串流深度数据](streaming-depth-data-from-the-truedepth-camera.md) — 以 2D 和 3D 形式可视化来自 TrueDepth 相机的深度数据。
- [利用 TrueDepth 相机数据增强实况视频](enhancing-live-video-by-leveraging-truedepth-camera-data.md) — 为来自前置 TrueDepth 相机的实况捕捉画面应用你自己的背景。
- [AVCaptureDepthDataOutput](avcapturedepthdataoutput.md) — 一种捕捉输出，在兼容的相机设备上记录场景深度信息。
- [AVDepthData](avdepthdata.md) — 一个容器，用于存放由兼容相机设备捕捉的逐像素距离或视差信息。
- [AVCameraCalibrationData](avcameracalibrationdata.md) — 关于用于捕捉图像和深度数据的相机特性的信息。

## 下载

- [CapturingDepthUsingTheLiDARCamera.zip](https://docs-assets.developer.apple.com/published/fc8364208145/CapturingDepthUsingTheLiDARCamera.zip)
