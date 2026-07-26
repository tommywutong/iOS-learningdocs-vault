---
title: attributed
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/integerformatstyle/currency/attributed
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/currency/attributed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/currency/attributed.json'
content_hash: 'sha256:db179aa38adeaabe'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [IntegerFormatStyle](../../integerformatstyle.md) · [Currency](../currency.md)

# attributed

<sub>Instance Property</sub>

An attributed format style based on the integer currency format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var attributed: IntegerFormatStyle<Value>.Attributed { get }
```

## Discussion

Use this modifier to create an [Attributed](../attributed-swift.struct.md) instance, which formats values as [AttributedString](../../attributedstring.md) instances. These attributed strings contain attributes from the [NumberFormatAttributes](../../attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

## See Also

### Creating attributed strings

- [Attributed](../attributed-swift.struct.md) — A format style that converts integers into attributed strings.
