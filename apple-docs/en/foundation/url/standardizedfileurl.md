---
title: standardizedFileURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/standardizedfileurl
source_url: 'https://developer.apple.com/documentation/foundation/url/standardizedfileurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/standardizedfileurl.json'
content_hash: 'sha256:a9cb2bd5e5694a24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# standardizedFileURL

<sub>Instance Property</sub>

A standardized version of the path of a file URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var standardizedFileURL: URL { get }
```

## Discussion

If the `isFileURL` is false, this method returns `self`.

## See Also

### Accessing URL representations

- [baseURL](baseurl.md) — The base URL.
- [absoluteString](absolutestring.md) — The absolute string for the URL.
- [absoluteURL](absoluteurl.md) — The absolute URL.
- [relativePath](relativepath.md) — The relative path of the URL if the URL conforms to RFC 3986, otherwise nil.
- [relativeString](relativestring.md) — The relative portion of a URL.
- [standardized](standardized.md) — A version of the URL with any instances of “..” or “.” resolved in its path.
