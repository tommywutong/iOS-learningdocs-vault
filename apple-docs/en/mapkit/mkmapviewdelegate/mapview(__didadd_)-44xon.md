---
title: 'mapView(_:didAdd:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:didadd:)-44xon'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didadd:)-44xon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Adidadd%3A%29-44xon.json'
content_hash: 'sha256:9eb160180d391262'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:didAdd:)

<sub>Instance Method</sub>

Tells the delegate when the map view adds one or more annotation views to the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, didAdd views: [MKAnnotationView])
```

## Parameters

- `mapView` — The map view that adds the annotation views.

- `views` — An array of `MKAnnotationView` objects representing the views that the map view adds.

## Discussion

By the time the map view calls this method, MapKit has added the specified views to the map.

## See Also

### Managing annotation views

- [- mapView:viewForAnnotation:](<mapview(__viewfor_)-8humz.md>) — Returns the view associated with the specified annotation object.
- [- mapView:annotationView:calloutAccessoryControlTapped:](<mapview(__annotationview_calloutaccessorycontroltapped_).md>) — Tells the delegate when the user taps one of the annotation view’s accessory buttons.
- [- mapView:clusterAnnotationForMemberAnnotations:](<mapview(__clusterannotationformemberannotations_).md>) — Asks the delegate to provide a cluster annotation object for the specified annotations.
