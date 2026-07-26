---
title: subtitle
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkclusterannotation/subtitle
source_url: 'https://developer.apple.com/documentation/mapkit/mkclusterannotation/subtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkclusterannotation/subtitle.json'
content_hash: 'sha256:654f7b65dd46cfed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKClusterAnnotation](../mkclusterannotation.md)

# subtitle

<sub>Instance Property</sub>

The subtitle string to display for the group of annotations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var subtitle: String? { get set }
```

## Discussion

The cluster annotation object sets this property to a string that conveys how many additional annotations the group includes, except for the annotation with the title that the [title](title.md) property displays.

## See Also

### Getting the cluster attributes

- [title](title.md) — The title string to display for the group of annotations.
