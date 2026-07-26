---
title: MKAnnotationView.DragState.none
framework: MapKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/dragstate-swift.enum/none
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/dragstate-swift.enum/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/dragstate-swift.enum/none.json'
content_hash: 'sha256:186d87d05d1d0546'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKAnnotationView](../../mkannotationview.md) · [DragState](../dragstate-swift.enum.md)

# MKAnnotationView.DragState.none

<sub>Case</sub>

An annotation view that doesn’t have a drag operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
case none
```

## Discussion

The view isn’t involved in a drag operation. The annotation view is responsible for returning itself to this state when a drag ends or cancels.

## See Also

### Constants

- [MKAnnotationViewDragStateStarting](starting.md) — An annotation view begins dragging.
- [MKAnnotationViewDragStateDragging](dragging.md) — An annotation view is actively dragging.
- [MKAnnotationViewDragStateCanceling](canceling.md) — An annotation view cancels drag operation.
- [MKAnnotationViewDragStateEnding](ending.md) — An annotation view ends dragging.
