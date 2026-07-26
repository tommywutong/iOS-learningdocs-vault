---
title: dataValue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmetadataitem/datavalue
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/datavalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/datavalue.json'
content_hash: 'sha256:c11789a63e9c1d4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# dataValue

<sub>Instance Property</sub>

The value of the metadata item as a data value.

> [!warning] Deprecated
> Load the value of [dataValue](../avpartialasyncproperty/datavalue.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dataValue: Data? { get }
```

## See Also

### Accessing values

- [value](value.md) — The value of the metadata item. _(deprecated)_
- [extraAttributes](extraattributes.md) — A dictionary of additional attributes for a metadata item. _(deprecated)_
- [stringValue](stringvalue.md) — The value of the metadata item as a string. _(deprecated)_
- [numberValue](numbervalue.md) — The value of the metadata item as a number. _(deprecated)_
- [dateValue](datevalue.md) — The value of the metadata item as a date. _(deprecated)_
