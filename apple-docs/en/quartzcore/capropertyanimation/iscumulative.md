---
title: isCumulative
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/capropertyanimation/iscumulative
source_url: 'https://developer.apple.com/documentation/quartzcore/capropertyanimation/iscumulative'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/capropertyanimation/iscumulative.json'
content_hash: 'sha256:b8fa595403520587'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAPropertyAnimation](../capropertyanimation.md)

# isCumulative

<sub>Instance Property</sub>

Determines if the value of the property is the value at the end of the previous repeat cycle, plus the value of the current repeat cycle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isCumulative: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), then the value of the property is the value at the end of the previous repeat cycle, plus the value of the current repeat cycle. If [false](../../swift/false.md), the value of the property is simply the value calculated for the current repeat cycle. The default is [false](../../swift/false.md).

## See Also

### Property Value Calculation Behavior

- [additive](isadditive.md) — Determines if the value specified by the animation is added to the current render tree value to produce the new render tree value.
- [valueFunction](valuefunction.md) — An optional value function that is applied to interpolated values.
