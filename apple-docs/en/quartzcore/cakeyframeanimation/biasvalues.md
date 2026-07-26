---
title: biasValues
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cakeyframeanimation/biasvalues
source_url: 'https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/biasvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cakeyframeanimation/biasvalues.json'
content_hash: 'sha256:c4d4df94952d33a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAKeyframeAnimation](../cakeyframeanimation.md)

# biasValues

<sub>Instance Property</sub>

An array of numbers that define the position of the curve relative to a control point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var biasValues: [NSNumber]? { get set }
```

## Discussion

This property is an array of [NSNumber](../../foundation/nsnumber.md) objects, used only for the cubic calculation modes. Positive values move the curve before the control point while negative values move it after the control point. The first value defines the behavior of the tangent to the first control point, the second value controls the second point’s tangents, and so on. If you do not specify a value for a given control point, the value `0` is used.

## See Also

### Cubic Mode Attributes

- [tensionValues](tensionvalues.md) — An array of numbers that define the tightness of the curve.
- [continuityValues](continuityvalues.md) — An array of numbers that define the sharpness of the timing curve’s corners.
