---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/dictionary/subscript(_:)-1uuzk'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/subscript(_:)-1uuzk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/subscript%28_%3A%29-1uuzk.json'
content_hash: 'sha256:873c0c2fec3b1db0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Subscript that shadows the standard Dictionary subscript to provide path-based access. When the key contains `":"`, it is treated as a path with `":"` as the delimiter; otherwise the regular dictionary key semantics apply.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(key: String) -> USDValue? { get set }
```
