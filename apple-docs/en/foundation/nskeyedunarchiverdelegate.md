---
title: NSKeyedUnarchiverDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyedunarchiverdelegate
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiverdelegate.json'
content_hash: 'sha256:4dffaad9e7ea61e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSKeyedUnarchiverDelegate

<sub>Protocol</sub>

The optional methods implemented by the delegate of a keyed unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSKeyedUnarchiverDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Decoding Objects

- [- unarchiver:cannotDecodeObjectOfClassName:originalClasses:](<nskeyedunarchiverdelegate/unarchiver(__cannotdecodeobjectofclassname_originalclasses_).md>) — Informs the delegate that the class with a given name is not available during decoding.
- [- unarchiver:didDecodeObject:](<nskeyedunarchiverdelegate/unarchiver(__diddecode_).md>) — Informs the delegate that a given object has been decoded.
- [- unarchiver:willReplaceObject:withObject:](<nskeyedunarchiverdelegate/unarchiver(__willreplace_with_).md>) — Informs the delegate that one object is being substituted for another.

### Finishing Decoding

- [- unarchiverDidFinish:](<nskeyedunarchiverdelegate/unarchiverdidfinish(__).md>) — Notifies the delegate that decoding has finished.
- [- unarchiverWillFinish:](<nskeyedunarchiverdelegate/unarchiverwillfinish(__).md>) — Notifies the delegate that decoding is about to finish.

## See Also

### Keyed Archivers

- [NSKeyedArchiver](nskeyedarchiver.md) — An encoder that stores an object’s data to an archive referenced by keys.
- [NSKeyedArchiverDelegate](nskeyedarchiverdelegate.md) — The optional methods implemented by the delegate of a keyed archiver.
- [NSKeyedUnarchiver](nskeyedunarchiver.md) — A decoder that restores data from an archive referenced by keys.
- [NSCoder](nscoder.md) — An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.
- [NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md) — A value transformer that converts data to and from classes that support secure coding.
