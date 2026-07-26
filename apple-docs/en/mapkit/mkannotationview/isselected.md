---
title: isSelected
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/isselected
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/isselected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/isselected.json'
content_hash: 'sha256:8bf67ae1989cd9fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# isSelected

<sub>Instance Property</sub>

A Boolean value that indicates whether the annotation view is in a selected state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isSelected: Bool { get set }
```

## Discussion

Don’t set the value of this property directly. If the property contains [true](../../swift/true.md), the annotation view is displaying a callout.

## See Also

### Managing the selection state

- [- setSelected:animated:](<setselected(__animated_).md>) — Sets the selection state of the annotation view.
