---
title: utf8CodeUnitCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/staticstring/utf8codeunitcount
source_url: 'https://developer.apple.com/documentation/swift/staticstring/utf8codeunitcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/staticstring/utf8codeunitcount.json'
content_hash: 'sha256:0f4bac4d9be35f41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StaticString](../staticstring.md)

# utf8CodeUnitCount

<sub>Instance Property</sub>

The number of UTF-8 code units (excluding the null terminator).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var utf8CodeUnitCount: Int { get }
```

## Discussion

> [!important] Important
> Accessing this property when `hasPointerRepresentation` is `false` triggers a runtime error.
