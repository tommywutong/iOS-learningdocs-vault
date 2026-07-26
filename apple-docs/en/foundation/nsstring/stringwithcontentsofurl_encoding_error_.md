---
title: 'stringWithContentsOfURL:encoding:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/stringwithcontentsofurl:encoding:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/stringwithcontentsofurl:encoding:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/stringwithcontentsofurl%3Aencoding%3Aerror%3A.json'
content_hash: 'sha256:cda0ffbcbd78f25d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# stringWithContentsOfURL:encoding:error:

<sub>Type Method</sub>

Returns a string created by reading data from the file at a given path interpreted using a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) stringWithContentsOfURL:(NSURL *) url encoding:(NSStringEncoding) enc error:(NSError **) error;
```
