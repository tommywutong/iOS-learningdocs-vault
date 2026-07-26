---
title: sortBy
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/resultsobserver/sortby
source_url: 'https://developer.apple.com/documentation/swiftdata/resultsobserver/sortby'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultsobserver/sortby.json'
content_hash: 'sha256:36574a587178fe7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsObserver](../resultsobserver.md)

# sortBy

<sub>Instance Property</sub>

The sort descriptors used to order the results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var sortBy: [SortDescriptor<Element>] { get set }
```

## Discussion

Setting this property updates the underlying [fetchDescriptor](fetchdescriptor.md)‘s sort descriptors and immediately refetches on the calling actor. When sectioning is active, the section’s sort descriptor is automatically re-prepended if not already the first descriptor. A `SortDescriptor` by `persistentModelID` is appended automatically if not already present to ensure stable ordering for difference computation.

## See Also

### Accessing observer properties

- [fetchDescriptor](fetchdescriptor.md) — The fetch descriptor used to query the model context. _(beta)_
- [filterBy](filterby.md) — The predicate used to filter which models are included in the results. _(beta)_
- [modelContext](modelcontext.md) — The model context from which models are fetched. _(beta)_
- [sectionBy](sectionby.md) — The key path on the element used to determine section grouping. _(beta)_
- [sections](sections.md) — The sections computed from the current results, grouped by [sectionBy](sectionby.md). _(beta)_
- [ResultsSectionCollection](../resultssectioncollection.md) — A collection of sections as returned by [sections](sections.md) or `Query.sections`. _(beta)_
