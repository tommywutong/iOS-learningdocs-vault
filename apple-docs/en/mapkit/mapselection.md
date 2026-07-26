---
title: MapSelection
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapselection
source_url: 'https://developer.apple.com/documentation/mapkit/mapselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapselection.json'
content_hash: 'sha256:92881b703b113ea1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapSelection

<sub>Structure</sub>

A value representing a selected feature on a map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapSelection<SelectionValue> where SelectionValue : Hashable
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MapSelectable](mapselectable.md)

## Topics

### Creating a map selection

- [init(_:)](<mapselection/init(__).md>) — Creates a map selection with a tag.

### Getting the properties

- [value](mapselection/value.md) — The selection of the given tag value.

## See Also

### Map features

- [MapFeature](mapfeature.md) — A tappable map feature.
- [MapSelectable](mapselectable.md)
