---
title: 'stringWithContentsOfURL:usedEncoding:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/stringwithcontentsofurl:usedencoding:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/stringwithcontentsofurl:usedencoding:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/stringwithcontentsofurl%3Ausedencoding%3Aerror%3A.json'
content_hash: 'sha256:a2eba971a3e2d1d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# stringWithContentsOfURL:usedEncoding:error:

<sub>Type Method</sub>

Returns a string created by reading data from the file at a given URL and returns by reference the encoding used to interpret the data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) stringWithContentsOfURL:(NSURL *) url usedEncoding:(NSStringEncoding *) enc error:(NSError **) error;
```
