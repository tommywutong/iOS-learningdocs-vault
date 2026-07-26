---
title: 'init(contentsOf:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsstring/init(contentsof:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(contentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28contentsof%3A%29.json'
content_hash: 'sha256:2ae5baa1926afe10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(contentsOf:)

<sub>Initializer</sub>

Returns an @c NSString object initialized by reading data from the URL named by @c url.

> [!warning] Deprecated
> Use -initWithContentsOfURL:encoding:error: instead

<sub>tvOS, visionOS, watchOS</sub>

```swift
convenience init?(contentsOf url: URL)
```
