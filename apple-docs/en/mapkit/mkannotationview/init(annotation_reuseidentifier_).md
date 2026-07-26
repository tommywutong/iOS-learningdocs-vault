---
title: 'init(annotation:reuseIdentifier:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkannotationview/init(annotation:reuseidentifier:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/init(annotation:reuseidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/init%28annotation%3Areuseidentifier%3A%29.json'
content_hash: 'sha256:f9d84857698dc463'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# init(annotation:reuseIdentifier:)

<sub>Initializer</sub>

Creates and returns a new annotation view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(annotation: (any MKAnnotation)?, reuseIdentifier: String?)
```

## Parameters

- `annotation` — The annotation object to associate with the new view.

- `reuseIdentifier` — If you plan to reuse the annotation view for similar types of annotations, pass a string to identify it. Although you can pass `nil` if you don’t intend to reuse the view, reusing annotation views is generally best practice.

## Return Value

The initialized annotation view, or `nil` if there’s a problem initializing the object.

## Discussion

The reuse identifier provides a way for you to improve performance by recycling annotation views as the map scrolls on and off of the map. As MapKit no longer needs views, the map view moves them to a reuse queue. When a new annotation becomes visible, your app can request a view for that annotation by passing the appropriate reuse identifier string to the [- dequeueReusableAnnotationViewWithIdentifier:](<../mkmapview/dequeuereusableannotationview(withidentifier_).md>) method of [MKMapView](../mkmapview.md).

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Creating and preparing an annotation view

- [- initWithCoder:](<init(coder_).md>) — Creates an annotation view using data from the specified unarchiver.
- [- prepareForReuse](<prepareforreuse().md>) — Calls this method when removing the view from the reuse queue.
- [- prepareForDisplay](<preparefordisplay().md>) — Notifies the annotation view that the map view is about to display it.
