---
title: 拍摄缩略图和预览图
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capturing-thumbnail-and-preview-images
source_url: 'https://developer.apple.com/documentation/avfoundation/capturing-thumbnail-and-preview-images'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capturing-thumbnail-and-preview-images.json'
content_hash: 'sha256:1aab342ec7db11a9'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [照片捕捉](photo-capture.md) · [捕捉静态照片和实况照片](capturing-still-and-live-photos.md)

# 拍摄缩略图和预览图

<sub>文章</sub>

在照片捕捉中启用随主图像一起提供缩小尺寸的图像。

## 概述

从高分辨率来源图像生成你自己的预览图或缩略图可能既困难又耗时。你可以改用 [AVCapturePhotoOutput](avcapturephotooutput.md)，把轻松、快速的预览图和缩略图生成作为捕捉过程的一部分。

在捕捉系统中，_预览图_和_缩略图_这两个名称有特定含义：

- _预览图_是照片的缩小版本（屏幕分辨率或更小），采用未压缩格式，仅在内存中提供，用于在捕捉后不久显示反馈。例如，系统「相机」App 会显示最后一张捕捉到的照片的预览图。
- _缩略图_是照片的更小版本，以压缩格式编码并内嵌在输出图像文件中，供其他软件使用。例如，浏览装满图像的文件夹的图像浏览器无需读取和解码每个文件的全部内容，就能预览许多文件的内容。

你可以通过对任何 [AVCapturePhotoOutput](avcapturephotooutput.md) 工作流程（参见[捕捉静态照片和实况照片](capturing-still-and-live-photos.md)及相关主题）做少量补充来添加预览图、缩略图或两者。

### 选择设置

为你计划拍摄的照片类型创建 [AVCapturePhotoSettings](avcapturephotosettings.md) 对象后，使用它的 [previewPhotoFormat](avcapturephotosettings/previewphotoformat.md) 字典指定你想要的预览图的格式和大小。

```swift
if photoSettings.availablePreviewPhotoPixelFormatTypes.count > 0 {
    photoSettings.previewPhotoFormat = [
        kCVPixelBufferPixelFormatTypeKey : photoSettings.availablePreviewPhotoPixelFormatTypes.first!,
        kCVPixelBufferWidthKey : 512,
        kCVPixelBufferHeightKey : 512
    ] as [String: Any]
}

```

要请求将照片的缩略图版本内嵌到生成的图像文件中，请使用照片设置对象的 [embeddedThumbnailPhotoFormat](avcapturephotosettings/embeddedthumbnailphotoformat.md) 字典指定缩略图的格式和大小。

```swift
photoSettings.embeddedThumbnailPhotoFormat = [
    AVVideoCodecKey: AVVideoCodecType.jpeg,
    AVVideoWidthKey: 1024,
    AVVideoHeightKey: 1024,
]
```

### 处理结果

当照片输出调用你的委托的 [- captureOutput:didFinishProcessingPhoto:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) 方法时，你可以从 [AVCapturePhoto](avcapturephoto.md) 的 [previewPixelBuffer](avcapturephoto/previewpixelbuffer.md) 属性获取预览图。像素缓冲区提供对像素数据的直接访问，因此你可以使用 Metal、Vision 或 Core Image 等其他图形技术来处理或显示它。在 UI 中简单显示预览图的一种方法是使用 Core Image 把缓冲区包装成 UIImage 对象：

```swift
func showPreview(for photo: AVCapturePhoto) {
    guard let previewPixelBuffer = photo.previewPixelBuffer else { return }
    let ciImage = CIImage(cvPixelBuffer: previewPixelBuffer)
    let uiImage = UIImage(ciImage: ciImage)
    self.imageView.image = uiImage
}

```

如果你请求了内嵌缩略图，该图像无法直接从 [AVCapturePhoto](avcapturephoto.md) 对象访问——它内嵌在通过调用照片对象的 [- fileDataRepresentation](<avcapturephoto/filedatarepresentation().md>) 方法获得的图像文件数据中。

## 另请参阅

### 更多捕捉选项

- [捕捉带深度的照片](capturing-photos-with-depth.md) — 获取带深度图的照片，以创建类似系统相机人像模式的效果（在兼容设备上）。
- [捕捉包围曝光照片序列](capturing-a-bracketed-photo-sequence.md) — 一次捕捉多张照片，并改变曝光时长或感光度等参数。
- [捕捉未压缩的图像数据](capturing-uncompressed-image-data.md) — 获取未经压缩的已处理图像数据，用于滤镜处理或无损输出。
