---
title: baseURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/baseurl
source_url: 'https://developer.apple.com/documentation/foundation/url/baseurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/baseurl.json'
content_hash: 'sha256:8019407400924e71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# baseURL

<sub>Instance Property</sub>

The base URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var baseURL: URL? { get }
```

## Discussion

If the URL is itself absolute, then this value is `nil`.

## See Also

### Accessing URL representations

- [absoluteString](absolutestring.md) — The absolute string for the URL.
- [absoluteURL](absoluteurl.md) — The absolute URL.
- [relativePath](relativepath.md) — The relative path of the URL if the URL conforms to RFC 3986, otherwise nil.
- [relativeString](relativestring.md) — The relative portion of a URL.
- [standardized](standardized.md) — A version of the URL with any instances of “..” or “.” resolved in its path.
- [standardizedFileURL](standardizedfileurl.md) — A standardized version of the path of a file URL.
