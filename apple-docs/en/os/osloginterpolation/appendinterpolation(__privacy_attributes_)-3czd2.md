---
title: 'appendInterpolation(_:privacy:attributes:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:privacy:attributes:)-3czd2'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:privacy:attributes:)-3czd2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aprivacy%3Aattributes%3A%29-3czd2.json'
content_hash: 'sha256:339db309d4028366'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:privacy:attributes:)

<sub>Instance Method</sub>

Appends an interpolated object description with the specified attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ argumentObject: @autoclosure @escaping () -> NSObject, privacy: OSLogPrivacy = .auto, attributes: String)
```

## Parameters

- `argumentObject` — The interpolated object, which the system automatically wraps in a closure. The object itself doesn’t appear in the log message. Instead, the system calls the object’s [description](../../objectivec/nsobjectprotocol/description.md) method and incorporates the value it returns.

- `privacy` — The privacy level of the interpolated value, which the system applies when it renders the value in a log message. For more information, see [OSLogPrivacy](../oslogprivacy.md). The default value is [auto](../oslogprivacy/auto.md).

- `attributes` — Additional information about the interpolated value. Tools that process log messages interpret these attributes, which you typically provide as key-value pairs. For example, Instruments processes any e_ngineering types_ you embed in this value. For more information, see [Instruments Developer Help](https://help.apple.com/instruments/developer/mac/current/#/devcd5016d31).

## Discussion

> [!important] Important
> You don’t call this method directly. Instead, the framework calls it automatically when you append an interpolated object description to a log message.

## See Also

### Appending Objects

- [appendInterpolation(_:privacy:)](<appendinterpolation(__privacy_).md>) — Appends an interpolated object description.
