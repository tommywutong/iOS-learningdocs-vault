---
title: 'encodeConditionalObject(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiver/encodeconditionalobject(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/encodeconditionalobject(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/encodeconditionalobject%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:2f508ad1ed45aaa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# encodeConditionalObject(_:forKey:)

<sub>Instance Method</sub>

Encodes a reference to a given object and associates it with a key only if it has been unconditionally encoded elsewhere in the archive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encodeConditionalObject(_ object: Any?, forKey key: String)
```

## Parameters

- `object` — The object to encode.

- `key` — The key with which to associate the encoded value. This value must not be `nil`.

## Discussion

This method is effective only if you’ve previously archived this object with this key by calling [encodeInt:forKey:](encodeint_forkey_.md).

## See Also

### Encoding Data and Objects

- [encodeEncodable(_:forKey:)](<encodeencodable(__forkey_).md>) — Encodes a given value and associates it with a key.
- [- encodeBool:forKey:](<encode(__forkey_)-9pxhm.md>) — Encodes a given Boolean value and associates it with a key.
- [- encodeBytes:length:forKey:](<encodebytes(__length_forkey_).md>) — Encodes a given number of bytes from a given C array of bytes and associates them with a key.
- [- encodeDouble:forKey:](<encode(__forkey_)-1mkfl.md>) — Encodes a given `double` value and associates it with a key.
- [- encodeFloat:forKey:](<encode(__forkey_)-67rcs.md>) — Encodes a given `float` value and associates it with a key.
- [- encodeInt32:forKey:](<encode(__forkey_)-5i7tc.md>) — Encodes a given 32-bit integer value and associates it with a key.
- [- encodeInt64:forKey:](<encode(__forkey_)-ycdd.md>) — Encodes a given 64-bit integer value and associates it with a key.
- [- encodeObject:forKey:](<encode(__forkey_)-9f4n9.md>) — Encodes a given object and associates it with a given key.
