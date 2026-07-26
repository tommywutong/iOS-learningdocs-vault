---
title: keyTimes
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cakeyframeanimation/keytimes
source_url: 'https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/keytimes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cakeyframeanimation/keytimes.json'
content_hash: 'sha256:fde18a57fbb92e4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAKeyframeAnimation](../cakeyframeanimation.md)

# keyTimes

<sub>Instance Property</sub>

An optional array of `NSNumber` objects that define the time at which to apply a given keyframe segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var keyTimes: [NSNumber]? { get set }
```

## Discussion

Each value in the array is a floating point number between `0.0` and `1.0` that defines the time point (specified as a fraction of the animation’s total duration) at which to apply the corresponding keyframe value. Each successive value in the array must be greater than, or equal to, the previous value. Usually, the number of elements in the array should match the number of elements in the [values](values.md) property or the number of control points in the [path](path.md) property. If they do not, the timing of your animation might not be what you expect.

The appropriate values to include in the array are dependent on the [calculationMode](calculationmode.md) property.

- If the [calculationMode](calculationmode.md) is set to [kCAAnimationLinear](../caanimationcalculationmode/linear.md) or [kCAAnimationCubic](../caanimationcalculationmode/cubic.md), the first value in the array must be `0.0` and the last value must be `1.0`. All intermediate values represent time points between the start and end times.
- If the [calculationMode](calculationmode.md) is set to [kCAAnimationDiscrete](../caanimationcalculationmode/discrete.md), the first value in the array must be `0.0` and the last value must be `1.0`. The array should have one more entry than appears in the values array. For example, if there are two values, there should be three key times.
- If the [calculationMode](calculationmode.md) is set to [kCAAnimationPaced](../caanimationcalculationmode/paced.md) or [kCAAnimationCubicPaced](../caanimationcalculationmode/cubicpaced.md), the values in this property are ignored.

If the values in this array are invalid or inappropriate for the current calculation mode, they are ignored.

## See Also

### Keyframe timing

- [timingFunctions](timingfunctions.md) — An optional array of `CAMediaTimingFunction` objects that define the pacing for each keyframe segment.
- [calculationMode](calculationmode.md) — Specifies how intermediate keyframe values are calculated by the receiver.
