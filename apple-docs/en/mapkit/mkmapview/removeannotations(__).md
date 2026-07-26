---
title: 'removeAnnotations(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/removeannotations(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/removeannotations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/removeannotations%28_%3A%29.json'
content_hash: 'sha256:5a23fb3b670994d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# removeAnnotations(_:)

<sub>Instance Method</sub>

Removes an array of annotation objects from the map view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeAnnotations(_ annotations: [any MKAnnotation])
```

## Parameters

- `annotations` — The array of annotations to remove. Objects in the array need to conform to the [MKAnnotation](../mkannotation.md) protocol.

## Discussion

If any annotation object in the array has an associated annotation view, and if that view has a reuse identifier, this method removes the annotation view and queues it internally for later reuse. You can retrieve queued annotation views (and associate them with new annotations) using the [- dequeueReusableAnnotationViewWithIdentifier:](<dequeuereusableannotationview(withidentifier_).md>) method.

Removing annotation objects disassociates them from the map view entirely, preventing the map view from displaying them on the map. Typically, you call this method only when you want to hide or delete the specified annotations.

## See Also

### Annotating the map

- [annotations](annotations.md) — The annotations associated with the map view.
- [- addAnnotation:](<addannotation(__).md>) — Adds the specified annotation to the map view.
- [- addAnnotations:](<addannotations(__).md>) — Adds an array of annotation objects to the map view.
- [- removeAnnotation:](<removeannotation(__).md>) — Removes the specified annotation object from the map view.
- [- annotationsInMapRect:](<annotations(in_).md>) — Returns the annotation objects within the specified map rectangle.
