---
title: annotation
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/annotation
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/annotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/annotation.json'
content_hash: 'sha256:88b25289bede42e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# annotation

<sub>Instance Property</sub>

The annotation object associated with the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var annotation: (any MKAnnotation)? { get set }
```

## Discussion

Don’t change the value of this property directly. This property contains a non-`nil` value only while the annotation view is visible on the map. If the map view queues this annotation view and is waiting to reuse it, the value is `nil`.

## See Also

### Getting and setting attributes

- [enabled](isenabled.md) — A Boolean value that indicates whether the annotation is in an enabled state.
- [image](image.md) — The image the annotation view displays.
- [highlighted](ishighlighted.md) — A Boolean value that indicates whether the map view highlights the annotation view.
- [centerOffset](centeroffset.md) — The offset (in points) at which to display the view.
- [calloutOffset](calloutoffset.md) — The offset (in points) at which to place the callout.
- [reuseIdentifier](reuseidentifier.md) — The string that identifies that the annotation view is reusable.
