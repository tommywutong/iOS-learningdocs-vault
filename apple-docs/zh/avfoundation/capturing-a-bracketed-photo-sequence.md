---
title: 拍摄包围曝光照片序列
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capturing-a-bracketed-photo-sequence
source_url: 'https://developer.apple.com/documentation/avfoundation/capturing-a-bracketed-photo-sequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capturing-a-bracketed-photo-sequence.json'
content_hash: 'sha256:0bfc8e3b35230d32'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Photo capture](photo-capture.md) · [Capturing still and Live Photos](capturing-still-and-live-photos.md)

# 拍摄包围曝光照片序列

<sub>文章</sub>

一次拍摄多张照片，改变曝光时长或感光度等参数。

## 概述

包围曝光（bracketing）是一种广为人知的摄影技术：对同一场景快速连续拍摄一组照片，通常只在单一参数上有所变化，例如光圈或快门速度（曝光时长）。经验丰富的摄影师用这项技术在拍摄后挑选最佳照片，或应用离线后期处理，把多张图像融合在一起，以生成扩展动态范围或其他特殊效果。

在 iOS 中，你可以使用 [AVCapturePhotoOutput](avcapturephotooutput.md) 和 [AVCapturePhotoBracketSettings](avcapturephotobracketsettings.md)，让每次 [- capturePhotoWithSettings:delegate:](<avcapturephotooutput/capturephoto(with_delegate_).md>) 调用自动拍摄一组包围曝光照片。在你的 App 中构建好单次曝光相机之后（参见[拍摄静态照片和实况照片](capturing-still-and-live-photos.md)），按以下步骤添加多图像包围支持。

### 选择包围设置

你通过提供一个包围设置对象数组来指定多曝光包围。iOS 提供两种自动包围方式：

- 使用 [AVCaptureAutoExposureBracketedStillImageSettings](avcaptureautoexposurebracketedstillimagesettings.md) 创建一个相对自动曝光改变曝光补偿值的包围。
- 使用 [AVCaptureManualExposureBracketedStillImageSettings](avcapturemanualexposurebracketedstillimagesettings.md) 创建一个为包围中的每张照片指定自定曝光时长和 ISO 感光度值的包围。

要定义一个包围，创建一个由这些类型之一组成的数组，其中的值描述你要拍摄的设置变化。例如，下面的代码定义了一个包围，以三个不同的曝光值拍摄三张图像。

```swift
// Get AVCaptureBracketedStillImageSettings for a set of exposure values.
let exposureValues: [Float] = [-2, 0, +2]
let makeAutoExposureSettings = AVCaptureAutoExposureBracketedStillImageSettings.autoExposureSettings(exposureTargetBias:)
let exposureSettings = exposureValues.map(makeAutoExposureSettings)

```

> [!tip] 提示
> 在 Swift 中，你可以像上面那样，通过把相应的初始化方法传给 `map(_:)` 函数，轻松地把一个曝光值数组转换成一个包围设置数组。

### 创建照片设置并拍摄

不需要拍摄单张照片时创建的 [AVCapturePhotoSettings](avcapturephotosettings.md) 对象，要拍摄包围曝光你需要一个 [AVCapturePhotoBracketSettings](avcapturephotobracketsettings.md) 对象。这个对象把适用于包围中所有照片的通用设置，与你指定包围中各照片差异的包围设置结合在一起。

与单张图像拍摄一样，你通过为生成的照片选择图像编解码器和文件格式来创建照片设置对象，但还要提供你选定的包围设置。

```swift
// Create photo settings for HEIF/HEVC capture and no RAW output
// and enable cross-bracket image stabilization.
let photoSettings = AVCapturePhotoBracketSettings(rawPixelFormatType: 0,
    processedFormat: [AVVideoCodecKey : AVVideoCodecType.hevc],
    bracketedSettings: exposureSettings)
photoSettings.isLensStabilizationEnabled =
    self.photoOutput.isLensStabilizationDuringBracketedCaptureSupported

// Shoot the bracket, using a custom class to handle capture delegate callbacks.
let captureProcessor = PhotoCaptureProcessor()
self.photoOutput.capturePhoto(with: photoSettings, delegate: captureProcessor)

```

> [!tip] 提示
> 打开 [lensStabilizationEnabled](avcapturephotobracketsettings/islensstabilizationenabled.md)（如果受支持）会让相机在整个包围范围内应用光学图像防抖（OIS），这样即使设备在拍摄期间发生移动，包围产生的照片仍然能够彼此对齐。

### 处理包围拍摄结果

对于包围中的每次曝光，照片输出至少会调用一次你的代理的 [- captureOutput:didFinishProcessingPhoto:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) 方法，并且根据你的拍摄设置可能调用更多次。例如，如果你在一个三次曝光的包围中请求 RAW+HEIF 拍摄，照片输出会调用你的代理的 `didFinishProcessingPhoto` 方法六次（2 种格式 × 3 次曝光），提供六个 [AVCapturePhoto](avcapturephoto.md) 对象。

要跟踪多个结果，请把每张照片的 [photoCount](avcapturephoto/photocount.md) 与你的已解析设置的 [expectedPhotoCount](avcaptureresolvedphotosettings/expectedphotocount.md) 进行比较。当这两个数字相等时，说明你已收到这次拍摄的全部结果。

## 另请参阅

### 更多拍摄选项

- [拍摄带深度的照片](capturing-photos-with-depth.md) — 获取随照片一起的深度图，以创建类似系统相机人像模式的效果（在兼容设备上）。
- [拍摄未压缩的图像数据](capturing-uncompressed-image-data.md) — 获取未经压缩的处理后图像数据，用于滤镜处理或无损输出。
- [拍摄缩略图和预览图像](capturing-thumbnail-and-preview-images.md) — 让照片拍摄在主图像之外同时交付缩小尺寸的图像。
