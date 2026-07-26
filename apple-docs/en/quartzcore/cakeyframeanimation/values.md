---
title: values
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cakeyframeanimation/values
source_url: 'https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cakeyframeanimation/values.json'
content_hash: 'sha256:916a7262c1415d29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAKeyframeAnimation](../cakeyframeanimation.md)

# values

<sub>Instance Property</sub>

An array of objects that specify the keyframe values to use for the animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var values: [Any]? { get set }
```

## Discussion

The keyframe values represent the values through which the animation must proceed. The time at which a given keyframe value is applied to the layer depends on the animation timing, which is controlled by the [calculationMode](calculationmode.md), [keyTimes](keytimes.md), and [timingFunctions](timingfunctions.md) properties. Values between keyframes are created using interpolation, unless the calculation mode is set to [kCAAnimationDiscrete](../caanimationcalculationmode/discrete.md).

Depending on the type of the property, you may need to wrap the values in this array with an [NSNumber](../../foundation/nsnumber.md) of [NSValue](../../foundation/nsvalue.md) object. For some Core Graphics data types, you may also need to cast them to `id` before adding them to the array.

The values in this property are used only if the value in the [path](path.md) property is `nil`.

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)

### Providing keyframe values

- [path](path.md) — The path for a point-based property to follow.
