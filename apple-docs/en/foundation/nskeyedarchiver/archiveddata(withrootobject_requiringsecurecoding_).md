---
title: 'archivedData(withRootObject:requiringSecureCoding:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiver/archiveddata(withrootobject:requiringsecurecoding:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/archiveddata(withrootobject:requiringsecurecoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/archiveddata%28withrootobject%3Arequiringsecurecoding%3A%29.json'
content_hash: 'sha256:777bfe26a3933127'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# archivedData(withRootObject:requiringSecureCoding:)

<sub>Type Method</sub>

Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func archivedData(withRootObject object: Any, requiringSecureCoding requiresSecureCoding: Bool) throws -> Data
```

## Parameters

- `object` — The root of the object graph to archive.

- `requiresSecureCoding` — A Boolean value indicating whether all encoded objects must conform to [NSSecureCoding](../nssecurecoding.md).

## Discussion

To prevent the possibility of encoding an object that [NSKeyedUnarchiver](../nskeyedunarchiver.md) can’t decode, set `requiresSecureCoding` to true whenever possible. This ensures that all encoded objects conform to [NSSecureCoding](../nssecurecoding.md).

> [!note] Note
> Enabling secure coding doesn’t change the output format of the archive. This means that you can encode archives with secure coding enabled, and decode them later with secure coding disabled.

## See Also

### Archiving Data

- [- finishEncoding](<finishencoding().md>) — Instructs the receiver to construct the final data stream.
- [encodedData](encodeddata.md) — The encoded data for the archiver.
- [outputFormat](outputformat.md) — The format in which the receiver encodes its data.
- [requiresSecureCoding](requiressecurecoding.md) — Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [+ archivedDataWithRootObject:](<archiveddata(withrootobject_).md>) — Returns a data object that contains the encoded form of the object graph formed by the given root object. _(deprecated)_
- [+ archiveRootObject:toFile:](<archiverootobject(__tofile_).md>) — Archives an object graph rooted at a given object to a file at a given path. _(deprecated)_
