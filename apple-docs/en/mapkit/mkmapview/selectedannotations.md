---
title: selectedAnnotations
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/selectedannotations
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/selectedannotations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/selectedannotations.json'
content_hash: 'sha256:b415c90b06514fda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# selectedAnnotations

<sub>Instance Property</sub>

The selected annotations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var selectedAnnotations: [any MKAnnotation] { get set }
```

## Discussion

Assigning a new array to this property selects only the first annotation in the array.

## See Also

### Managing annotation selections

- [annotationVisibleRect](annotationvisiblerect.md) — The visible rectangle where the map is displaying annotation views.
- [- selectAnnotation:animated:](<selectannotation(__animated_).md>) — Selects the specified annotation and displays a callout view for it.
- [- deselectAnnotation:animated:](<deselectannotation(__animated_).md>) — Deselects the specified annotation and hides its callout view.
