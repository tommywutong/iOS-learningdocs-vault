---
title: exponential
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogfloatformatting/exponential
source_url: 'https://developer.apple.com/documentation/os/oslogfloatformatting/exponential'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogfloatformatting/exponential.json'
content_hash: 'sha256:51306e9c78da3215'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogFloatFormatting](../oslogfloatformatting.md)

# exponential

<sub>Type Property</sub>

The standard exponential format option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var exponential: OSLogFloatFormatting { get }
```

## Discussion

This option is equivalent to the `%e` option in `fprintf`. It prints the number in the form `[-]d.ddde±dd`, with `d` representing the digits of the number. The number of digits after the radix point is system-specific.

## See Also

### Getting the Standard Formats

- [fixed](fixed.md) — The standard fixed-point format option.
- [hex](hex.md) — The standard hexadecimal format for floating-point values.
- [hybrid](hybrid.md) — A hybrid option that changes the format according to the size of the number.
