---
title: 'init(signOf:magnitudeOf:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/init(signof:magnitudeof:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/init(signof:magnitudeof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/init%28signof%3Amagnitudeof%3A%29.json'
content_hash: 'sha256:011bdcb9a709bc73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Decimal](../decimal.md)

# init(signOf:magnitudeOf:)

<sub>Initializer</sub>

Creates and initializes a decimal with the sign and magnitude of the given decimals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(signOf: Decimal, magnitudeOf magnitude: Decimal)
```

## Parameters

- `signOf` — A [Decimal](../decimal.md) to use for the sign of the newly-created [Decimal](../decimal.md).

- `magnitude` — A [Decimal](../decimal.md) to use for the magnitude of the newly-created [Decimal](../decimal.md).

## See Also

### Creating a decimal from another decimal

- [NSDecimalCopy](<../nsdecimalcopy(____).md>) — Copies the value of a decimal number.
