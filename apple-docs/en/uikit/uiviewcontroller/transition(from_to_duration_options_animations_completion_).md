---
title: 'transition(from:to:duration:options:animations:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/transition(from:to:duration:options:animations:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/transition(from:to:duration:options:animations:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/transition%28from%3Ato%3Aduration%3Aoptions%3Aanimations%3Acompletion%3A%29.json'
content_hash: 'sha256:85d340b5b3cc8a91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# transition(from:to:duration:options:animations:completion:)

<sub>Instance Method</sub>

Transitions between two of the view controller’s child view controllers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func transition(from fromViewController: UIViewController, to toViewController: UIViewController, duration: TimeInterval, options: UIView.AnimationOptions = [], animations: (() -> Void)?, completion: ((Bool) -> Void)? = nil)
```

## Parameters

- `fromViewController` — A view controller whose view is currently visible in the parent’s view hierarchy.

- `toViewController` — A child view controller whose view is not currently in the view hierarchy.

- `duration` — The total duration of the animations, in seconds. If you pass zero, the changes are made without animating them.

- `options` — A mask of options indicating how you want to perform the animations. For a list of valid constants, see [AnimationOptions](../uiview/animationoptions.md).

- `animations` — A block object containing the changes to commit to the views. Here you programmatically change any animatable properties of the views in your view hierarchy. This block takes no parameters and has no return value. This parameter must not be `NULL`.

- `completion` — A block to be called when the animation completes. The block takes the following parameters: - **_finished_** — [true](../../swift/true.md) if the animation finished; [false](../../swift/false.md) if it was skipped.

## Discussion

This method adds the second view controller’s view to the view hierarchy and then performs the animations defined in your animations block. After the animation completes, it removes the first view controller’s view from the view hierarchy.

This method is only intended to be called by an implementation of a custom container view controller. If you override this method, you must call `super` in your implementation.

## See Also

### Managing child view controllers in a custom container

- [childViewControllers](children.md) — An array of view controllers that are children of the current view controller.
- [- addChildViewController:](<addchild(__).md>) — Adds the specified view controller as a child of the current view controller.
- [- removeFromParentViewController](<removefromparent().md>) — Removes the view controller from its parent.
- [shouldAutomaticallyForwardAppearanceMethods](shouldautomaticallyforwardappearancemethods.md) — Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.
- [- beginAppearanceTransition:animated:](<beginappearancetransition(__animated_).md>) — Tells a child controller its appearance is about to change.
- [- endAppearanceTransition](<endappearancetransition().md>) — Tells a child controller its appearance has changed.
- [UIViewControllerHierarchyInconsistencyException](hierarchyinconsistencyexception.md) — Raised if the view controller hierarchy is inconsistent with the view hierarchy.
