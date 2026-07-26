---
title: TupleMapContent
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/tuplemapcontent
source_url: 'https://developer.apple.com/documentation/mapkit/tuplemapcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/tuplemapcontent.json'
content_hash: 'sha256:3532640f931d5c7e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# TupleMapContent

<sub>Structure</sub>

A view created from a Swift tuple of map content values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @frozen @preconcurrency struct TupleMapContent<T>
```

## Relationships

- **Conforms To**: [MapContent](mapcontent.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the tuple value

- [value](tuplemapcontent/value.md) — The contents of the tuple.

## See Also

### Structures

- [DefaultUserAnnotationContent](defaultuserannotationcontent.md) — A structure that represents the view to show at the user’s location on the map.
- [EmptyMapContent](emptymapcontent.md) — A map content element that doesn’t contain any content.
- [MapProxy](mapproxy.md) — A proxy for accessing sizing information about a given map view.
- [MapReader](mapreader.md) — A container view that defines its contents as a function of information about the first contained map.
- [MapSelectableContentView](mapselectablecontentview.md)
