---
title: 'continueAnimation(withTimingParameters:durationFactor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewimplicitlyanimating/continueanimation(withtimingparameters:durationfactor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating/continueanimation(withtimingparameters:durationfactor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewimplicitlyanimating/continueanimation%28withtimingparameters%3Adurationfactor%3A%29.json'
content_hash: 'sha256:9927edb57035ca7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewImplicitlyAnimating](../uiviewimplicitlyanimating.md)

# continueAnimation(withTimingParameters:durationFactor:)

<sub>Instance Method</sub>

Adjusts the final timing and duration of a paused animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func continueAnimation(withTimingParameters parameters: (any UITimingCurveProvider)?, durationFactor: CGFloat)
```

## Parameters

- `parameters` — The new timing information to apply to the animation. Your custom animator determines how to transition from any current animations to the new animations specified by this parameter.

- `durationFactor` — A multiplying factor to apply to the animation’s original duration. Multiply this value by your animation’s original duration value to obtain the new duration for the animations.

## Discussion

Use this method to change the timing and duration parameters for the current animations temporarily. You define the conditions for which it’s safe to call this method, but typically it’s an error to call this method on an animator that’s inactive, running, or not interruptible. You should retain the original timing and duration values and restore them when your animator transitions back to the inactive state.

## See Also

### Related Documentation

- [- pauseAnimation](<../uiviewanimating/pauseanimation().md>) — Pauses a running animation at its current position.

### Modifying animations

- [- addAnimations:](<addanimations(__).md>) — Adds the specified animation block to the animator.
- [- addAnimations:delayFactor:](<addanimations(__delayfactor_).md>) — Adds the specified animation block to the animator with a delay.
- [- addCompletion:](<addcompletion(__).md>) — Adds the specified completion block to the animator.
