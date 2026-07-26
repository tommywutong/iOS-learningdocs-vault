---
title: 'init(_:within:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/init(_:within:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/init(_:within:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/init%28_%3Awithin%3A%29.json'
content_hash: 'sha256:cac233b60d8953bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# init(_:within:)

<sub>Initializer</sub>

Creates a new range set containing ranges that contain only the specified indices in the given collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S, C>(_ indices: S, within collection: C) where Bound == S.Element, S : Sequence, C : Collection, S.Element == C.Index
```

## Parameters

- `collection` — The collection that contains `index`.
