---
title: 'mapView(_:annotationView:calloutAccessoryControlTapped:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:annotationview:calloutaccessorycontroltapped:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:annotationview:calloutaccessorycontroltapped:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Aannotationview%3Acalloutaccessorycontroltapped%3A%29.json'
content_hash: 'sha256:8524e57d06e51b92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:annotationView:calloutAccessoryControlTapped:)

<sub>Instance Method</sub>

Tells the delegate when the user taps one of the annotation view’s accessory buttons.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, annotationView view: MKAnnotationView, calloutAccessoryControlTapped control: UIControl)
```

## Parameters

- `mapView` — The map view containing the specified annotation view.

- `view` — The annotation view with the button that the person taps.

- `control` — The control that the person taps.

## Discussion

Accessory views contain custom content and the map view positions it on either side of the annotation title text. If a view you specify is a descendant of the [UIControl](../../uikit/uicontrol.md) class, the map view calls this method as a convenience whenever the user taps your view. You can use this method to respond to taps and perform any actions associated with that control. For example, if your control displays additional information about the annotation, you can use this method to present a modal panel with that information.

If your custom accessory views aren’t descendants of the [UIControl](../../uikit/uicontrol.md) class, the map view doesn’t call this method.

## See Also

### Managing annotation views

- [- mapView:viewForAnnotation:](<mapview(__viewfor_)-8humz.md>) — Returns the view associated with the specified annotation object.
- [- mapView:didAddAnnotationViews:](<mapview(__didadd_)-44xon.md>) — Tells the delegate when the map view adds one or more annotation views to the map.
- [- mapView:clusterAnnotationForMemberAnnotations:](<mapview(__clusterannotationformemberannotations_).md>) — Asks the delegate to provide a cluster annotation object for the specified annotations.
