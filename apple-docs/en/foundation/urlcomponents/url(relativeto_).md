---
title: 'url(relativeTo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcomponents/url(relativeto:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcomponents/url(relativeto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcomponents/url%28relativeto%3A%29.json'
content_hash: 'sha256:66c747d9707f3564'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLComponents](../urlcomponents.md)

# url(relativeTo:)

<sub>Instance Method</sub>

Returns a URL based on the component settings and relative to a given base URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func url(relativeTo base: URL?) -> URL?
```

## Discussion

If the NSURLComponents has an authority component (user, password, host or port) and a path component, then the path must either begin with “/” or be an empty string. If the NSURLComponents does not have an authority component (user, password, host or port) and has a path component, the path component must not start with “//”. If those requirements are not met, nil is returned.

## See Also

### Getting the URL

- [url](url.md) — A URL created from the components.
- [string](string.md) — A URL derived from the components object, in string form.
