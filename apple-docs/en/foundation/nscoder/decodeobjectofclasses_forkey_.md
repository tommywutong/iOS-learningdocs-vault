---
title: 'decodeObjectOfClasses:forKey:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodeobjectofclasses:forkey:'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodeobjectofclasses:forkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodeobjectofclasses%3Aforkey%3A.json'
content_hash: 'sha256:742a44d515b90df0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeObjectOfClasses:forKey:

<sub>Instance Method</sub>

Decodes an object for the key, restricted to the specified classes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (id) decodeObjectOfClasses:(NSSet<Class> *) classes forKey:(NSString *) key;
```

## Parameters

- `classes` — A set of the expected classes.

- `key` — The coder key.

## Return Value

The decoded object.

## Discussion

The class of the object may be any class in the `classes` set, or a subclass of any class in the set. Otherwise, the behavior is the same as [decodeObjectOfClass:forKey:](decodeobjectofclass_forkey_.md).

## See Also

### Decoding General Data

- [- decodeArrayOfObjCType:count:at:](<decodearray(ofobjctype_count_at_).md>) — Decodes an array of `count` items, whose Objective-C type is given by `itemType`.
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
- [decodeNXObject](decodenxobject.md) — Decodes an object previously written with [encodeNXObject:](encodenxobject_.md). _(deprecated)_
- [- decodeObject](<decodeobject().md>) — Decodes and returns an object that was previously encoded with any of the `encode…Object` methods.
- [- decodeObjectForKey:](<decodeobject(forkey_).md>) — Decodes and returns a previously-encoded object that was previously encoded with [- encodeObject:forKey:](<encode(__forkey_)-1mlmu.md>) or [- encodeConditionalObject:forKey:](<encodeconditionalobject(__forkey_).md>) and associated with the string `key`.
- [- decodePoint](<decodepoint().md>) — Decodes and returns an NSPoint structure that was previously encoded with [- encodePoint:](<encode(__)-75jv4.md>).
