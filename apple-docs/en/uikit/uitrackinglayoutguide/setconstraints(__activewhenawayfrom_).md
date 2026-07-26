---
title: 'setConstraints(_:activeWhenAwayFrom:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitrackinglayoutguide/setconstraints(_:activewhenawayfrom:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitrackinglayoutguide/setconstraints(_:activewhenawayfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitrackinglayoutguide/setconstraints%28_%3Aactivewhenawayfrom%3A%29.json'
content_hash: 'sha256:dd9f91dd6a1859ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITrackingLayoutGuide](../uitrackinglayoutguide.md)

# setConstraints(_:activeWhenAwayFrom:)

<sub>Instance Method</sub>

Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is away from the given edge.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setConstraints(_ trackingConstraints: [NSLayoutConstraint], activeWhenAwayFrom edge: NSDirectionalRectEdge)
```

## Parameters

- `trackingConstraints` — The constraints to deactivate when the tracking layout guide is close to `edge`, and to activate when it moves away from `edge`. If you pass `nil`, the guide deactivates any currently active constraints associated with this edge and removes them from tracking.

- `edge` — The edge that the tracking layout guide uses to determine whether to activate or deactivate the constraints.

## See Also

### Configuring automatic constraint activation

- [- setConstraints:activeWhenNearEdge:](<setconstraints(__activewhennearedge_).md>) — Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is close to the given edge.
- [- constraintsActiveWhenNearEdge:](<constraints(activewhennearedge_).md>) — Returns the constraints that the tracking layout guide activates when it’s near the given edge, and deactivates when it’s away from the given edge.
- [- constraintsActiveWhenAwayFromEdge:](<constraints(activewhenawayfrom_).md>) — Returns the constraints that the tracking layout guide activates when it’s away from the given edge, and deactivates when it’s near the edge.
