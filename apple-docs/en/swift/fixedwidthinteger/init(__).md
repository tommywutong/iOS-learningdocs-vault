---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 26.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/fixedwidthinteger/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/fixedwidthinteger/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/fixedwidthinteger/init%28_%3A%29.json'
content_hash: 'sha256:15fcf2a1216d52ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FixedWidthInteger](../fixedwidthinteger.md)

# init(_:)

<sub>Initializer</sub>

Convert from an Backtrace.Address.

<sub>Mac Catalyst, macOS</sub>

```swift
init?(_ address: Backtrace.Address)
```

## Discussion

This initializer will return nil if the address width is larger than the type you are attempting to convert into.
