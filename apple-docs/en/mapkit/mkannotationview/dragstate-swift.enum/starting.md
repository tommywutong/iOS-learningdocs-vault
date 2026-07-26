---
title: MKAnnotationView.DragState.starting
framework: MapKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/dragstate-swift.enum/starting
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/dragstate-swift.enum/starting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/dragstate-swift.enum/starting.json'
content_hash: 'sha256:f558558978703d29'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKAnnotationView](../../mkannotationview.md) · [DragState](../dragstate-swift.enum.md)

# MKAnnotationView.DragState.starting

<sub>Case</sub>

An annotation view begins dragging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
case starting
```

## Discussion

A user action causes the view to begin the drag operation. The map view automatically moves annotation views to this state in response to appropriate user actions.

## See Also

### Constants

- [MKAnnotationViewDragStateNone](none.md) — An annotation view that doesn’t have a drag operation.
- [MKAnnotationViewDragStateDragging](dragging.md) — An annotation view is actively dragging.
- [MKAnnotationViewDragStateCanceling](canceling.md) — An annotation view cancels drag operation.
- [MKAnnotationViewDragStateEnding](ending.md) — An annotation view ends dragging.
