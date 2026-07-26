---
title: numberValue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/numbervalue
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/numbervalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/numbervalue.json'
content_hash: 'sha256:3e5df97b84f5ee96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# numberValue

<sub>Type Property</sub>

The value of the metadata item as a number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var numberValue: AVAsyncProperty<Root, NSNumber?> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

This value is `nil` if the system can’t represent the value as a number.

## See Also

### Loading values

- [dataType](../avmetadataitem/datatype.md) — The data type of the metadata item’s value.
- [value](value.md) — The value of the metadata item.
- [stringValue](stringvalue.md) — The value of the metadata item as a string.
- [dateValue](datevalue.md) — The value of the metadata item as a date.
- [dataValue](datavalue.md) — The value of the metadata item as a data value.
- [extraAttributes](extraattributes.md) — A dictionary of additional attributes for the item.
