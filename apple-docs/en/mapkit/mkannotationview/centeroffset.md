---
title: centerOffset
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/centeroffset
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/centeroffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/centeroffset.json'
content_hash: 'sha256:0760a62b6b4b8e67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# centerOffset

<sub>Instance Property</sub>

The offset (in points) at which to display the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var centerOffset: CGPoint { get set }
```

## Discussion

By default, the map view places the center point of an annotation view at the coordinate point of the associated annotation. You can use this property to reposition the annotation view as necessary. MapKit measures the x- and y-offset values in points. Positive offset values move the annotation view down and to the right, and negative values move it up and to the left.

## See Also

### Getting and setting attributes

- [enabled](isenabled.md) — A Boolean value that indicates whether the annotation is in an enabled state.
- [image](image.md) — The image the annotation view displays.
- [highlighted](ishighlighted.md) — A Boolean value that indicates whether the map view highlights the annotation view.
- [annotation](annotation.md) — The annotation object associated with the view.
- [calloutOffset](calloutoffset.md) — The offset (in points) at which to place the callout.
- [reuseIdentifier](reuseidentifier.md) — The string that identifies that the annotation view is reusable.
