---
title: 'setConstraints(_:activeWhenNearEdge:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitrackinglayoutguide/setconstraints(_:activewhennearedge:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitrackinglayoutguide/setconstraints(_:activewhennearedge:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitrackinglayoutguide/setconstraints%28_%3Aactivewhennearedge%3A%29.json'
content_hash: 'sha256:e9e843d8a9b12e0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITrackingLayoutGuide](../uitrackinglayoutguide.md)

# setConstraints(_:activeWhenNearEdge:)

<sub>Instance Method</sub>

Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is close to the given edge.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setConstraints(_ trackingConstraints: [NSLayoutConstraint], activeWhenNearEdge edge: NSDirectionalRectEdge)
```

## Parameters

- `trackingConstraints` — The constraints to activate when the tracking layout guide is close to `edge`, and to deactivate when it moves away from `edge`. If you pass `nil`, the guide stops tracking the constraints associated with `edge`.

- `edge` — The edge that the tracking layout guide uses to determine whether to activate or deactivate the constraints.

## See Also

### Configuring automatic constraint activation

- [- setConstraints:activeWhenAwayFromEdge:](<setconstraints(__activewhenawayfrom_).md>) — Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is away from the given edge.
- [- constraintsActiveWhenNearEdge:](<constraints(activewhennearedge_).md>) — Returns the constraints that the tracking layout guide activates when it’s near the given edge, and deactivates when it’s away from the given edge.
- [- constraintsActiveWhenAwayFromEdge:](<constraints(activewhenawayfrom_).md>) — Returns the constraints that the tracking layout guide activates when it’s away from the given edge, and deactivates when it’s near the edge.
