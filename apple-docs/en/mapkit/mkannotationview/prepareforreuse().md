---
title: prepareForReuse()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/prepareforreuse()
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/prepareforreuse()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/prepareforreuse%28%29.json'
content_hash: 'sha256:a8efeb4cbbcaf7f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# prepareForReuse()

<sub>Instance Method</sub>

Calls this method when removing the view from the reuse queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func prepareForReuse()
```

## Discussion

The default implementation of this method does nothing. You can override it in your custom annotation views and use it to put the view in a known state before the map view returns it to your map view delegate.

## See Also

### Related Documentation

- [- dequeueReusableAnnotationViewWithIdentifier:](<../mkmapview/dequeuereusableannotationview(withidentifier_).md>) — Returns a reusable annotation view using its identifier.

### Creating and preparing an annotation view

- [- initWithAnnotation:reuseIdentifier:](<init(annotation_reuseidentifier_).md>) — Creates and returns a new annotation view.
- [- initWithCoder:](<init(coder_).md>) — Creates an annotation view using data from the specified unarchiver.
- [- prepareForDisplay](<preparefordisplay().md>) — Notifies the annotation view that the map view is about to display it.
