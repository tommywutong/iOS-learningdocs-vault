---
title: numberValue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemetadataitem/numbervalue
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/numbervalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemetadataitem/numbervalue.json'
content_hash: 'sha256:4c2a259788230acf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMetadataItem](../avmutablemetadataitem.md)

# numberValue

<sub>Instance Property</sub>

The value of the metadata item as a number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberValue: NSNumber? { get }
```

## Discussion

This value is `nil` if the system can’t represent the value as a number.

## See Also

### Accessing values

- [value](value.md) — The value for the mutable metadata item.
- [extraAttributes](extraattributes.md) — A dictionary of additional attributes for a metadata item.
- [dataType](datatype.md) — The data type of the metadata item’s value.
- [stringValue](stringvalue.md) — The value of the metadata item as a string.
- [dateValue](datevalue.md) — The value of the metadata item as a date.
- [dataValue](datavalue.md) — The value of the metadata item as a data value.
