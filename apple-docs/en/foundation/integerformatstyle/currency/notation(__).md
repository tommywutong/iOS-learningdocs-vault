---
title: 'notation(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/integerformatstyle/currency/notation(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/currency/notation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/currency/notation%28_%3A%29.json'
content_hash: 'sha256:71dfe6620962b9b9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [IntegerFormatStyle](../../integerformatstyle.md) · [Currency](../currency.md)

# notation(_:)

<sub>Instance Method</sub>

Modifies the format style to use the specified notation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func notation(_ notation: IntegerFormatStyle<Value>.Currency.Configuration.Notation) -> IntegerFormatStyle<Value>.Currency
```

## Parameters

- `notation` — The notation to apply to the format style.

## Return Value

An integer currency format style modified to use the specified notation.
