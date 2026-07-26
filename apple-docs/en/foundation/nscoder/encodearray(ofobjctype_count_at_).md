---
title: 'encodeArray(ofObjCType:count:at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/encodearray(ofobjctype:count:at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/encodearray(ofobjctype:count:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/encodearray%28ofobjctype%3Acount%3Aat%3A%29.json'
content_hash: 'sha256:4d66970362373000'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# encodeArray(ofObjCType:count:at:)

<sub>Instance Method</sub>

Encodes an array of the given Objective-C type, provided the number of items and a pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encodeArray(ofObjCType type: UnsafePointer<CChar>, count: Int, at array: UnsafeRawPointer)
```

## Discussion

The values are encoded from the buffer beginning at `address`. `itemType` must contain exactly one type code. `NSCoder`’s implementation invokes [- encodeValueOfObjCType:at:](<encodevalue(ofobjctype_at_).md>) to encode the entire array of items. Subclasses that implement the [- encodeValueOfObjCType:at:](<encodevalue(ofobjctype_at_).md>) method do not need to override this method.

This method must be matched by a subsequent [- decodeArrayOfObjCType:count:at:](<decodearray(ofobjctype_count_at_).md>) message.

For information on creating an Objective-C type code suitable for `itemType`, see [Type Encodings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100).

### Special Considerations

You should not use this method to encode C arrays of Objective-C objects. See [- decodeArrayOfObjCType:count:at:](<decodearray(ofobjctype_count_at_).md>) for more details.

## See Also

### Encoding General Data

- [- encodeBool:forKey:](<encode(__forkey_)-7o6mu.md>) — Encodes a Boolean value and associates it with the string `key`.
- [- encodeBycopyObject:](<encodebycopyobject(__).md>) — An encoding method for subclasses to override such that it creates a copy, rather than a proxy, when decoded.
- [- encodeByrefObject:](<encodebyrefobject(__).md>) — An encoding method for subclasses to override such that it creates a proxy, rather than a copy, when decoded.
- [- encodeBytes:length:](<encodebytes(__length_).md>) — Encodes a buffer of data of an unspecified type.
- [- encodeBytes:length:forKey:](<encodebytes(__length_forkey_).md>) — Encodes a buffer of data, given its length and a pointer, and associates it with a string key.
- [- encodeConditionalObject:](<encodeconditionalobject(__).md>) — An encoding method for subclasses to override to conditionally encode an object, preserving common references to it.
- [- encodeConditionalObject:forKey:](<encodeconditionalobject(__forkey_).md>) — An encoding method for subclasses to override to conditionally encode an object, preserving common references to it, only if it has been unconditionally encoded.
- [- encodeDataObject:](<encode(__)-1qd1e.md>) — Encodes a given data object.
- [- encodeDouble:forKey:](<encode(__forkey_)-9xiiu.md>) — Encodes a double-precision floating point value and associates it with the string key.
- [- encodeFloat:forKey:](<encode(__forkey_)-84cez.md>) — Encodes a floating point value and associates it with the string key.
- [- encodeInt:forKey:](<encodecint(__forkey_).md>) — Encodes a C integer value and associates it with the string key.
- [- encodeInteger:forKey:](<encode(__forkey_)-2dprz.md>) — Encodes an integer value and associates it with the string key.
- [- encodeInt32:forKey:](<encode(__forkey_)-5sk4z.md>) — Encodes a 32-bit integer value and associates it with the string key.
- [- encodeInt64:forKey:](<encode(__forkey_)-dixg.md>) — Encodes a 64-bit integer value and associates it with the string key.
- [- encodeObject:](<encode(__)-9648d.md>) — Encodes an object.
