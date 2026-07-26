---
title: 'mapView(_:annotationView:didChange:fromOldState:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:annotationview:didchange:fromoldstate:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:annotationview:didchange:fromoldstate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Aannotationview%3Adidchange%3Afromoldstate%3A%29.json'
content_hash: 'sha256:3246a81f4577ffbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:annotationView:didChange:fromOldState:)

<sub>Instance Method</sub>

Tells the delegate when the drag state of one of its annotation views changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, annotationView view: MKAnnotationView, didChange newState: MKAnnotationView.DragState, fromOldState oldState: MKAnnotationView.DragState)
```

## Parameters

- `mapView` — The map view containing the annotation view.

- `view` — The annotation view whose drag state changed.

- `newState` — The new drag state of the annotation view.

- `oldState` — The previous drag state of the annotation view.

## Discussion

The drag state typically changes in response to user interactions with the annotation view. However, the annotation view itself is responsible for changing that state as well.
