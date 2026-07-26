---
title: 'encodeEncodable(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiver/encodeencodable(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/encodeencodable(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/encodeencodable%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:36debc5473d23508'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# encodeEncodable(_:forKey:)

<sub>Instance Method</sub>

Encodes a given value and associates it with a key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc func encodeEncodable<T>(_ value: T, forKey key: String) throws where T : Encodable
```

## Parameters

- `value` — The value to encode.

- `key` — The key with which to associate the encoded value.

## Discussion

If there’s a problem encoding the value you supply, this method throws an error based on the type of problem:

- The value fails to encode, or contains a nested value that fails to encode—this method throws the corresponding error.
- The value can’t be encoded as a property list—this method throws the [EncodingError.invalidValue(_:_:)](<../../swift/encodingerror/invalidvalue(____).md>) error.

## See Also

### Encoding Data and Objects

- [- encodeBool:forKey:](<encode(__forkey_)-9pxhm.md>) — Encodes a given Boolean value and associates it with a key.
- [- encodeBytes:length:forKey:](<encodebytes(__length_forkey_).md>) — Encodes a given number of bytes from a given C array of bytes and associates them with a key.
- [- encodeConditionalObject:forKey:](<encodeconditionalobject(__forkey_).md>) — Encodes a reference to a given object and associates it with a key only if it has been unconditionally encoded elsewhere in the archive.
- [- encodeDouble:forKey:](<encode(__forkey_)-1mkfl.md>) — Encodes a given `double` value and associates it with a key.
- [- encodeFloat:forKey:](<encode(__forkey_)-67rcs.md>) — Encodes a given `float` value and associates it with a key.
- [- encodeInt32:forKey:](<encode(__forkey_)-5i7tc.md>) — Encodes a given 32-bit integer value and associates it with a key.
- [- encodeInt64:forKey:](<encode(__forkey_)-ycdd.md>) — Encodes a given 64-bit integer value and associates it with a key.
- [- encodeObject:forKey:](<encode(__forkey_)-9f4n9.md>) — Encodes a given object and associates it with a given key.
