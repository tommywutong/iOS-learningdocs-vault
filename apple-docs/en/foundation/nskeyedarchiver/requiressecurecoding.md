---
title: requiresSecureCoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyedarchiver/requiressecurecoding
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/requiressecurecoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/requiressecurecoding.json'
content_hash: 'sha256:f959eef6083a2883'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# requiresSecureCoding

<sub>Instance Property</sub>

Indicates whether the archiver requires all archived classes to resist object substitution attacks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var requiresSecureCoding: Bool { get set }
```

## Parameters

- `flag` — [true](../../swift/true.md) if the receiver requires [NSSecureCoding](../nssecurecoding.md); [false](../../swift/false.md) if not.

## Discussion

If you set the archiver to require secure coding, it throws an exception if you attempt to archive a class which doesn’t conform to [NSSecureCoding](../nssecurecoding.md).

Note that the getter is on the superclass, [NSCoder](../nscoder.md). See [NSCoder](../nscoder.md) for more information about secure coding.

> [!note] Note
> Enabling secure coding doesn’t change the output format of the archive. This means that you can encode archives with secure coding enabled, and decode them later with secure coding disabled.

## See Also

### Archiving Data

- [+ archivedDataWithRootObject:requiringSecureCoding:error:](<archiveddata(withrootobject_requiringsecurecoding_).md>) — Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [- finishEncoding](<finishencoding().md>) — Instructs the receiver to construct the final data stream.
- [encodedData](encodeddata.md) — The encoded data for the archiver.
- [outputFormat](outputformat.md) — The format in which the receiver encodes its data.
- [+ archivedDataWithRootObject:](<archiveddata(withrootobject_).md>) — Returns a data object that contains the encoded form of the object graph formed by the given root object. _(deprecated)_
- [+ archiveRootObject:toFile:](<archiverootobject(__tofile_).md>) — Archives an object graph rooted at a given object to a file at a given path. _(deprecated)_
