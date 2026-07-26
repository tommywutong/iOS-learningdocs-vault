---
title: 'decodeArray(ofObjCType:count:at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodearray(ofobjctype:count:at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodearray(ofobjctype:count:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodearray%28ofobjctype%3Acount%3Aat%3A%29.json'
content_hash: 'sha256:39e4fffd83f8bc81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeArray(ofObjCType:count:at:)

<sub>Instance Method</sub>

Decodes an array of `count` items, whose Objective-C type is given by `itemType`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeArray(ofObjCType itemType: UnsafePointer<CChar>, count: Int, at array: UnsafeMutableRawPointer)
```

## Discussion

The items are decoded into the buffer beginning at `address`, which must be large enough to contain them all. `itemType` must contain exactly one type code. `NSCoder`’s implementation invokes [- decodeValueOfObjCType:at:](<decodevalue(ofobjctype_at_).md>) to decode the entire array of items.

This method matches an [- encodeArrayOfObjCType:count:at:](<encodearray(ofobjctype_count_at_).md>) message used during encoding.

For information on creating an Objective-C type code suitable for `itemType`, see [Type Encodings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100).

### Special Considerations

You should not use this method to decode C arrays of Objective-C objects. For historical reasons, returned objects will have an additional ownership reference which you can only relinquish using [CFRelease](../../corefoundation/cfrelease.md).

## See Also

### Decoding General Data

- [- decodeBoolForKey:](<decodebool(forkey_).md>) — Decodes and returns a boolean value that was previously encoded with [- encodeBool:forKey:](<encode(__forkey_)-7o6mu.md>) and associated with the string `key`.
- [- decodeBytesForKey:returnedLength:](<decodebytes(forkey_returnedlength_).md>) — Decodes a buffer of data that was previously encoded with [- encodeBytes:length:forKey:](<encodebytes(__length_forkey_).md>) and associated with the string `key`.
- [- decodeBytesWithReturnedLength:](<decodebytes(withreturnedlength_).md>) — Decodes a buffer of data whose types are unspecified.
- [- decodeDataObject](<decodedata().md>) — Decodes and returns an `NSData` object that was previously encoded with [- encodeDataObject:](<encode(__)-1qd1e.md>). Subclasses must override this method.
- [- decodeDoubleForKey:](<decodedouble(forkey_).md>) — Decodes and returns a double value that was previously encoded with either [- encodeFloat:forKey:](<encode(__forkey_)-84cez.md>) or [- encodeDouble:forKey:](<encode(__forkey_)-9xiiu.md>) and associated with the string `key`.
- [- decodeFloatForKey:](<decodefloat(forkey_).md>) — Decodes and returns a float value that was previously encoded with [- encodeFloat:forKey:](<encode(__forkey_)-84cez.md>) or [- encodeDouble:forKey:](<encode(__forkey_)-9xiiu.md>) and associated with the string `key`.
- [- decodeIntForKey:](<decodecint(forkey_).md>) — Decodes and returns an int value that was previously encoded with [- encodeInt:forKey:](<encodecint(__forkey_).md>), [- encodeInteger:forKey:](<encode(__forkey_)-2dprz.md>), [- encodeInt32:forKey:](<encode(__forkey_)-5sk4z.md>), or [- encodeInt64:forKey:](<encode(__forkey_)-dixg.md>) and associated with the string `key`.
- [- decodeIntegerForKey:](<decodeinteger(forkey_).md>) — Decodes and returns an NSInteger value that was previously encoded with [- encodeInt:forKey:](<encodecint(__forkey_).md>), [- encodeInteger:forKey:](<encode(__forkey_)-2dprz.md>), [- encodeInt32:forKey:](<encode(__forkey_)-5sk4z.md>), or [- encodeInt64:forKey:](<encode(__forkey_)-dixg.md>) and associated with the string `key`.
- [- decodeInt32ForKey:](<decodeint32(forkey_).md>) — Decodes and returns a 32-bit integer value that was previously encoded with [- encodeInt:forKey:](<encodecint(__forkey_).md>), [- encodeInteger:forKey:](<encode(__forkey_)-2dprz.md>), [- encodeInt32:forKey:](<encode(__forkey_)-5sk4z.md>), or [- encodeInt64:forKey:](<encode(__forkey_)-dixg.md>) and associated with the string `key`.
- [- decodeInt64ForKey:](<decodeint64(forkey_).md>) — Decodes and returns a 64-bit integer value that was previously encoded with [- encodeInt:forKey:](<encodecint(__forkey_).md>), [- encodeInteger:forKey:](<encode(__forkey_)-2dprz.md>), [- encodeInt32:forKey:](<encode(__forkey_)-5sk4z.md>), or [- encodeInt64:forKey:](<encode(__forkey_)-dixg.md>) and associated with the string `key`.
- [- decodeObject](<decodeobject().md>) — Decodes and returns an object that was previously encoded with any of the `encode…Object` methods.
- [- decodeObjectForKey:](<decodeobject(forkey_).md>) — Decodes and returns a previously-encoded object that was previously encoded with [- encodeObject:forKey:](<encode(__forkey_)-1mlmu.md>) or [- encodeConditionalObject:forKey:](<encodeconditionalobject(__forkey_).md>) and associated with the string `key`.
- [- decodePoint](<decodepoint().md>) — Decodes and returns an NSPoint structure that was previously encoded with [- encodePoint:](<encode(__)-75jv4.md>).
- [- decodePointForKey:](<decodepoint(forkey_).md>) — Decodes and returns an NSPoint structure that was previously encoded with [- encodePoint:forKey:](<encode(__forkey_)-27lif.md>).
- [- decodePropertyList](<decodepropertylist().md>) — Decodes a property list that was previously encoded with [- encodePropertyList:](<encodepropertylist(__).md>).
