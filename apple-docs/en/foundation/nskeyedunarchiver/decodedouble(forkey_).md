---
title: 'decodeDouble(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiver/decodedouble(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/decodedouble(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/decodedouble%28forkey%3A%29.json'
content_hash: 'sha256:24dd083e5f1dba52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# decodeDouble(forKey:)

<sub>Instance Method</sub>

Decodes a double-precision floating-point value associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeDouble(forKey key: String) -> Double
```

## Parameters

- `key` — A key in the archive within the current decoding scope. `key` must not be `nil`.

## Return Value

The double-precision floating-point value associated with the key `key`. Returns `0.0` if `key` does not exist.

## Discussion

If the archived value was encoded as single-precision, the type is coerced.

## See Also

### Related Documentation

- [- encodeFloat:forKey:](<../nskeyedarchiver/encode(__forkey_)-67rcs.md>) — Encodes a given `float` value and associates it with a key.
- [- encodeDouble:forKey:](<../nskeyedarchiver/encode(__forkey_)-1mkfl.md>) — Encodes a given `double` value and associates it with a key.

### Decoding Data

- [- containsValueForKey:](<containsvalue(forkey_).md>) — Returns a Boolean value that indicates whether the archive contains a value for a given key within the current decoding scope.
- [decodeDecodable(_:forKey:)](<decodedecodable(__forkey_).md>) — Decodes a decodable value associated with a given key.
- [decodeTopLevelDecodable(_:forKey:)](<decodetopleveldecodable(__forkey_).md>) — Decodes a top-level decodable value associated with a given key.
- [- decodeBoolForKey:](<decodebool(forkey_).md>) — Decodes a Boolean value associated with a given key.
- [- decodeBytesForKey:returnedLength:](<decodebytes(forkey_returnedlength_).md>) — Decodes a stream of bytes associated with a given key.
- [- decodeFloatForKey:](<decodefloat(forkey_).md>) — Decodes a single-precision floating-point value associated with a given key.
- [- decodeInt32ForKey:](<decodeint32(forkey_).md>) — Decodes a 32-bit integer value associated with a given key.
- [- decodeInt64ForKey:](<decodeint64(forkey_).md>) — Decodes a 64-bit integer value associated with a given key.
- [- decodeObjectForKey:](<decodeobject(forkey_).md>) — Decodes and returns an object associated with a given key.
- [- finishDecoding](<finishdecoding().md>) — Tells the receiver that you are finished decoding objects.
- [decodingFailurePolicy](decodingfailurepolicy.md) — The action to take when this unarchiver fails to decode an entry.
