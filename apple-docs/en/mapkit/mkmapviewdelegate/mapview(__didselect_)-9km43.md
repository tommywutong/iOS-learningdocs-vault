---
title: 'mapView(_:didSelect:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:didselect:)-9km43'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didselect:)-9km43'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Adidselect%3A%29-9km43.json'
content_hash: 'sha256:cda2a33b9d71f11c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:didSelect:)

<sub>Instance Method</sub>

Tells the delegate when the user selects one or more annotations.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, didSelect annotation: any MKAnnotation)
```

## Parameters

- `mapView` — The map view containing the annotation view.

- `annotation` — The selected annotation view.

## See Also

### Selecting annotations and annotations views

- [- mapView:didSelectAnnotationView:](<mapview(__didselect_)-41by3.md>) — Tells the delegate when the user selects one or more of its annotation views.
- [- mapView:didDeselectAnnotationView:](<mapview(__diddeselect_)-yo7q.md>) — Tells the delegate when the user deselects one or more of its annotation views.
- [- mapView:didDeselectAnnotation:](<mapview(__diddeselect_)-4ldss.md>) — Tells the delegate when the user deselects one or more annotations.
- [selectableMapFeatures](../mkmapview/selectablemapfeatures.md) — The property that describes which selectable features the map responds to.
