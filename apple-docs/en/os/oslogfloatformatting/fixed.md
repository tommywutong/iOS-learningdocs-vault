---
title: fixed
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogfloatformatting/fixed
source_url: 'https://developer.apple.com/documentation/os/oslogfloatformatting/fixed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogfloatformatting/fixed.json'
content_hash: 'sha256:2769246ef9e215a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogFloatFormatting](../oslogfloatformatting.md)

# fixed

<sub>Type Property</sub>

The standard fixed-point format option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var fixed: OSLogFloatFormatting { get }
```

## Discussion

This option is equivalent to the `%f` option of `fprintf`, which prints all digits before the radix point and a system-specific number of digits after the radix point.

## See Also

### Getting the Standard Formats

- [hex](hex.md) — The standard hexadecimal format for floating-point values.
- [exponential](exponential.md) — The standard exponential format option.
- [hybrid](hybrid.md) — A hybrid option that changes the format according to the size of the number.
