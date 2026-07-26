---
title: image
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/image
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/image.json'
content_hash: 'sha256:0ed4f9526ee0e5d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# image

<sub>Instance Property</sub>

The image the annotation view displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var image: UIImage? { get set }
```

<sub>macOS</sub>

```swift
var image: NSImage? { get set }
```

## Discussion

Assigning a new image to this property also changes the size of the view’s frame so that it matches the width and height of the new image. The position of the view’s frame doesn’t change.

## See Also

### Getting and setting attributes

- [enabled](isenabled.md) — A Boolean value that indicates whether the annotation is in an enabled state.
- [highlighted](ishighlighted.md) — A Boolean value that indicates whether the map view highlights the annotation view.
- [annotation](annotation.md) — The annotation object associated with the view.
- [centerOffset](centeroffset.md) — The offset (in points) at which to display the view.
- [calloutOffset](calloutoffset.md) — The offset (in points) at which to place the callout.
- [reuseIdentifier](reuseidentifier.md) — The string that identifies that the annotation view is reusable.
