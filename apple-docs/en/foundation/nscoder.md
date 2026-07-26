---
title: NSCoder
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscoder
source_url: 'https://developer.apple.com/documentation/foundation/nscoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder.json'
content_hash: 'sha256:ea0739b53d5e5d21'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCoder

<sub>Class</sub>

An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSCoder
```

## Overview

[NSCoder](nscoder.md) declares the interface used by concrete subclasses to transfer objects and other values between memory and some other format. This capability provides the basis for archiving (storing objects and data on disk) and distribution (copying objects and data items between different processes or threads). The concrete subclasses provided by Foundation for these purposes are [NSArchiver](nsarchiver.md), [NSUnarchiver](nsunarchiver.md), [NSKeyedArchiver](nskeyedarchiver.md), [NSKeyedUnarchiver](nskeyedunarchiver.md), and [NSPortCoder](nsportcoder.md). Concrete subclasses of [NSCoder](nscoder.md) are “coder classes”, and instances of these classes are “coder objects” (or simply “coders”). A coder that can only encode values is an “encoder”, and one that can only decode values is a “decoder”.

[NSCoder](nscoder.md) operates on objects, scalars, C arrays, structures, strings, and on pointers to these types. It doesn’t handle types whose implementation varies across platforms, such as `union`, `void *`, function pointers, and long chains of pointers. A coder stores object type information along with the data, so an object decoded from a stream of bytes is normally of the same class as the object that was originally encoded into the stream. An object can change its class when encoded, however; this is described in [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

The AVFoundation framework adds methods to the [NSCoder](nscoder.md) class to make it easier to create archives including Core Media time structures, and extract Core Media time structure from archives.

### Subclassing Notes

For details of how to create a subclass of `NSCoder`, see [Subclassing NSCoder](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/subclassing.html#//apple_ref/doc/uid/20000951) in [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSArchiver](nsarchiver.md), [NSKeyedArchiver](nskeyedarchiver.md), [NSKeyedUnarchiver](nskeyedunarchiver.md), [NSUnarchiver](nsunarchiver.md), [NSXPCCoder](nsxpccoder.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting a Coder

- [allowsKeyedCoding](nscoder/allowskeyedcoding.md) — A Boolean value that indicates whether the receiver supports keyed coding of objects.
- [- containsValueForKey:](<nscoder/containsvalue(forkey_).md>) — Returns a Boolean value that indicates whether an encoded value is available for a string.
- [decodingFailurePolicy](nscoder/decodingfailurepolicy-swift.property.md) — The action the coder should take when decoding fails.
- [DecodingFailurePolicy](nscoder/decodingfailurepolicy-swift.enum.md) — Policies describing the action the coder should take when encountering decode failures.

### Encoding General Data

- [- encodeArrayOfObjCType:count:at:](<nscoder/encodearray(ofobjctype_count_at_).md>) — Encodes an array of the given Objective-C type, provided the number of items and a pointer.
- [- encodeBool:forKey:](<nscoder/encode(__forkey_)-7o6mu.md>) — Encodes a Boolean value and associates it with the string `key`.
- [- encodeBycopyObject:](<nscoder/encodebycopyobject(__).md>) — An encoding method for subclasses to override such that it creates a copy, rather than a proxy, when decoded.
- [- encodeByrefObject:](<nscoder/encodebyrefobject(__).md>) — An encoding method for subclasses to override such that it creates a proxy, rather than a copy, when decoded.
- [- encodeBytes:length:](<nscoder/encodebytes(__length_).md>) — Encodes a buffer of data of an unspecified type.
- [- encodeBytes:length:forKey:](<nscoder/encodebytes(__length_forkey_).md>) — Encodes a buffer of data, given its length and a pointer, and associates it with a string key.
- [- encodeConditionalObject:](<nscoder/encodeconditionalobject(__).md>) — An encoding method for subclasses to override to conditionally encode an object, preserving common references to it.
- [- encodeConditionalObject:forKey:](<nscoder/encodeconditionalobject(__forkey_).md>) — An encoding method for subclasses to override to conditionally encode an object, preserving common references to it, only if it has been unconditionally encoded.
- [- encodeDataObject:](<nscoder/encode(__)-1qd1e.md>) — Encodes a given data object.
- [- encodeDouble:forKey:](<nscoder/encode(__forkey_)-9xiiu.md>) — Encodes a double-precision floating point value and associates it with the string key.
- [- encodeFloat:forKey:](<nscoder/encode(__forkey_)-84cez.md>) — Encodes a floating point value and associates it with the string key.
- [- encodeInt:forKey:](<nscoder/encodecint(__forkey_).md>) — Encodes a C integer value and associates it with the string key.
- [- encodeInteger:forKey:](<nscoder/encode(__forkey_)-2dprz.md>) — Encodes an integer value and associates it with the string key.
- [- encodeInt32:forKey:](<nscoder/encode(__forkey_)-5sk4z.md>) — Encodes a 32-bit integer value and associates it with the string key.
- [- encodeInt64:forKey:](<nscoder/encode(__forkey_)-dixg.md>) — Encodes a 64-bit integer value and associates it with the string key.
- [- encodeObject:](<nscoder/encode(__)-9648d.md>) — Encodes an object.
- [- encodeObject:forKey:](<nscoder/encode(__forkey_)-1mlmu.md>) — Encodes an object and associates it with the string key.
- [- encodePoint:](<nscoder/encode(__)-75jv4.md>) — Encodes a point.
- [- encodePoint:forKey:](<nscoder/encode(__forkey_)-27lif.md>) — Encodes a point and associates it with the string key.
- [- encodePropertyList:](<nscoder/encodepropertylist(__).md>) — Encodes a property list.
- [- encodeRect:](<nscoder/encode(__)-3c1wz.md>) — Encodes a rectangle structure.
- [- encodeRect:forKey:](<nscoder/encode(__forkey_)-2knxx.md>) — Encodes a rectangle structure and associates it with the string key.
- [- encodeRootObject:](<nscoder/encoderootobject(__).md>) — An encoding method for subclasses to override to encode an interconnected group of objects, starting with the provided root object.
- [- encodeSize:](<nscoder/encode(__)-82i7c.md>) — Encodes a size structure.
- [- encodeSize:forKey:](<nscoder/encode(__forkey_)-9imtu.md>) — Encodes a size structure and associates it with the given string key.
- [- encodeValueOfObjCType:at:](<nscoder/encodevalue(ofobjctype_at_).md>) — Encodes a value of the given type at the given address.

### Encoding Geometry-Based Data

- [- encodeCGAffineTransform:forKey:](<nscoder/encode(__forkey_)-29jyx.md>) — Encodes an affine transform and associates it with the specified key in the receiver’s archive.
- [- encodeCGPoint:forKey:](<nscoder/encode(__forkey_)-7z9kc.md>) — Encodes a point and associates it with the specified key in the receiver’s archive.
- [- encodeCGRect:forKey:](<nscoder/encode(__forkey_)-10qhm.md>) — Encodes a rectangle and associates it with the specified key in the receiver’s archive.
- [- encodeCGSize:forKey:](<nscoder/encode(__forkey_)-6wq3n.md>) — Encodes size information and associates it with the specified key in the coder’s archive.
- [- encodeCGVector:forKey:](<nscoder/encode(__forkey_)-26fxa.md>) — Encodes vector data and associates it with the specified key in the coder’s archive.
- [- encodeDirectionalEdgeInsets:forKey:](<nscoder/encode(__forkey_)-7oo2n.md>) — Encodes directional edge inset data and associates it with the specified key in the coder’s archive.
- [- encodeUIEdgeInsets:forKey:](<nscoder/encode(__forkey_)-44zsc.md>) — Encodes edge inset data and associates it with the specified key in the coder’s archive.
- [- encodeUIOffset:forKey:](<nscoder/encode(__forkey_)-9d1qy.md>) — Encodes offset data and associates it with the specified key in the coder’s archive.

### Encoding Core Media Time Structures

- [- encodeCMTime:forKey:](<nscoder/encode(__forkey_)-6wbby.md>) — Encodes a given Core Media time structure and associates it with a specified key.
- [- encodeCMTimeRange:forKey:](<nscoder/encode(__forkey_)-46lo8.md>) — Encodes a given Core Media time range structure and associates it with a specified key.
- [- encodeCMTimeMapping:forKey:](<nscoder/encode(__forkey_)-8tefb.md>) — Encodes a given Core Media time mapping structure and associates it with a specified key.

### Secure Coding

- [requiresSecureCoding](nscoder/requiressecurecoding.md) — Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [allowedClasses](nscoder/allowedclasses.md) — The set of coded classes allowed for secure coding.

### Decoding Top-Level Objects

- [decodeObject(of:forKey:)](<nscoder/decodeobject(of_forkey_)-7tmft.md>) — Decode an object as an expected type, failing if the archived type doesn’t match.
- [decodeObject(of:forKey:)](<nscoder/decodeobject(of_forkey_)-roif.md>) — Decode an object as one of several expected types, failing if the archived type doesn’t match any of the types.
- [decodeTopLevelObject()](<nscoder/decodetoplevelobject().md>) — Decodes a previously-encoded object. _(deprecated)_
- [decodeTopLevelObject(forKey:)](<nscoder/decodetoplevelobject(forkey_).md>) — Decodes the previously-encoded object associated by a key.
- [decodeTopLevelObject(of:forKey:)](<nscoder/decodetoplevelobject(of_forkey_)-3w6pd.md>) — Decode an object as one of several expected types, failing if the archived type does not match.
- [decodeTopLevelObject(of:forKey:)](<nscoder/decodetoplevelobject(of_forkey_)-5lnnn.md>) — Decode an object as one of several expected types, failing if the archived type does not match.

### Decoding General Data

- [- decodeArrayOfObjCType:count:at:](<nscoder/decodearray(ofobjctype_count_at_).md>) — Decodes an array of `count` items, whose Objective-C type is given by `itemType`.
- [- decodeBoolForKey:](<nscoder/decodebool(forkey_).md>) — Decodes and returns a boolean value that was previously encoded with [- encodeBool:forKey:](<nscoder/encode(__forkey_)-7o6mu.md>) and associated with the string `key`.
- [- decodeBytesForKey:returnedLength:](<nscoder/decodebytes(forkey_returnedlength_).md>) — Decodes a buffer of data that was previously encoded with [- encodeBytes:length:forKey:](<nscoder/encodebytes(__length_forkey_).md>) and associated with the string `key`.
- [- decodeBytesWithReturnedLength:](<nscoder/decodebytes(withreturnedlength_).md>) — Decodes a buffer of data whose types are unspecified.
- [- decodeDataObject](<nscoder/decodedata().md>) — Decodes and returns an `NSData` object that was previously encoded with [- encodeDataObject:](<nscoder/encode(__)-1qd1e.md>). Subclasses must override this method.
- [- decodeDoubleForKey:](<nscoder/decodedouble(forkey_).md>) — Decodes and returns a double value that was previously encoded with either [- encodeFloat:forKey:](<nscoder/encode(__forkey_)-84cez.md>) or [- encodeDouble:forKey:](<nscoder/encode(__forkey_)-9xiiu.md>) and associated with the string `key`.
- [- decodeFloatForKey:](<nscoder/decodefloat(forkey_).md>) — Decodes and returns a float value that was previously encoded with [- encodeFloat:forKey:](<nscoder/encode(__forkey_)-84cez.md>) or [- encodeDouble:forKey:](<nscoder/encode(__forkey_)-9xiiu.md>) and associated with the string `key`.
- [- decodeIntForKey:](<nscoder/decodecint(forkey_).md>) — Decodes and returns an int value that was previously encoded with [- encodeInt:forKey:](<nscoder/encodecint(__forkey_).md>), [- encodeInteger:forKey:](<nscoder/encode(__forkey_)-2dprz.md>), [- encodeInt32:forKey:](<nscoder/encode(__forkey_)-5sk4z.md>), or [- encodeInt64:forKey:](<nscoder/encode(__forkey_)-dixg.md>) and associated with the string `key`.
- [- decodeIntegerForKey:](<nscoder/decodeinteger(forkey_).md>) — Decodes and returns an NSInteger value that was previously encoded with [- encodeInt:forKey:](<nscoder/encodecint(__forkey_).md>), [- encodeInteger:forKey:](<nscoder/encode(__forkey_)-2dprz.md>), [- encodeInt32:forKey:](<nscoder/encode(__forkey_)-5sk4z.md>), or [- encodeInt64:forKey:](<nscoder/encode(__forkey_)-dixg.md>) and associated with the string `key`.
- [- decodeInt32ForKey:](<nscoder/decodeint32(forkey_).md>) — Decodes and returns a 32-bit integer value that was previously encoded with [- encodeInt:forKey:](<nscoder/encodecint(__forkey_).md>), [- encodeInteger:forKey:](<nscoder/encode(__forkey_)-2dprz.md>), [- encodeInt32:forKey:](<nscoder/encode(__forkey_)-5sk4z.md>), or [- encodeInt64:forKey:](<nscoder/encode(__forkey_)-dixg.md>) and associated with the string `key`.
- [- decodeInt64ForKey:](<nscoder/decodeint64(forkey_).md>) — Decodes and returns a 64-bit integer value that was previously encoded with [- encodeInt:forKey:](<nscoder/encodecint(__forkey_).md>), [- encodeInteger:forKey:](<nscoder/encode(__forkey_)-2dprz.md>), [- encodeInt32:forKey:](<nscoder/encode(__forkey_)-5sk4z.md>), or [- encodeInt64:forKey:](<nscoder/encode(__forkey_)-dixg.md>) and associated with the string `key`.
- [- decodeObject](<nscoder/decodeobject().md>) — Decodes and returns an object that was previously encoded with any of the `encode…Object` methods.
- [- decodeObjectForKey:](<nscoder/decodeobject(forkey_).md>) — Decodes and returns a previously-encoded object that was previously encoded with [- encodeObject:forKey:](<nscoder/encode(__forkey_)-1mlmu.md>) or [- encodeConditionalObject:forKey:](<nscoder/encodeconditionalobject(__forkey_).md>) and associated with the string `key`.
- [- decodePoint](<nscoder/decodepoint().md>) — Decodes and returns an NSPoint structure that was previously encoded with [- encodePoint:](<nscoder/encode(__)-75jv4.md>).
- [- decodePointForKey:](<nscoder/decodepoint(forkey_).md>) — Decodes and returns an NSPoint structure that was previously encoded with [- encodePoint:forKey:](<nscoder/encode(__forkey_)-27lif.md>).
- [- decodePropertyList](<nscoder/decodepropertylist().md>) — Decodes a property list that was previously encoded with [- encodePropertyList:](<nscoder/encodepropertylist(__).md>).
- [- decodeRect](<nscoder/decoderect().md>) — Decodes and returns an NSRect structure that was previously encoded with [- encodeRect:](<nscoder/encode(__)-3c1wz.md>).
- [- decodeRectForKey:](<nscoder/decoderect(forkey_).md>) — Decodes and returns an NSRect structure that was previously encoded with [- encodeRect:forKey:](<nscoder/encode(__forkey_)-2knxx.md>).
- [- decodeSize](<nscoder/decodesize().md>) — Decodes and returns an NSSize structure that was previously encoded with [- encodeSize:](<nscoder/encode(__)-82i7c.md>).
- [- decodeSizeForKey:](<nscoder/decodesize(forkey_).md>) — Decodes and returns an NSSize structure that was previously encoded with [- encodeSize:forKey:](<nscoder/encode(__forkey_)-9imtu.md>).
- [- decodeValueOfObjCType:at:](<nscoder/decodevalue(ofobjctype_at_).md>) — Decodes a single value, whose Objective-C type is given by `valueType`. _(deprecated)_
- [- decodeValueOfObjCType:at:size:](<nscoder/decodevalue(ofobjctype_at_size_).md>) — Decodes a single value of a known type from the specified data buffer.
- [- decodePropertyListForKey:](<nscoder/decodepropertylist(forkey_).md>) — Returns a decoded property list for the specified key.

### Decoding Geometry-Based Data

- [- decodeCGAffineTransformForKey:](<nscoder/decodecgaffinetransform(forkey_).md>) — Decodes and returns the Core Graphics affine transform structure associated with the specified key in the coder’s archive.
- [- decodeCGPointForKey:](<nscoder/decodecgpoint(forkey_).md>) — Decodes and returns the Core Graphics point structure associated with the specified key in the coder’s archive.
- [- decodeCGRectForKey:](<nscoder/decodecgrect(forkey_).md>) — Decodes and returns the Core Graphics rectangle structure associated with the specified key in the coder’s archive.
- [- decodeCGSizeForKey:](<nscoder/decodecgsize(forkey_).md>) — Decodes and returns the Core Graphics size structure associated with the specified key in the coder’s archive.
- [- decodeCGVectorForKey:](<nscoder/decodecgvector(forkey_).md>) — Decodes and returns the Core Graphics vector data associated with the specified key in the coder’s archive.
- [- decodeDirectionalEdgeInsetsForKey:](<nscoder/decodedirectionaledgeinsets(forkey_).md>) — Decodes and returns the UIKit directional edge insets structure associated with the specified key in the coder’s archive.
- [- decodeUIEdgeInsetsForKey:](<nscoder/decodeuiedgeinsets(forkey_).md>) — Decodes and returns the UIKit edge insets structure associated with the specified key in the coder’s archive.
- [- decodeUIOffsetForKey:](<nscoder/decodeuioffset(forkey_).md>) — Decodes and returns the UIKit offset structure associated with the specified key in the coder’s archive.

### Decoding Core Media Time Structures

- [- decodeCMTimeForKey:](<nscoder/decodetime(forkey_).md>) — Returns the Core Media time structure associated with a given key.
- [- decodeCMTimeRangeForKey:](<nscoder/decodetimerange(forkey_).md>) — Returns the Core Media time range structure associated with a given key.
- [- decodeCMTimeMappingForKey:](<nscoder/decodetimemapping(forkey_).md>) — Returns the Core Media time mapping structure associated with a given key.

### Managing Decode Errors

- [- failWithError:](<nscoder/failwitherror(__).md>) — Signals to this coder that the decode operation has failed.
- [error](nscoder/error.md) — An error in the top-level encode.

### Getting Version Information

- [systemVersion](nscoder/systemversion.md) — The system version in effect for the archive.
- [- versionForClassName:](<nscoder/version(forclassname_).md>) — This method is present for historical reasons and is not used with keyed archivers.

### Representing Geometric Types as Strings

- [cgAffineTransform(for:)](<nscoder/cgaffinetransform(for_).md>) — Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [cgPoint(for:)](<nscoder/cgpoint(for_).md>) — Returns a Core Graphics point structure corresponding to the data in a given string.
- [cgRect(for:)](<nscoder/cgrect(for_).md>) — Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [cgSize(for:)](<nscoder/cgsize(for_).md>) — Returns a Core Graphics size structure corresponding to the data in a given string.
- [cgVector(for:)](<nscoder/cgvector(for_).md>) — Returns a Core Graphics vector corresponding to the data in a given string.
- [nsDirectionalEdgeInsets(for:)](<nscoder/nsdirectionaledgeinsets(for_).md>) — Returns a directional edge insets structure based on data in the specified string.
- [uiEdgeInsets(for:)](<nscoder/uiedgeinsets(for_).md>) — Returns a UIKit edge insets structure based on the data in the specified string.
- [uiOffset(for:)](<nscoder/uioffset(for_).md>) — Returns a UIKit offset structure corresponding to the data in a given string.
- [string(for:)](<nscoder/string(for_)-4qz0a.md>) — Returns a string formatted to contain the data from a rectangle.
- [string(for:)](<nscoder/string(for_)-4omzv.md>) — Returns a string formatted to contain the data from a vector data structure.
- [string(for:)](<nscoder/string(for_)-6yx6n.md>) — Returns a string formatted to contain the data from an affine transform.
- [string(for:)](<nscoder/string(for_)-6ix86.md>) — Returns a string formatted to contain the data from a point.
- [string(for:)](<nscoder/string(for_)-2f1xb.md>) — Returns a string formatted to contain the data from a size data structure.
- [string(for:)](<nscoder/string(for_)-hp8b.md>) — Returns a string formatted to contain the data from a directional edge insets structure.
- [string(for:)](<nscoder/string(for_)-26b4z.md>) — Returns a string formatted to contain the data from an edge insets structure.
- [string(for:)](<nscoder/string(for_)-454dj.md>) — Returns a string formatted to contain the data from an offset structure.

### Error Codes

- [NSCoderErrorMaximum](nscodererrormaximum-swift.var.md) — The end of the range of error codes reserved for coder errors.
- [NSCoderErrorMinimum](nscodererrorminimum-swift.var.md) — The start of the range of error codes reserved for coder errors.
- [NSCoderReadCorruptError](nscoderreadcorrupterror-swift.var.md) — Decoding failed due to corrupt data.
- [NSCoderValueNotFoundError](nscodervaluenotfounderror-swift.var.md) — The requested data wasn’t found.
- [NSCoderInvalidValueError](nscoderinvalidvalueerror-swift.var.md) — Data wasn’t valid to encode.

### Instance Methods

- [decodeArrayOfObjects(ofClass:forKey:)](<nscoder/decodearrayofobjects(ofclass_forkey_).md>)
- [decodeArrayOfObjects(ofClasses:forKey:)](<nscoder/decodearrayofobjects(ofclasses_forkey_).md>)
- [- decodeBytesForKey:minimumLength:](<nscoder/decodebytes(forkey_minimumlength_).md>) — Decode bytes from the decoder for a given key. The length of the bytes must be greater than or equal to the `length` parameter. If the result exists, but is of insufficient length, then the decoder uses `failWithError` to fail the entire decode operation. The result of that is configurable on a per-NSCoder basis using `NSDecodingFailurePolicy`.
- [- decodeBytesWithMinimumLength:](<nscoder/decodebytes(withminimumlength_).md>) — Decode bytes from the decoder. The length of the bytes must be greater than or equal to the `length` parameter. If the result exists, but is of insufficient length, then the decoder uses `failWithError` to fail the entire decode operation. The result of that is configurable on a per-NSCoder basis using `NSDecodingFailurePolicy`.
- [decodeDictionary(withKeyClass:objectClass:forKey:)](<nscoder/decodedictionary(withkeyclass_objectclass_forkey_).md>)
- [decodeDictionary(withKeysOfClasses:objectsOfClasses:forKey:)](<nscoder/decodedictionary(withkeysofclasses_objectsofclasses_forkey_).md>)

## See Also

### Keyed Archivers

- [NSKeyedArchiver](nskeyedarchiver.md) — An encoder that stores an object’s data to an archive referenced by keys.
- [NSKeyedArchiverDelegate](nskeyedarchiverdelegate.md) — The optional methods implemented by the delegate of a keyed archiver.
- [NSKeyedUnarchiver](nskeyedunarchiver.md) — A decoder that restores data from an archive referenced by keys.
- [NSKeyedUnarchiverDelegate](nskeyedunarchiverdelegate.md) — The optional methods implemented by the delegate of a keyed unarchiver.
- [NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md) — A value transformer that converts data to and from classes that support secure coding.
