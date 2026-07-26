---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/init(_:)-35b1j'
source_url: 'https://developer.apple.com/documentation/swift/range/init(_:)-35b1j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/init%28_%3A%29-35b1j.json'
content_hash: 'sha256:17ba46eace07888b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# init(_:)

<sub>Initializer</sub>

Now that Range is conditionally a collection when Bound: Strideable, CountableRange is no longer needed. This is a deprecated initializer for any remaining uses of Range(countableRange).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ other: Range<Bound>)
```
