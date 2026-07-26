---
title: paced
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caanimationcalculationmode/paced
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimationcalculationmode/paced'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimationcalculationmode/paced.json'
content_hash: 'sha256:aec3c84e141ef2a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimationCalculationMode](../caanimationcalculationmode.md)

# paced

<sub>Type Property</sub>

Linear keyframe values are interpolated to produce an even pace throughout the animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let paced: CAAnimationCalculationMode
```

## Discussion

`kCAAnimationPaced` gives a linearly interpolated animation, but [keyTimes](../cakeyframeanimation/keytimes.md) and [timingFunction](../caanimation/timingfunction.md) are ignored and keyframe times are automatically generated to give the animation a constant velocity.

The following code shows how to create a keyframe animation object using paced interpolation.

Listing 1. Creating paced key values

```objc
let keyframeAnimation = CAKeyframeAnimation(keyPath: "position.y")
keyframeAnimation.calculationMode = kCAAnimationPaced
keyframeAnimation.values = [310, 60, 120, 60, 310]
```

A layer animated with the keyframe animation created by the code above and with linearly interpolated horizontal movement would describe a path similar to the following figure.

![Tracing the path of an animation using paced key values](../../../../attachments/59fe9ad7c28a77c4f7d2456ef55d3394/media-2776792@2x.png)

## See Also

### Constants

- [kCAAnimationLinear](linear.md) — Simple linear calculation between keyframe values.
- [kCAAnimationDiscrete](discrete.md) — Each keyframe value is used in turn, no interpolated values are calculated.
- [kCAAnimationCubic](cubic.md) — Smooth spline calculation between keyframe values.
- [kCAAnimationCubicPaced](cubicpaced.md) — Cubic keyframe values are interpolated to produce an even pace throughout the animation.
