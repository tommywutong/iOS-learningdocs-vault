---
title: 'init(unicodeScalarLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/staticstring/init(unicodescalarliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/staticstring/init(unicodescalarliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/staticstring/init%28unicodescalarliteral%3A%29.json'
content_hash: 'sha256:026a0f2975eced88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StaticString](../staticstring.md)

# init(unicodeScalarLiteral:)

<sub>Initializer</sub>

Creates an instance initialized to a single Unicode scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(unicodeScalarLiteral value: StaticString)
```

## Discussion

Do not call this initializer directly. It may be used by the compiler when you initialize a static string with a Unicode scalar.
