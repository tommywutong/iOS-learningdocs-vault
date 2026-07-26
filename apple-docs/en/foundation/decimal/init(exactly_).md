---
title: 'init(exactly:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/init(exactly:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/init(exactly:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/init%28exactly%3A%29.json'
content_hash: 'sha256:32e9e72b29b95a4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Decimal](../decimal.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new decimal value exactly representing the provided integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<T>(exactly source: T) where T : BinaryInteger
```

## Parameters

- `source` — The integer to convert.

## Discussion

If `source` isn’t representable as a `Decimal` instance, the result is `nil`.

## See Also

### Creating a decimal from an integer

- [init(_:)](<init(__)-2tcho.md>) — Creates and initializes a decimal with the provided integer value.
- [init(_:)](<init(__)-4gk29.md>) — Creates and initializes a decimal with the provided integer value.
- [init(_:)](<init(__)-5aznh.md>) — Creates and initializes a decimal with the provided integer value.
- [init(_:)](<init(__)-7dmlc.md>) — Creates and initializes a decimal with the provided integer value.
- [init(_:)](<init(__)-7a033.md>) — Creates and initializes a decimal with the provided integer value.
- [init(integerLiteral:)](<init(integerliteral_).md>) — Creates and initializes a decimal with the provided integer value.
