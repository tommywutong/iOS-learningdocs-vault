---
title: 'addAnnotation(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/addannotation(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/addannotation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/addannotation%28_%3A%29.json'
content_hash: 'sha256:5ff0502afd9f2aef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# addAnnotation(_:)

<sub>Instance Method</sub>

Adds the specified annotation to the map view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addAnnotation(_ annotation: any MKAnnotation)
```

## Parameters

- `annotation` — The annotation object to add to the receiver. This object must conform to the [MKAnnotation](../mkannotation.md) protocol. The map view retains the specified object.

## See Also

### Annotating the map

- [annotations](annotations.md) — The annotations associated with the map view.
- [- addAnnotations:](<addannotations(__).md>) — Adds an array of annotation objects to the map view.
- [- removeAnnotation:](<removeannotation(__).md>) — Removes the specified annotation object from the map view.
- [- removeAnnotations:](<removeannotations(__).md>) — Removes an array of annotation objects from the map view.
- [- annotationsInMapRect:](<annotations(in_).md>) — Returns the annotation objects within the specified map rectangle.
