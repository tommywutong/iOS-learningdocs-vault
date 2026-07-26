---
title: 'addAnimations(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewimplicitlyanimating/addanimations(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating/addanimations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewimplicitlyanimating/addanimations%28_%3A%29.json'
content_hash: 'sha256:4a155e538c0fc04f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewImplicitlyAnimating](../uiviewimplicitlyanimating.md)

# addAnimations(_:)

<sub>Instance Method</sub>

Adds the specified animation block to the animator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func addAnimations(_ animation: @escaping () -> Void)
```

## Parameters

- `animation` — A block containing the animations to add to the animator object. This block has no return value and takes no parameters.

## Discussion

Use this method to add new animation blocks to your custom animator object. The animations in the specified block should run alongside any previously configured animations, starting at the current time and finishing at the same time as any original animations. Your implementation must be able to handle multiple calls to this method.

## See Also

### Modifying animations

- [- addAnimations:delayFactor:](<addanimations(__delayfactor_).md>) — Adds the specified animation block to the animator with a delay.
- [- addCompletion:](<addcompletion(__).md>) — Adds the specified completion block to the animator.
- [- continueAnimationWithTimingParameters:durationFactor:](<continueanimation(withtimingparameters_durationfactor_).md>) — Adjusts the final timing and duration of a paused animation.
