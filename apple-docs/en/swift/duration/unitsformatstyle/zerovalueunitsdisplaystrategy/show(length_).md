---
title: 'show(length:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/unitsformatstyle/zerovalueunitsdisplaystrategy/show(length:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/zerovalueunitsdisplaystrategy/show(length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/zerovalueunitsdisplaystrategy/show%28length%3A%29.json'
content_hash: 'sha256:3e80ebcc7373ec0d'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Duration](../../../duration.md) · [UnitsFormatStyle](../../unitsformatstyle.md) · [ZeroValueUnitsDisplayStrategy](../zerovalueunitsdisplaystrategy.md)

# show(length:)

<sub>Type Method</sub>

Returns display strategy that shows leading fields whose value is zero, with a given number of digits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func show(length: Int) -> Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy
```

## Parameters

- `length` — The number of digits to show for zero-value units.

## See Also

### Using common strategies

- [hide](hide.md) — A display strategy that hides leading fields whose value is zero.
