---
title: 'settingContentHeadroom(_:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/settingcontentheadroom(_:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/settingcontentheadroom(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/settingcontentheadroom%28_%3A%29.json'
content_hash: 'sha256:16e3824515f30697'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# settingContentHeadroom(_:)

<sub>Instance Method</sub>

Create an image by changing the receiver’s contentHeadroom property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func settingContentHeadroom(_ headroom: Float) -> CIImage
```

## Return Value

An autoreleased [CIImage](../ciimage.md).

## Discussion

Changing this value will alter the behavior of the `CIToneMapHeadroom` and `CISystemToneMap` filters.

- If the value is set to 0.0 then the returned image’s headroom is unknown.
- If the value is set to 1.0 then the returned image is SDR.
- If the value is set to greater 1.0 then the returned image is HDR.
- Otherwise the returned image’s headroom is unknown.
