---
title: scaleX
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cavaluefunctionname/scalex
source_url: 'https://developer.apple.com/documentation/quartzcore/cavaluefunctionname/scalex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cavaluefunctionname/scalex.json'
content_hash: 'sha256:825a687babf48e08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAValueFunctionName](../cavaluefunctionname.md)

# scaleX

<sub>Type Property</sub>

A value function scales by the input value along the x-axis. Animations referencing this value transform function must provide a single animation value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let scaleX: CAValueFunctionName
```

## See Also

### Constants

- [kCAValueFunctionScale](scale.md) — A value function scales by the input value along all three axis. Animations using this value transform function must provide animation values in an `NSArray` of three `NSNumber` instances that specify the (x, y, z) scale values.
- [kCAValueFunctionScaleY](scaley.md) — A value function scales by the input value along the y-axis. Animations referencing this value function must provide a single animation value.
- [kCAValueFunctionScaleZ](scalez.md) — A value function that scales by the input value along the z-axis. Animations referencing this value function must provide a single animation value.
