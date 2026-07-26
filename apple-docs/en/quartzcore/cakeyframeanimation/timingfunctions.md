---
title: timingFunctions
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cakeyframeanimation/timingfunctions
source_url: 'https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/timingfunctions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cakeyframeanimation/timingfunctions.json'
content_hash: 'sha256:2559512e099091a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAKeyframeAnimation](../cakeyframeanimation.md)

# timingFunctions

<sub>Instance Property</sub>

An optional array of `CAMediaTimingFunction` objects that define the pacing for each keyframe segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var timingFunctions: [CAMediaTimingFunction]? { get set }
```

## Discussion

You can use this array to apply ease-in, ease-out, or custom timing curves to the points that lie between two keyframe values. If the number of keyframes in the values property is _n_, then this property should contain _n_`-1` objects.

If you provide timing information in the [keyTimes](keytimes.md) property, the timing functions you specify using this property further modify the timing between those values. If you do not assign a value to the [keyTimes](keytimes.md) property, the timing functions modify the default timing provided by the animation object.

If you also specify a timing function in the animation object’s [timingFunction](../caanimation/timingfunction.md) property, that function is applied first followed by the timing function for the specific keyframe segment.

For information on how to create a timing function, see [CAMediaTimingFunction](../camediatimingfunction.md).

## See Also

### Keyframe timing

- [keyTimes](keytimes.md) — An optional array of `NSNumber` objects that define the time at which to apply a given keyframe segment.
- [calculationMode](calculationmode.md) — Specifies how intermediate keyframe values are calculated by the receiver.
