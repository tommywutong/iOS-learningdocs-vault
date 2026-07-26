---
title: relativePath
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/relativepath
source_url: 'https://developer.apple.com/documentation/foundation/url/relativepath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/relativepath.json'
content_hash: 'sha256:f3f8ad038ec3f91c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# relativePath

<sub>Instance Property</sub>

The relative path of the URL if the URL conforms to RFC 3986, otherwise nil.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var relativePath: String { get }
```

## Return Value

The relative path, or an empty string if the URL has an empty path.

## Discussion

> [!note] Note
> This function resolve against the base `URL`.

## See Also

### Accessing URL representations

- [baseURL](baseurl.md) — The base URL.
- [absoluteString](absolutestring.md) — The absolute string for the URL.
- [absoluteURL](absoluteurl.md) — The absolute URL.
- [relativeString](relativestring.md) — The relative portion of a URL.
- [standardized](standardized.md) — A version of the URL with any instances of “..” or “.” resolved in its path.
- [standardizedFileURL](standardizedfileurl.md) — A standardized version of the path of a file URL.
