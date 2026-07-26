---
title: 'mapView(_:clusterAnnotationForMemberAnnotations:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:clusterannotationformemberannotations:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:clusterannotationformemberannotations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Aclusterannotationformemberannotations%3A%29.json'
content_hash: 'sha256:730e5796ec96e00e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:clusterAnnotationForMemberAnnotations:)

<sub>Instance Method</sub>

Asks the delegate to provide a cluster annotation object for the specified annotations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, clusterAnnotationForMemberAnnotations memberAnnotations: [any MKAnnotation]) -> MKClusterAnnotation
```

## Parameters

- `mapView` — The map view containing the specified annotations.

- `memberAnnotations` — The annotations for the map to cluster together. The returned [MKClusterAnnotation](../mkclusterannotation.md) object needs to include the specific annotations in this parameter.

## Return Value

The cluster annotation object.

## Discussion

Use this method to customize the cluster annotations that display on your map. Typically, MapKit creates cluster annotation objects automatically when one or more annotations with the same cluster identifier are too close together. However, you can implement this method and return a custom cluster annotation object for the specified set of annotations.

## See Also

### Managing annotation views

- [- mapView:viewForAnnotation:](<mapview(__viewfor_)-8humz.md>) — Returns the view associated with the specified annotation object.
- [- mapView:didAddAnnotationViews:](<mapview(__didadd_)-44xon.md>) — Tells the delegate when the map view adds one or more annotation views to the map.
- [- mapView:annotationView:calloutAccessoryControlTapped:](<mapview(__annotationview_calloutaccessorycontroltapped_).md>) — Tells the delegate when the user taps one of the annotation view’s accessory buttons.
