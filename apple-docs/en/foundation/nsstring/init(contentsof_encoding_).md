---
title: 'init(contentsOf:encoding:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/init(contentsof:encoding:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(contentsof:encoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28contentsof%3Aencoding%3A%29.json'
content_hash: 'sha256:1680c87f247d0b75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(contentsOf:encoding:)

<sub>Initializer</sub>

Returns an @c NSString object initialized by reading data from a given URL interpreted using a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(contentsOf url: URL, encoding enc: UInt) throws
```

## Parameters

- `url` — The URL to read.

- `enc` — The encoding of the file at @c url.

## Return Value

An @c NSString object initialized by reading data from @c url. Returns @c nil if the URL can’t be opened or there is an encoding error.
