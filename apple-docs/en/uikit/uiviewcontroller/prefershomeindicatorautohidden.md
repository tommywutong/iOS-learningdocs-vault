---
title: prefersHomeIndicatorAutoHidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/prefershomeindicatorautohidden
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/prefershomeindicatorautohidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/prefershomeindicatorautohidden.json'
content_hash: 'sha256:e4959a8ba5784cf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# prefersHomeIndicatorAutoHidden

<sub>Instance Property</sub>

A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var prefersHomeIndicatorAutoHidden: Bool { get }
```

## Return Value

[true](../../swift/true.md) if your view controller lets the system determine when to hide the indicator, or [false](../../swift/false.md) if you want the indicator to show at all times. The default implementation of this method returns [false](../../swift/false.md).

## Discussion

Override this method to signal your preference for displaying the visual indicator. The system takes your preference into account, but returning [true](../../swift/true.md) is no guarantee that the indicator will be hidden.

For information on allowing app-defined gestures to take precedence over system gestures for certain screen edges, see [preferredScreenEdgesDeferringSystemGestures](preferredscreenedgesdeferringsystemgestures.md).

## See Also

### Coordinating with system gestures

- [preferredScreenEdgesDeferringSystemGestures](preferredscreenedgesdeferringsystemgestures.md) — The screen edges for which you want your gestures to take precedence over the system gestures.
- [childViewControllerForScreenEdgesDeferringSystemGestures](childforscreenedgesdeferringsystemgestures.md) — Returns the child view controller that should be queried to see if its gestures should take precedence.
- [- setNeedsUpdateOfScreenEdgesDeferringSystemGestures](<setneedsupdateofscreenedgesdeferringsystemgestures().md>) — Notifies the system of changes to the screen edges that defer system gestures.
- [childViewControllerForHomeIndicatorAutoHidden](childforhomeindicatorautohidden.md) — Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
- [- setNeedsUpdateOfHomeIndicatorAutoHidden](<setneedsupdateofhomeindicatorautohidden().md>) — Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.
