---
title: 'init(ascii:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint8/init(ascii:)'
source_url: 'https://developer.apple.com/documentation/swift/uint8/init(ascii:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint8/init%28ascii%3A%29.json'
content_hash: 'sha256:625529b396b858e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt8](../uint8.md)

# init(ascii:)

<sub>Initializer</sub>

Construct with value `v.value`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(ascii v: Unicode.Scalar)
```

## Discussion

> [!info] Precondition
> `v.value` can be represented as ASCII (0..\<128).
