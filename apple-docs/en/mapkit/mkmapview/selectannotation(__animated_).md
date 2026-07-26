---
title: 'selectAnnotation(_:animated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/selectannotation(_:animated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/selectannotation(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/selectannotation%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:6b4ef2592e24af2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# selectAnnotation(_:animated:)

<sub>Instance Method</sub>

Selects the specified annotation and displays a callout view for it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func selectAnnotation(_ annotation: any MKAnnotation, animated: Bool)
```

## Parameters

- `annotation` — The annotation object to select.

- `animated` — If [true](../../swift/true.md), the map view animates the callout view into position.

## Discussion

If the specified annotation isn’t onscreen, and, therefore, doesn’t have an associated annotation view, this method has no effect.

## See Also

### Managing annotation selections

- [annotationVisibleRect](annotationvisiblerect.md) — The visible rectangle where the map is displaying annotation views.
- [selectedAnnotations](selectedannotations.md) — The selected annotations.
- [- deselectAnnotation:animated:](<deselectannotation(__animated_).md>) — Deselects the specified annotation and hides its callout view.
