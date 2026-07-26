---
title: NSKeyedArchiver
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyedarchiver
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver.json'
content_hash: 'sha256:c7715d927b69ea10'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSKeyedArchiver

<sub>Class</sub>

An encoder that stores an object’s data to an archive referenced by keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSKeyedArchiver
```

## Overview

[NSKeyedArchiver](nskeyedarchiver.md), a concrete subclass of [NSCoder](nscoder.md), provides a way to encode objects (and scalar values) into an architecture-independent format suitable for storage in a file. When you archive a set of objects, the archiver writes the class information and instance variables for each object to the archive. The companion class [NSKeyedUnarchiver](nskeyedunarchiver.md) decodes the data in an archive and creates a set of objects equivalent to the original set.

A keyed archive differs from a non-keyed archive in that all the objects and values encoded into the archive have names, or keys. When decoding a non-keyed archive, the decoder must decode values in the same order the original encoder used. When decoding a keyed archive, the decoder requests values by name, meaning it can decode values out of sequence or not at all. Keyed archives, therefore, provide better support for forward and backward compatibility.

The keys given to encoded values must be unique only within the scope of the currently-encoding object. A keyed archive is hierarchical, so the keys used by object A to encode its instance variables don’t conflict with the keys used by object B. This is true even if A and B are instances of the same class. Within a single object, however, the keys used by a subclass can conflict with keys used in its superclasses.

An [NSArchiver](nsarchiver.md) object can write the archive data to a file or to a mutable-data object (an instance of [NSMutableData](nsmutabledata.md)) that you provide.

## Relationships

- **Inherits From**: [NSCoder](nscoder.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Keyed Archiver

- [- initRequiringSecureCoding:](<nskeyedarchiver/init(requiringsecurecoding_).md>) — Creates an archiver to encode data, and optionally disables secure coding.
- [- init](<nskeyedarchiver/init().md>) — Initializes an archiver to encode data. _(deprecated)_
- [- initForWritingWithMutableData:](<nskeyedarchiver/init(forwritingwith_).md>) — Initializes an archiver to encode data into a given a mutable-data object. _(deprecated)_

### Archiving Data

- [+ archivedDataWithRootObject:requiringSecureCoding:error:](<nskeyedarchiver/archiveddata(withrootobject_requiringsecurecoding_).md>) — Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [- finishEncoding](<nskeyedarchiver/finishencoding().md>) — Instructs the receiver to construct the final data stream.
- [encodedData](nskeyedarchiver/encodeddata.md) — The encoded data for the archiver.
- [outputFormat](nskeyedarchiver/outputformat.md) — The format in which the receiver encodes its data.
- [requiresSecureCoding](nskeyedarchiver/requiressecurecoding.md) — Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [+ archivedDataWithRootObject:](<nskeyedarchiver/archiveddata(withrootobject_).md>) — Returns a data object that contains the encoded form of the object graph formed by the given root object. _(deprecated)_
- [+ archiveRootObject:toFile:](<nskeyedarchiver/archiverootobject(__tofile_).md>) — Archives an object graph rooted at a given object to a file at a given path. _(deprecated)_

### Encoding Data and Objects

- [encodeEncodable(_:forKey:)](<nskeyedarchiver/encodeencodable(__forkey_).md>) — Encodes a given value and associates it with a key.
- [- encodeBool:forKey:](<nskeyedarchiver/encode(__forkey_)-9pxhm.md>) — Encodes a given Boolean value and associates it with a key.
- [- encodeBytes:length:forKey:](<nskeyedarchiver/encodebytes(__length_forkey_).md>) — Encodes a given number of bytes from a given C array of bytes and associates them with a key.
- [- encodeConditionalObject:forKey:](<nskeyedarchiver/encodeconditionalobject(__forkey_).md>) — Encodes a reference to a given object and associates it with a key only if it has been unconditionally encoded elsewhere in the archive.
- [- encodeDouble:forKey:](<nskeyedarchiver/encode(__forkey_)-1mkfl.md>) — Encodes a given `double` value and associates it with a key.
- [- encodeFloat:forKey:](<nskeyedarchiver/encode(__forkey_)-67rcs.md>) — Encodes a given `float` value and associates it with a key.
- [- encodeInt32:forKey:](<nskeyedarchiver/encode(__forkey_)-5i7tc.md>) — Encodes a given 32-bit integer value and associates it with a key.
- [- encodeInt64:forKey:](<nskeyedarchiver/encode(__forkey_)-ycdd.md>) — Encodes a given 64-bit integer value and associates it with a key.
- [- encodeObject:forKey:](<nskeyedarchiver/encode(__forkey_)-9f4n9.md>) — Encodes a given object and associates it with a given key.

### Managing the Delegate

- [delegate](nskeyedarchiver/delegate.md) — The archiver’s delegate.

### Managing Classes and Class Names

- [+ setClassName:forClass:](<nskeyedarchiver/setclassname(__for_)-swift.type.method.md>) — Sets a global translation mapping to encode instances of a given class with the provided name, rather than their real name.
- [+ classNameForClass:](<nskeyedarchiver/classname(for_)-swift.type.method.md>) — Returns the class name with which the archiver class encodes instances of a given class.
- [- setClassName:forClass:](<nskeyedarchiver/setclassname(__for_)-swift.method.md>) — Sets a mapping for this archiver to encode instances of a given class with the provided name, rather than their real name.
- [- classNameForClass:](<nskeyedarchiver/classname(for_)-swift.method.md>) — Returns the class name with which this archiver encodes instances of a given class.

### Constants

- [Keyed Archiving Exception Names](keyed-archiving-exception-names.md) — Names of exceptions raised by this class if problems occur while creating an archive.
- [Keyed Archiver Root Object Key](keyed-archiver-root-object-key.md) — Keys that the archiver uses in the hierarchy of encoded objects.

### Initializers

- [init(forWritingWithMutableData:)](<nskeyedarchiver/init(forwritingwithmutabledata_).md>) _(deprecated)_

## See Also

### Keyed Archivers

- [NSKeyedArchiverDelegate](nskeyedarchiverdelegate.md) — The optional methods implemented by the delegate of a keyed archiver.
- [NSKeyedUnarchiver](nskeyedunarchiver.md) — A decoder that restores data from an archive referenced by keys.
- [NSKeyedUnarchiverDelegate](nskeyedunarchiverdelegate.md) — The optional methods implemented by the delegate of a keyed unarchiver.
- [NSCoder](nscoder.md) — An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.
- [NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md) — A value transformer that converts data to and from classes that support secure coding.
