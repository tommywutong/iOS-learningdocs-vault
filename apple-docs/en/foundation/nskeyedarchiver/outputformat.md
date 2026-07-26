---
title: outputFormat
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyedarchiver/outputformat
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/outputformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/outputformat.json'
content_hash: 'sha256:036d58b3c3fcb71d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# outputFormat

<sub>Instance Property</sub>

The format in which the receiver encodes its data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var outputFormat: PropertyListSerialization.PropertyListFormat { get set }
```

## Discussion

The available formats are [NSPropertyListXMLFormat_v1_0](../propertylistserialization/propertylistformat/xml.md) and [NSPropertyListBinaryFormat_v1_0](../propertylistserialization/propertylistformat/binary.md).

## See Also

### Archiving Data

- [+ archivedDataWithRootObject:requiringSecureCoding:error:](<archiveddata(withrootobject_requiringsecurecoding_).md>) — Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [- finishEncoding](<finishencoding().md>) — Instructs the receiver to construct the final data stream.
- [encodedData](encodeddata.md) — The encoded data for the archiver.
- [requiresSecureCoding](requiressecurecoding.md) — Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [+ archivedDataWithRootObject:](<archiveddata(withrootobject_).md>) — Returns a data object that contains the encoded form of the object graph formed by the given root object. _(deprecated)_
- [+ archiveRootObject:toFile:](<archiverootobject(__tofile_).md>) — Archives an object graph rooted at a given object to a file at a given path. _(deprecated)_
