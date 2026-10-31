---
title: 拍摄静态图像和实况照片
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capturing-still-and-live-photos
source_url: 'https://developer.apple.com/documentation/avfoundation/capturing-still-and-live-photos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capturing-still-and-live-photos.json'
content_hash: 'sha256:85d11cdd16c80bea'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [照片拍摄](photo-capture.md)

# 拍摄静态图像和实况照片

配置并拍摄单张或多张静态图像、实况照片（Live Photo）以及其他形式的摄影。

## 概述

在运行 iOS 11 或更高版本的 iPhone 8、iPhone 8 Plus 和 iPhone X 上拍摄的视频默认使用 HEVC 编解码器。如果你的 App 使用系统共享面板分享所拍摄的视频，视频会被自动转换为目标设备兼容的格式。

AVFoundation 支持多种拍摄照片的方式。你可以简单地拍摄静态的 HEIF 或 JPEG 图像，以 RAW 格式拍摄以便进行自定义处理，一次连拍多张图像，创建带有动态和声音的实况照片，等等。在 iOS 上，所有摄影工作流都使用 [AVCapturePhotoOutput](avcapturephotooutput.md) 类。

> [!note] 注意
> 在 macOS 上，请改为参阅 [AVCaptureStillImageOutput](avcapturestillimageoutput.md)。

### 准备照片拍摄

首先，设置一个 [AVCaptureSession](avcapturesession.md)，其中包含一个受支持的相机设备作为其输入之一，以及一个 [AVCapturePhotoOutput](avcapturephotooutput.md) 作为其输出之一。（详情请参阅[选择捕获设备](choosing-a-capture-device.md)和[设置捕获会话](setting-up-a-capture-session.md)。）每个相机设备都支持多种分辨率和帧速率设置。为了轻松地为用户的设备获得最佳的照片质量，你可以使用 [AVCaptureSessionPresetPhoto](avcapturesession/preset/photo.md) 会话预设，而不是直接选择各项设置。

某些拍摄选项会影响媒体捕获管线的内部配置。由于更改这些选项会导致管线重新配置自身（这需要时间），因此请在向用户提供使用这些设置拍照的能力之前启用它们。否则，配置延迟可能会让用户无法在恰当的时机拍摄照片。

例如，要配置捕获管线以支持实况照片，请在照片输出上启用该属性，如下所示。启用实况照片拍摄后，你可以针对每次拍摄自行选择使用静态拍摄还是实况照片拍摄（请参阅[拍摄并保存实况照片](capturing-and-saving-live-photos.md)）。

```swift
self.captureSession.beginConfiguration()

let photoOutput = AVCapturePhotoOutput()
photoOutput.isHighResolutionCaptureEnabled = true
photoOutput.isLivePhotoCaptureEnabled = photoOutput.isLivePhotoCaptureSupported

guard self.captureSession.canAddOutput(photoOutput) else { return }
self.captureSession.sessionPreset = .photo
self.captureSession.addOutput(photoOutput)

self.previewView.session = captureSession

self.captureSession.commitConfiguration()
self.captureSession.startRunning()
```

### 选择设置

要拍摄照片，请先创建一个 [AVCapturePhotoSettings](avcapturephotosettings.md) 对象，描述你想为该次拍摄使用的设置以及生成的静态照片的数据格式。例如：

- 在受支持的设备上，你可以使用 HEIF/HEVC 格式，以更小的文件尺寸获得更好的图像质量：使用 [+ photoSettingsWithFormat:](<avcapturephotosettings/init(format_).md>) 并选择 [AVVideoCodecTypeHEVC](avvideocodectype/hevc.md) 作为视频编解码器。在不支持 HEVC 的设备上，使用默认的初始化方法 [init()](<../objectivec/nsobject-swift.class/init().md>) 回退到 JPEG 格式。
- 要以 RAW 格式拍摄，请使用 [+ photoSettingsWithRawPixelFormatType:](<avcapturephotosettings/init(rawpixelformattype_).md>)，并指定照片输出所支持的 [availableRawPhotoPixelFormatTypes](avcapturephotooutput/availablerawphotopixelformattypes-5fatm.md) 中的一种。

创建照片设置对象后，你可以为照片选择其他设置。例如，下面的代码创建了一个用于 HEIF/HEVC 拍摄的设置对象，带有自动闪光和图像防抖动。

```swift
let photoSettings: AVCapturePhotoSettings
if self.photoOutput.availablePhotoCodecTypes.contains(.hevc) {
    photoSettings = AVCapturePhotoSettings(format:
        [AVVideoCodecKey: AVVideoCodecType.hevc])
} else {
    photoSettings = AVCapturePhotoSettings()
}
photoSettings.flashMode = .auto
photoSettings.isAutoStillImageStabilizationEnabled =
    self.photoOutput.isStillImageStabilizationSupported

```

