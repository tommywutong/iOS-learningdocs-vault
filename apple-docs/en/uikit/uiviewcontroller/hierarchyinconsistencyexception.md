---
title: hierarchyInconsistencyException
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/hierarchyinconsistencyexception
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/hierarchyinconsistencyexception'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/hierarchyinconsistencyexception.json'
content_hash: 'sha256:7e2dcea1a9c49172'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# hierarchyInconsistencyException

<sub>Type Property</sub>

Raised if the view controller hierarchy is inconsistent with the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class let hierarchyInconsistencyException: NSExceptionName
```

## Discussion

When a view controller’s view is added to the view hierarchy, the system walks up the view hierarchy to find the first parent view that has a view controller. That view controller must be the parent of the view controller whose view is being added. Otherwise, this exception is raised. This consistency check is also performed when a view controller is added as a child by calling the [- addChildViewController:](<addchild(__).md>) method.

It is also allowed for a view controller that has no parent to add its view to the view hierarchy. This is generally not recommended, but is useful in some special cases.

## See Also

### Managing child view controllers in a custom container

- [childViewControllers](children.md) — An array of view controllers that are children of the current view controller.
- [- addChildViewController:](<addchild(__).md>) — Adds the specified view controller as a child of the current view controller.
- [- removeFromParentViewController](<removefromparent().md>) — Removes the view controller from its parent.
- [- transitionFromViewController:toViewController:duration:options:animations:completion:](<transition(from_to_duration_options_animations_completion_).md>) — Transitions between two of the view controller’s child view controllers.
- [shouldAutomaticallyForwardAppearanceMethods](shouldautomaticallyforwardappearancemethods.md) — Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.
- [- beginAppearanceTransition:animated:](<beginappearancetransition(__animated_).md>) — Tells a child controller its appearance is about to change.
- [- endAppearanceTransition](<endappearancetransition().md>) — Tells a child controller its appearance has changed.
