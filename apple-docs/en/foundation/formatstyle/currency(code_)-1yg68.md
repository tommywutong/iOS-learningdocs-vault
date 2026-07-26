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
doc_path: '/documentation/foundation/formatstyle/currency(code:)-1yg68'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/currency(code:)-1yg68'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/currency%28code%3A%29-1yg68.json'
content_hash: 'sha256:aea9520607767529'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# currency(code:)

<sub>Type Method</sub>

Returns a format style to use floating-point currency notation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func currency<Value>(code: String) -> Self where Self == FloatingPointFormatStyle<Value>.Currency, Value : BinaryFloatingPoint
```

## Parameters

- `code` — The currency code to use, such as `EUR` or `JPY`. See ISO-4217 for a list of valid codes.

## Return Value

A floating-point format style that uses the specified currency code.

## Discussion

Use the dot-notation form of this method when the call point allows the use of [FloatingPointFormatStyle](../floatingpointformatstyle.md). You typically do this when calling the `formatted` methods of types that conform to [BinaryFloatingPoint](../../swift/binaryfloatingpoint.md).

The following example creates an array of doubles, then uses [formatted(_:)](<../../swift/binaryfloatingpoint/formatted(__)-83x4n.md>) and the currency style provided by this method to format the doubles as US dollars:

```swift
let nums: [Double] = [100.01, 1000.02, 10000.03, 100000.04, 1000000.05]
let currencyNums = nums.map { $0.formatted(
    .currency(code:"USD")) } // ["$100.01", "$1,000.02", "$10,000.03", "$100,000.04", "$1,000,000.05"]
```

## See Also

### Applying currency styles

- [currency(code:)](<currency(code_)-is0v.md>) — Returns a format style to use integer currency notation.
- [currency(code:)](<currency(code_)-6fhr2.md>) — Returns a format style to use decimal currency notation.
