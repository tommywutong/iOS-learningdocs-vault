---
title: 'browserAccessibilityImageData(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, macOS, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/browseraccessibilityimagedata(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/browseraccessibilityimagedata(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/browseraccessibilityimagedata%28_%3A%29.json'
content_hash: 'sha256:d9895af8fa1b97e7'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# browserAccessibilityImageData(_:)

<sub>实例方法</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func browserAccessibilityImageData(_ attributes: [AnyHashable : Any]) -> CVPixelBuffer?
```

## 参数

- `attributes` — 指定所需格式和大小的 CVPixelBuffer 属性字典。

## 返回值

包含图像像素数据的 CVPixelBuffer；若此元素不表示图像或请求的像素格式不受支持则为 NULL。调用者负责释放返回的像素缓冲区。

## 讨论

以 CVPixelBuffer 形式返回此元素的图像像素数据。

支持的键：kCVPixelBufferPixelFormatTypeKey（NSNumber / OSType）— 所需像素格式，例如 kCVPixelFormatType_32RGBA。必需。kCVPixelBufferWidthKey（NSNumber）— 目标图像宽度（像素）。缺省表示原生宽度。kCVPixelBufferHeightKey（NSNumber）— 目标图像高度（像素）。缺省表示原生高度。
