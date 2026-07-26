---
title: SectionCollection
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectioncollection
source_url: 'https://developer.apple.com/documentation/swiftui/sectioncollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectioncollection.json'
content_hash: 'sha256:c422ee5ac912187d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SectionCollection

<sub>Structure</sub>

An opaque collection representing the sections of view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SectionCollection
```

## Overview

Sections are constructed lazily, on demand, so access only as much of this collection as is necessary to create the resulting content.

You can get access to a view’s [SectionCollection](sectioncollection.md) by using the `Group/init(sectionsOf:transform:)` initializer.

Any content of the given view which is not explicitly specified as a section is grouped with its sibling content to form implicit sections, meaning the minimum number of sections in a `SectionCollection` is one.

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sequence](../swift/sequence.md)

## See Also

### Organizing views into sections

- [Section](section.md) — A container view that you can use to add hierarchy within certain views.
- [SectionConfiguration](sectionconfiguration.md) — Specifies the contents of a section.
