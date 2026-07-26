---
title: translate
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cavaluefunctionname/translate
source_url: 'https://developer.apple.com/documentation/quartzcore/cavaluefunctionname/translate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cavaluefunctionname/translate.json'
content_hash: 'sha256:09b0fec9c46c68fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAValueFunctionName](../cavaluefunctionname.md)

# translate

<sub>Type Property</sub>

A value function that translates by the input values along all three axis. Animations using this value transform function must provide animation values in an `NSArray` of three `NSNumber` instances that specify the (x, y, z) translate values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let translate: CAValueFunctionName
```

## See Also

### Constants

- [kCAValueFunctionTranslateX](translatex.md) — A value function translates by the input value along the x-axis. Animations referencing this value function must provide a single input value.
- [kCAValueFunctionTranslateY](translatey.md) — A value function translates by the input value along the y-axis. Animations referencing this value function must provide a single input value.
- [kCAValueFunctionTranslateZ](translatez.md) — A value function translates by the input value along the z-axis. Animations referencing this value function must provide a single input value.
