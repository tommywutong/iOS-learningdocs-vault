---
title: 'init(cStringNoCopy:length:freeWhenDone:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsstring/init(cstringnocopy:length:freewhendone:)-7ssxw'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(cstringnocopy:length:freewhendone:)-7ssxw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28cstringnocopy%3Alength%3Afreewhendone%3A%29-7ssxw.json'
content_hash: 'sha256:9ca3f3f56b5dd30a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(cStringNoCopy:length:freeWhenDone:)

<sub>Initializer</sub>

> [!warning] Deprecated
> Use -initWithCString:encoding: instead

<sub>tvOS, visionOS, watchOS</sub>

```swift
convenience init?(cStringNoCopy bytes: UnsafeMutablePointer<CChar>, length: Int, freeWhenDone freeBuffer: Bool)
```
