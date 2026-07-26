---
title: shouldAutomaticallyForwardAppearanceMethods
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/shouldautomaticallyforwardappearancemethods
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/shouldautomaticallyforwardappearancemethods'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/shouldautomaticallyforwardappearancemethods.json'
content_hash: 'sha256:9add5020feb4abcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# shouldAutomaticallyForwardAppearanceMethods

<sub>Instance Property</sub>

Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var shouldAutomaticallyForwardAppearanceMethods: Bool { get }
```

## Return Value

[true](../../swift/true.md) if appearance methods are forwarded or [false](../../swift/false.md) if they are not.

## Discussion

This method is called to determine whether to automatically forward appearance-related containment callbacks to child view controllers.

The default implementation returns [true](../../swift/true.md). Subclasses of the [UIViewController](../uiviewcontroller.md) class that implement containment logic may override this method to control how these methods are forwarded. If you override this method and return [false](../../swift/false.md), you are responsible for telling the child when its views are going to appear or disappear. You do this by calling the child view controller’s [- beginAppearanceTransition:animated:](<beginappearancetransition(__animated_).md>) and [- endAppearanceTransition](<endappearancetransition().md>) methods.

## See Also

### Managing child view controllers in a custom container

- [childViewControllers](children.md) — An array of view controllers that are children of the current view controller.
- [- addChildViewController:](<addchild(__).md>) — Adds the specified view controller as a child of the current view controller.
- [- removeFromParentViewController](<removefromparent().md>) — Removes the view controller from its parent.
- [- transitionFromViewController:toViewController:duration:options:animations:completion:](<transition(from_to_duration_options_animations_completion_).md>) — Transitions between two of the view controller’s child view controllers.
- [- beginAppearanceTransition:animated:](<beginappearancetransition(__animated_).md>) — Tells a child controller its appearance is about to change.
- [- endAppearanceTransition](<endappearancetransition().md>) — Tells a child controller its appearance has changed.
- [UIViewControllerHierarchyInconsistencyException](hierarchyinconsistencyexception.md) — Raised if the view controller hierarchy is inconsistent with the view hierarchy.
