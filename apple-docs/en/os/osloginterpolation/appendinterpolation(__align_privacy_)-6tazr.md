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
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:)-6tazr'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:)-6tazr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aalign%3Aprivacy%3A%29-6tazr.json'
content_hash: 'sha256:022930d49dc5db18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:align:privacy:)

<sub>Instance Method</sub>

Appends an interpolated string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ argumentString: @autoclosure @escaping () -> String, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto)
```

## Parameters

- `argumentString` — The interpolated string value to add to the message.

- `align` — The alignment to apply to the string. Use this parameter to specify the width of the column that contains the data, and the alignment of the data within that column. If you don’t specify this parameter, the system doesn’t align the value.

- `privacy` — The privacy level of the information. If you don’t specify this parameter, the default rules redact the string’s value.

## Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## See Also

### Appending Strings

- [appendInterpolation(_:align:privacy:attributes:)](<appendinterpolation(__align_privacy_attributes_)-7g68v.md>) — Appends an interpolated string with the specified attributes.
