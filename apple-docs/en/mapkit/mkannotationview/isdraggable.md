---
title: isDraggable
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/isdraggable
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/isdraggable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/isdraggable.json'
content_hash: 'sha256:04c01d2936386e83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# isDraggable

<sub>Instance Property</sub>

A Boolean value that indicates whether the annotation view is draggable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var isDraggable: Bool { get set }
```

## Discussion

Setting this property to [true](../../swift/true.md) makes an annotation draggable by the user. If [true](../../swift/true.md), the associated annotation object needs to also implement the [setCoordinate:](../mkannotation/setcoordinate_.md) method. The default value of this property is [false](../../swift/false.md).

Setting this property to [true](../../swift/true.md) lets the map view know that the annotation is draggable. You can’t conditionalize drag operations by attempting to stop an operation the user initiates. Doing so can lead to undefined behavior. After it begins, the drag operation needs to continue to completion.

## See Also

### Supporting drag operations

- [- setDragState:animated:](<setdragstate(__animated_).md>) — Sets the drag state for the annotation view.
- [dragState](dragstate-swift.property.md) — The drag state of the annotation view.
