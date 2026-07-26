---
title: 'encode(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiver/encode(_:forkey:)-5i7tc'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/encode(_:forkey:)-5i7tc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/encode%28_%3Aforkey%3A%29-5i7tc.json'
content_hash: 'sha256:f2d54ebfd2e918f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# encode(_:forKey:)

<sub>Instance Method</sub>

Encodes a given 32-bit integer value and associates it with a key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(_ value: Int32, forKey key: String)
```

## Parameters

- `value` — The value to encode.

- `key` — The key with which to associate `intv`. This value must not be `nil`.

## See Also

### Related Documentation

- [- decodeInt32ForKey:](<../nskeyedunarchiver/decodeint32(forkey_).md>) — Decodes a 32-bit integer value associated with a given key.

### Encoding Data and Objects

- [encodeEncodable(_:forKey:)](<encodeencodable(__forkey_).md>) — Encodes a given value and associates it with a key.
- [- encodeBool:forKey:](<encode(__forkey_)-9pxhm.md>) — Encodes a given Boolean value and associates it with a key.
- [- encodeBytes:length:forKey:](<encodebytes(__length_forkey_).md>) — Encodes a given number of bytes from a given C array of bytes and associates them with a key.
- [- encodeConditionalObject:forKey:](<encodeconditionalobject(__forkey_).md>) — Encodes a reference to a given object and associates it with a key only if it has been unconditionally encoded elsewhere in the archive.
- [- encodeDouble:forKey:](<encode(__forkey_)-1mkfl.md>) — Encodes a given `double` value and associates it with a key.
- [- encodeFloat:forKey:](<encode(__forkey_)-67rcs.md>) — Encodes a given `float` value and associates it with a key.
- [- encodeInt64:forKey:](<encode(__forkey_)-ycdd.md>) — Encodes a given 64-bit integer value and associates it with a key.
- [- encodeObject:forKey:](<encode(__forkey_)-9f4n9.md>) — Encodes a given object and associates it with a given key.
