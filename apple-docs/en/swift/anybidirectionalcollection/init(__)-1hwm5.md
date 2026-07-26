---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/anybidirectionalcollection/init(_:)-1hwm5'
source_url: 'https://developer.apple.com/documentation/swift/anybidirectionalcollection/init(_:)-1hwm5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anybidirectionalcollection/init%28_%3A%29-1hwm5.json'
content_hash: 'sha256:531422c229fabae0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyBidirectionalCollection](../anybidirectionalcollection.md)

# init(_:)

<sub>Initializer</sub>

Creates an `AnyBidirectionalCollection` having the same underlying collection as `other`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ other: AnyCollection<Element>)
```

## Discussion

If the underlying collection stored by `other` does not satisfy `BidirectionalCollection`, the result is `nil`.

> [!abstract] Complexity
> O(1)
