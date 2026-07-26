---
title: children
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/children
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/children'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/children.json'
content_hash: 'sha256:84766b1730f7cd6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# children

<sub>Instance Property</sub>

An array of view controllers that are children of the current view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var children: [UIViewController] { get }
```

## Discussion

This property does not include any presented view controllers. This property is only intended to be read by an implementation of a custom container view controller.

## See Also

### Managing child view controllers in a custom container

- [- addChildViewController:](<addchild(__).md>) — Adds the specified view controller as a child of the current view controller.
- [- removeFromParentViewController](<removefromparent().md>) — Removes the view controller from its parent.
- [- transitionFromViewController:toViewController:duration:options:animations:completion:](<transition(from_to_duration_options_animations_completion_).md>) — Transitions between two of the view controller’s child view controllers.
- [shouldAutomaticallyForwardAppearanceMethods](shouldautomaticallyforwardappearancemethods.md) — Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.
- [- beginAppearanceTransition:animated:](<beginappearancetransition(__animated_).md>) — Tells a child controller its appearance is about to change.
- [- endAppearanceTransition](<endappearancetransition().md>) — Tells a child controller its appearance has changed.
- [UIViewControllerHierarchyInconsistencyException](hierarchyinconsistencyexception.md) — Raised if the view controller hierarchy is inconsistent with the view hierarchy.
