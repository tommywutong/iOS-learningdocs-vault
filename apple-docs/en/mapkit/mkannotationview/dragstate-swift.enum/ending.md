---
title: MKAnnotationView.DragState.ending
framework: MapKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/dragstate-swift.enum/ending
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/dragstate-swift.enum/ending'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/dragstate-swift.enum/ending.json'
content_hash: 'sha256:84623734ef01406c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKAnnotationView](../../mkannotationview.md) · [DragState](../dragstate-swift.enum.md)

# MKAnnotationView.DragState.ending

<sub>Case</sub>

An annotation view ends dragging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
case ending
```

## Discussion

A user action indicates the user dropped the view. The map view automatically moves annotation views to this state in response to appropriate user actions.

## See Also

### Constants

- [MKAnnotationViewDragStateNone](none.md) — An annotation view that doesn’t have a drag operation.
- [MKAnnotationViewDragStateStarting](starting.md) — An annotation view begins dragging.
- [MKAnnotationViewDragStateDragging](dragging.md) — An annotation view is actively dragging.
- [MKAnnotationViewDragStateCanceling](canceling.md) — An annotation view cancels drag operation.
