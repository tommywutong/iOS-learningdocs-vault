---
title: preferredScreenEdgesDeferringSystemGestures
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/preferredscreenedgesdeferringsystemgestures
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredscreenedgesdeferringsystemgestures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/preferredscreenedgesdeferringsystemgestures.json'
content_hash: 'sha256:44305a2cd2839000'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# preferredScreenEdgesDeferringSystemGestures

<sub>Instance Property</sub>

The screen edges for which you want your gestures to take precedence over the system gestures.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredScreenEdgesDeferringSystemGestures: UIRectEdge { get }
```

## Discussion

Normally, the screen-edge gestures defined by the system take precedence over any gesture recognizers that you define. The system uses its gestures to implement system-level behaviors, such as to display Control Center.

Whenever possible, you should allow the system gestures to take precedence. However, immersive apps can use this property to allow app-defined gestures to take precedence over the system gestures. You do that by overriding this property and returning the screen edges for which your gestures should take precedence.

If you change the edges preferred by your view controller, update the value of this property and call the [- setNeedsUpdateOfScreenEdgesDeferringSystemGestures](<setneedsupdateofscreenedgesdeferringsystemgestures().md>) method to notify the system that the edges have changed.

For information on showing and hiding the visual indicator for returning to the Home Screen, see [prefersHomeIndicatorAutoHidden](prefershomeindicatorautohidden.md).

## See Also

### Coordinating with system gestures

- [childViewControllerForScreenEdgesDeferringSystemGestures](childforscreenedgesdeferringsystemgestures.md) — Returns the child view controller that should be queried to see if its gestures should take precedence.
- [- setNeedsUpdateOfScreenEdgesDeferringSystemGestures](<setneedsupdateofscreenedgesdeferringsystemgestures().md>) — Notifies the system of changes to the screen edges that defer system gestures.
- [prefersHomeIndicatorAutoHidden](prefershomeindicatorautohidden.md) — A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [childViewControllerForHomeIndicatorAutoHidden](childforhomeindicatorautohidden.md) — Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
- [- setNeedsUpdateOfHomeIndicatorAutoHidden](<setneedsupdateofhomeindicatorautohidden().md>) — Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.
