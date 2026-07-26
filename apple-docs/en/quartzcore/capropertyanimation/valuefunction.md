---
title: valueFunction
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/capropertyanimation/valuefunction
source_url: 'https://developer.apple.com/documentation/quartzcore/capropertyanimation/valuefunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/capropertyanimation/valuefunction.json'
content_hash: 'sha256:f57afa410f77ca73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAPropertyAnimation](../capropertyanimation.md)

# valueFunction

<sub>Instance Property</sub>

An optional value function that is applied to interpolated values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var valueFunction: CAValueFunction? { get set }
```

## Discussion

If the `valueFunction` property is not `nil`, the function is applied to the values interpolated by the animation as they are applied to the presentation layer. Defaults to `nil`.

## See Also

### Property Value Calculation Behavior

- [cumulative](iscumulative.md) — Determines if the value of the property is the value at the end of the previous repeat cycle, plus the value of the current repeat cycle.
- [additive](isadditive.md) — Determines if the value specified by the animation is added to the current render tree value to produce the new render tree value.
