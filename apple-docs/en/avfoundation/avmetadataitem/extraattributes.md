---
title: extraAttributes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmetadataitem/extraattributes
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/extraattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/extraattributes.json'
content_hash: 'sha256:2b6db9b25ad869d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# extraAttributes

<sub>Instance Property</sub>

A dictionary of additional attributes for a metadata item.

> [!warning] Deprecated
> Load the value of [extraAttributes](../avpartialasyncproperty/extraattributes.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var extraAttributes: [AVMetadataExtraAttributeKey : Any]? { get }
```

## Discussion

Extra attributes, when they’re present, are specific to metadata container formats and keys in their associated key-spaces. For example, a metadata item can represent the “attached picture” frame defined by the ID3 tag specification with keyspace [AVMetadataKeySpaceID3](../avmetadatakeyspace/id3.md) and key [AVMetadataID3MetadataKeyAttachedPicture](../avmetadatakey/id3metadatakeyattachedpicture.md), a value that carries the image data, and extra attributes that include a description of the picture as carried in the ‘APIC’ frame of the ID3 tag.

## See Also

### Accessing values

- [value](value.md) — The value of the metadata item. _(deprecated)_
- [stringValue](stringvalue.md) — The value of the metadata item as a string. _(deprecated)_
- [numberValue](numbervalue.md) — The value of the metadata item as a number. _(deprecated)_
- [dateValue](datevalue.md) — The value of the metadata item as a date. _(deprecated)_
- [dataValue](datavalue.md) — The value of the metadata item as a data value. _(deprecated)_
