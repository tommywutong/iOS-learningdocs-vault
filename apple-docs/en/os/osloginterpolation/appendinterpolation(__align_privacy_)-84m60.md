---
title: 'appendInterpolation(_:align:privacy:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:)-84m60'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:)-84m60'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aalign%3Aprivacy%3A%29-84m60.json'
content_hash: 'sha256:82dc71cb4acac9a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:align:privacy:)

<sub>Instance Method</sub>

Appends an interpolated textual representation of a type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation<T>(_ value: @autoclosure @escaping () -> T, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto) where T : CustomStringConvertible
```

## Parameters

- `value` — An item that conforms to the [CustomStringConvertible](../../swift/customstringconvertible.md) protocol.

- `align` — The alignment to apply to the string. Use this parameter to specify the width of the column containing the data, and the alignment of the data within that column. If you don’t specify this parameter, the system doesn’t align the value.

- `privacy` — The privacy level of the information. If you don’t specify this parameter, the system uses the default rules to determine whether to show the information.

## Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## See Also

### Appending Generic Types

- [appendInterpolation(_:align:privacy:attributes:)](<appendinterpolation(__align_privacy_attributes_)-xyum.md>) — Appends an interpolated textual representation of a type using the specified attributes.
- [appendInterpolation(_:format:align:privacy:attributes:)](<appendinterpolation(__format_align_privacy_attributes_)-8107a.md>) — Appends an interpolated numeric type using the specified attributes.
- [appendInterpolation(_:align:privacy:)](<appendinterpolation(__align_privacy_)-8hwmt.md>) — Appends an interpolated type description.
- [appendInterpolation(_:align:privacy:attributes:)](<appendinterpolation(__align_privacy_attributes_)-9hehv.md>) — Appends an interpolated type description with the specified attributes.
