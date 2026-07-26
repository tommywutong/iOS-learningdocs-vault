---
title: 'appendInterpolation(_:format:align:privacy:attributes:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:format:align:privacy:attributes:)-8107a'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:align:privacy:attributes:)-8107a'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aformat%3Aalign%3Aprivacy%3Aattributes%3A%29-8107a.json'
content_hash: 'sha256:f7980105ce28d10f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:format:align:privacy:attributes:)

<sub>Instance Method</sub>

Appends an interpolated numeric type using the specified attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation<T>(_ number: @autoclosure @escaping () -> T, format: OSLogIntegerFormatting = .decimal, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto, attributes: String) where T : FixedWidthInteger
```

## Parameters

- `number` — The interpolated numeric type, which the system automatically wraps in a closure. The type itself doesn’t appear in the log message. Instead, the system incorporates the type’s integer value.

- `format` — The format to apply to the value when the system renders it in a log message. For more information, see [OSLogIntegerFormatting](../oslogintegerformatting.md). The default value is [decimal](../oslogintegerformatting/decimal.md).

- `align` — The alignment and minimum number of columns to use when the system renders the value in a log message. For more information, see [OSLogStringAlignment](../oslogstringalignment.md). The default value is [none](../oslogstringalignment/none.md).

- `privacy` — The privacy level of the value, which the system applies when it renders the value in a log message. For more information, see [OSLogPrivacy](../oslogprivacy.md). The default value is [auto](../oslogprivacy/auto.md).

- `attributes` — Additional information about the value. Tools that process log messages interpret these attributes, which you typically provide as key-value pairs. For example, Instruments processes any  e_ngineering types_ you embed in this value. For more information, see [Instruments Developer Help](https://help.apple.com/instruments/developer/mac/current/#/devcd5016d31).

## Discussion

> [!important] Important
> You don’t call this method directly. Instead, the framework calls it automatically when you append an interpolated type that adopts the [FixedWidthInteger](../../swift/fixedwidthinteger.md) protocol to a log message.

## See Also

### Appending Generic Types

- [appendInterpolation(_:align:privacy:)](<appendinterpolation(__align_privacy_)-84m60.md>) — Appends an interpolated textual representation of a type.
- [appendInterpolation(_:align:privacy:attributes:)](<appendinterpolation(__align_privacy_attributes_)-xyum.md>) — Appends an interpolated textual representation of a type using the specified attributes.
- [appendInterpolation(_:align:privacy:)](<appendinterpolation(__align_privacy_)-8hwmt.md>) — Appends an interpolated type description.
- [appendInterpolation(_:align:privacy:attributes:)](<appendinterpolation(__align_privacy_attributes_)-9hehv.md>) — Appends an interpolated type description with the specified attributes.
