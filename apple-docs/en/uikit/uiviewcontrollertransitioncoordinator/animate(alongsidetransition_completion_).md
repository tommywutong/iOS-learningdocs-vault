---
title: 'animate(alongsideTransition:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollertransitioncoordinator/animate(alongsidetransition:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/animate(alongsidetransition:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinator/animate%28alongsidetransition%3Acompletion%3A%29.json'
content_hash: 'sha256:c8b997864bed247b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinator](../uiviewcontrollertransitioncoordinator.md)

# animate(alongsideTransition:completion:)

<sub>Instance Method</sub>

Runs the specified animations at the same time as the view controller transition animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func animate(alongsideTransition animation: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((any UIViewControllerTransitionCoordinatorContext) -> Void)? = nil) -> Bool
```

## Parameters

- `animation` — A block containing the animations you want to perform. These animations run in the same context as the transition animations and therefore have the same default attributes. You may specify `nil` for this parameter. The block has no return value and takes the following parameter: - **context** — The contextual information for performing the animations. Use this object to get the animation-related information, including the container view in which to run your animations. For more information, see [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md). The animation you specify must take place in a view descended from the container view.

- `completion` — The block of code to execute after the transition finishes. You may specify `nil` for this parameter. The block has no return value and takes the following parameter: - **context** — The contextual information for performing the animations. Use this object to get the animation-related information, including the container view in which to run your animations. For more information, see [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md).

## Return Value

[true](../../swift/true.md) if the animations were successfully queued to run or [false](../../swift/false.md) if they were not.

## Discussion

Use this method to perform animations that aren’t handled by the animator objects themselves. All of the animations you specify must occur inside the animation context’s container view (or one of its descendants). Use the [containerView](../uiviewcontrollertransitioncoordinatorcontext/containerview.md) property of the context object to get the container view. To perform animations in a view that doesn’t descend from the container view, use the [- animateAlongsideTransitionInView:animation:completion:](<animatealongsidetransition(in_animation_completion_).md>) method instead.

The animations in the `animation` parameter are normally performed concurrently with the view controller transition animations. That behavior applies when the animator object’s [- animateTransition:](<../uiviewcontrolleranimatedtransitioning/animatetransition(using_).md>) method is implemented using [UIView](../uiview.md)-based animations. If the animator object uses Core Animation to animate the layer contents directly, your animations are run shortly after the animateTransition: method returns.

This method returns [false](../../swift/false.md) when the block in the `animation` parameter can’t be queued to run. The completion block can still run even when this method returns [false](../../swift/false.md).

## See Also

### Responding to view controller transition progress

- [- animateAlongsideTransitionInView:animation:completion:](<animatealongsidetransition(in_animation_completion_).md>) — Runs the specified animations in a view that’s outside of the designated container view.
- [- notifyWhenInteractionChangesUsingBlock:](<notifywheninteractionchanges(__).md>) — Registers a block to be executed when a transition changes from interactive to non-interactive.
- [- notifyWhenInteractionEndsUsingBlock:](<notifywheninteractionends(__).md>) — Registers a block to be executed when a transition changes from interactive to non-interactive. _(deprecated)_
