---
title: 'currency(code:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/currency(code:)-is0v'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/currency(code:)-is0v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/currency%28code%3A%29-is0v.json'
content_hash: 'sha256:8b4e3336ef5913b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# currency(code:)

<sub>Type Method</sub>

Returns a format style to use integer currency notation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func currency<V>(code: String) -> Self where Self == IntegerFormatStyle<V>.Currency, V : BinaryInteger
```

## Parameters

- `code` — The currency code to use, such as `EUR` or `JPY`. See ISO-4217 for a list of valid codes.

## Return Value

An integer format style that uses the specified currency code.

## Discussion

Use the dot-notation form of this method when the call point allows the use of [IntegerFormatStyle](../integerformatstyle.md). You typically do this when calling the `formatted` methods of types that conform to [BinaryInteger](../../swift/binaryinteger.md).

The following example creates an array of integers, then uses [formatted(_:)](<../../swift/binaryinteger/formatted(__)-73k3e.md>) and the currency style provided by this method to format the integers as US dollars:

```swift
let nums: [Int] = [100, 1000, 10000, 100000, 1000000]
let currencyNums = nums.map { $0.formatted(
    .currency(code:"USD")) } // ["$100.00", "$1,000.00", "$10,000.00", "$100,000.00", "$1,000,000.00"]
```

## See Also

### Applying currency styles

- [currency(code:)](<currency(code_)-1yg68.md>) — Returns a format style to use floating-point currency notation.
- [currency(code:)](<currency(code_)-6fhr2.md>) — Returns a format style to use decimal currency notation.
