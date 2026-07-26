---
title: utf8String
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/utf8string
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/utf8string'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/utf8string.json'
content_hash: 'sha256:b7ae5d8411e301cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# utf8String

<sub>Instance Property</sub>

A null-terminated UTF8 representation of the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var utf8String: UnsafePointer<CChar>? { get }
```

## Discussion

This C string is a pointer to a structure inside the string object, which may have a lifetime shorter than the string object and will certainly not have a longer lifetime. Therefore, you should copy the C string if it needs to be stored outside of the memory context in which you use this property.

## See Also

### Getting C Strings

- [- cStringUsingEncoding:](<cstring(using_).md>) — Returns a representation of the string as a C string using a given encoding.
- [- getCString:maxLength:encoding:](<getcstring(__maxlength_encoding_).md>) — Converts the string to a given encoding and stores it in a buffer.
