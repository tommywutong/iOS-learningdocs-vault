---
title: 'removeAnnotation(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/removeannotation(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/removeannotation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/removeannotation%28_%3A%29.json'
content_hash: 'sha256:9f89da206c601fd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# removeAnnotation(_:)

<sub>Instance Method</sub>

Removes the specified annotation object from the map view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeAnnotation(_ annotation: any MKAnnotation)
```

## Parameters

- `annotation` — The annotation object to remove. This object needs to conform to the [MKAnnotation](../mkannotation.md) protocol.

## Discussion

If the annotation is associated with an annotation view, and that view has a reuse identifier, this method removes the annotation view and queues it internally for later reuse. You can retrieve queued annotation views (and associate them with new annotations) using the [- dequeueReusableAnnotationViewWithIdentifier:](<dequeuereusableannotationview(withidentifier_).md>) method.

Removing an annotation object disassociates it from the map view entirely, preventing the map view from displaying it on the map. Typically, you call this method only when you want to hide or delete a specified annotation.

## See Also

### Annotating the map

- [annotations](annotations.md) — The annotations associated with the map view.
- [- addAnnotation:](<addannotation(__).md>) — Adds the specified annotation to the map view.
- [- addAnnotations:](<addannotations(__).md>) — Adds an array of annotation objects to the map view.
- [- removeAnnotations:](<removeannotations(__).md>) — Removes an array of annotation objects from the map view.
- [- annotationsInMapRect:](<annotations(in_).md>) — Returns the annotation objects within the specified map rectangle.
