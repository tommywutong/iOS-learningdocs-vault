---
title: 'appendInterpolation(_:format:privacy:attributes:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-93lbs'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-93lbs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aformat%3Aprivacy%3Aattributes%3A%29-93lbs.json'
content_hash: 'sha256:779046553b44d591'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:format:privacy:attributes:)

<sub>Instance Method</sub>

Appends an interpolated collection of raw bytes with the specified attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ pointer: @autoclosure @escaping () -> UnsafeRawBufferPointer, format: OSLogPointerFormat = .none, privacy: OSLogPrivacy = .auto, attributes: String)
```

## Parameters

- `pointer` — The interpolated collection of raw bytes. The system automatically wraps this value in a closure.

- `format` — The format to apply to the value when the system renders it in a log message. For more information, see [OSLogPointerFormat](../oslogpointerformat.md). The default value is [OSLogPointerFormat.none](../oslogpointerformat/none.md).

- `privacy` — The privacy level of the value, which the system applies when it renders the value in a log message. For more information, see [OSLogPrivacy](../oslogprivacy.md). The default value is [auto](../oslogprivacy/auto.md).

- `attributes` — Additional information about the value. Tools that process log messages interpret these attributes, which you typically provide as key-value pairs. For example, Instruments processes any  e_ngineering types_ you embed in this value. For more information, see [Instruments Developer Help](https://help.apple.com/instruments/developer/mac/current/#/devcd5016d31).

## Discussion

> [!important] Important
> You don’t call this method directly. Instead, the framework calls it automatically when you append an interpolated collection of raw bytes to a log message.

## See Also

### Appending Pointer Data

- [appendInterpolation(_:bytes:format:privacy:)](<appendinterpolation(__bytes_format_privacy_).md>) — Appends interpolated pointer data.
- [appendInterpolation(_:bytes:format:privacy:attributes:)](<appendinterpolation(__bytes_format_privacy_attributes_).md>) — Appends interpolated pointer data with the specified attributes.
- [appendInterpolation(_:format:privacy:)](<appendinterpolation(__format_privacy_)-5qaau.md>) — Appends an interpolated collection of raw bytes.
