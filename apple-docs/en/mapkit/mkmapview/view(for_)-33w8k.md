---
title: 'view(for:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/view(for:)-33w8k'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/view(for:)-33w8k'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/view%28for%3A%29-33w8k.json'
content_hash: 'sha256:4210e82a7275c9c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# view(for:)

<sub>Instance Method</sub>

Returns the annotation view associated with the specified annotation object, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func view(for annotation: any MKAnnotation) -> MKAnnotationView?
```

## Parameters

- `annotation` — The annotation object whose view you want.

## Return Value

The annotation view or `nil` if the view has not yet been created. This method may also return `nil` if the annotation is not in the visible map region and therefore does not have an associated annotation view.

## See Also

### Creating annotation views

- [- registerClass:forAnnotationViewWithReuseIdentifier:](<register(__forannotationviewwithreuseidentifier_).md>) — Registers an annotation view class that the map can create automatically.
- [- dequeueReusableAnnotationViewWithIdentifier:forAnnotation:](<dequeuereusableannotationview(withidentifier_for_).md>) — Returns a reusable annotation view using the specified identifier with a specified existing annotation view, if possible.
- [- dequeueReusableAnnotationViewWithIdentifier:](<dequeuereusableannotationview(withidentifier_).md>) — Returns a reusable annotation view using its identifier.
- [MKMapViewDefaultAnnotationViewReuseIdentifier](../mkmapviewdefaultannotationviewreuseidentifier.md) — The default reuse identifier for your map’s annotation views.
- [MKMapViewDefaultClusterAnnotationViewReuseIdentifier](../mkmapviewdefaultclusterannotationviewreuseidentifier.md) — The default reuse identifier for the annotation view representing a cluster of annotations.
