---
title: 'stringWithUTF8String:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/stringwithutf8string:'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/stringwithutf8string:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/stringwithutf8string%3A.json'
content_hash: 'sha256:e30aa2a062f628b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# stringWithUTF8String:

<sub>Type Method</sub>

Returns a string created by copying the data from a given C array of UTF8-encoded bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) stringWithUTF8String:(const char *) nullTerminatedCString;
```
