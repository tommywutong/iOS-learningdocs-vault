---
title: value
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmetadataitem/value
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/value.json'
content_hash: 'sha256:f1ee804b927d6e46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# value

<sub>Instance Property</sub>

The value of the metadata item.

> [!warning] Deprecated
> Load [value](../avpartialasyncproperty/value.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var value: (any NSCopying & NSObjectProtocol)? { get }
```

## See Also

### Accessing values

- [extraAttributes](extraattributes.md) — A dictionary of additional attributes for a metadata item. _(deprecated)_
- [stringValue](stringvalue.md) — The value of the metadata item as a string. _(deprecated)_
- [numberValue](numbervalue.md) — The value of the metadata item as a number. _(deprecated)_
- [dateValue](datevalue.md) — The value of the metadata item as a date. _(deprecated)_
- [dataValue](datavalue.md) — The value of the metadata item as a data value. _(deprecated)_
