---
title: 'beginAppearanceTransition(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/beginappearancetransition(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/beginappearancetransition(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/beginappearancetransition%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:cec84f35c5390fd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# beginAppearanceTransition(_:animated:)

<sub>Instance Method</sub>

Tells a child controller its appearance is about to change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func beginAppearanceTransition(_ isAppearing: Bool, animated: Bool)
```

## Parameters

- `isAppearing` — [true](../../swift/true.md) if the child view controller’s view is about to be added to the view hierarchy, [false](../../swift/false.md) if it is being removed.

- `animated` — If [true](../../swift/true.md), the transition is being animated.

## Discussion

If you are implementing a custom container controller, use this method to tell the child that its views are about to appear or disappear. Do not invoke [- viewWillAppear:](<viewwillappear(__).md>), [- viewWillDisappear:](<viewwilldisappear(__).md>), [- viewDidAppear:](<viewdidappear(__).md>), or [- viewDidDisappear:](<viewdiddisappear(__).md>) directly.

## See Also

### Managing child view controllers in a custom container

- [childViewControllers](children.md) — An array of view controllers that are children of the current view controller.
- [- addChildViewController:](<addchild(__).md>) — Adds the specified view controller as a child of the current view controller.
- [- removeFromParentViewController](<removefromparent().md>) — Removes the view controller from its parent.
- [- transitionFromViewController:toViewController:duration:options:animations:completion:](<transition(from_to_duration_options_animations_completion_).md>) — Transitions between two of the view controller’s child view controllers.
- [shouldAutomaticallyForwardAppearanceMethods](shouldautomaticallyforwardappearancemethods.md) — Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.
- [- endAppearanceTransition](<endappearancetransition().md>) — Tells a child controller its appearance has changed.
- [UIViewControllerHierarchyInconsistencyException](hierarchyinconsistencyexception.md) — Raised if the view controller hierarchy is inconsistent with the view hierarchy.
