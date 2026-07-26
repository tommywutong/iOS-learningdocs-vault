---
title: httpShouldSetCookies
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/httpshouldsetcookies
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/httpshouldsetcookies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/httpshouldsetcookies.json'
content_hash: 'sha256:dd36ba10dc64cad6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# httpShouldSetCookies

<sub>Instance Property</sub>

A Boolean value that determines whether requests should contain cookies from the cookie store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpShouldSetCookies: Bool { get set }
```

## Discussion

This property controls whether tasks within sessions based on this configuration should automatically provide cookies from the shared cookie store when making requests.

If you want to provide cookies yourself, set this value to [false](../../swift/false.md) and provide a `Cookie` header either through the session’s [HTTPAdditionalHeaders](httpadditionalheaders.md) property or on a per-request level using a custom [NSURLRequest](../nsurlrequest.md) object.

The default value is [true](../../swift/true.md).

## See Also

### Setting cookie policies

- [HTTPCookieAcceptPolicy](httpcookieacceptpolicy.md) — A policy constant that determines when cookies should be accepted.
- [HTTPCookieStorage](httpcookiestorage.md) — The cookie store for storing cookies within this session.
- [HTTPCookie](../httpcookie.md) — A representation of an HTTP cookie.
