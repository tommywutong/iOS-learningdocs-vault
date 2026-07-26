---
title: NSKeyedUnarchiver
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyedunarchiver
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver.json'
content_hash: 'sha256:0ac43e4a68a8cfc3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSKeyedUnarchiver

<sub>Class</sub>

A decoder that restores data from an archive referenced by keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSKeyedUnarchiver
```

## Overview

[NSKeyedUnarchiver](nskeyedunarchiver.md) is a concrete subclass of [NSCoder](nscoder.md) that defines methods for decoding a set of named objects (and scalar values) from a keyed archive. The [NSKeyedArchiver](nskeyedarchiver.md) class produces archives that this class can decode.

The archiver creates keyed archive as a hierarchy of objects. The archiver treats each object as a namespace into which it can encode other objects. This means that an unarchiver can only decode objects encoded within the immediate scope of their parent object. Objects encoded elsewhere in the hierarchy — whether higher than, lower than, or parallel to this particular object — aren’t accessible. In this way, the keys used by a particular object to encode its instance variables need to be unique only within the scope of that object.

If you invoke one of the `decode`-prefixed methods of this class using a key that does not exist in the archive, the return value indicates failure. This value varies by decoded type. For example, if a key does not exist in an archive, [- decodeBoolForKey:](<nskeyedunarchiver/decodebool(forkey_).md>) returns [false](../swift/false.md), [decodeIntForKey:](nskeyedunarchiver/decodeintforkey_.md) returns `0`, and [- decodeObjectForKey:](<nskeyedunarchiver/decodeobject(forkey_).md>) returns `nil`.

[NSKeyedUnarchiver](nskeyedunarchiver.md) supports limited type coercion for numeric types. You can use any of the integer decode methods to decode a value encoded as any type of integer, whether a standard `Int` or an explicit 32-bit or 64-bit integer. Likewise, you can use the `Float`- or `Double`-returning decode methods to handle value encoded as a `Float` or `Double`. If an encoded value is too large to fit within the coerced type, the decoding method throws a [NSRangeException](nsexceptionname/rangeexception.md). Further, when trying to coerce a value to an incompatible type — for example decoding an `Int` as a `Float` — the decoding method throws an [NSInvalidUnarchiveOperationException](nsexceptionname/invalidunarchiveoperationexception.md).

## Relationships

- **Inherits From**: [NSCoder](nscoder.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Keyed Unarchiver

- [- initForReadingFromData:error:](<nskeyedunarchiver/init(forreadingfrom_).md>) — Initializes an archiver to decode data from the specified location.
- [- init](<nskeyedunarchiver/init().md>) — Initializes an archiver to decode data. _(deprecated)_
- [- initForReadingWithData:](<nskeyedunarchiver/init(forreadingwith_).md>) — Initializes an archiver to decode data from the specified location. _(deprecated)_

### Unarchiving Data

- [unarchiveTopLevelObjectWithData(_:)](<nskeyedunarchiver/unarchivetoplevelobjectwithdata(__).md>) — Decodes a previously-archived object graph, and returns the root object.
- [unarchivedObject(ofClass:from:)](<nskeyedunarchiver/unarchivedobject(ofclass_from_).md>) — Decodes a previously-archived object graph, and returns the root object as the specified type.
- [+ unarchivedObjectOfClasses:fromData:error:](<nskeyedunarchiver/unarchivedobject(ofclasses_from_)-b9t5.md>) — Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [unarchivedObject(ofClasses:from:)](<nskeyedunarchiver/unarchivedobject(ofclasses_from_)-3h32t.md>) — Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [requiresSecureCoding](nskeyedunarchiver/requiressecurecoding.md) — Indicates whether the receiver requires all unarchived classes to conform to [NSSecureCoding](nssecurecoding.md).
- [+ unarchiveObjectWithData:](<nskeyedunarchiver/unarchiveobject(with_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object. _(deprecated)_
- [+ unarchiveObjectWithFile:](<nskeyedunarchiver/unarchiveobject(withfile_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path. _(deprecated)_

### Decoding Data

- [- containsValueForKey:](<nskeyedunarchiver/containsvalue(forkey_).md>) — Returns a Boolean value that indicates whether the archive contains a value for a given key within the current decoding scope.
- [decodeDecodable(_:forKey:)](<nskeyedunarchiver/decodedecodable(__forkey_).md>) — Decodes a decodable value associated with a given key.
- [decodeTopLevelDecodable(_:forKey:)](<nskeyedunarchiver/decodetopleveldecodable(__forkey_).md>) — Decodes a top-level decodable value associated with a given key.
- [- decodeBoolForKey:](<nskeyedunarchiver/decodebool(forkey_).md>) — Decodes a Boolean value associated with a given key.
- [- decodeBytesForKey:returnedLength:](<nskeyedunarchiver/decodebytes(forkey_returnedlength_).md>) — Decodes a stream of bytes associated with a given key.
- [- decodeDoubleForKey:](<nskeyedunarchiver/decodedouble(forkey_).md>) — Decodes a double-precision floating-point value associated with a given key.
- [- decodeFloatForKey:](<nskeyedunarchiver/decodefloat(forkey_).md>) — Decodes a single-precision floating-point value associated with a given key.
- [- decodeInt32ForKey:](<nskeyedunarchiver/decodeint32(forkey_).md>) — Decodes a 32-bit integer value associated with a given key.
- [- decodeInt64ForKey:](<nskeyedunarchiver/decodeint64(forkey_).md>) — Decodes a 64-bit integer value associated with a given key.
- [- decodeObjectForKey:](<nskeyedunarchiver/decodeobject(forkey_).md>) — Decodes and returns an object associated with a given key.
- [- finishDecoding](<nskeyedunarchiver/finishdecoding().md>) — Tells the receiver that you are finished decoding objects.
- [decodingFailurePolicy](nskeyedunarchiver/decodingfailurepolicy.md) — The action to take when this unarchiver fails to decode an entry.

### Managing the Delegate

- [delegate](nskeyedunarchiver/delegate.md) — The receiver’s delegate.

### Managing Class Names

- [+ setClass:forClassName:](<nskeyedunarchiver/setclass(__forclassname_)-swift.type.method.md>) — Sets a global translation mapping to decode objects encoded with a given class name as instances of a given class instead.
- [+ classForClassName:](<nskeyedunarchiver/class(forclassname_)-swift.type.method.md>) — Returns the class from which this unarchiver instantiates an encoded object with a given class name.
- [- setClass:forClassName:](<nskeyedunarchiver/setclass(__forclassname_)-swift.method.md>) — Sets a translation mapping on this unarchiver to decode objects encoded with a given class name as instances of a given class instead.
- [- classForClassName:](<nskeyedunarchiver/class(forclassname_)-swift.method.md>) — Returns the class from which this unarchiver instantiates an encoded object with a given class name.

### Constants

- [Keyed Unarchiving Exception Names](keyed-unarchiving-exception-names.md) — Names of exceptions that are raised by `NSKeyedUnarchiver` if there is a problem extracting an archive.

### Initializers

- [init(forReadingFromData:)](<nskeyedunarchiver/init(forreadingfromdata_).md>)
- [init(forReadingWithData:)](<nskeyedunarchiver/init(forreadingwithdata_).md>) _(deprecated)_

### Type Methods

- [unarchivedArrayOfObjects(ofClass:from:)](<nskeyedunarchiver/unarchivedarrayofobjects(ofclass_from_).md>)
- [unarchivedArrayOfObjects(ofClasses:from:)](<nskeyedunarchiver/unarchivedarrayofobjects(ofclasses_from_).md>)
- [unarchivedDictionary(keysOfClasses:objectsOfClasses:from:)](<nskeyedunarchiver/unarchiveddictionary(keysofclasses_objectsofclasses_from_).md>)
- [unarchivedDictionary(ofKeyClass:objectClass:from:)](<nskeyedunarchiver/unarchiveddictionary(ofkeyclass_objectclass_from_).md>)

## See Also

### Keyed Archivers

- [NSKeyedArchiver](nskeyedarchiver.md) — An encoder that stores an object’s data to an archive referenced by keys.
- [NSKeyedArchiverDelegate](nskeyedarchiverdelegate.md) — The optional methods implemented by the delegate of a keyed archiver.
- [NSKeyedUnarchiverDelegate](nskeyedunarchiverdelegate.md) — The optional methods implemented by the delegate of a keyed unarchiver.
- [NSCoder](nscoder.md) — An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.
- [NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md) — A value transformer that converts data to and from classes that support secure coding.
