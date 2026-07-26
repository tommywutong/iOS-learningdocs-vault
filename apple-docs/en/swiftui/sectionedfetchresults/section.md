---
title: SectionedFetchResults.Section
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionedfetchresults/section
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchresults/section'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchresults/section.json'
content_hash: 'sha256:86511566a2587927'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionedFetchResults](../sectionedfetchresults.md)

# SectionedFetchResults.Section

<sub>Structure</sub>

A collection of fetched results that share a specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct Section
```

## Overview

Examine a `Section` instance to find the entities that satisfy a [SectionedFetchRequest](../sectionedfetchrequest.md) predicate, and that have a particular property with the value stored in the section’s [id](section/id.md) parameter. You specify which property by setting the fetch request’s `sectionIdentifier` parameter during initialization, or by modifying the corresponding [SectionedFetchResults](../sectionedfetchresults.md) instance’s [sectionIdentifier](sectionidentifier.md) property.

Obtain specific sections by treating the fetch results as a collection. For example, consider the following property declaration that fetches `Quake` managed objects that the [Loading and Displaying a Large Data Feed](../loading_and_displaying_a_large_data_feed.md) sample code project defines to store earthquake data:

```swift
@SectionedFetchRequest<String, Quake>(
    sectionIdentifier: \.day,
    sortDescriptors: [SortDescriptor(\.time, order: .reverse)]
)
private var quakes: SectionedFetchResults<String, Quake>
```

Get the first section using a subscript:

```swift
let firstSection = quakes[0]
```

Alternatively, you can loop over the sections to create a list of sections.

```swift
ForEach(quakes) { section in
    Text("Section \(section.id) has \(section.count) elements")
}
```

The sections also act as collections, which means you can use elements like the [count](../../swift/collection/count-4l4qk.md) property in the example above.

## Relationships

- **Conforms To**: [BidirectionalCollection](../../swift/bidirectionalcollection.md), [Collection](../../swift/collection.md), [Identifiable](../../swift/identifiable.md), [RandomAccessCollection](../../swift/randomaccesscollection.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Sequence](../../swift/sequence.md)

## Topics

### Identifying the section

- [id](section/id.md) — The value that all entities in the section share for a specified key path.

### Getting indices

- [startIndex](section/startindex.md) — The index of the first entity in the section.
- [endIndex](section/endindex.md) — The index that’s one greater than that of the last entity in the section.

### Getting results

- [subscript(_:)](<section/subscript(__).md>) — Gets the entity at the specified index within the section.

## See Also

### Configuring the associated sectioned fetch request

- [nsPredicate](nspredicate.md) — The request’s predicate.
- [sortDescriptors](sortdescriptors.md) — The request’s sort descriptors, accessed as value types.
- [nsSortDescriptors](nssortdescriptors.md) — The request’s sort descriptors, accessed as reference types.
- [sectionIdentifier](sectionidentifier.md) — The key path that the system uses to group fetched results into sections.
