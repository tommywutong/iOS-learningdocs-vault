---
title: 'dequeueReusableAnnotationView(withIdentifier:for:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/dequeuereusableannotationview(withidentifier:for:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/dequeuereusableannotationview(withidentifier:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/dequeuereusableannotationview%28withidentifier%3Afor%3A%29.json'
content_hash: 'sha256:647bc9829dd3c479'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# dequeueReusableAnnotationView(withIdentifier:for:)

<sub>Instance Method</sub>

Returns a reusable annotation view using the specified identifier with a specified existing annotation view, if possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func dequeueReusableAnnotationView(withIdentifier identifier: String, for annotation: any MKAnnotation) -> MKAnnotationView
```

## Parameters

- `identifier` — A string identifying the annotation view to create.

- `annotation` — The annotation the map is displaying. This method automatically assigns this annotation object to the returned annotation view.

## Return Value

An annotation view with the specified identifier.

## Discussion

For performance reasons, be sure to reuse [MKAnnotationView](../mkannotationview.md) objects in your map views. As annotation views move offscreen, the map view moves them to an internally managed reuse queue. As new annotations move onscreen, and the map view prompts your code to provide a corresponding annotation view, use this method to dequeue an existing view. Dequeueing saves time and memory during performance-critical operations, such as scrolling.

If the map view can dequeue an existing view, this method tries to create one from the specified identifier. Before this can happen, you need to register an annotation view class using the [- registerClass:forAnnotationViewWithReuseIdentifier:](<register(__forannotationviewwithreuseidentifier_).md>) method. If there’s no registered class with the appropriate identifier, this method throws an exception.

## See Also

### Creating annotation views

- [- registerClass:forAnnotationViewWithReuseIdentifier:](<register(__forannotationviewwithreuseidentifier_).md>) — Registers an annotation view class that the map can create automatically.
- [- dequeueReusableAnnotationViewWithIdentifier:](<dequeuereusableannotationview(withidentifier_).md>) — Returns a reusable annotation view using its identifier.
- [- viewForAnnotation:](<view(for_)-33w8k.md>) — Returns the annotation view associated with the specified annotation object, if any.
- [MKMapViewDefaultAnnotationViewReuseIdentifier](../mkmapviewdefaultannotationviewreuseidentifier.md) — The default reuse identifier for your map’s annotation views.
- [MKMapViewDefaultClusterAnnotationViewReuseIdentifier](../mkmapviewdefaultclusterannotationviewreuseidentifier.md) — The default reuse identifier for the annotation view representing a cluster of annotations.
