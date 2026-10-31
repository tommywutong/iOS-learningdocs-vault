---
title: 捕捉未压缩的图像数据
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capturing-uncompressed-image-data
source_url: 'https://developer.apple.com/documentation/avfoundation/capturing-uncompressed-image-data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capturing-uncompressed-image-data.json'
content_hash: 'sha256:63d5993895a2f4e4'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [照片捕捉](photo-capture.md) · [捕捉静态照片和实况照片](capturing-still-and-live-photos.md)

# 捕捉未压缩的图像数据

<sub>文章</sub>

获取未经压缩的已处理图像数据，用于滤镜处理或无损输出。

## 概述

典型的摄影工作流程会以压缩格式（例如 HEIF/HEVC 或 JPEG）保存图像。这些格式使用有损压缩，在保留图像中可察觉的细节与降低数据存储需求之间取得平衡。然而，有时使用未压缩的图像数据更有帮助——例如，某些图像处理和分析算法可能会被有损压缩引入的视觉伪影干扰。

> [!note] 注意
> 未压缩的图像数据不要与未经处理的（即 RAW）图像数据混淆。RAW 数据是直接来自相机图像传感器的、经过最少处理的数据。未压缩的图像数据已经过处理以生成可显示的图像，但没有经过压缩来生成较小的文件。

在 iOS 中，捕捉未压缩的图像数据只需要对[捕捉静态照片和实况照片](capturing-still-and-live-photos.md)中介绍的基本摄影工作流程做少量修改。

### 选择未压缩格式设置

要以未压缩格式进行捕捉，请使用 [+ photoSettingsWithFormat:](<avcapturephotosettings/init(format_).md>) 创建一个照片设置对象。在格式字典中，用照片输出的 [availablePhotoPixelFormatTypes](avcapturephotooutput/availablephotopixelformattypes-6eyb.md) 数组中列出的某个值为 [kCVPixelBufferPixelFormatTypeKey](../corevideo/kcvpixelbufferpixelformattypekey.md) 指定值。下面的示例选择了 32 位 BGRA 像素格式，这在某些 GPU 处理工作流程中很有用：

```swift
// 选择 32 位 BGRA 像素格式，并验证相机是否支持它。
let pixelFormatType = kCVPixelFormatType_32BGRA
guard self.photoOutput.availablePhotoPixelFormatTypes.contains(pixelFormatType) else { return }
let photoSettings = AVCapturePhotoSettings(format:
    [ kCVPixelBufferPixelFormatTypeKey as String : pixelFormatType ])

// 使用自定类处理捕捉委托回调，拍摄照片。
let layerOrientation = previewView.videoPreviewLayer.connection!.videoOrientation
let colorSpace = self.videoCaptureDevice.activeColorSpace
let captureProcessor = UncompressedCaptureProcessor(orientation: layerOrientation,
                                                    colorSpace: colorSpace)
self.photoOutput.capturePhoto(with: photoSettings, delegate: captureProcessor)

```

### 处理结果

与其他格式一样，未压缩数据的捕捉结果会以 [AVCapturePhoto](avcapturephoto.md) 对象的形式送达你的委托的 [- captureOutput:didFinishProcessingPhoto:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) 方法。要直接访问未压缩的像素数据，请使用照片的 [pixelBuffer](avcapturephoto/pixelbuffer.md) 属性。

例如，以下代码将一个 Core Image 滤镜直接应用到像素缓冲区，并将滤镜处理后的图像写入 PNG 文件：

```swift
class UncompressedCaptureProcessor: NSObject, AVCapturePhotoCaptureDelegate {
    
    // 在捕捉完成之前，保留单独交付的 RAW 和压缩照片数据。
    func photoOutput(_ output: AVCapturePhotoOutput, didFinishProcessingPhoto photo: AVCapturePhoto, error: Error?) {
        guard error != nil else { print("Error capturing photo: \(error!)"); return }
        
        // 从像素缓冲区创建 CIImage 并应用滤镜
        let image = CIImage(cvPixelBuffer: photo.pixelBuffer!)
        let imageOrientation = self.imageOrientation(for: videoOrientation)
        let filteredImage = image.oriented(imageOrientation)
            .applyingFilter("CIPhotoEffectNoir", parameters: [:])
        
        let imageColorSpace = self.imageColorSpace(for: colorSpace)
        guard let pngData = CIContext()
            .pngRepresentation(of: filteredImage, format: kCIFormatBGRA8, colorSpace: imageColorSpace)
            else { print("Error creating filtered PNG image"); return }
        self.exportToFile(pngData)
    }
}
```

或者，要获得可直接写入文件的未压缩照片，请使用照片的 [- fileDataRepresentation](<avcapturephoto/filedatarepresentation().md>) 方法获取格式化为 TIFF 文件的数据。

## 另请参阅

### 更多捕捉选项

- [捕捉带深度的照片](capturing-photos-with-depth.md) — 获取带深度图的照片，以创建类似系统相机人像模式的效果（在兼容设备上）。
- [捕捉包围曝光照片序列](capturing-a-bracketed-photo-sequence.md) — 一次捕捉多张照片，并改变曝光时长或感光度等参数。
- [拍摄缩略图和预览图](capturing-thumbnail-and-preview-images.md) — 在照片捕捉中启用随主图像一起提供缩小尺寸的图像。
