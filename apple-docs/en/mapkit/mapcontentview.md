---
title: MapContentView
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapcontentview
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontentview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontentview.json'
content_hash: 'sha256:f98d47834d437db6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapContentView

<sub>Structure</sub>

A view that contains content that displays on a map at a specific position, and that responds to specific interactions you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct MapContentView<SelectionValue, Content> where SelectionValue : Hashable, Content : MapContent
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## See Also

### Protocols

- [DynamicMapContent](dynamicmapcontent.md) — A  type of view that generates views from an underlying collection of data.
- [MapContent](mapcontent.md) — A protocol used to construct map content such as controls, markers, and annotations.
- [MapContentBuilder](mapcontentbuilder.md) — A result builder that creates map content from closures you provide.
