---
title: 'encodeConditionalObject(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/encodeconditionalobject(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/encodeconditionalobject(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/encodeconditionalobject%28_%3A%29.json'
content_hash: 'sha256:c5cb6192d3040ab4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# encodeConditionalObject(_:)

<sub>Instance Method</sub>

An encoding method for subclasses to override to conditionally encode an object, preserving common references to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encodeConditionalObject(_ object: Any?)
```

## Discussion

In the overriding method, `object` should be encoded only if it’s unconditionally encoded elsewhere (with any other `encode...Object:` method).

This method must be matched by a subsequent [- decodeObject](<decodeobject().md>) message. Upon decoding, if `object` was never encoded unconditionally, `decodeObject` returns `nil` in place of `object`. However, if `object` was encoded unconditionally, all references to `object` must be resolved.

`NSCoder`’s implementation simply invokes [- encodeObject:](<encode(__)-9648d.md>).

## See Also

### Related Documentation

- [- encodeConditionalObject:](<../nsarchiver/encodeconditionalobject(__).md>) — Conditionally archives a given object. _(deprecated)_

### Encoding General Data

- [- encodeArrayOfObjCType:count:at:](<encodearray(ofobjctype_count_at_).md>) — Encodes an array of the given Objective-C type, provided the number of items and a pointer.
- [- encodeBool:forKey:](<encode(__forkey_)-7o6mu.md>) — Encodes a Boolean value and associates it with the string `key`.
- [- encodeBycopyObject:](<encodebycopyobject(__).md>) — An encoding method for subclasses to override such that it creates a copy, rather than a proxy, when decoded.
- [- encodeByrefObject:](<encodebyrefobject(__).md>) — An encoding method for subclasses to override such that it creates a proxy, rather than a copy, when decoded.
- [- encodeBytes:length:](<encodebytes(__length_).md>) — Encodes a buffer of data of an unspecified type.
- [- encodeBytes:length:forKey:](<encodebytes(__length_forkey_).md>) — Encodes a buffer of data, given its length and a pointer, and associates it with a string key.
- [- encodeConditionalObject:forKey:](<encodeconditionalobject(__forkey_).md>) — An encoding method for subclasses to override to conditionally encode an object, preserving common references to it, only if it has been unconditionally encoded.
- [- encodeDataObject:](<encode(__)-1qd1e.md>) — Encodes a given data object.
- [- encodeDouble:forKey:](<encode(__forkey_)-9xiiu.md>) — Encodes a double-precision floating point value and associates it with the string key.
- [- encodeFloat:forKey:](<encode(__forkey_)-84cez.md>) — Encodes a floating point value and associates it with the string key.
- [- encodeInt:forKey:](<encodecint(__forkey_).md>) — Encodes a C integer value and associates it with the string key.
- [- encodeInteger:forKey:](<encode(__forkey_)-2dprz.md>) — Encodes an integer value and associates it with the string key.
- [- encodeInt32:forKey:](<encode(__forkey_)-5sk4z.md>) — Encodes a 32-bit integer value and associates it with the string key.
- [- encodeInt64:forKey:](<encode(__forkey_)-dixg.md>) — Encodes a 64-bit integer value and associates it with the string key.
- [- encodeObject:](<encode(__)-9648d.md>) — Encodes an object.
