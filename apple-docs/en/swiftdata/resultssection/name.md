---
title: name
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/resultssection/name
source_url: 'https://developer.apple.com/documentation/swiftdata/resultssection/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultssection/name.json'
content_hash: 'sha256:22da3d4c80e01aad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsSection](../resultssection.md)

# name

<sub>Instance Property</sub>

The identifier of the section.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let name: SectionName
```

## Discussion

This is the common value shared by all elements in this section, as determined by the `sectionBy` key path provided at creation.

## See Also

### Accessing section properties

- [id](id.md) — The unique identifier for the section, which is its [name](name.md). _(beta)_
