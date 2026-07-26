---
title: 'continueAnimation(withTimingParameters:durationFactor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewpropertyanimator/continueanimation(withtimingparameters:durationfactor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/continueanimation(withtimingparameters:durationfactor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/continueanimation%28withtimingparameters%3Adurationfactor%3A%29.json'
content_hash: 'sha256:55861ad5671e7874'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# continueAnimation(withTimingParameters:durationFactor:)

<sub>Instance Method</sub>

Adjusts the timing and duration of a paused animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func continueAnimation(withTimingParameters parameters: (any UITimingCurveProvider)?, durationFactor: CGFloat)
```

## Parameters

- `parameters` — The new timing information to apply to the animation. The animator may transition from the previous timing curve to the new timing curve over time to keep the transition from becoming too jarring. For example, if the previous timing curve used a spring animation, the animator may add some of spring behavior to the new animation.

- `durationFactor` — A multiplying factor to apply to the animation’s original duration. The value of this parameter is multiplied by the original [duration](duration.md) value to obtain the new duration for the animations.

## Discussion

This method overrides the timing and duration parameters for the current animations. When calling this method, the animator must be active and currently paused. It’s a programmer error to call this method when the animator is inactive, running, or its [interruptible](isinterruptible.md) property is set to [false](../../swift/false.md).

This method overrides the original timing and duration values only until the current animations finish. The original timing and duration values are restored when the animator transitions back to the inactive state.

## See Also

### Related Documentation

- [- pauseAnimation](<../uiviewanimating/pauseanimation().md>) — Pauses a running animation at its current position.

### Modifying animations

- [- addAnimations:](<addanimations(__).md>) — Adds the specified animation block to the animator.
- [- addAnimations:delayFactor:](<addanimations(__delayfactor_).md>) — Adds the specified animation block with a delay.
- [- addCompletion:](<addcompletion(__).md>) — Adds the specified completion block to the animator.
