---
title: translateY
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cavaluefunctionname/translatey
source_url: 'https://developer.apple.com/documentation/quartzcore/cavaluefunctionname/translatey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cavaluefunctionname/translatey.json'
content_hash: 'sha256:71cb73603c09a29c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAValueFunctionName](../cavaluefunctionname.md)

# translateY

<sub>Type Property</sub>

A value function translates by the input value along the y-axis. Animations referencing this value function must provide a single input value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let translateY: CAValueFunctionName
```

## See Also

### Constants

- [kCAValueFunctionTranslate](translate.md) — A value function that translates by the input values along all three axis. Animations using this value transform function must provide animation values in an `NSArray` of three `NSNumber` instances that specify the (x, y, z) translate values.
- [kCAValueFunctionTranslateX](translatex.md) — A value function translates by the input value along the x-axis. Animations referencing this value function must provide a single input value.
- [kCAValueFunctionTranslateZ](translatez.md) — A value function translates by the input value along the z-axis. Animations referencing this value function must provide a single input value.
