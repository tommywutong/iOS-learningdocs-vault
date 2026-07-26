---
title: 'deselectAnnotation(_:animated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/deselectannotation(_:animated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/deselectannotation(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/deselectannotation%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:16e7ab929a456ebb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# deselectAnnotation(_:animated:)

<sub>Instance Method</sub>

Deselects the specified annotation and hides its callout view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func deselectAnnotation(_ annotation: (any MKAnnotation)?, animated: Bool)
```

## Parameters

- `annotation` — The annotation object to deselect.

- `animated` — If [true](../../swift/true.md), the map view animates the callout view offscreen.

## See Also

### Managing annotation selections

- [annotationVisibleRect](annotationvisiblerect.md) — The visible rectangle where the map is displaying annotation views.
- [selectedAnnotations](selectedannotations.md) — The selected annotations.
- [- selectAnnotation:animated:](<selectannotation(__animated_).md>) — Selects the specified annotation and displays a callout view for it.
