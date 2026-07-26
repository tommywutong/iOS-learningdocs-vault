---
title: childForScreenEdgesDeferringSystemGestures
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/childforscreenedgesdeferringsystemgestures
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/childforscreenedgesdeferringsystemgestures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/childforscreenedgesdeferringsystemgestures.json'
content_hash: 'sha256:6c1b949ccb16a329'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# childForScreenEdgesDeferringSystemGestures

<sub>Instance Property</sub>

Returns the child view controller that should be queried to see if its gestures should take precedence.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var childForScreenEdgesDeferringSystemGestures: UIViewController? { get }
```

## Discussion

When implementing a container view controller, override this method if one of your child view controllers defines screen-edge gestures that should take precedence over the system gestures. UIKit then uses the [preferredScreenEdgesDeferringSystemGestures](preferredscreenedgesdeferringsystemgestures.md) property of the returned child view controller to determine which screen edges have competing gesture recognizers.

## See Also

### Coordinating with system gestures

- [preferredScreenEdgesDeferringSystemGestures](preferredscreenedgesdeferringsystemgestures.md) — The screen edges for which you want your gestures to take precedence over the system gestures.
- [- setNeedsUpdateOfScreenEdgesDeferringSystemGestures](<setneedsupdateofscreenedgesdeferringsystemgestures().md>) — Notifies the system of changes to the screen edges that defer system gestures.
- [prefersHomeIndicatorAutoHidden](prefershomeindicatorautohidden.md) — A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [childViewControllerForHomeIndicatorAutoHidden](childforhomeindicatorautohidden.md) — Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
- [- setNeedsUpdateOfHomeIndicatorAutoHidden](<setneedsupdateofhomeindicatorautohidden().md>) — Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.
