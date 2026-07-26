---
title: filterBy
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/resultsobserver/filterby
source_url: 'https://developer.apple.com/documentation/swiftdata/resultsobserver/filterby'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultsobserver/filterby.json'
content_hash: 'sha256:9c76d8cb3ee03166'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsObserver](../resultsobserver.md)

# filterBy

<sub>Instance Property</sub>

The predicate used to filter which models are included in the results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var filterBy: Predicate<Element>? { get set }
```

## Discussion

Setting this property updates the underlying [fetchDescriptor](fetchdescriptor.md)’s predicate and immediately refetches on the calling actor — results are synchronously up to date before the setter returns. Set to `nil` to remove filtering and include all models of this type.

## See Also

### Accessing observer properties

- [fetchDescriptor](fetchdescriptor.md) — The fetch descriptor used to query the model context. _(beta)_
- [modelContext](modelcontext.md) — The model context from which models are fetched. _(beta)_
- [sortBy](sortby.md) — The sort descriptors used to order the results. _(beta)_
- [sectionBy](sectionby.md) — The key path on the element used to determine section grouping. _(beta)_
- [sections](sections.md) — The sections computed from the current results, grouped by [sectionBy](sectionby.md). _(beta)_
- [ResultsSectionCollection](../resultssectioncollection.md) — A collection of sections as returned by [sections](sections.md) or `Query.sections`. _(beta)_
