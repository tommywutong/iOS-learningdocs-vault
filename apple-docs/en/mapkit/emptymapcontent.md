---
title: EmptyMapContent
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/emptymapcontent
source_url: 'https://developer.apple.com/documentation/mapkit/emptymapcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/emptymapcontent.json'
content_hash: 'sha256:158893c34788c4aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# EmptyMapContent

<sub>Structure</sub>

A map content element that doesn’t contain any content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct EmptyMapContent
```

## Relationships

- **Conforms To**: [MapContent](mapcontent.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an empty map content structure

- [init()](<emptymapcontent/init().md>) — Creates an empty map content element.

## See Also

### Structures

- [DefaultUserAnnotationContent](defaultuserannotationcontent.md) — A structure that represents the view to show at the user’s location on the map.
- [MapProxy](mapproxy.md) — A proxy for accessing sizing information about a given map view.
- [MapReader](mapreader.md) — A container view that defines its contents as a function of information about the first contained map.
- [TupleMapContent](tuplemapcontent.md) — A view created from a Swift tuple of map content values.
- [MapSelectableContentView](mapselectablecontentview.md)
