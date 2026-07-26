---
title: 'constraints(activeWhenAwayFrom:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitrackinglayoutguide/constraints(activewhenawayfrom:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitrackinglayoutguide/constraints(activewhenawayfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitrackinglayoutguide/constraints%28activewhenawayfrom%3A%29.json'
content_hash: 'sha256:5facd5a5be05e9dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITrackingLayoutGuide](../uitrackinglayoutguide.md)

# constraints(activeWhenAwayFrom:)

<sub>Instance Method</sub>

Returns the constraints that the tracking layout guide activates when it’s away from the given edge, and deactivates when it’s near the edge.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func constraints(activeWhenAwayFrom edge: NSDirectionalRectEdge) -> [NSLayoutConstraint]
```

## Parameters

- `edge` — The edge that the tracking layout guide uses to determine when to activate or deactivate the constraints.

## Return Value

An array of layout constraints that the tracking layout guide automatically activates and deactivates.

## See Also

### Configuring automatic constraint activation

- [- setConstraints:activeWhenNearEdge:](<setconstraints(__activewhennearedge_).md>) — Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is close to the given edge.
- [- setConstraints:activeWhenAwayFromEdge:](<setconstraints(__activewhenawayfrom_).md>) — Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is away from the given edge.
- [- constraintsActiveWhenNearEdge:](<constraints(activewhennearedge_).md>) — Returns the constraints that the tracking layout guide activates when it’s near the given edge, and deactivates when it’s away from the given edge.
