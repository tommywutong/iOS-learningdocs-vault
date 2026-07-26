---
title: hybrid
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogfloatformatting/hybrid
source_url: 'https://developer.apple.com/documentation/os/oslogfloatformatting/hybrid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogfloatformatting/hybrid.json'
content_hash: 'sha256:ea7c6a267b9ee0d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogFloatFormatting](../oslogfloatformatting.md)

# hybrid

<sub>Type Property</sub>

A hybrid option that changes the format according to the size of the number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var hybrid: OSLogFloatFormatting { get }
```

## Discussion

This option is equivalent to the `%g` option in `fprintf`. It behaves like the [fixed](fixed.md) option when the number is close to `1.0`, and like the [exponential](exponential.md) option when the number has a large exponent.

## See Also

### Getting the Standard Formats

- [fixed](fixed.md) — The standard fixed-point format option.
- [hex](hex.md) — The standard hexadecimal format for floating-point values.
- [exponential](exponential.md) — The standard exponential format option.
