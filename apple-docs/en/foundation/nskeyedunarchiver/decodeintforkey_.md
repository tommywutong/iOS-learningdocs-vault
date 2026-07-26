---
title: 'decodeIntForKey:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiver/decodeintforkey:'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/decodeintforkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/decodeintforkey%3A.json'
content_hash: 'sha256:a1ea72f2b3f1e1fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# decodeIntForKey:

<sub>Instance Method</sub>

Decodes an integer value associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (int) decodeIntForKey:(NSString *) key;
```

## Parameters

- `key` — A key in the archive within the current decoding scope. `key` must not be `nil`.

## Return Value

The integer value associated with the key `key`. Returns `0` if `key` does not exist.

## Discussion

If the archived value was encoded with a different size but is still an integer, the type is coerced. If the archived value is too large to fit into the default size for an integer, the method raises an `NSRangeException`.

## See Also

### Related Documentation

- [encodeInt:forKey:](../nskeyedarchiver/encodeint_forkey_.md) — Encodes a given `int` value and associates it with a key.

### Decoding Data

- [- containsValueForKey:](<containsvalue(forkey_).md>) — Returns a Boolean value that indicates whether the archive contains a value for a given key within the current decoding scope.
- [- decodeBoolForKey:](<decodebool(forkey_).md>) — Decodes a Boolean value associated with a given key.
- [- decodeBytesForKey:returnedLength:](<decodebytes(forkey_returnedlength_).md>) — Decodes a stream of bytes associated with a given key.
- [- decodeDoubleForKey:](<decodedouble(forkey_).md>) — Decodes a double-precision floating-point value associated with a given key.
- [- decodeFloatForKey:](<decodefloat(forkey_).md>) — Decodes a single-precision floating-point value associated with a given key.
- [- decodeInt32ForKey:](<decodeint32(forkey_).md>) — Decodes a 32-bit integer value associated with a given key.
- [- decodeInt64ForKey:](<decodeint64(forkey_).md>) — Decodes a 64-bit integer value associated with a given key.
- [- decodeObjectForKey:](<decodeobject(forkey_).md>) — Decodes and returns an object associated with a given key.
- [- finishDecoding](<finishdecoding().md>) — Tells the receiver that you are finished decoding objects.
- [decodingFailurePolicy](decodingfailurepolicy.md) — The action to take when this unarchiver fails to decode an entry.
