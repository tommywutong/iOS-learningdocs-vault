---
title: stringValue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/stringvalue
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/stringvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/stringvalue.json'
content_hash: 'sha256:faedc5fd69253adf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# stringValue

<sub>Type Property</sub>

The value of the metadata item as a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var stringValue: AVAsyncProperty<Root, String?> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

This value is `nil` if the system can’t represent the value as a string.

## See Also

### Loading values

- [dataType](../avmetadataitem/datatype.md) — The data type of the metadata item’s value.
- [value](value.md) — The value of the metadata item.
- [numberValue](numbervalue.md) — The value of the metadata item as a number.
- [dateValue](datevalue.md) — The value of the metadata item as a date.
- [dataValue](datavalue.md) — The value of the metadata item as a data value.
- [extraAttributes](extraattributes.md) — A dictionary of additional attributes for the item.
