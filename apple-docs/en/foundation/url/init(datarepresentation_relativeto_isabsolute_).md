---
title: 'init(dataRepresentation:relativeTo:isAbsolute:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/init(datarepresentation:relativeto:isabsolute:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(datarepresentation:relativeto:isabsolute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28datarepresentation%3Arelativeto%3Aisabsolute%3A%29.json'
content_hash: 'sha256:e0043df6a836abba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(dataRepresentation:relativeTo:isAbsolute:)

<sub>Initializer</sub>

Initializes a newly created URL using the contents of the given data, relative to a base URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(dataRepresentation: Data, relativeTo base: URL?, isAbsolute: Bool = false)
```

## Discussion

If the data representation isn’t a legal URL string as ASCII bytes, the URL object may not behave as expected. This initializer returns nil if it can’t form a valid URL from the provided string.

## See Also

### Working with the data representation of a URL

- [dataRepresentation](datarepresentation.md) — The data representation of the URL’s relativeString.
