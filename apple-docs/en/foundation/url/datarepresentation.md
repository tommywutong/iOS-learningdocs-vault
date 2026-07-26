---
title: dataRepresentation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/datarepresentation
source_url: 'https://developer.apple.com/documentation/foundation/url/datarepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/datarepresentation.json'
content_hash: 'sha256:bd5f6ca2b6906597'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# dataRepresentation

<sub>Instance Property</sub>

The data representation of the URL’s relativeString.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dataRepresentation: Data { get }
```

## Discussion

If the URL was initialized with `init?(dataRepresentation:relativeTo:isAbsolute:)`, the data representation returned are the same bytes as those used at initialization; otherwise, the data representation returned are the bytes of the `relativeString` encoded with UTF8 string encoding.

## See Also

### Working with the data representation of a URL

- [init(dataRepresentation:relativeTo:isAbsolute:)](<init(datarepresentation_relativeto_isabsolute_).md>) — Initializes a newly created URL using the contents of the given data, relative to a base URL.