其他可能的照片设置包括实况照片、深度数据拍摄和多图像（包围式）拍摄，以及在输出图像文件中嵌入预览图或缩略图的选项。更多信息请参阅下方的「后续步骤」和「更多拍摄选项」。

### 拍摄照片

将你的照片设置对象传递给 [- capturePhotoWithSettings:delegate:](<avcapturephotooutput/capturephoto(with_delegate_).md>) 方法，以使用你所选择的设置触发照片拍摄。

> [!important] 重要
> 调用 [- capturePhotoWithSettings:delegate:](<avcapturephotooutput/capturephoto(with_delegate_).md>) 类似于按下相机的快门按钮——每次调用都会开始一次新的照片拍摄。每次调用都需要一个唯一的 [AVCapturePhotoSettings](avcapturephotosettings.md) 对象，其中包含该次拍摄的设置。要在多次拍摄中重用设置，请参阅 [+ photoSettingsFromPhotoSettings:](<avcapturephotosettings/init(from_).md>)。

### 处理拍摄结果

你传递给 [- capturePhotoWithSettings:delegate:](<avcapturephotooutput/capturephoto(with_delegate_).md>) 方法的 `delegate` 是一个对象，用于跟踪该次照片拍摄的进度并处理其结果。拍摄照片是一个包含多个步骤的异步过程，这些步骤会随时间逐步展开。由于你的 App 可以在较早的拍摄仍在处理时触发额外的拍摄，因此你的委托实现应当能够同时处理多个拍摄。处理并发拍摄的一个简单方法是定义一个采用 [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) 协议的类，并为每次拍摄创建该类的一个单独实例：

```swift
class PhotoCaptureProcessor: NSObject, AVCapturePhotoCaptureDelegate {
    // ...
}

let captureProcessor = PhotoCaptureProcessor()
self.photoOutput.capturePhoto(with: photoSettings, delegate: captureProcessor)
```

当你的拍摄图像数据可供使用时，照片输出会调用你的委托的 [- captureOutput:didFinishProcessingPhoto:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) 方法。你可以在那里使用生成的 [AVCapturePhoto](avcapturephoto.md) 对象来显示、处理或保存图像。

## 主题

### 后续步骤

- [保存拍摄的照片](saving-captured-photos.md) — 将照片拍摄得到的图像和其他数据添加到照片图库。
- [跟踪照片拍摄进度](tracking-photo-capture-progress.md) — 监控拍摄过程中的关键事件，以便在你的相机 UI 中提供反馈。
- [拍摄并保存实况照片](capturing-and-saving-live-photos.md) — 拍摄与系统「相机」App 中创建的实况照片类似的照片，并将其保存到「照片」图库。

### 更多拍摄选项

- [拍摄带深度信息的照片](capturing-photos-with-depth.md) — 在拍摄照片的同时获取深度图，以创建类似系统相机人像模式的效果（在兼容设备上）。
- [拍摄包围式照片序列](capturing-a-bracketed-photo-sequence.md) — 一次拍摄多张照片，并改变曝光时长或感光度等参数。
- [拍摄未压缩的图像数据](capturing-uncompressed-image-data.md) — 获取未经压缩的已处理图像数据，用于滤镜处理或无损输出。
- [拍摄缩略图和预览图](capturing-thumbnail-and-preview-images.md) — 在照片拍摄中启用随主图像一起提供缩小尺寸的图像。

## 另请参阅

### 照片拍摄

- [拍摄色彩一致的照片](capturing-consistent-color-images.md) — 通过新的 Constant Color API，为你的 App 带来摄影工作室和灯光设备的力量。
- [以 RAW 和 Apple ProRAW 格式拍摄照片](capturing-photos-in-raw-and-apple-proraw-formats.md) — 在你的相机 App 中启用最低程度处理的图像拍摄，以支持专业摄影工作流。
- [在你的 Mac App 中支持连续互通相机](../appkit/supporting-continuity-camera-in-your-mac-app.md) — 使用连续互通相机将用户 iPhone、iPad 或 iPod touch 上扫描的文稿和图片整合到你的 Mac App 中。
- [AVCapturePhoto](avcapturephoto.md) — 来自照片拍摄输出的图像数据的容器。
- [AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md) — 一种轻度处理的照片，其数据可供系统稍后用于处理并获取更高分辨率的媒体资源。
- [AVCapturePhotoOutput](avcapturephotooutput.md) — 用于静态图像、实况照片和其他摄影工作流的捕获输出。
- [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) — 用于监控进度并接收照片拍摄输出结果的方法。
- [AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md) — 一个监控照片输出的拍摄就绪状态变化的对象。
- [AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md) — 用于接收照片输出拍摄就绪状态更新的委托协议。
- [AVCaptureStillImageOutput](avcapturestillimageoutput.md) — 用于拍摄静态照片的捕获输出。 _(已废弃)_
