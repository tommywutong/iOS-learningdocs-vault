---
title: 在你的 App 中支持 HDR 图像
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/supporting-hdr-images-in-your-app
source_url: 'https://developer.apple.com/documentation/uikit/supporting-hdr-images-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/supporting-hdr-images-in-your-app.json'
content_hash: 'sha256:a3797680097dd2d2'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [图像与 PDF](images-and-pdf.md)

# 在你的 App 中支持 HDR 图像

<sub>示例代码</sub>

​ 使用 SwiftUI 和 Core Image 加载、显示、编辑和保存 HDR 图像。 ​

## 概述

此示例代码项目展示了如何使用 SwiftUI、UIKit、AppKit、Core Image 和 Core Graphics 读取、写入、编辑和显示 HDR 图像。它从磁盘或「照片」图库加载由多张图像组成的胶片带（film strip），然后让你能够以 HDR 格式选择、编辑和保存图像。该示例使用不同框架中的多项新 API，在完整的 HDR 工作流程中正确处理 HDR 图像。 ​

> [!note] 注意
> 此示例代码项目与 WWDC23 场次 10181：[在你的 App 中支持 HDR 图像](https://developer.apple.com/wwdc23/10181/)相关联。 ​

### 配置示例代码项目

在 Xcode 中运行此示例代码项目前，请确保 iOS 目标使用 iOS 17 或更高版本，Mac 目标使用 macOS 14 或更高版本。 ​

### 在图像视图上启用 HDR

为在 SwiftUI 图像视图中打开 HDR，该示例对胶片带使用 `allowedDynamicRange` 修饰器，以显示受限的 HDR 余量。

```swift
FilmStrip(assets: $assets, selectedAsset: $selectedAsset)
    .allowedDynamicRange(.constrainedHigh)
    .frame(height: geometry.size.height / 10.0)
```

​对于 UIKit 主图像视图，该示例向 `UIImageView` 添加 `preferredImageDynamicRange` 属性。 ​

```swift
let view = UIImageView()
view.preferredImageDynamicRange = .high
```

​ ​对于 AppKit，该示例向 `NSImageView` 添加此属性。

```swift
let view = NSImageView()
view.preferredImageDynamicRange = .high
```

​​ ​

### 使用 Core Image 编辑 HDR

为确保 Core Image 将增益映射 HDR（Gain Map HDR）图像作为 HDR 读取，该示例将 `CIImageOption.expandToHDR` 属性设为 `true`。为修改 HDR 图像数据，它使用 `CIFilter` 滤镜。

```swift
let ciOptions: [CIImageOption: Any] = [.applyOrientationProperty: true, .expandToHDR: true]
```

​ ​如果图像最初就是磁盘文件，该示例会将图像保存到磁盘。示例使用 `CIContext` 和 `CGImageDestination` 将 `CIImage` 渲染为 `CGImage`，并写入 10 位 HEIC 图像文件。

```swift
let cgImage = context.createCGImage(image,
                                    from: image.extent,
                                    format: .RGB10,
                                    colorSpace: colorspace ?? CGColorSpace(name: CGColorSpace.itur_2100_PQ)!,
                                    deferred: true)
```

​ ​该示例通过将 10 位 HEIC 图像写入 `PHContentEditingOutput` 对象的 `renderedContentURL`，把编辑后的 HDR 图像数据写回「照片」图库。只有在使用 `PhotosPicker` 从「照片」图库获取图像时，示例才会使用此路径。

```swift
guard let outputURL = try? output.renderedContentURL(for: .heic) else {
    print("Failed to obtain HEIC output URL.")
    return nil
}
```

## 另请参阅

### 创建图像

- [UIImageJPEGRepresentation](<uiimage/jpegdata(compressionquality_).md>) — 返回包含 JPEG 格式图像的数据对象。
- [UIImagePNGRepresentation](<uiimage/pngdata().md>) — 返回包含指定 PNG 格式图像的数据对象。

## 下载

- [SupportingHDRImagesInYourApp.zip](https://docs-assets.developer.apple.com/published/6bb6a5a2302b/SupportingHDRImagesInYourApp.zip)
