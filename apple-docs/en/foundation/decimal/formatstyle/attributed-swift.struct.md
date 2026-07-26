---
title: Decimal.FormatStyle.Attributed
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/decimal/formatstyle/attributed-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle/attributed-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle/attributed-swift.struct.json'
content_hash: 'sha256:e24eb5fe7da3ec9b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Decimal](../../decimal.md) · [FormatStyle](../formatstyle.md)

# Decimal.FormatStyle.Attributed

<sub>Structure</sub>

A format style that converts integers into attributed strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Attributed
```

## Overview

Use the [attributed](../../integerformatstyle/attributed-swift.property.md) modifier on a [FloatingPointFormatStyle](../../floatingpointformatstyle.md) to create a format style of this type.

The attributed strings that this format style creates contain attributes from the [NumberFormatAttributes](../../attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

The following example finds runs of the attributed string that represent different parts of a formatted currency, and adds additional attributes like [foregroundColor](../../attributescopes/swiftuiattributes/foregroundcolor.md) and [inlinePresentationIntent](../../attributescopes/foundationattributes/inlinepresentationintent.md).

```swift
func attributedPrice(price: Decimal) -> AttributedString {
    var attributedPrice = price.formatted(
        .currency(code: "USD")
        .attributed)

    for run in attributedPrice.runs {
        if run.attributes.numberSymbol == .currency ||
            run.attributes.numberSymbol == .decimalSeparator  {
            attributedPrice[run.range].foregroundColor = .red
        }
        if run.attributes.numberPart == .integer ||
            run.attributes.numberPart == .fraction {
            attributedPrice[run.range].inlinePresentationIntent = [.stronglyEmphasized]
        }
    }
    return attributedPrice
}
```

User interface frameworks like SwiftUI can use these attributes when presenting the attributed string, as seen here:

![The currency value $1,234.56, with the dollar sign and decimal separator in red, and the digits in bold.](../../../../../attachments/7a4b9269c09c3f9fcab491116254bbc9/media-4099417@2x.png)

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [FormatStyle](../../formatstyle.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Formatting a decimal value

- [format(_:)](<attributed-swift.struct/format(__).md>) — Formats a decimal value, using this style.

### Modifying the locale

- [locale(_:)](<attributed-swift.struct/locale(__).md>) — Modifies the format style to use the specified locale.

## See Also

### Creating attributed strings

- [attributed](attributed-swift.property.md) — An attributed format style based on the decimal format style.
