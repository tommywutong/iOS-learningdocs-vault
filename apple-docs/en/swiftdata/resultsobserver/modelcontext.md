---
title: modelContext
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/resultsobserver/modelcontext
source_url: 'https://developer.apple.com/documentation/swiftdata/resultsobserver/modelcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultsobserver/modelcontext.json'
content_hash: 'sha256:4d125846e359b69a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsObserver](../resultsobserver.md)

# modelContext

<sub>Instance Property</sub>

The model context from which models are fetched.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final let modelContext: ModelContext
```

## Discussion

This context is set at initialization and determines the data store and change-tracking scope for the observer.

## See Also

### Accessing observer properties

- [fetchDescriptor](fetchdescriptor.md) — The fetch descriptor used to query the model context. _(beta)_
- [filterBy](filterby.md) — The predicate used to filter which models are included in the results. _(beta)_
- [sortBy](sortby.md) — The sort descriptors used to order the results. _(beta)_
- [sectionBy](sectionby.md) — The key path on the element used to determine section grouping. _(beta)_
- [sections](sections.md) — The sections computed from the current results, grouped by [sectionBy](sectionby.md). _(beta)_
- [ResultsSectionCollection](../resultssectioncollection.md) — A collection of sections as returned by [sections](sections.md) or `Query.sections`. _(beta)_
