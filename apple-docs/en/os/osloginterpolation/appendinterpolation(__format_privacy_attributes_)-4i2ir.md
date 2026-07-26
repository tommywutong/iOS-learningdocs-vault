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
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-4i2ir'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-4i2ir'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aformat%3Aprivacy%3Aattributes%3A%29-4i2ir.json'
content_hash: 'sha256:c5a91f5809ff97f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:format:privacy:attributes:)

<sub>Instance Method</sub>

Appends an interpolated 32-bit integer with the specified attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ number: @autoclosure @escaping () -> Int32, format: OSLogInt32ExtendedFormat, privacy: OSLogPrivacy = .auto, attributes: String)
```

## Parameters

- `number` — The interpolated 32-bit integer. The system automatically wraps this value in a closure.

- `format` — The format to apply to the value when the system renders it in a log message. For more information, see [OSLogInt32ExtendedFormat](../oslogint32extendedformat.md).

- `privacy` — The privacy level of the value, which the system applies when it renders the value in a log message. For more information, see [OSLogPrivacy](../oslogprivacy.md). The default value is [auto](../oslogprivacy/auto.md).

- `attributes` — Additional information about the value. Tools that process log messages interpret these attributes, which you typically provide as key-value pairs. For example, Instruments processes any  e_ngineering types_ you embed in this value. For more information, see [Instruments Developer Help](https://help.apple.com/instruments/developer/mac/current/#/devcd5016d31).

## Discussion

> [!important] Important
> You don’t call this method directly. Instead, the framework calls it automatically when you append an interpolated 32-bit integer to a log message.

## See Also

### Appending Signed Integers

- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-8kli1.md>) — Appends an interpolated integer.
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-5ihzf.md>) — Appends an interpolated 8-bit integer.
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-190d0.md>) — Appends an interpolated 16-bit integer.
- [appendInterpolation(_:format:privacy:)](<appendinterpolation(__format_privacy_)-3ji02.md>) — Appends an interpolated 32-bit integer.
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-2sb1i.md>) — Appends an interpolated 32-bit integer with the specified alignment.
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-802m9.md>) — Appends an interpolated 64-bit integer.
