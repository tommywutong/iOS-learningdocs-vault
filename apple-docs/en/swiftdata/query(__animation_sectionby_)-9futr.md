---
title: 'Query(_:animation:sectionBy:)'
framework: SwiftData
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftdata/query(_:animation:sectionby:)-9futr'
source_url: 'https://developer.apple.com/documentation/swiftdata/query(_:animation:sectionby:)-9futr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query%28_%3Aanimation%3Asectionby%3A%29-9futr.json'
content_hash: 'sha256:7bcdba801f4a3f1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Query(_:animation:sectionBy:)

<sub>Macro</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(accessor) @attached(peer, names: prefixed(`_`)) macro Query<Element>(_ descriptor: FetchDescriptor<Element>, animation: Animation, sectionBy sectionKeyPath: KeyPath<Element, String>) where Element : PersistentModel
```

## See Also

### Basic queries

- [Query(animation:)](<query(animation_).md>) — Fetches all instances of the attached model type, using the specified animation to animate any subsequent changes.
- [Query(_:animation:sectionBy:)](<query(__animation_sectionby_)-91gkm.md>) _(beta)_
- [Query(transaction:)](<query(transaction_).md>) — Fetches all instances of the attached model type, using the specified transaction to animate any subsequent changes.
- [Query(_:transaction:sectionBy:)](<query(__transaction_sectionby_)-1poj9.md>) _(beta)_
- [Query(_:transaction:sectionBy:)](<query(__transaction_sectionby_)-2iol.md>) _(beta)_
- [Query(filter:sort:transaction:sectionBy:)](<query(filter_sort_transaction_sectionby_)-4wwsy.md>) _(beta)_
- [Query(filter:sort:transaction:sectionBy:)](<query(filter_sort_transaction_sectionby_)-6qrae.md>) _(beta)_
