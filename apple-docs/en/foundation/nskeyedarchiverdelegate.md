---
title: NSKeyedArchiverDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyedarchiverdelegate
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiverdelegate.json'
content_hash: 'sha256:14d421be5ea09aa0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSKeyedArchiverDelegate

<sub>Protocol</sub>

The optional methods implemented by the delegate of a keyed archiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSKeyedArchiverDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Encoding Data and Objects

- [- archiver:didEncodeObject:](<nskeyedarchiverdelegate/archiver(__didencode_).md>) — Informs the delegate that a given object has been encoded.
- [- archiverDidFinish:](<nskeyedarchiverdelegate/archiverdidfinish(__).md>) — Notifies the delegate that encoding has finished.
- [- archiver:willEncodeObject:](<nskeyedarchiverdelegate/archiver(__willencode_).md>) — Informs the delegate that `object` is about to be encoded.
- [- archiverWillFinish:](<nskeyedarchiverdelegate/archiverwillfinish(__).md>) — Notifies the delegate that encoding is about to finish.
- [- archiver:willReplaceObject:withObject:](<nskeyedarchiverdelegate/archiver(__willreplace_with_).md>) — Informs the delegate that one given object is being substituted for another given object.

## See Also

### Keyed Archivers

- [NSKeyedArchiver](nskeyedarchiver.md) — An encoder that stores an object’s data to an archive referenced by keys.
- [NSKeyedUnarchiver](nskeyedunarchiver.md) — A decoder that restores data from an archive referenced by keys.
- [NSKeyedUnarchiverDelegate](nskeyedunarchiverdelegate.md) — The optional methods implemented by the delegate of a keyed unarchiver.
- [NSCoder](nscoder.md) — An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.
- [NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md) — A value transformer that converts data to and from classes that support secure coding.
