---
title: standardized
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/standardized
source_url: 'https://developer.apple.com/documentation/foundation/url/standardized'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/standardized.json'
content_hash: 'sha256:51786124979625c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# standardized

<sub>Instance Property</sub>

A version of the URL with any instances of “..” or “.” resolved in its path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var standardized: URL { get }
```

## See Also

### Accessing URL representations

- [baseURL](baseurl.md) — The base URL.
- [absoluteString](absolutestring.md) — The absolute string for the URL.
- [absoluteURL](absoluteurl.md) — The absolute URL.
- [relativePath](relativepath.md) — The relative path of the URL if the URL conforms to RFC 3986, otherwise nil.
- [relativeString](relativestring.md) — The relative portion of a URL.
- [standardizedFileURL](standardizedfileurl.md) — A standardized version of the path of a file URL.
