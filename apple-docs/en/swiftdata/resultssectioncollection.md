---
title: ResultsSectionCollection
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/resultssectioncollection
source_url: 'https://developer.apple.com/documentation/swiftdata/resultssectioncollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultssectioncollection.json'
content_hash: 'sha256:f5abe45263d6d63a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# ResultsSectionCollection

<sub>Structure</sub>

A collection of sections as returned by [sections](resultsobserver/sections.md) or `Query.sections`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ResultsSectionCollection<Element, SectionName> where Element : PersistentModel, SectionName : Hashable
```

## Overview

This is a lightweight `RandomAccessCollection` of [ResultsSection](resultssection.md) instances, ordered by their first appearance in the sorted results.

Because each section’s [name](resultssection/name.md) is its identity, the collection provides O(1) lookup by section name via [subscript(sectionName:)](<resultssectioncollection/subscript(sectionname_).md>) and [contains(sectionName:)](<resultssectioncollection/contains(sectionname_).md>).

You typically access this collection through [sections](resultsobserver/sections.md) or `Query.sections`.

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sequence](../swift/sequence.md)

## Topics

### Finding sections

- [sectionNames](resultssectioncollection/sectionnames.md) — The section names in order. _(beta)_
- [contains(sectionName:)](<resultssectioncollection/contains(sectionname_).md>) — Returns whether a section with the given name exists in the collection. _(beta)_
- [index(ofSectionNamed:)](<resultssectioncollection/index(ofsectionnamed_).md>) — Returns the ordered index of the section with the given name, or `nil` if not found. _(beta)_

### Retrieving sections

- [subscript(sectionName:)](<resultssectioncollection/subscript(sectionname_).md>) — Returns the section with the given name, or `nil` if no such section exists. _(beta)_
- [ResultsSection](resultssection.md) — A section of fetched results grouped by a common section key path value. _(beta)_

## See Also

### Accessing sections

- [sections](query/sections.md) — The sections computed from the current results, grouped by the `sectionBy` key path. _(beta)_
