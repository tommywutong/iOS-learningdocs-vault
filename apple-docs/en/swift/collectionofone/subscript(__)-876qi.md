---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collectionofone/subscript(_:)-876qi'
source_url: 'https://developer.apple.com/documentation/swift/collectionofone/subscript(_:)-876qi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectionofone/subscript%28_%3A%29-876qi.json'
content_hash: 'sha256:4d74225e8dbacca3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionOfOne](../collectionofone.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: Int) -> Element { get set }
```

## Parameters

- `position` — The position of the element to access. The only valid position in a `CollectionOfOne` instance is `0`.
