---
title: inputImage
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cisigneddistancegradientfromredmask/inputimage
source_url: 'https://developer.apple.com/documentation/coreimage/cisigneddistancegradientfromredmask/inputimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cisigneddistancegradientfromredmask/inputimage.json'
content_hash: 'sha256:cebe25d75cf06b67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CISignedDistanceGradientFromRedMask](../cisigneddistancegradientfromredmask.md)

# inputImage

<sub>Instance Property</sub>

The input image whose red channel defines a mask. If the red channel pixel value is greater than 0.5 then the point is considered in the mask and output pixel will be a value between zero and negative one. Otherwise the output pixel will be a value between zero and one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var inputImage: CIImage? { get set }
```
