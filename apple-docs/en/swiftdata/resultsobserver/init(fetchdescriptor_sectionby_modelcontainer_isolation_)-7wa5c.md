---
title: 'init(fetchDescriptor:sectionBy:modelContainer:isolation:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftdata/resultsobserver/init(fetchdescriptor:sectionby:modelcontainer:isolation:)-7wa5c'
source_url: 'https://developer.apple.com/documentation/swiftdata/resultsobserver/init(fetchdescriptor:sectionby:modelcontainer:isolation:)-7wa5c'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultsobserver/init%28fetchdescriptor%3Asectionby%3Amodelcontainer%3Aisolation%3A%29-7wa5c.json'
content_hash: 'sha256:851546e710d56d04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsObserver](../resultsobserver.md)

# init(fetchDescriptor:sectionBy:modelContainer:isolation:)

<sub>Initializer</sub>

Creates a new observer with the given fetch descriptor, a String section key path, and a model container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(fetchDescriptor: FetchDescriptor<Element> = FetchDescriptor<Element>(), sectionBy: KeyPath<Element, String>, modelContainer: ModelContainer, isolation: isolated (any Actor)? = #isolation) throws
```

## Parameters

- `fetchDescriptor` — The descriptor defining the fetch criteria.

- `sectionBy` — A key path on the element type that returns the section name.

- `modelContainer` — The model container from which a new context will be created.

## Discussion

A new `ModelContext` is created from the provided container.

> [!danger] Throws
> An error if the initial fetch fails.

## See Also

### Creating a results observer with a fetch descriptor

- [init(fetchDescriptor:modelContext:isolation:)](<init(fetchdescriptor_modelcontext_isolation_).md>) — Creates a new unsectioned observer with the given fetch descriptor and model context. _(beta)_
- [init(fetchDescriptor:sectionBy:modelContext:isolation:)](<init(fetchdescriptor_sectionby_modelcontext_isolation_)-7ms14.md>) — Creates a new observer with the given fetch descriptor, a String section key path, and a model context. _(beta)_
- [init(fetchDescriptor:sectionBy:modelContext:isolation:)](<init(fetchdescriptor_sectionby_modelcontext_isolation_)-9kg1q.md>) — Creates a new observer with the given fetch descriptor, an optional String section key path, and a model context. _(beta)_
- [init(fetchDescriptor:modelContainer:isolation:)](<init(fetchdescriptor_modelcontainer_isolation_).md>) — Creates a new unsectioned observer with the given fetch descriptor and model container. _(beta)_
- [init(fetchDescriptor:sectionBy:modelContainer:isolation:)](<init(fetchdescriptor_sectionby_modelcontainer_isolation_)-4tuzk.md>) — Creates a new observer with the given fetch descriptor, an optional String section key path, and a model container. _(beta)_
