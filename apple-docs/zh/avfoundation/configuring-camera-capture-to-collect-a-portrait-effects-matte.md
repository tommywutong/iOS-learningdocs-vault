---
title: 配置相机采集以收集人像效果蒙版
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/configuring-camera-capture-to-collect-a-portrait-effects-matte
source_url: 'https://developer.apple.com/documentation/avfoundation/configuring-camera-capture-to-collect-a-portrait-effects-matte'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/configuring-camera-capture-to-collect-a-portrait-effects-matte.json'
content_hash: 'sha256:fced6b8335f53cee'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Photo capture](photo-capture.md) · [AVPortraitEffectsMatte](avportraiteffectsmatte.md)

# 配置相机采集以收集人像效果蒙版

<sub>文章</sub>

让你的 App 准备好在拍照时采集人像效果蒙版（portrait effects matte）。

## 概述

在 iOS 相机 App 中拍摄照片时，你可以进入人像模式并检测到人脸，从而让人像效果蒙版得以生成。你可以通过查看取景框中是否出现四个黄色边框来判断相机是否找到了人脸；在人像模式下拍摄一张已检测到人脸的照片并不保证会生成蒙版，但这是一个前提条件。

与 iOS 相机 App 一样，你的 App 也可以选择加入人像效果蒙版的创建，并把蒙版嵌入拍摄的照片中，最终把它们保存为 HEIC 和 JPEG 图像。使用 AVFoundation 的 [AVCapturePhotoOutput](avcapturephotooutput.md)，你的 App 可以查明特定相机配置是否支持向静态图像交付人像效果蒙版，并选择加入以按单张照片请求的方式交付。[AVCapturePhotoOutput](avcapturephotooutput.md) 使用一个名为 [AVCapturePhoto](avcapturephoto.md) 的内存包装对象交付照片结果。

**Swift**

```swift
// private let photoOutput = AVCapturePhotoOutput()
...
// Check that portrait effects matte delivery is supported on this particular device:
if self.photoOutput.isPortraitEffectsMatteDeliverySupported {
    self.photoOutput.isPortraitEffectsMatteDeliveryEnabled = true
}
```

**Objective-C**

```objc
// AVCapturePhotoOutput* photoOutput;
...
// Check that portrait effects matte delivery is supported on this particular device:
if (self.photoOutput.portraitEffectsMatteDeliverySupported) {
    self.photoOutput.portraitEffectsMatteDeliveryEnabled = YES;
}
```

如果你已选择加入人像效果蒙版交付，可以在你的 [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) 中检查传给你的 [AVCaptureResolvedPhotoSettings](avcaptureresolvedphotosettings.md)，并读取 [portraitEffectsMatteDimensions](avcaptureresolvedphotosettings/portraiteffectsmattedimensions.md) 属性来了解将要交付的蒙版图像的尺寸，而不必把尺寸假设硬编码进代码。

即使你的 App 选择加入了蒙版交付，也不保证最终得到的 [AVCapturePhoto](avcapturephoto.md) 中会交付蒙版图像。负责生成人像效果蒙版的神经网络经过训练，用来检测和分割人物。如果图像场景中没有人，该图像就无法从人像效果蒙版中受益，因此不会交付蒙版。[AVCapturePhoto](avcapturephoto.md) 对象在 iOS 12 中新增了一个只读存取属性，用于访问图像的 [portraitEffectsMatte](avcapturephoto/portraiteffectsmatte.md)。如果你读取该属性且其返回值为 `nil`，说明没有为该图像生成人像效果蒙版（因为没有需要）。相机是作为后处理步骤生成蒙版图像的，因此你无法在拍摄照片之前检查是否会生成蒙版。你所能做的最佳做法，是使用 [AVMetadataFaceObject](avmetadatafaceobject.md) 检查检测到的人脸，并启用深度和人像效果蒙版。

人像效果蒙版算法结合使用人物分割和深度作为细化手段，因此只有支持深度的相机和相机格式才支持蒙版交付。人像效果蒙版图像不应嵌入到不包含深度图像的图像文件中；两者应一同保存。[AVCapturePhotoOutput](avcapturephotooutput.md) 层面会强制执行这条规则。如果你选择加入人像效果蒙版交付，并要求把它嵌入 [AVCapturePhotoOutput](avcapturephotooutput.md) 容器，那么你还必须选择加入嵌入式深度数据交付。

### 把拍摄的人像效果蒙版写入磁盘

[AVCapturePhoto](avcapturephoto.md) 通过 [- fileDataRepresentation](<avcapturephoto/filedatarepresentation().md>) 让客户端访问底层的内存文件容器。得到的 [NSData](../foundation/nsdata.md) 适合作为 HEIC 或 JPEG 文件写入磁盘。要替换或剥离图像文件中的人像效果蒙版，可调用 [- fileDataRepresentationWithCustomizer:](<avcapturephoto/filedatarepresentation(with_).md>)，它会调用一个自定器（customizer）对象，在把图像打包进适合写入磁盘的容器之前修改、替换或剥离图像的各个部分。

JPEG 和 HEIC 文件都可以存储嵌入式的人像效果蒙版数据。存储在 JFIF/JPEG 中时，蒙版使用 JPEG 压缩。存储在 HEIC 文件中时，它使用 HEVC 编解码器压缩。蒙版图像通常包含大片平坦的黑色或白色区域，因此压缩后的文件大小比 iOS 11 照片更小。

## 另请参阅

### 创建人像效果蒙版

- [+ portraitEffectsMatteFromDictionaryRepresentation:error:](<avportraiteffectsmatte/init(fromdictionaryrepresentation_).md>) — 从图像文件中的辅助图像信息初始化一个人像效果蒙版实例。
- [- portraitEffectsMatteByApplyingExifOrientation:](<avportraiteffectsmatte/applyingexiforientation(__).md>) — 应用指定的 EXIF 方向后，返回一个衍生的人像效果蒙版。
- [- portraitEffectsMatteByReplacingPortraitEffectsMatteWithPixelBuffer:error:](<avportraiteffectsmatte/replacingportraiteffectsmatte(with_).md>) — 通过包装替换用的像素缓冲，返回一个人像效果蒙版。
