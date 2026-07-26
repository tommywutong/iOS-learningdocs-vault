---
title: 'stringWithCString:encoding:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/stringwithcstring:encoding:'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/stringwithcstring:encoding:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/stringwithcstring%3Aencoding%3A.json'
content_hash: 'sha256:2042898f240f0b5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# stringWithCString:encoding:

<sub>Type Method</sub>

Returns a string containing the bytes in a given C array, interpreted according to a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) stringWithCString:(const char *) cString encoding:(NSStringEncoding) enc;
```
