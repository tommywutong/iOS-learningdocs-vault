---
title: endAppearanceTransition()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/endappearancetransition()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/endappearancetransition()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/endappearancetransition%28%29.json'
content_hash: 'sha256:25ae60e77050c4c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# endAppearanceTransition()

<sub>Instance Method</sub>

Tells a child controller its appearance has changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func endAppearanceTransition()
```

## Discussion

If you are implementing a custom container controller, use this method to tell the child that the view transition is complete.

## See Also

### Managing child view controllers in a custom container

- [childViewControllers](children.md) — An array of view controllers that are children of the current view controller.
- [- addChildViewController:](<addchild(__).md>) — Adds the specified view controller as a child of the current view controller.
- [- removeFromParentViewController](<removefromparent().md>) — Removes the view controller from its parent.
- [- transitionFromViewController:toViewController:duration:options:animations:completion:](<transition(from_to_duration_options_animations_completion_).md>) — Transitions between two of the view controller’s child view controllers.
- [shouldAutomaticallyForwardAppearanceMethods](shouldautomaticallyforwardappearancemethods.md) — Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.
- [- beginAppearanceTransition:animated:](<beginappearancetransition(__animated_).md>) — Tells a child controller its appearance is about to change.
- [UIViewControllerHierarchyInconsistencyException](hierarchyinconsistencyexception.md) — Raised if the view controller hierarchy is inconsistent with the view hierarchy.
