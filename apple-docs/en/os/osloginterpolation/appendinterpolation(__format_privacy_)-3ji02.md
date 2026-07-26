---
title: 'appendInterpolation(_:format:privacy:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:)-3ji02'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:)-3ji02'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aformat%3Aprivacy%3A%29-3ji02.json'
content_hash: 'sha256:97920a1ff0078bcf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:format:privacy:)

<sub>Instance Method</sub>

Appends an interpolated 32-bit integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ number: @autoclosure @escaping () -> Int32, format: OSLogInt32ExtendedFormat, privacy: OSLogPrivacy = .auto)
```

## Parameters

- `number` — The 32-bit integer value to add to the message.

- `format` — The format to apply to the integer value. You format integers as decimal, hexadecimal, or octal values. If you don’t specify this parameter, the default format uses a decimal value. For more information, see [OSLogIntegerFormatting](../oslogintegerformatting.md).

- `privacy` — The privacy level of the information. If you don’t specify this parameter, the system uses the default rules to determine whether to show the information.

## Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## See Also

### Appending Signed Integers

- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-8kli1.md>) — Appends an interpolated integer.
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-5ihzf.md>) — Appends an interpolated 8-bit integer.
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-190d0.md>) — Appends an interpolated 16-bit integer.
- [appendInterpolation(_:format:privacy:attributes:)](<appendinterpolation(__format_privacy_attributes_)-4i2ir.md>) — Appends an interpolated 32-bit integer with the specified attributes.
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-2sb1i.md>) — Appends an interpolated 32-bit integer with the specified alignment.
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-802m9.md>) — Appends an interpolated 64-bit integer.
