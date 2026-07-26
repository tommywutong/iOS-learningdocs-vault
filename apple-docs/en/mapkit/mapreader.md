---
title: MapReader
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapreader
source_url: 'https://developer.apple.com/documentation/mapkit/mapreader'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapreader.json'
content_hash: 'sha256:1e3597267a72bd4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapReader

<sub>Structure</sub>

A container view that defines its contents as a function of information about the first contained map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct MapReader<Content> where Content : View
```

## Overview

The map reader’s content builder receives a [MapProxy](mapproxy.md) instance. You can use this instance to get the information you’ll need to convert between a [MapCamera](mapcamera.md) and a [MKMapRect](mkmaprect.md) or [MKCoordinateRegion](mkcoordinateregion.md).

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a map reader

- [init(content:)](<mapreader/init(content_).md>) — Creates an instance that allows view content to reference information about a contained map.

## See Also

### Structures

- [DefaultUserAnnotationContent](defaultuserannotationcontent.md) — A structure that represents the view to show at the user’s location on the map.
- [EmptyMapContent](emptymapcontent.md) — A map content element that doesn’t contain any content.
- [MapProxy](mapproxy.md) — A proxy for accessing sizing information about a given map view.
- [TupleMapContent](tuplemapcontent.md) — A view created from a Swift tuple of map content values.
- [MapSelectableContentView](mapselectablecontentview.md)
