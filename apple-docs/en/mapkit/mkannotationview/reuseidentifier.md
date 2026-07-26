---
title: reuseIdentifier
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/reuseidentifier
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/reuseidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/reuseidentifier.json'
content_hash: 'sha256:d2db06298dc5f68e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# reuseIdentifier

<sub>Instance Property</sub>

The string that identifies that the annotation view is reusable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var reuseIdentifier: String? { get }
```

## Discussion

You specify the reuse identifier when you create the view. You use this type to retrieve an annotation view that MapKit isn’t currently using because its annotation isn’t onscreen.

If you define distinctly different types of annotations (with distinctly different annotation views to go with them), you can differentiate between the annotation types by specifying different reuse identifiers for each one.

## See Also

### Getting and setting attributes

- [enabled](isenabled.md) — A Boolean value that indicates whether the annotation is in an enabled state.
- [image](image.md) — The image the annotation view displays.
- [highlighted](ishighlighted.md) — A Boolean value that indicates whether the map view highlights the annotation view.
- [annotation](annotation.md) — The annotation object associated with the view.
- [centerOffset](centeroffset.md) — The offset (in points) at which to display the view.
- [calloutOffset](calloutoffset.md) — The offset (in points) at which to place the callout.
