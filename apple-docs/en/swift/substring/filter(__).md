---
title: 'filter(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/filter(_:)'
source_url: 'https://developer.apple.com/documentation/swift/substring/filter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/filter%28_%3A%29.json'
content_hash: 'sha256:7a630e7878cc1153'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# filter(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter<E>(_ isIncluded: (Substring.Element) throws(E) -> Bool) throws(E) -> String where E : Error
```
