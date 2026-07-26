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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# browserAccessibilityImageData(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func browserAccessibilityImageData(_ attributes: [AnyHashable : Any]) -> CVPixelBuffer?
```

## Parameters

- `attributes` — A dictionary of CVPixelBuffer attributes specifying the desired format and size.

## Return Value

A CVPixelBuffer containing the image pixel data, or NULL if this element does not represent an image or the requested pixel format is unsupported. The caller is responsible for releasing the returned pixel buffer.

## Discussion

Returns image pixel data for this element as a CVPixelBuffer.

Supported keys: kCVPixelBufferPixelFormatTypeKey (NSNumber / OSType) — The desired pixel format, e.g. kCVPixelFormatType_32RGBA. Required. kCVPixelBufferWidthKey  (NSNumber) — Target image width in pixels. Absent means native width. kCVPixelBufferHeightKey (NSNumber) — Target image height in pixels. Absent means native height.
