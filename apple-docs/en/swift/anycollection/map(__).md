---
title: 'map(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/anycollection/map(_:)'
source_url: 'https://developer.apple.com/documentation/swift/anycollection/map(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anycollection/map%28_%3A%29.json'
content_hash: 'sha256:8ea795800414622c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyCollection](../anycollection.md)

# map(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<T, E>(_ transform: (Element) throws(E) -> T) throws(E) -> [T] where E : Error
```
