---
title: 'appendInterpolation(_:format:align:privacy:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:format:align:privacy:)-4qvu9'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:align:privacy:)-4qvu9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aformat%3Aalign%3Aprivacy%3A%29-4qvu9.json'
content_hash: 'sha256:4c47636dd6e0a8c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:format:align:privacy:)

<sub>Instance Method</sub>

Appends an interpolated unsigned 8-bit integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ number: @autoclosure @escaping () -> UInt8, format: OSLogIntegerFormatting = .decimal, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto)
```

## Parameters

- `number` — The unsigned 8-bit integer value to add to the message.

- `format` — The format to apply to the integer value. You format integers as decimal, hexadecimal, or octal values. If you don’t specify this parameter, the default format uses a decimal value. For more information, see [OSLogIntegerFormatting](../oslogintegerformatting.md).

- `align` — The alignment to apply to the value. Use this parameter to specify the width of the column containing the data, and the alignment of the data within that column. If you don’t specify this parameter, the system doesn’t align the value.

- `privacy` — The privacy level of the information. If you don’t specify this parameter, the system uses the default rules to determine whether to show the information.

## Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## See Also

### Appending Unsigned Integers

- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-20jin.md>) — Appends an interpolated unsigned integer.
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-7k91g.md>) — Appends an interpolated unsigned 16-bit integer.
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-2i3qh.md>) — Appends an interpolated unsigned 32-bit integer.
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-81jbm.md>) — Appends an interpolated unsigned 64-bit integer.
