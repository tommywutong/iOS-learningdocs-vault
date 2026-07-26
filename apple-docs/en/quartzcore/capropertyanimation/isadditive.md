---
title: isAdditive
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/capropertyanimation/isadditive
source_url: 'https://developer.apple.com/documentation/quartzcore/capropertyanimation/isadditive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/capropertyanimation/isadditive.json'
content_hash: 'sha256:b58cd08477a02a4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAPropertyAnimation](../capropertyanimation.md)

# isAdditive

<sub>Instance Property</sub>

Determines if the value specified by the animation is added to the current render tree value to produce the new render tree value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isAdditive: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the value specified by the animation will be added to the current render tree value of the property to produce the new render tree value. The addition function is type-dependent, e.g. for affine transforms the two matrices are concatenated. The default is [false](../../swift/false.md).

## See Also

### Property Value Calculation Behavior

- [cumulative](iscumulative.md) — Determines if the value of the property is the value at the end of the previous repeat cycle, plus the value of the current repeat cycle.
- [valueFunction](valuefunction.md) — An optional value function that is applied to interpolated values.
