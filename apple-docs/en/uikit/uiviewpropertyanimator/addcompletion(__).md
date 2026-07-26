---
title: 'addCompletion(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewpropertyanimator/addcompletion(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/addcompletion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/addcompletion%28_%3A%29.json'
content_hash: 'sha256:b1033676a3f24b44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# addCompletion(_:)

<sub>Instance Method</sub>

Adds the specified completion block to the animator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addCompletion(_ completion: @escaping (UIViewAnimatingPosition) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addCompletion() async -> UIViewAnimatingPosition
```

## Parameters

- `completion` — A block to execute when the animations finish. This block has no return value and takes the following parameter: - **finalPosition** — The ending position of the animations. Use this value to determine whether the animations stopped at the beginning, end, or somewhere in the middle.

## Discussion

Completion blocks are executed after the animations finish normally. If you call the [- stopAnimation:](<../uiviewanimating/stopanimation(__).md>) method, the completion blocks are not called if you specify [true](../../swift/true.md) for the method’s parameter. If you specify [false](../../swift/false.md) for the parameter, the animator executes the completion blocks normally after you call the its [- finishAnimationAtPosition:](<../uiviewanimating/finishanimation(at_).md>) method.

You may add completion blocks to an animator at any time, including while it is stopped.

## See Also

### Modifying animations

- [- addAnimations:](<addanimations(__).md>) — Adds the specified animation block to the animator.
- [- addAnimations:delayFactor:](<addanimations(__delayfactor_).md>) — Adds the specified animation block with a delay.
- [- continueAnimationWithTimingParameters:durationFactor:](<continueanimation(withtimingparameters_durationfactor_).md>) — Adjusts the timing and duration of a paused animation.
