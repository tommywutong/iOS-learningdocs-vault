---
title: 'addAnnotations(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/addannotations(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/addannotations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/addannotations%28_%3A%29.json'
content_hash: 'sha256:74f8e1126e5ebdb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# addAnnotations(_:)

<sub>Instance Method</sub>

Adds an array of annotation objects to the map view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addAnnotations(_ annotations: [any MKAnnotation])
```

## Parameters

- `annotations` — An array of annotation objects. Each object in the array must conform to the [MKAnnotation](../mkannotation.md) protocol. The map view retains the individual annotation objects.

## See Also

### Annotating the map

- [annotations](annotations.md) — The annotations associated with the map view.
- [- addAnnotation:](<addannotation(__).md>) — Adds the specified annotation to the map view.
- [- removeAnnotation:](<removeannotation(__).md>) — Removes the specified annotation object from the map view.
- [- removeAnnotations:](<removeannotations(__).md>) — Removes an array of annotation objects from the map view.
- [- annotationsInMapRect:](<annotations(in_).md>) — Returns the annotation objects within the specified map rectangle.
