---
title: setNeedsUpdateOfHomeIndicatorAutoHidden()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/setneedsupdateofhomeindicatorautohidden()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofhomeindicatorautohidden()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/setneedsupdateofhomeindicatorautohidden%28%29.json'
content_hash: 'sha256:0ee904c0b794cab0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setNeedsUpdateOfHomeIndicatorAutoHidden()

<sub>Instance Method</sub>

Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setNeedsUpdateOfHomeIndicatorAutoHidden()
```

## Discussion

When you change the value returned by your view controller’s [prefersHomeIndicatorAutoHidden](prefershomeindicatorautohidden.md) or [childViewControllerForHomeIndicatorAutoHidden](childforhomeindicatorautohidden.md) method, call this method to let UIKit know that it should call those methods again.

## See Also

### Coordinating with system gestures

- [preferredScreenEdgesDeferringSystemGestures](preferredscreenedgesdeferringsystemgestures.md) — The screen edges for which you want your gestures to take precedence over the system gestures.
- [childViewControllerForScreenEdgesDeferringSystemGestures](childforscreenedgesdeferringsystemgestures.md) — Returns the child view controller that should be queried to see if its gestures should take precedence.
- [- setNeedsUpdateOfScreenEdgesDeferringSystemGestures](<setneedsupdateofscreenedgesdeferringsystemgestures().md>) — Notifies the system of changes to the screen edges that defer system gestures.
- [prefersHomeIndicatorAutoHidden](prefershomeindicatorautohidden.md) — A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [childViewControllerForHomeIndicatorAutoHidden](childforhomeindicatorautohidden.md) — Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
