---
title: 'Query(animation:)'
framework: SwiftData
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/query(animation:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/query(animation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query%28animation%3A%29.json'
content_hash: 'sha256:da76afc4eafd103d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Query(animation:)

<sub>Macro</sub>

Fetches all instances of the attached model type, using the specified animation to animate any subsequent changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(accessor) @attached(peer, names: prefixed(`_`)) macro Query(animation: Animation)
```

## Parameters

- `animation` — The animation to use when updates to the fetched models trigger user interface changes.

## See Also

### Basic queries

- [Query(_:animation:sectionBy:)](<query(__animation_sectionby_)-91gkm.md>) _(beta)_
- [Query(_:animation:sectionBy:)](<query(__animation_sectionby_)-9futr.md>) _(beta)_
- [Query(transaction:)](<query(transaction_).md>) — Fetches all instances of the attached model type, using the specified transaction to animate any subsequent changes.
- [Query(_:transaction:sectionBy:)](<query(__transaction_sectionby_)-1poj9.md>) _(beta)_
- [Query(_:transaction:sectionBy:)](<query(__transaction_sectionby_)-2iol.md>) _(beta)_
- [Query(filter:sort:transaction:sectionBy:)](<query(filter_sort_transaction_sectionby_)-4wwsy.md>) _(beta)_
- [Query(filter:sort:transaction:sectionBy:)](<query(filter_sort_transaction_sectionby_)-6qrae.md>) _(beta)_
