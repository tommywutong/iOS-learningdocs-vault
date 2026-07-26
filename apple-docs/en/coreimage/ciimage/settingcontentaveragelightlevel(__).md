---
title: 'settingContentAverageLightLevel(_:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/settingcontentaveragelightlevel(_:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/settingcontentaveragelightlevel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/settingcontentaveragelightlevel%28_%3A%29.json'
content_hash: 'sha256:c9b8360c11987617'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# settingContentAverageLightLevel(_:)

<sub>Instance Method</sub>

Create an image by changing the receiver’s contentAverageLightLevel property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func settingContentAverageLightLevel(_ average: Float) -> CIImage
```

## Return Value

An autoreleased [CIImage](../ciimage.md).

## Discussion

Changing this value will alter the behavior of the `CIToneMapHeadroom` and `CISystemToneMap` filters.

- If the value is set to 0.0 or less then the returned image’s [contentAverageLightLevel](contentaveragelightlevel.md) is unknown.
