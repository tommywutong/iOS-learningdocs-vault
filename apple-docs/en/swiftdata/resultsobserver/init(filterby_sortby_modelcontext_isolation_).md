---
title: 'init(filterBy:sortBy:modelContext:isolation:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftdata/resultsobserver/init(filterby:sortby:modelcontext:isolation:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/resultsobserver/init(filterby:sortby:modelcontext:isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultsobserver/init%28filterby%3Asortby%3Amodelcontext%3Aisolation%3A%29.json'
content_hash: 'sha256:f80ec141558cf05a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsObserver](../resultsobserver.md)

# init(filterBy:sortBy:modelContext:isolation:)

<sub>Initializer</sub>

Creates a new unsectioned observer with individual filter and sort criteria and a model context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(filterBy: Predicate<Element>? = nil, sortBy: [SortDescriptor<Element>]? = nil, modelContext: ModelContext, isolation: isolated (any Actor)? = #isolation) throws
```

## Parameters

- `filterBy` — An optional predicate to filter the results.

- `sortBy` — An optional array of sort descriptors to order the results.

- `modelContext` — The model context to fetch from and observe for changes.

## Discussion

> [!danger] Throws
> An error if the initial fetch fails.

## See Also

### Creating a results observer with a predicate

- [init(filterBy:sortBy:sectionBy:modelContext:isolation:)](<init(filterby_sortby_sectionby_modelcontext_isolation_)-4ainb.md>) — Creates a new observer with individual filter and sort criteria, an optional String section key path, and a model context. _(beta)_
- [init(filterBy:sortBy:sectionBy:modelContext:isolation:)](<init(filterby_sortby_sectionby_modelcontext_isolation_)-gsuz.md>) — Creates a new observer with individual filter and sort criteria, a String section key path, and a model context. _(beta)_
- [init(filterBy:sortBy:modelContainer:isolation:)](<init(filterby_sortby_modelcontainer_isolation_).md>) — Creates a new unsectioned observer with individual filter and sort criteria and a model container. _(beta)_
- [init(filterBy:sortBy:sectionBy:modelContainer:isolation:)](<init(filterby_sortby_sectionby_modelcontainer_isolation_)-5ufvn.md>) — Creates a new observer with individual filter and sort criteria, a String section key path, and a model container. _(beta)_
- [init(filterBy:sortBy:sectionBy:modelContainer:isolation:)](<init(filterby_sortby_sectionby_modelcontainer_isolation_)-9lfy0.md>) — Creates a new observer with individual filter and sort criteria, an optional String section key path, and a model container. _(beta)_
