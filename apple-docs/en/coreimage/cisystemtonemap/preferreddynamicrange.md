---
title: preferredDynamicRange
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cisystemtonemap/preferreddynamicrange
source_url: 'https://developer.apple.com/documentation/coreimage/cisystemtonemap/preferreddynamicrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cisystemtonemap/preferreddynamicrange.json'
content_hash: 'sha256:5cc8626b48a37e3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CISystemToneMap](../cisystemtonemap.md)

# preferredDynamicRange

<sub>Instance Property</sub>

Specifies the preferred dynamic range behavior of the tone mapping. The value should be kCIDynamicRangeStandard, kCIDynamicRangeConstrainedHigh, kCIDynamicRangeHigh or nil.  If nil then it will behave as kCIDynamicRangeHigh.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preferredDynamicRange: CIDynamicRangeOption? { get set }
```
