---
title: 'archivedData(withRootObject:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.14 起废弃）, tvOS 9.0+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（5.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nskeyedarchiver/archiveddata(withrootobject:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/archiveddata(withrootobject:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/archiveddata%28withrootobject%3A%29.json'
content_hash: 'sha256:5af0e1a76721bd2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# archivedData(withRootObject:)

<sub>Type Method</sub>

Returns a data object that contains the encoded form of the object graph formed by the given root object.

> [!warning] Deprecated
> Use +archivedDataWithRootObject:requiringSecureCoding:error: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func archivedData(withRootObject rootObject: Any) -> Data
```

## Parameters

- `rootObject` — The root of the object graph to archive.

## Return Value

An `NSData` object containing the encoded form of the object graph whose root object is `rootObject`. The format of the archive is [NSPropertyListBinaryFormat_v1_0](../propertylistserialization/propertylistformat/binary.md).

## See Also

### Archiving Data

- [+ archivedDataWithRootObject:requiringSecureCoding:error:](<archiveddata(withrootobject_requiringsecurecoding_).md>) — Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [- finishEncoding](<finishencoding().md>) — Instructs the receiver to construct the final data stream.
- [encodedData](encodeddata.md) — The encoded data for the archiver.
- [outputFormat](outputformat.md) — The format in which the receiver encodes its data.
- [requiresSecureCoding](requiressecurecoding.md) — Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [+ archiveRootObject:toFile:](<archiverootobject(__tofile_).md>) — Archives an object graph rooted at a given object to a file at a given path. _(deprecated)_
