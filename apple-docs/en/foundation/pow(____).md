---
title: 'pow(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/pow(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/pow(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/pow%28_%3A_%3A%29.json'
content_hash: 'sha256:c487384cb35e7911'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# pow(_:_:)

<sub>Function</sub>

Returns a decimal number raised to a given power.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func pow(_ x: Decimal, _ y: Int) -> Decimal
```

## Parameters

- `x` — A decimal value.

- `y` — The power by which to raise `x`.

## Return Value

The result of raising `x` to the power of `y`.

## Discussion

If the result of this operation requires more precision than the `Decimal` type can provide, the result is rounded using the [NSRoundPlain](nsdecimalnumber/roundingmode/plain.md) rounding mode. To specify a different rounding mode, use the [NSDecimalPower](<nsdecimalpower(________).md>) function instead.
