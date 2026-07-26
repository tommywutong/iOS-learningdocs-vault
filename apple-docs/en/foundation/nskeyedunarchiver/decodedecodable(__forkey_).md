---
title: 'decodeDecodable(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiver/decodedecodable(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/decodedecodable(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/decodedecodable%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:9b0d36b5251334b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# decodeDecodable(_:forKey:)

<sub>Instance Method</sub>

Decodes a decodable value associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc func decodeDecodable<T>(_ type: T.Type, forKey key: String) -> T? where T : Decodable
```

## Parameters

- `type` — The type of the value to decode.

- `key` — The key in the archive associated with the value to decode.

## See Also

### Decoding Data

- [- containsValueForKey:](<containsvalue(forkey_).md>) — Returns a Boolean value that indicates whether the archive contains a value for a given key within the current decoding scope.
- [decodeTopLevelDecodable(_:forKey:)](<decodetopleveldecodable(__forkey_).md>) — Decodes a top-level decodable value associated with a given key.
- [- decodeBoolForKey:](<decodebool(forkey_).md>) — Decodes a Boolean value associated with a given key.
- [- decodeBytesForKey:returnedLength:](<decodebytes(forkey_returnedlength_).md>) — Decodes a stream of bytes associated with a given key.
- [- decodeDoubleForKey:](<decodedouble(forkey_).md>) — Decodes a double-precision floating-point value associated with a given key.
- [- decodeFloatForKey:](<decodefloat(forkey_).md>) — Decodes a single-precision floating-point value associated with a given key.
- [- decodeInt32ForKey:](<decodeint32(forkey_).md>) — Decodes a 32-bit integer value associated with a given key.
- [- decodeInt64ForKey:](<decodeint64(forkey_).md>) — Decodes a 64-bit integer value associated with a given key.
- [- decodeObjectForKey:](<decodeobject(forkey_).md>) — Decodes and returns an object associated with a given key.
- [- finishDecoding](<finishdecoding().md>) — Tells the receiver that you are finished decoding objects.
- [decodingFailurePolicy](decodingfailurepolicy.md) — The action to take when this unarchiver fails to decode an entry.
