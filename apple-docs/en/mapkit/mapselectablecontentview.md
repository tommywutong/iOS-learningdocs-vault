---
title: MapSelectableContentView
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapselectablecontentview
source_url: 'https://developer.apple.com/documentation/mapkit/mapselectablecontentview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapselectablecontentview.json'
content_hash: 'sha256:b66eac873799a8cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapSelectableContentView

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency struct MapSelectableContentView<SelectionValue, Content> where SelectionValue : MapSelectable, Content : MapContent
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## See Also

### Structures

- [DefaultUserAnnotationContent](defaultuserannotationcontent.md) — A structure that represents the view to show at the user’s location on the map.
- [EmptyMapContent](emptymapcontent.md) — A map content element that doesn’t contain any content.
- [MapProxy](mapproxy.md) — A proxy for accessing sizing information about a given map view.
- [MapReader](mapreader.md) — A container view that defines its contents as a function of information about the first contained map.
- [TupleMapContent](tuplemapcontent.md) — A view created from a Swift tuple of map content values.
