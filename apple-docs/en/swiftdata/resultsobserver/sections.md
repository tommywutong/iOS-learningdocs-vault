---
title: sections
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/resultsobserver/sections
source_url: 'https://developer.apple.com/documentation/swiftdata/resultsobserver/sections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultsobserver/sections.json'
content_hash: 'sha256:67b9219e22b450ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsObserver](../resultsobserver.md)

# sections

<sub>Instance Property</sub>

The sections computed from the current results, grouped by [sectionBy](sectionby.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var sections: ResultsSectionCollection<Element, SectionName>? { get set }
```

## Discussion

Returns `nil` if this observer was created without a `sectionBy` key path (i.e. `SectionName == Never`). When sectioning is enabled, returns a [ResultsSectionCollection](../resultssectioncollection.md) of sections ordered by their first appearance in the sorted results.

The `sectionBy` key path is automatically prepended as the first sort descriptor at initialization, and re-prepended if [sortBy](sortby.md) is mutated, ensuring results are always contiguous within each section.

## See Also

### Accessing observer properties

- [fetchDescriptor](fetchdescriptor.md) — The fetch descriptor used to query the model context. _(beta)_
- [filterBy](filterby.md) — The predicate used to filter which models are included in the results. _(beta)_
- [modelContext](modelcontext.md) — The model context from which models are fetched. _(beta)_
- [sortBy](sortby.md) — The sort descriptors used to order the results. _(beta)_
- [sectionBy](sectionby.md) — The key path on the element used to determine section grouping. _(beta)_
- [ResultsSectionCollection](../resultssectioncollection.md) — A collection of sections as returned by [sections](sections.md) or `Query.sections`. _(beta)_
