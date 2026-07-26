---
title: 'appendInterpolation(_:privacy:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:privacy:)'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:privacy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aprivacy%3A%29.json'
content_hash: 'sha256:76ff40f36f85b831'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:privacy:)

<sub>Instance Method</sub>

Appends an interpolated object description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ argumentObject: @autoclosure @escaping () -> NSObject, privacy: OSLogPrivacy = .auto)
```

## Parameters

- `argumentObject` — The object with the description you want to add to the message. This function calls the [description](../../objectivec/nsobjectprotocol/description.md) method of the object and incorporates that value into the message string.

- `privacy` — The privacy level of the information. If you don’t specify this parameter, the default rules redact the object description.

## Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## See Also

### Appending Objects

- [appendInterpolation(_:privacy:attributes:)](<appendinterpolation(__privacy_attributes_)-3czd2.md>) — Appends an interpolated object description with the specified attributes.
