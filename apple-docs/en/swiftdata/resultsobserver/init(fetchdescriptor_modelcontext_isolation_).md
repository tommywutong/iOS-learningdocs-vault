---
title: 'init(fetchDescriptor:modelContext:isolation:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftdata/resultsobserver/init(fetchdescriptor:modelcontext:isolation:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/resultsobserver/init(fetchdescriptor:modelcontext:isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultsobserver/init%28fetchdescriptor%3Amodelcontext%3Aisolation%3A%29.json'
content_hash: 'sha256:dfd94b05123900f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsObserver](../resultsobserver.md)

# init(fetchDescriptor:modelContext:isolation:)

<sub>Initializer</sub>

Creates a new unsectioned observer with the given fetch descriptor and model context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(fetchDescriptor: FetchDescriptor<Element> = FetchDescriptor<Element>(), modelContext: ModelContext, isolation: isolated (any Actor)? = #isolation) throws
```

## Parameters

- `fetchDescriptor` — The descriptor defining the fetch criteria.

- `modelContext` — The model context to fetch from and observe for changes.

## Discussion

> [!danger] Throws
> An error if the initial fetch fails.

## See Also

### Creating a results observer with a fetch descriptor

- [init(fetchDescriptor:sectionBy:modelContext:isolation:)](<init(fetchdescriptor_sectionby_modelcontext_isolation_)-7ms14.md>) — Creates a new observer with the given fetch descriptor, a String section key path, and a model context. _(beta)_
- [init(fetchDescriptor:sectionBy:modelContext:isolation:)](<init(fetchdescriptor_sectionby_modelcontext_isolation_)-9kg1q.md>) — Creates a new observer with the given fetch descriptor, an optional String section key path, and a model context. _(beta)_
- [init(fetchDescriptor:modelContainer:isolation:)](<init(fetchdescriptor_modelcontainer_isolation_).md>) — Creates a new unsectioned observer with the given fetch descriptor and model container. _(beta)_
- [init(fetchDescriptor:sectionBy:modelContainer:isolation:)](<init(fetchdescriptor_sectionby_modelcontainer_isolation_)-4tuzk.md>) — Creates a new observer with the given fetch descriptor, an optional String section key path, and a model container. _(beta)_
- [init(fetchDescriptor:sectionBy:modelContainer:isolation:)](<init(fetchdescriptor_sectionby_modelcontainer_isolation_)-7wa5c.md>) — Creates a new observer with the given fetch descriptor, a String section key path, and a model container. _(beta)_
