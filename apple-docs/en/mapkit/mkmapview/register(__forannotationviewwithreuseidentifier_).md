---
title: 'register(_:forAnnotationViewWithReuseIdentifier:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/register(_:forannotationviewwithreuseidentifier:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/register(_:forannotationviewwithreuseidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/register%28_%3Aforannotationviewwithreuseidentifier%3A%29.json'
content_hash: 'sha256:edbbcbb01707718e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# register(_:forAnnotationViewWithReuseIdentifier:)

<sub>Instance Method</sub>

Registers an annotation view class that the map can create automatically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func register(_ viewClass: AnyClass?, forAnnotationViewWithReuseIdentifier identifier: String)
```

## Parameters

- `viewClass` — The class of an annotation view that you use in your map. The class needs to be a subclass of [MKAnnotationView](../mkannotationview.md).

- `identifier` — The reuse identifier to associate with the specified class. This parameter can’t be `nil` or an empty string.

## Discussion

Use this method to register one or more views that you use to display annotations on your map. Register your classes before adding any annotations to the map.

When you register an annotation view class using this method, the [- dequeueReusableAnnotationViewWithIdentifier:forAnnotation:](<dequeuereusableannotationview(withidentifier_for_).md>) method uses the provided identifier to create the view that you register. It creates a new view only if an existing view isn’t available for reuse.

## See Also

### Creating annotation views

- [- dequeueReusableAnnotationViewWithIdentifier:forAnnotation:](<dequeuereusableannotationview(withidentifier_for_).md>) — Returns a reusable annotation view using the specified identifier with a specified existing annotation view, if possible.
- [- dequeueReusableAnnotationViewWithIdentifier:](<dequeuereusableannotationview(withidentifier_).md>) — Returns a reusable annotation view using its identifier.
- [- viewForAnnotation:](<view(for_)-33w8k.md>) — Returns the annotation view associated with the specified annotation object, if any.
- [MKMapViewDefaultAnnotationViewReuseIdentifier](../mkmapviewdefaultannotationviewreuseidentifier.md) — The default reuse identifier for your map’s annotation views.
- [MKMapViewDefaultClusterAnnotationViewReuseIdentifier](../mkmapviewdefaultclusterannotationviewreuseidentifier.md) — The default reuse identifier for the annotation view representing a cluster of annotations.
