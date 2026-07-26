---
title: 'Query(_:transaction:)'
framework: SwiftData
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/query(_:transaction:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/query(_:transaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query%28_%3Atransaction%3A%29.json'
content_hash: 'sha256:62296bddfc39aea8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Query(_:transaction:)

<sub>Macro</sub>

Fetches only the subset of the attached model type that satisfy the provided fetch descriptor’s criteria.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(accessor) @attached(peer, names: prefixed(`_`)) macro Query<Element>(_ descriptor: FetchDescriptor<Element>, transaction: Transaction? = nil) where Element : PersistentModel
```

## Parameters

- `descriptor` — The criteria, sort order, and any additional configuration to use when performing the fetch.

- `transaction` — The animation to use when updates to the fetched models trigger user interface changes.

## See Also

### Descriptor-based queries

- [Query(_:animation:)](<query(__animation_).md>) — Fetches only the subset of the attached model type that satisfy the provided fetch descriptor’s criteria.
