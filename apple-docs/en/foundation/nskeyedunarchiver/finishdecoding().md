---
title: finishDecoding()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyedunarchiver/finishdecoding()
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/finishdecoding()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/finishdecoding%28%29.json'
content_hash: 'sha256:222c32b4fec55d31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# finishDecoding()

<sub>Instance Method</sub>

Tells the receiver that you are finished decoding objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finishDecoding()
```

## Discussion

Invoking this method allows the receiver to notify its delegate and to perform any final operations on the archive. Once this method is invoked, the receiver cannot decode any further values.

## See Also

### Decoding Data

- [- containsValueForKey:](<containsvalue(forkey_).md>) — Returns a Boolean value that indicates whether the archive contains a value for a given key within the current decoding scope.
- [decodeDecodable(_:forKey:)](<decodedecodable(__forkey_).md>) — Decodes a decodable value associated with a given key.
- [decodeTopLevelDecodable(_:forKey:)](<decodetopleveldecodable(__forkey_).md>) — Decodes a top-level decodable value associated with a given key.
- [- decodeBoolForKey:](<decodebool(forkey_).md>) — Decodes a Boolean value associated with a given key.
- [- decodeBytesForKey:returnedLength:](<decodebytes(forkey_returnedlength_).md>) — Decodes a stream of bytes associated with a given key.
- [- decodeDoubleForKey:](<decodedouble(forkey_).md>) — Decodes a double-precision floating-point value associated with a given key.
- [- decodeFloatForKey:](<decodefloat(forkey_).md>) — Decodes a single-precision floating-point value associated with a given key.
- [- decodeInt32ForKey:](<decodeint32(forkey_).md>) — Decodes a 32-bit integer value associated with a given key.
- [- decodeInt64ForKey:](<decodeint64(forkey_).md>) — Decodes a 64-bit integer value associated with a given key.
- [- decodeObjectForKey:](<decodeobject(forkey_).md>) — Decodes and returns an object associated with a given key.
- [decodingFailurePolicy](decodingfailurepolicy.md) — The action to take when this unarchiver fails to decode an entry.
