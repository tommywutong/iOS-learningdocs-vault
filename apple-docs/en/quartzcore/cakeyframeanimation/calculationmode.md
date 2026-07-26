---
title: calculationMode
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cakeyframeanimation/calculationmode
source_url: 'https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/calculationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cakeyframeanimation/calculationmode.json'
content_hash: 'sha256:21c7648ef04e277a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAKeyframeAnimation](../cakeyframeanimation.md)

# calculationMode

<sub>Instance Property</sub>

Specifies how intermediate keyframe values are calculated by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var calculationMode: CAAnimationCalculationMode { get set }
```

## Discussion

The possible values are described in [Value calculation modes](../value-calculation-modes.md). The default value of this property is [kCAAnimationLinear](../caanimationcalculationmode/linear.md).

## See Also

### Keyframe timing

- [keyTimes](keytimes.md) — An optional array of `NSNumber` objects that define the time at which to apply a given keyframe segment.
- [timingFunctions](timingfunctions.md) — An optional array of `CAMediaTimingFunction` objects that define the pacing for each keyframe segment.
