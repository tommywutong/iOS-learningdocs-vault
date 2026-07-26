---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collectiondifference/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/collectiondifference/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectiondifference/init%28_%3A%29.json'
content_hash: 'sha256:fa402c306d80763c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionDifference](../collectiondifference.md)

# init(_:)

<sub>Initializer</sub>

Creates a new collection difference from a collection of changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<Changes>(_ changes: Changes) where Changes : Collection, Changes.Element == CollectionDifference<ChangeElement>.Change
```

## Parameters

- `changes` — A collection of changes that represent a transition between two states.

## Discussion

To find the difference between two collections, use the `difference(from:)` method declared on the `BidirectionalCollection` protocol.

The collection of changes passed as `changes` must meet these requirements:

- All insertion offsets are unique
- All removal offsets are unique
- All associations between insertions and removals are symmetric

> [!abstract] Complexity
> O(_n_ * log(_n_)), where _n_ is the length of the parameter.
