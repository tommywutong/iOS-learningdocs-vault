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
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:format:align:privacy:attributes:)-8bi90'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:align:privacy:attributes:)-8bi90'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aformat%3Aalign%3Aprivacy%3Aattributes%3A%29-8bi90.json'
content_hash: 'sha256:ed5b25c884b5ac87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:format:align:privacy:attributes:)

<sub>Instance Method</sub>

Appends an interpolated double with the specified attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ number: @autoclosure @escaping () -> Double, format: OSLogFloatFormatting = .fixed, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto, attributes: String)
```

## Parameters

- `number` — The interpolated double. The system automatically wraps this value in a closure.

- `format` — The format to apply to the value when the system renders it in a log message. For more information, see [OSLogFloatFormatting](../oslogfloatformatting.md). The default value is [fixed](../oslogfloatformatting/fixed.md).

- `align` — The alignment and minimum number of columns to use when the system renders the value in a log message. For more information, see [OSLogStringAlignment](../oslogstringalignment.md). The default value is [none](../oslogstringalignment/none.md).

- `privacy` — The privacy level of the value, which the system applies when it renders the value in a log message. For more information, see [OSLogPrivacy](../oslogprivacy.md). The default value is [auto](../oslogprivacy/auto.md).

- `attributes` — Additional information about the value. Tools that process log messages interpret these attributes, which you typically provide as key-value pairs. For example, Instruments processes any  e_ngineering types_ you embed in this value. For more information, see [Instruments Developer Help](https://help.apple.com/instruments/developer/mac/current/#/devcd5016d31).

## Discussion

> [!important] Important
> You don’t call this method directly. Instead, the framework calls it automatically when you append an interpolated double to a log message.

## See Also

### Appending Doubles

- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-6mu00.md>) — Appends an interpolated double.
