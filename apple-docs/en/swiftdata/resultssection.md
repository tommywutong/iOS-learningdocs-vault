---
title: ResultsSection
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/resultssection
source_url: 'https://developer.apple.com/documentation/swiftdata/resultssection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultssection.json'
content_hash: 'sha256:f76947a1c12512cc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# ResultsSection

<sub>Structure</sub>

A section of fetched results grouped by a common section key path value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ResultsSection<Element, SectionName> where Element : PersistentModel, SectionName : Hashable
```

## Overview

Each section represents a group of elements that share the same value for the `sectionBy` key path used at creation.

You access sections through [sections](resultsobserver/sections.md) or `Query.sections`. Each section conforms to `RandomAccessCollection` — iterate it directly to access its elements, and use [name](resultssection/name.md) (or [id](resultssection/id.md)) to access the section identifier.

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [Identifiable](../swift/identifiable.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sequence](../swift/sequence.md)

## Topics

### Accessing section properties

- [id](resultssection/id.md) — The unique identifier for the section, which is its [name](resultssection/name.md). _(beta)_
- [name](resultssection/name.md) — The identifier of the section. _(beta)_

## See Also

### Retrieving sections

- [subscript(sectionName:)](<resultssectioncollection/subscript(sectionname_).md>) — Returns the section with the given name, or `nil` if no such section exists. _(beta)_
