---
title: DefaultUserAnnotationContent
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/defaultuserannotationcontent
source_url: 'https://developer.apple.com/documentation/mapkit/defaultuserannotationcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/defaultuserannotationcontent.json'
content_hash: 'sha256:cee8ef609eb76759'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# DefaultUserAnnotationContent

<sub>Structure</sub>

A structure that represents the view to show at the user’s location on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct DefaultUserAnnotationContent
```

## Overview

Don’t use this type directly. Instead, MapKit creates this type on your behalf.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## See Also

### Structures

- [EmptyMapContent](emptymapcontent.md) — A map content element that doesn’t contain any content.
- [MapProxy](mapproxy.md) — A proxy for accessing sizing information about a given map view.
- [MapReader](mapreader.md) — A container view that defines its contents as a function of information about the first contained map.
- [TupleMapContent](tuplemapcontent.md) — A view created from a Swift tuple of map content values.
- [MapSelectableContentView](mapselectablecontentview.md)
