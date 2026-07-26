---
title: childForHomeIndicatorAutoHidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/childforhomeindicatorautohidden
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/childforhomeindicatorautohidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/childforhomeindicatorautohidden.json'
content_hash: 'sha256:65caab02b02c9a38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# childForHomeIndicatorAutoHidden

<sub>Instance Property</sub>

Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var childForHomeIndicatorAutoHidden: UIViewController? { get }
```

## Return Value

The child view controller to consult. The default implementation of this method returns `nil`.

## Discussion

When implementing a container view controller, override this method if you want one your child view controllers to determine whether to display the visual indicator. If you do, the system calls the [prefersHomeIndicatorAutoHidden](prefershomeindicatorautohidden.md) method of the returned view controller. If the method returns `nil`, the system calls the [prefersHomeIndicatorAutoHidden](prefershomeindicatorautohidden.md) method of the current view controller.

## See Also

### Coordinating with system gestures

- [preferredScreenEdgesDeferringSystemGestures](preferredscreenedgesdeferringsystemgestures.md) — The screen edges for which you want your gestures to take precedence over the system gestures.
- [childViewControllerForScreenEdgesDeferringSystemGestures](childforscreenedgesdeferringsystemgestures.md) — Returns the child view controller that should be queried to see if its gestures should take precedence.
- [- setNeedsUpdateOfScreenEdgesDeferringSystemGestures](<setneedsupdateofscreenedgesdeferringsystemgestures().md>) — Notifies the system of changes to the screen edges that defer system gestures.
- [prefersHomeIndicatorAutoHidden](prefershomeindicatorautohidden.md) — A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [- setNeedsUpdateOfHomeIndicatorAutoHidden](<setneedsupdateofhomeindicatorautohidden().md>) — Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.
