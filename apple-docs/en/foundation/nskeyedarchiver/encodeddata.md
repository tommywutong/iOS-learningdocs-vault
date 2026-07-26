---
title: encodedData
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyedarchiver/encodeddata
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/encodeddata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/encodeddata.json'
content_hash: 'sha256:9a590a74ba0c9161'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# encodedData

<sub>Instance Property</sub>

The encoded data for the archiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var encodedData: Data { get }
```

## Discussion

If encoding has not yet finished, invoking this property calls [- finishEncoding](<finishencoding().md>) and populates this property with the encoded data. If you initialized the keyed archiver with [- initForWritingWithMutableData:](<init(forwritingwith_).md>) and a specific mutable data instance, this property contains that instance.

## See Also

### Archiving Data

- [+ archivedDataWithRootObject:requiringSecureCoding:error:](<archiveddata(withrootobject_requiringsecurecoding_).md>) — Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [- finishEncoding](<finishencoding().md>) — Instructs the receiver to construct the final data stream.
- [outputFormat](outputformat.md) — The format in which the receiver encodes its data.
- [requiresSecureCoding](requiressecurecoding.md) — Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [+ archivedDataWithRootObject:](<archiveddata(withrootobject_).md>) — Returns a data object that contains the encoded form of the object graph formed by the given root object. _(deprecated)_
- [+ archiveRootObject:toFile:](<archiverootobject(__tofile_).md>) — Archives an object graph rooted at a given object to a file at a given path. _(deprecated)_
