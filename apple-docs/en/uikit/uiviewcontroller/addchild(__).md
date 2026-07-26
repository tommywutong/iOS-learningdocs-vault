---
title: 'addChild(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/addchild(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/addchild(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/addchild%28_%3A%29.json'
content_hash: 'sha256:3ce550356cf920fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# addChild(_:)

<sub>Instance Method</sub>

Adds the specified view controller as a child of the current view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addChild(_ childController: UIViewController)
```

## Parameters

- `childController` — The view controller to be added as a child.

## Discussion

This method creates a parent-child relationship between the current view controller and the object in the `childController` parameter. This relationship is necessary when embedding the child view controller’s view into the current view controller’s content. If the new child view controller is already the child of a container view controller, it is removed from that container before being added.

This method is only intended to be called by an implementation of a custom container view controller. If you override this method, you must call `super` in your implementation.

## See Also

### Managing child view controllers in a custom container

- [childViewControllers](children.md) — An array of view controllers that are children of the current view controller.
- [- removeFromParentViewController](<removefromparent().md>) — Removes the view controller from its parent.
- [- transitionFromViewController:toViewController:duration:options:animations:completion:](<transition(from_to_duration_options_animations_completion_).md>) — Transitions between two of the view controller’s child view controllers.
- [shouldAutomaticallyForwardAppearanceMethods](shouldautomaticallyforwardappearancemethods.md) — Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.
- [- beginAppearanceTransition:animated:](<beginappearancetransition(__animated_).md>) — Tells a child controller its appearance is about to change.
- [- endAppearanceTransition](<endappearancetransition().md>) — Tells a child controller its appearance has changed.
- [UIViewControllerHierarchyInconsistencyException](hierarchyinconsistencyexception.md) — Raised if the view controller hierarchy is inconsistent with the view hierarchy.
