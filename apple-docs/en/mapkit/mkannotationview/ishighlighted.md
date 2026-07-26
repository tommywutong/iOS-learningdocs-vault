---
title: isHighlighted
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/ishighlighted
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/ishighlighted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/ishighlighted.json'
content_hash: 'sha256:229695e4f4bb4a0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# isHighlighted

<sub>Instance Property</sub>

A Boolean value that indicates whether the map view highlights the annotation view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isHighlighted: Bool { get set }
```

## Discussion

Don’t set the value of this property directly. The map view sets it in response to touch events entering or exiting the annotation view’s bounds.

## See Also

### Getting and setting attributes

- [enabled](isenabled.md) — A Boolean value that indicates whether the annotation is in an enabled state.
- [image](image.md) — The image the annotation view displays.
- [annotation](annotation.md) — The annotation object associated with the view.
- [centerOffset](centeroffset.md) — The offset (in points) at which to display the view.
- [calloutOffset](calloutoffset.md) — The offset (in points) at which to place the callout.
- [reuseIdentifier](reuseidentifier.md) — The string that identifies that the annotation view is reusable.
