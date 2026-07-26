---
title: linear
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caanimationcalculationmode/linear
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimationcalculationmode/linear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimationcalculationmode/linear.json'
content_hash: 'sha256:271b035ec5692d5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimationCalculationMode](../caanimationcalculationmode.md)

# linear

<sub>Type Property</sub>

Simple linear calculation between keyframe values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let linear: CAAnimationCalculationMode
```

## Discussion

The following code shows how to create a keyframe animation object using linear interpolation.

Listing 1. Creating linearly interpolated keyframes

```swift
let keyframeAnimation = CAKeyframeAnimation(keyPath: "position.y")
keyframeAnimation.calculationMode = kCAAnimationLinear
keyframeAnimation.keyTimes = [0, 0.25, 0.5, 0.75, 1]
keyframeAnimation.values = [310, 60, 120, 60, 310]
```

A layer animated with the keyframe animation created by the code above and with linearly interpolated horizontal movement would describe a path similar to the following figure.

![Tracing the path of an animation using linearly interpolated keyframes](../../../../attachments/0c5d43aa12ef1a5f2a1deb521dc2f0c1/media-2776788@2x.png)

## See Also

### Constants

- [kCAAnimationDiscrete](discrete.md) — Each keyframe value is used in turn, no interpolated values are calculated.
- [kCAAnimationPaced](paced.md) — Linear keyframe values are interpolated to produce an even pace throughout the animation.
- [kCAAnimationCubic](cubic.md) — Smooth spline calculation between keyframe values.
- [kCAAnimationCubicPaced](cubicpaced.md) — Cubic keyframe values are interpolated to produce an even pace throughout the animation.
