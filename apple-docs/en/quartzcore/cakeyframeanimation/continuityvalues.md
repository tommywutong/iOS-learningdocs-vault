---
title: continuityValues
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cakeyframeanimation/continuityvalues
source_url: 'https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/continuityvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cakeyframeanimation/continuityvalues.json'
content_hash: 'sha256:a171f0bdf243e3a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAKeyframeAnimation](../cakeyframeanimation.md)

# continuityValues

<sub>Instance Property</sub>

An array of numbers that define the sharpness of the timing curve’s corners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var continuityValues: [NSNumber]? { get set }
```

## Discussion

This property is an array of [NSNumber](../../foundation/nsnumber.md) objects, used only for the cubic calculation modes. Positive values result in sharper corners while negative values create inverted corners. The first value defines the behavior of the tangent to the first control point, the second value controls the second point’s tangents, and so on. If you do not specify a value for a given control point, the value `0` is used.

## See Also

### Cubic Mode Attributes

- [tensionValues](tensionvalues.md) — An array of numbers that define the tightness of the curve.
- [biasValues](biasvalues.md) — An array of numbers that define the position of the curve relative to a control point.
