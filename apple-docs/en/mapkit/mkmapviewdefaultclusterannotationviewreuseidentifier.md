---
title: MKMapViewDefaultClusterAnnotationViewReuseIdentifier
framework: MapKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapviewdefaultclusterannotationviewreuseidentifier
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdefaultclusterannotationviewreuseidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdefaultclusterannotationviewreuseidentifier.json'
content_hash: 'sha256:a1b2efa99a83bb34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapViewDefaultClusterAnnotationViewReuseIdentifier

<sub>Global Variable</sub>

The default reuse identifier for the annotation view representing a cluster of annotations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let MKMapViewDefaultClusterAnnotationViewReuseIdentifier: String
```

## Discussion

Use this constant to register a default annotation view to use for clusters of annotations. The map view uses this cluster annotation view when your map view’s delegate doesn’t implement the [- mapView:viewForAnnotation:](<mkmapviewdelegate/mapview(__viewfor_)-8humz.md>) method, or when that method returns `nil`.

## See Also

### Creating annotation views

- [- registerClass:forAnnotationViewWithReuseIdentifier:](<mkmapview/register(__forannotationviewwithreuseidentifier_).md>) — Registers an annotation view class that the map can create automatically.
- [- dequeueReusableAnnotationViewWithIdentifier:forAnnotation:](<mkmapview/dequeuereusableannotationview(withidentifier_for_).md>) — Returns a reusable annotation view using the specified identifier with a specified existing annotation view, if possible.
- [- dequeueReusableAnnotationViewWithIdentifier:](<mkmapview/dequeuereusableannotationview(withidentifier_).md>) — Returns a reusable annotation view using its identifier.
- [- viewForAnnotation:](<mkmapview/view(for_)-33w8k.md>) — Returns the annotation view associated with the specified annotation object, if any.
- [MKMapViewDefaultAnnotationViewReuseIdentifier](mkmapviewdefaultannotationviewreuseidentifier.md) — The default reuse identifier for your map’s annotation views.
