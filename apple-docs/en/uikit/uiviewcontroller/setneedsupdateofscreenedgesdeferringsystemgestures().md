---
title: setNeedsUpdateOfScreenEdgesDeferringSystemGestures()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/setneedsupdateofscreenedgesdeferringsystemgestures()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofscreenedgesdeferringsystemgestures()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/setneedsupdateofscreenedgesdeferringsystemgestures%28%29.json'
content_hash: 'sha256:150f372dd8cf7019'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setNeedsUpdateOfScreenEdgesDeferringSystemGestures()

<sub>Instance Method</sub>

Notifies the system of changes to the screen edges that defer system gestures.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setNeedsUpdateOfScreenEdgesDeferringSystemGestures()
```

## Discussion

Call this method whenever you modify the screen edges that defer system gestures, such as those that invoke Control Center, so the system can update accordingly. If the [childViewControllerForScreenEdgesDeferringSystemGestures](childforscreenedgesdeferringsystemgestures.md) property is `nil`, the system reads the edges from the current view controller’s [preferredScreenEdgesDeferringSystemGestures](preferredscreenedgesdeferringsystemgestures.md) property; otherwise, it uses the same property on the referenced child view controller.

## See Also

### Coordinating with system gestures

- [preferredScreenEdgesDeferringSystemGestures](preferredscreenedgesdeferringsystemgestures.md) — The screen edges for which you want your gestures to take precedence over the system gestures.
- [childViewControllerForScreenEdgesDeferringSystemGestures](childforscreenedgesdeferringsystemgestures.md) — Returns the child view controller that should be queried to see if its gestures should take precedence.
- [prefersHomeIndicatorAutoHidden](prefershomeindicatorautohidden.md) — A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [childViewControllerForHomeIndicatorAutoHidden](childforhomeindicatorautohidden.md) — Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
- [- setNeedsUpdateOfHomeIndicatorAutoHidden](<setneedsupdateofhomeindicatorautohidden().md>) — Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.
