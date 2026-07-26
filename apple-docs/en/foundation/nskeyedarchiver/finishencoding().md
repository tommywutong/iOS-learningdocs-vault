---
title: finishEncoding()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyedarchiver/finishencoding()
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/finishencoding()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/finishencoding%28%29.json'
content_hash: 'sha256:1f9f6d6aaab37b42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# finishEncoding()

<sub>Instance Method</sub>

Instructs the receiver to construct the final data stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finishEncoding()
```

## Discussion

No more values can be encoded after this method is called. You must call this method when finished.

## See Also

### Related Documentation

- [- initForWritingWithMutableData:](<init(forwritingwith_).md>) — Initializes an archiver to encode data into a given a mutable-data object. _(deprecated)_

### Archiving Data

- [+ archivedDataWithRootObject:requiringSecureCoding:error:](<archiveddata(withrootobject_requiringsecurecoding_).md>) — Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [encodedData](encodeddata.md) — The encoded data for the archiver.
- [outputFormat](outputformat.md) — The format in which the receiver encodes its data.
- [requiresSecureCoding](requiressecurecoding.md) — Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [+ archivedDataWithRootObject:](<archiveddata(withrootobject_).md>) — Returns a data object that contains the encoded form of the object graph formed by the given root object. _(deprecated)_
- [+ archiveRootObject:toFile:](<archiverootobject(__tofile_).md>) — Archives an object graph rooted at a given object to a file at a given path. _(deprecated)_
