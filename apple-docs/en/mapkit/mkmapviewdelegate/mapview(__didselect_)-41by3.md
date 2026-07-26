---
title: 'mapView(_:didSelect:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:didselect:)-41by3'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didselect:)-41by3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Adidselect%3A%29-41by3.json'
content_hash: 'sha256:0dba3af590a221b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:didSelect:)

<sub>Instance Method</sub>

Tells the delegate when the user selects one or more of its annotation views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, didSelect view: MKAnnotationView)
```

## Parameters

- `mapView` — The map view containing the annotation view.

- `view` — The selected annotation view.

## Discussion

You can use this method to track changes in the selection state of annotation views.

## See Also

### Selecting annotations and annotations views

- [- mapView:didDeselectAnnotationView:](<mapview(__diddeselect_)-yo7q.md>) — Tells the delegate when the user deselects one or more of its annotation views.
- [- mapView:didDeselectAnnotation:](<mapview(__diddeselect_)-4ldss.md>) — Tells the delegate when the user deselects one or more annotations.
- [- mapView:didSelectAnnotation:](<mapview(__didselect_)-9km43.md>) — Tells the delegate when the user selects one or more annotations.
- [selectableMapFeatures](../mkmapview/selectablemapfeatures.md) — The property that describes which selectable features the map responds to.
