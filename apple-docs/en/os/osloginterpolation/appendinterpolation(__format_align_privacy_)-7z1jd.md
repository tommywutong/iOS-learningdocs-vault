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
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:format:align:privacy:)-7z1jd'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:align:privacy:)-7z1jd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aformat%3Aalign%3Aprivacy%3A%29-7z1jd.json'
content_hash: 'sha256:c6bb71a5baf544c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:format:align:privacy:)

<sub>Instance Method</sub>

Appends an interpolated float.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ number: @autoclosure @escaping () -> Float, format: OSLogFloatFormatting = .fixed, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto)
```

## Parameters

- `number` — The float value to add to the message.

- `format` — The format to apply to the float value. You format floating-point numbers as fixed-point, hexadecimal, exponential, or hybrid values. If you don’t specify this parameter, the default format uses a fixed-point value. For more information, see [OSLogFloatFormatting](../oslogfloatformatting.md).

- `align` — The alignment to apply to the value. Use this parameter to specify the width of the column containing the data, and the alignment of the data within that column. If you don’t specify this parameter, the system doesn’t align the value.

- `privacy` — The privacy level of the information. If you don’t specify this parameter, the system uses the default rules to determine whether to show the information.

## Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## See Also

### Appending Floats

- [appendInterpolation(_:format:align:privacy:attributes:)](<appendinterpolation(__format_align_privacy_attributes_)-78sek.md>) — Appends an interpolated float with the specified attributes.
