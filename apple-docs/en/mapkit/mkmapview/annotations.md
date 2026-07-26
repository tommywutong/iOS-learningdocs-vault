---
title: annotations
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/annotations
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/annotations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/annotations.json'
content_hash: 'sha256:176c31f6daf93821'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# annotations

<sub>Instance Property</sub>

The annotations associated with the map view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var annotations: [any MKAnnotation] { get }
```

## Discussion

The objects in this array adopt the [MKAnnotation](../mkannotation.md) protocol. If the map view has no associated annotations, the value of this property is an empty array.

## See Also

### Annotating the map

- [- addAnnotation:](<addannotation(__).md>) — Adds the specified annotation to the map view.
- [- addAnnotations:](<addannotations(__).md>) — Adds an array of annotation objects to the map view.
- [- removeAnnotation:](<removeannotation(__).md>) — Removes the specified annotation object from the map view.
- [- removeAnnotations:](<removeannotations(__).md>) — Removes an array of annotation objects from the map view.
- [- annotationsInMapRect:](<annotations(in_).md>) — Returns the annotation objects within the specified map rectangle.
