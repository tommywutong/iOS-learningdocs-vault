---
title: fetchDescriptor
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/resultsobserver/fetchdescriptor
source_url: 'https://developer.apple.com/documentation/swiftdata/resultsobserver/fetchdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultsobserver/fetchdescriptor.json'
content_hash: 'sha256:e7dac3419a0b556c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsObserver](../resultsobserver.md)

# fetchDescriptor

<sub>Instance Property</sub>

The fetch descriptor used to query the model context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var fetchDescriptor: FetchDescriptor<Element> { get }
```

## Discussion

This descriptor defines the complete fetch criteria including predicate, sort descriptors, and other fetch options. It is configured at initialization and can be indirectly modified through the [filterBy](filterby.md) and [sortBy](sortby.md) computed properties.

## See Also

### Accessing observer properties

- [filterBy](filterby.md) — The predicate used to filter which models are included in the results. _(beta)_
- [modelContext](modelcontext.md) — The model context from which models are fetched. _(beta)_
- [sortBy](sortby.md) — The sort descriptors used to order the results. _(beta)_
- [sectionBy](sectionby.md) — The key path on the element used to determine section grouping. _(beta)_
- [sections](sections.md) — The sections computed from the current results, grouped by [sectionBy](sectionby.md). _(beta)_
- [ResultsSectionCollection](../resultssectioncollection.md) — A collection of sections as returned by [sections](sections.md) or `Query.sections`. _(beta)_
