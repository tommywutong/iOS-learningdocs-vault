---
title: 'addCompletion(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewimplicitlyanimating/addcompletion(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating/addcompletion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewimplicitlyanimating/addcompletion%28_%3A%29.json'
content_hash: 'sha256:bc25ec85a4ea6d1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewImplicitlyAnimating](../uiviewimplicitlyanimating.md)

# addCompletion(_:)

<sub>Instance Method</sub>

Adds the specified completion block to the animator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func addCompletion(_ completion: @escaping (UIViewAnimatingPosition) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func addCompletion() async -> UIViewAnimatingPosition
```

## Parameters

- `completion` — A block to execute when the animations finish. This block has no return value and takes the following parameter: - **finalPosition** — The position where the animations stopped. Use this value to specify whether the animations stopped at their starting point, their end point, or their current position.

## Discussion

Use this method to add the completion blocks to your custom animator object. Completion blocks should execute after the animations finish successfully. If the [- stopAnimation:](<../uiviewanimating/stopanimation(__).md>) method is called, do not execute any completion blocks if the `withoutFinishing` parameter for that method contains the value [true](../../swift/true.md). If the parameter is [false](../../swift/false.md) and the client subsequent calls the [- finishAnimationAtPosition:](<../uiviewanimating/finishanimation(at_).md>) method, execute the completion blocks in your implementation of that method. Your implementation must be able to handle multiple calls to this method.

## See Also

### Modifying animations

- [- addAnimations:](<addanimations(__).md>) — Adds the specified animation block to the animator.
- [- addAnimations:delayFactor:](<addanimations(__delayfactor_).md>) — Adds the specified animation block to the animator with a delay.
- [- continueAnimationWithTimingParameters:durationFactor:](<continueanimation(withtimingparameters_durationfactor_).md>) — Adjusts the final timing and duration of a paused animation.
