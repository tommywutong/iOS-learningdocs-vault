---
title: stringValue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemetadataitem/stringvalue
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/stringvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemetadataitem/stringvalue.json'
content_hash: 'sha256:ec47221647924caa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMetadataItem](../avmutablemetadataitem.md)

# stringValue

<sub>Instance Property</sub>

The value of the metadata item as a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var stringValue: String? { get }
```

## Discussion

This value is `nil` if the system can’t represent the value as a string.

## See Also

### Accessing values

- [value](value.md) — The value for the mutable metadata item.
- [extraAttributes](extraattributes.md) — A dictionary of additional attributes for a metadata item.
- [dataType](datatype.md) — The data type of the metadata item’s value.
- [numberValue](numbervalue.md) — The value of the metadata item as a number.
- [dateValue](datevalue.md) — The value of the metadata item as a date.
- [dataValue](datavalue.md) — The value of the metadata item as a data value.
