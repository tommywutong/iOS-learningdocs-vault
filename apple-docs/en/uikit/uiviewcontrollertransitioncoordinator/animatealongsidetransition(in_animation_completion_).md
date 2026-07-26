---
title: 'animateAlongsideTransition(in:animation:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollertransitioncoordinator/animatealongsidetransition(in:animation:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/animatealongsidetransition(in:animation:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinator/animatealongsidetransition%28in%3Aanimation%3Acompletion%3A%29.json'
content_hash: 'sha256:b327eec574ffab34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinator](../uiviewcontrollertransitioncoordinator.md)

# animateAlongsideTransition(in:animation:completion:)

<sub>Instance Method</sub>

Runs the specified animations in a view that’s outside of the designated container view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func animateAlongsideTransition(in view: UIView?, animation: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((any UIViewControllerTransitionCoordinatorContext) -> Void)? = nil) -> Bool
```

## Parameters

- `view` — The view (or one of its ancestors) in which the specified animations take place. This parameter must not be `nil`.

- `animation` — A block containing the animations you want to perform. These animations run in the same context as the transition animations and therefore have the same default attributes. You may specify `nil` for this parameter. The block has no return value and takes the following parameter: - **context** — The contextual information for performing the animations. Use this object to get the animation-related information. For more information, see [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md).

- `completion` — The block of code to execute after the transition finishes. You may specify `nil` for this parameter. The block has no return value and takes the following parameter: - **context** — The contextual information for performing the animations. Use this object to get the animation-related information. For more information, see [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md).

## Return Value

[true](../../swift/true.md) if the specified animation is successfully queued to run; otherwise [false](../../swift/false.md).

## Discussion

Use this method to perform animations that aren’t handled by the animator objects themselves. The animations you specify in the `animation` parameter must all take place in a view descended from the view you specify in the `view` parameter.

The animations in the `animation` parameter are normally performed concurrently with the view controller transition animations. That behavior applies when the animator object’s [- animateTransition:](<../uiviewcontrolleranimatedtransitioning/animatetransition(using_).md>) method is implemented using [UIView](../uiview.md)-based animations. If the animator object uses Core Animation to animate the layer contents directly, your animations are run shortly after the animateTransition: method returns.

This method returns [false](../../swift/false.md) when the block in the `animation` parameter can’t be queued to run. The completion block can still run even when this method returns [false](../../swift/false.md).

## See Also

### Responding to view controller transition progress

- [- animateAlongsideTransition:completion:](<animate(alongsidetransition_completion_).md>) — Runs the specified animations at the same time as the view controller transition animations.
- [- notifyWhenInteractionChangesUsingBlock:](<notifywheninteractionchanges(__).md>) — Registers a block to be executed when a transition changes from interactive to non-interactive.
- [- notifyWhenInteractionEndsUsingBlock:](<notifywheninteractionends(__).md>) — Registers a block to be executed when a transition changes from interactive to non-interactive. _(deprecated)_
