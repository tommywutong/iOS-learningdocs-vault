---
title: 手动创建辅助深度数据
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/creating-auxiliary-depth-data-manually
source_url: 'https://developer.apple.com/documentation/avfoundation/creating-auxiliary-depth-data-manually'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/creating-auxiliary-depth-data-manually.json'
content_hash: 'sha256:2bb2a815bdafa700'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Additional data capture](additional-data-capture.md)

# 手动创建辅助深度数据

<sub>文章</sub>

生成一张深度图像并把它附加到你自己的图像上。

## 概述

iOS 人像模式会生成一张深度图，并把它作为辅助元数据附加到图像上。但对于自定效果，你可以生成自己的辅助深度图像——一张并非由 iOS 人像模式或其他支持深度的采集设备拍摄的图像。本文向你展示如何生成这种图并把它附加到你的图像上。

### 把像素值转换成兼容的浮点格式

深度图像是一种单分量图像，必须逐像素地把灰度像素值（`0` = 黑色到 `1` = 白色，即 zNear 到 zFar）转换为深度（以米为单位）或视差（以 1/米为单位）。然后把这些值调整为你想要的浮点格式。

视差或深度图像支持的像素格式包括：

- `kCVPixelFormatType_DisparityFloat16 = 'hdis'`：IEEE754-2008 binary16（半精度浮点数），描述比较两幅图像时的归一化偏移。单位为 1/米：(pixelShift / (pixelFocalLength * baselineInMeters))
- `kCVPixelFormatType_DisparityFloat32 = 'fdis'`：IEEE754-2008 binary32 浮点数，描述比较两幅图像时的归一化偏移。单位为 1/米：(pixelShift / (pixelFocalLength * baselineInMeters))
- `kCVPixelFormatType_DepthFloat16 = 'hdep'`：IEEE754-2008 binary16（半精度浮点数），描述以米为单位的深度（到物体的距离）
- `kCVPixelFormatType_DepthFloat32 = 'fdep'`：IEEE754-2008 binary32 浮点数，描述以米为单位的深度（到物体的距离）

把灰度图像载入一个 [CVPixelBuffer](../corevideo/cvpixelbuffer-q2e.md)。把它通过 [CVPixelBufferLockBaseAddress(_:_:)](<../corevideo/cvpixelbufferlockbaseaddress(____).md>) 获得的基址作为数据（[CFData](../corefoundation/cfdata.md)）载入，并把它作为 [kCGImageAuxiliaryDataInfoData](../imageio/kcgimageauxiliarydatainfodata.md) 的值传入一个字典（[CFDictionary](../corefoundation/cfdictionary.md)）。

### 解析元数据字典

这个字典的格式在 `CGImageSource.h` 中有文档说明。使用 [CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)](<../imageio/cgimagesourcecopyauxiliarydatainfoatindex(______).md>) 访问这个字典。该字典支持 JPEG、HEIF 和 DNG 图像。[CFDictionary](../corefoundation/cfdictionary.md) 按以下格式包含辅助数据：

- [kCGImageAuxiliaryDataInfoData](../imageio/kcgimageauxiliarydatainfodata.md) → 深度数据（[CFData](../corefoundation/cfdata.md)）
- [kCGImageAuxiliaryDataInfoDataDescription](../imageio/kcgimageauxiliarydatainfodatadescription.md) → 深度数据描述（[CFDictionary](../corefoundation/cfdictionary.md)：详见下文。）
- [kCGImageAuxiliaryDataInfoMetadata](../imageio/kcgimageauxiliarydatainfometadata.md) → 可选元数据（[CGImageMetadata](../imageio/cgimagemetadata.md)）

如果图像不包含 `auxiliaryImageDataType` 数据，[CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)](<../imageio/cgimagesourcecopyauxiliarydatainfoatindex(______).md>) 会返回 `nil`。

[kCGImageAuxiliaryDataInfoDataDescription](../imageio/kcgimageauxiliarydatainfodatadescription.md) 键的值是一个 [CFDictionary](../corefoundation/cfdictionary.md)，你需要填充它来告诉图像系统如何解释这张深度图。它可以包含以下深度数据参数：

- [kCGImagePropertyPixelFormat](../imageio/kcgimagepropertypixelformat.md) → Core Video 的 `CVPixelBuffer.h` 中深度或视差格式之一
- [kCGImagePropertyWidth](../imageio/kcgimagepropertywidth.md) 和 [kCGImagePropertyHeight](../imageio/kcgimagepropertyheight.md) → 像素尺寸
- [kCGImagePropertyBytesPerRow](../imageio/kcgimagepropertybytesperrow.md) → 深度图中每行的字节数

### 把你的自定深度图附加到图像上

按如下方式把深度或视差字典附加到图像：

1. 使用 [+ depthDataFromDictionaryRepresentation:error:](<avdepthdata/init(fromdictionaryrepresentation_).md>) 创建 [AVDepthData](avdepthdata.md)，传入深度或视差字典。
2. 创建图像目标（image destination）。
3. 使用 [Image I/O](../imageio.md) 的辅助方法创建图像。

```swift
// Add an image to the destination.
CGImageDestinationAddImage(cgImageDestination, renderedCGImage, attachments)  

// Use AVDepthData to get the auxiliary data dictionary.         
var auxDataType :NSString? 
let auxData = depthData.dictionaryRepresentation(forAuxiliaryDataType: &auxDataType)  

// Add auxiliary data to the image destination. 
CGImageDestinationAddAuxiliaryDataInfo(cgImageDestination, auxDataType!, auxData! as CFDictionary)  

if CGImageDestinationFinalize(cgImageDestination) {  
	return data as Data
}  
```

## 另请参阅

### 深度数据拍摄

- [拍摄带深度的照片](capturing-photos-with-depth.md) — 获取随照片一起的深度图，以创建类似系统相机人像模式的效果（在兼容设备上）。
- [使用 LiDAR 相机拍摄深度](capturing-depth-using-the-lidar-camera.md) — 在支持的设备上访问 LiDAR 相机以拍摄精确的深度数据。
- [AVCamFilter：为采集流应用滤镜](avcamfilter-applying-filters-to-a-capture-stream.md) — 以玫红色滤镜和深度效果渲染采集流。
- [从原深感相机流式传输深度数据](streaming-depth-data-from-the-truedepth-camera.md) — 以二维和三维方式将原深感相机的深度数据可视化。
- [利用原深感相机数据增强实时视频](enhancing-live-video-by-leveraging-truedepth-camera-data.md) — 为从前置原深感相机流式传输的实时采集画面应用你自己的背景。
- [AVCaptureDepthDataOutput](avcapturedepthdataoutput.md) — 一种在兼容的相机设备上记录场景深度信息的拍摄输出。
- [AVDepthData](avdepthdata.md) — 一种容器，保存兼容相机设备拍摄的逐像素距离或视差信息。
- [AVCameraCalibrationData](avcameracalibrationdata.md) — 关于拍摄图像和深度数据所用相机特性的信息。
