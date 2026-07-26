---
title: 'mapView(_:didDeselect:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:diddeselect:)-4ldss'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:diddeselect:)-4ldss'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Adiddeselect%3A%29-4ldss.json'
content_hash: 'sha256:a968e73de28cd69c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:didDeselect:)

<sub>Instance Method</sub>

Tells the delegate when the user deselects one or more annotations.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, didDeselect annotation: any MKAnnotation)
```

## Parameters

- `mapView` — The map view containing the annotation view.

- `annotation` — The deselected annotation view.

## See Also

### Selecting annotations and annotations views

- [- mapView:didSelectAnnotationView:](<mapview(__didselect_)-41by3.md>) — Tells the delegate when the user selects one or more of its annotation views.
- [- mapView:didDeselectAnnotationView:](<mapview(__diddeselect_)-yo7q.md>) — Tells the delegate when the user deselects one or more of its annotation views.
- [- mapView:didSelectAnnotation:](<mapview(__didselect_)-9km43.md>) — Tells the delegate when the user selects one or more annotations.
- [selectableMapFeatures](../mkmapview/selectablemapfeatures.md) — The property that describes which selectable features the map responds to.
