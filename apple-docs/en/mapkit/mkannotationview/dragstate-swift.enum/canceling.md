---
title: MKAnnotationView.DragState.canceling
framework: MapKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/dragstate-swift.enum/canceling
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/dragstate-swift.enum/canceling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/dragstate-swift.enum/canceling.json'
content_hash: 'sha256:4aa2e72201787a47'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKAnnotationView](../../mkannotationview.md) · [DragState](../dragstate-swift.enum.md)

# MKAnnotationView.DragState.canceling

<sub>Case</sub>

An annotation view cancels drag operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
case canceling
```

## Discussion

A user action causes the view to cancel the drag operation. You can put an annotation view into this state to abort the operation.

## See Also

### Constants

- [MKAnnotationViewDragStateNone](none.md) — An annotation view that doesn’t have a drag operation.
- [MKAnnotationViewDragStateStarting](starting.md) — An annotation view begins dragging.
- [MKAnnotationViewDragStateDragging](dragging.md) — An annotation view is actively dragging.
- [MKAnnotationViewDragStateEnding](ending.md) — An annotation view ends dragging.
