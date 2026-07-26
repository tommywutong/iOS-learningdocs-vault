---
title: 'decodeObjectOfClass:forKey:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodeobjectofclass:forkey:'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodeobjectofclass:forkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodeobjectofclass%3Aforkey%3A.json'
content_hash: 'sha256:a211fdb5435b772c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeObjectOfClass:forKey:

<sub>Instance Method</sub>

Decodes an object for the key, restricted to the specified class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (id) decodeObjectOfClass:(Class) aClass forKey:(NSString *) key;
```

## Parameters

- `aClass` — The expect class type.

- `key` — The coder key.

## Return Value

The decoded object.

## Discussion

If the coder responds [true](../../swift/true.md) to [requiresSecureCoding](requiressecurecoding.md), then an exception will be thrown if the class to be decoded does not implement [NSSecureCoding](../nssecurecoding.md) or is not [isKind(of:)](<../../objectivec/nsobjectprotocol/iskind(of_).md>) of `aClass`.

If the coder responds [false](../../swift/false.md) to [requiresSecureCoding](requiressecurecoding.md), then the class argument is ignored and no check of the class of the decoded object is performed, exactly as if [- decodeObjectForKey:](<decodeobject(forkey_).md>) had been called.

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
