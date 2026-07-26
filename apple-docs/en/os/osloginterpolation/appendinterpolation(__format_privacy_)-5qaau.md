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
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:)-5qaau'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:)-5qaau'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aformat%3Aprivacy%3A%29-5qaau.json'
content_hash: 'sha256:1a4125a9b60df797'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:format:privacy:)

<sub>Instance Method</sub>

Appends an interpolated collection of raw bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ pointer: @autoclosure @escaping () -> UnsafeRawBufferPointer, format: OSLogPointerFormat = .none, privacy: OSLogPrivacy = .auto)
```

## Parameters

- `pointer` — A pointer to data with an implicit size.

- `format` — The format to apply to the pointer. You format pointers as one of several different options. If you don’t specify this parameter, the system doesn’t format the value. For more information, see [OSLogPointerFormat](../oslogpointerformat.md).

- `privacy` — The privacy level of the information. If you don’t specify this parameter, the system uses the default rules to determine whether to show the information.

## Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## See Also

### Appending Pointer Data

- [appendInterpolation(_:bytes:format:privacy:)](<appendinterpolation(__bytes_format_privacy_).md>) — Appends interpolated pointer data.
- [appendInterpolation(_:bytes:format:privacy:attributes:)](<appendinterpolation(__bytes_format_privacy_attributes_).md>) — Appends interpolated pointer data with the specified attributes.
- [appendInterpolation(_:format:privacy:attributes:)](<appendinterpolation(__format_privacy_attributes_)-93lbs.md>) — Appends an interpolated collection of raw bytes with the specified attributes.
