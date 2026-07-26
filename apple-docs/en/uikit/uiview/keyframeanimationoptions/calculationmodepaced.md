---
title: calculationModePaced
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/keyframeanimationoptions/calculationmodepaced
source_url: 'https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions/calculationmodepaced'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/keyframeanimationoptions/calculationmodepaced.json'
content_hash: 'sha256:f518aa5c938a207c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIView](../../uiview.md) · [KeyframeAnimationOptions](../keyframeanimationoptions.md)

# calculationModePaced

<sub>Type Property</sub>

The option to compute intermediate keyframe values using a simple pacing algorithm.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var calculationModePaced: UIView.KeyframeAnimationOptions { get }
```

## Discussion

This option results in an evenly paced animation.

## See Also

### Constants

- [UIViewKeyframeAnimationOptionLayoutSubviews](layoutsubviews.md) — The option to lay out subviews at commit time so that they’re animated along with their parent.
- [UIViewKeyframeAnimationOptionAllowUserInteraction](allowuserinteraction.md) — The option that allows a person to interact with views while they’re being animated.
- [UIViewKeyframeAnimationOptionBeginFromCurrentState](beginfromcurrentstate.md) — The option to start an animation from the current setting associated with an already in-flight animation.
- [UIViewKeyframeAnimationOptionRepeat](repeat.md) — The option to repeat an animation indefinitely.
- [UIViewKeyframeAnimationOptionAutoreverse](autoreverse.md) — The option to run an animation backwards and forwards.
- [UIViewKeyframeAnimationOptionOverrideInheritedDuration](overrideinheritedduration.md) — The option to force an animation to use the original duration value specified when the animation was submitted.
- [UIViewKeyframeAnimationOptionOverrideInheritedOptions](overrideinheritedoptions.md) — The option to not inherit the animation type or any options.
- [UIViewKeyframeAnimationOptionCalculationModeLinear](calculationmodelinear.md) — The option to use a simple linear calculation when interpolating between keyframe values.
- [UIViewKeyframeAnimationOptionCalculationModeDiscrete](calculationmodediscrete.md) — The option to not interpolate between keyframe values, but rather to jump directly to each new keyframe value.
- [UIViewKeyframeAnimationOptionCalculationModeCubic](calculationmodecubic.md) — The option to compute intermediate frames using a default Catmull-Rom spline that passes through the keyframe values.
- [UIViewKeyframeAnimationOptionCalculationModeCubicPaced](calculationmodecubicpaced.md) — The option to compute intermediate frames using the cubic scheme while ignoring the timing properties of the animation.
