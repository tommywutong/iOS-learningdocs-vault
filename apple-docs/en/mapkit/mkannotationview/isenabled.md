---
title: isEnabled
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/isenabled
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/isenabled.json'
content_hash: 'sha256:c406165da340e412'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the annotation is in an enabled state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

The default value of this property is [true](../../swift/true.md). If the value of this property is [false](../../swift/false.md), the annotation view ignores touch events and isn’t selectable. Subclasses may also display the annotation contents differently depending on the value of this property.

## See Also

### Getting and setting attributes

- [image](image.md) — The image the annotation view displays.
- [highlighted](ishighlighted.md) — A Boolean value that indicates whether the map view highlights the annotation view.
- [annotation](annotation.md) — The annotation object associated with the view.
- [centerOffset](centeroffset.md) — The offset (in points) at which to display the view.
- [calloutOffset](calloutoffset.md) — The offset (in points) at which to place the callout.
- [reuseIdentifier](reuseidentifier.md) — The string that identifies that the annotation view is reusable.
