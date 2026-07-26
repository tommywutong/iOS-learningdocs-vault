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
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:)-8hwmt'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:)-8hwmt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aalign%3Aprivacy%3A%29-8hwmt.json'
content_hash: 'sha256:cb5d7efba2ea2066'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:align:privacy:)

<sub>Instance Method</sub>

Appends an interpolated type description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ value: @autoclosure @escaping () -> any Any.Type, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto)
```

## Parameters

- `value` — A Swift type.

- `align` — The alignment to apply to the type name. Use this parameter to specify the width of the column containing the name, and the alignment of the name within that column. If you don’t specify this parameter, the system doesn’t align the value.

- `privacy` — The privacy level of the information. If you don’t specify this parameter, the system uses the default rules to determine whether to show the information.

## Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## See Also

### Appending Generic Types

- [appendInterpolation(_:align:privacy:)](<appendinterpolation(__align_privacy_)-84m60.md>) — Appends an interpolated textual representation of a type.
- [appendInterpolation(_:align:privacy:attributes:)](<appendinterpolation(__align_privacy_attributes_)-xyum.md>) — Appends an interpolated textual representation of a type using the specified attributes.
- [appendInterpolation(_:format:align:privacy:attributes:)](<appendinterpolation(__format_align_privacy_attributes_)-8107a.md>) — Appends an interpolated numeric type using the specified attributes.
- [appendInterpolation(_:align:privacy:attributes:)](<appendinterpolation(__align_privacy_attributes_)-9hehv.md>) — Appends an interpolated type description with the specified attributes.
