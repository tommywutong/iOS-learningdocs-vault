---
title: url
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcomponents/url
source_url: 'https://developer.apple.com/documentation/foundation/urlcomponents/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcomponents/url.json'
content_hash: 'sha256:0d2bad281d0a2a73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLComponents](../urlcomponents.md)

# url

<sub>Instance Property</sub>

A URL created from the components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var url: URL? { get }
```

## Discussion

If the NSURLComponents has an authority component (user, password, host or port) and a path component, then the path must either begin with “/” or be an empty string. If the NSURLComponents does not have an authority component (user, password, host or port) and has a path component, the path component must not start with “//”. If those requirements are not met, nil is returned.

## See Also

### Getting the URL

- [url(relativeTo:)](<url(relativeto_).md>) — Returns a URL based on the component settings and relative to a given base URL.
- [string](string.md) — A URL derived from the components object, in string form.
