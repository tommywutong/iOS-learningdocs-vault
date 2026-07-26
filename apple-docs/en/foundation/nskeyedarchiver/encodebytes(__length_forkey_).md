---
title: 'encodeBytes(_:length:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiver/encodebytes(_:length:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/encodebytes(_:length:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/encodebytes%28_%3Alength%3Aforkey%3A%29.json'
content_hash: 'sha256:0af95e2498a87b87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# encodeBytes(_:length:forKey:)

<sub>Instance Method</sub>

Encodes a given number of bytes from a given C array of bytes and associates them with a key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encodeBytes(_ bytes: UnsafePointer<UInt8>?, length: Int, forKey key: String)
```

## Parameters

- `bytes` — A C array of bytes to encode.

- `length` — The number of bytes from `bytesp` to encode.

- `key` — The key with which to associate the encoded value. This value must not be `nil`.

## See Also

### Related Documentation

- [- decodeBytesForKey:returnedLength:](<../nskeyedunarchiver/decodebytes(forkey_returnedlength_).md>) — Decodes a stream of bytes associated with a given key.

### Encoding Data and Objects

- [encodeEncodable(_:forKey:)](<encodeencodable(__forkey_).md>) — Encodes a given value and associates it with a key.
- [- encodeBool:forKey:](<encode(__forkey_)-9pxhm.md>) — Encodes a given Boolean value and associates it with a key.
- [- encodeConditionalObject:forKey:](<encodeconditionalobject(__forkey_).md>) — Encodes a reference to a given object and associates it with a key only if it has been unconditionally encoded elsewhere in the archive.
- [- encodeDouble:forKey:](<encode(__forkey_)-1mkfl.md>) — Encodes a given `double` value and associates it with a key.
- [- encodeFloat:forKey:](<encode(__forkey_)-67rcs.md>) — Encodes a given `float` value and associates it with a key.
- [- encodeInt32:forKey:](<encode(__forkey_)-5i7tc.md>) — Encodes a given 32-bit integer value and associates it with a key.
- [- encodeInt64:forKey:](<encode(__forkey_)-ycdd.md>) — Encodes a given 64-bit integer value and associates it with a key.
- [- encodeObject:forKey:](<encode(__forkey_)-9f4n9.md>) — Encodes a given object and associates it with a given key.
