---
title: ResultsObserver
framework: SwiftData
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/resultsobserver
source_url: 'https://developer.apple.com/documentation/swiftdata/resultsobserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultsobserver.json'
content_hash: 'sha256:498ab7129c6353e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# ResultsObserver

<sub>Class</sub>

Observes and tracks changes to a collection of persistent models in a model context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class ResultsObserver<Element, SectionName> where Element : PersistentModel, SectionName : Hashable
```

## Overview

`ResultsObserver` automatically monitors changes to models that match specified fetch criteria, providing real-time updates when the underlying data changes. The observer maintains a collection of fetched results, making it ideal for keeping user interfaces synchronized with persistent data.

The observer responds to changes from multiple sources:

- Local changes made within the same model context
- Remote changes from other contexts within the same container
- External changes from other processes or CloudKit sync

You can configure the observer using either a complete `FetchDescriptor` or individual filter predicates and sort descriptors. The observer is `Observable`, allowing SwiftUI views to automatically update when results change.

Use `Never` as the `SectionName` type parameter when no sectioning is needed:

```swift
let observer = try ResultsObserver<Book, Never>(
    filterBy: #Predicate { $0.isPublished },
    sortBy: [SortDescriptor(\.title)],
    modelContext: context
)
```

Use a concrete type (e.g. `String`) when sectioning by a key path of that type:

```swift
let observer = try ResultsObserver<Book, String>(
    sectionBy: \.genre,
    modelContext: context
)
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Escapable](../swift/escapable.md), [Observable](../observation/observable.md)

## Topics

### Creating a results observer with a fetch descriptor

- [init(fetchDescriptor:modelContext:isolation:)](<resultsobserver/init(fetchdescriptor_modelcontext_isolation_).md>) — Creates a new unsectioned observer with the given fetch descriptor and model context. _(beta)_
- [init(fetchDescriptor:sectionBy:modelContext:isolation:)](<resultsobserver/init(fetchdescriptor_sectionby_modelcontext_isolation_)-7ms14.md>) — Creates a new observer with the given fetch descriptor, a String section key path, and a model context. _(beta)_
- [init(fetchDescriptor:sectionBy:modelContext:isolation:)](<resultsobserver/init(fetchdescriptor_sectionby_modelcontext_isolation_)-9kg1q.md>) — Creates a new observer with the given fetch descriptor, an optional String section key path, and a model context. _(beta)_
- [init(fetchDescriptor:modelContainer:isolation:)](<resultsobserver/init(fetchdescriptor_modelcontainer_isolation_).md>) — Creates a new unsectioned observer with the given fetch descriptor and model container. _(beta)_
- [init(fetchDescriptor:sectionBy:modelContainer:isolation:)](<resultsobserver/init(fetchdescriptor_sectionby_modelcontainer_isolation_)-4tuzk.md>) — Creates a new observer with the given fetch descriptor, an optional String section key path, and a model container. _(beta)_
- [init(fetchDescriptor:sectionBy:modelContainer:isolation:)](<resultsobserver/init(fetchdescriptor_sectionby_modelcontainer_isolation_)-7wa5c.md>) — Creates a new observer with the given fetch descriptor, a String section key path, and a model container. _(beta)_

### Creating a results observer with a predicate

- [init(filterBy:sortBy:modelContext:isolation:)](<resultsobserver/init(filterby_sortby_modelcontext_isolation_).md>) — Creates a new unsectioned observer with individual filter and sort criteria and a model context. _(beta)_
- [init(filterBy:sortBy:sectionBy:modelContext:isolation:)](<resultsobserver/init(filterby_sortby_sectionby_modelcontext_isolation_)-4ainb.md>) — Creates a new observer with individual filter and sort criteria, an optional String section key path, and a model context. _(beta)_
- [init(filterBy:sortBy:sectionBy:modelContext:isolation:)](<resultsobserver/init(filterby_sortby_sectionby_modelcontext_isolation_)-gsuz.md>) — Creates a new observer with individual filter and sort criteria, a String section key path, and a model context. _(beta)_
- [init(filterBy:sortBy:modelContainer:isolation:)](<resultsobserver/init(filterby_sortby_modelcontainer_isolation_).md>) — Creates a new unsectioned observer with individual filter and sort criteria and a model container. _(beta)_
- [init(filterBy:sortBy:sectionBy:modelContainer:isolation:)](<resultsobserver/init(filterby_sortby_sectionby_modelcontainer_isolation_)-5ufvn.md>) — Creates a new observer with individual filter and sort criteria, a String section key path, and a model container. _(beta)_
- [init(filterBy:sortBy:sectionBy:modelContainer:isolation:)](<resultsobserver/init(filterby_sortby_sectionby_modelcontainer_isolation_)-9lfy0.md>) — Creates a new observer with individual filter and sort criteria, an optional String section key path, and a model container. _(beta)_

### Accessing observer properties

- [fetchDescriptor](resultsobserver/fetchdescriptor.md) — The fetch descriptor used to query the model context. _(beta)_
- [filterBy](resultsobserver/filterby.md) — The predicate used to filter which models are included in the results. _(beta)_
- [modelContext](resultsobserver/modelcontext.md) — The model context from which models are fetched. _(beta)_
- [sortBy](resultsobserver/sortby.md) — The sort descriptors used to order the results. _(beta)_
- [sectionBy](resultsobserver/sectionby.md) — The key path on the element used to determine section grouping. _(beta)_
- [sections](resultsobserver/sections.md) — The sections computed from the current results, grouped by [sectionBy](resultsobserver/sectionby.md). _(beta)_
- [ResultsSectionCollection](resultssectioncollection.md) — A collection of sections as returned by [sections](resultsobserver/sections.md) or `Query.sections`. _(beta)_

### Accessing observer results

- [results](resultsobserver/results.md) — The current collection of fetched models matching the fetch criteria. _(beta)_
- [element(at:)](<resultsobserver/element(at_).md>) — Returns the element at the given index path in the sectioned results. _(beta)_
- [indexPath(for:)](<resultsobserver/indexpath(for_).md>) — Returns the index path of the given element within the sectioned results. _(beta)_

## See Also

### Data store observation

- [HistoryObserver](historyobserver.md) — Monitors a model container’s data stores for remote changes and notifies when new history transactions are available. _(beta)_
