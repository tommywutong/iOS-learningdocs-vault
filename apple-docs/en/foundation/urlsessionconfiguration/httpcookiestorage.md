---
title: httpCookieStorage
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/httpcookiestorage
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/httpcookiestorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/httpcookiestorage.json'
content_hash: 'sha256:a5daeebf6144a019'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# httpCookieStorage

<sub>Instance Property</sub>

The cookie store for storing cookies within this session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpCookieStorage: HTTPCookieStorage? { get set }
```

## Discussion

This property determines the cookie storage object used by all tasks within sessions based on this configuration.

To disable cookie storage, set this property to `nil`.

For default and background sessions, the default value is the [sharedHTTPCookieStorage](../httpcookiestorage/shared.md) cookie storage object.

For [ephemeralSessionConfiguration](ephemeral.md) sessions, the default value is a private cookie storage object that stores data in memory only, and is destroyed when you invalidate the session.

## See Also

### Setting cookie policies

- [HTTPCookieAcceptPolicy](httpcookieacceptpolicy.md) — A policy constant that determines when cookies should be accepted.
- [HTTPShouldSetCookies](httpshouldsetcookies.md) — A Boolean value that determines whether requests should contain cookies from the cookie store.
- [HTTPCookie](../httpcookie.md) — A representation of an HTTP cookie.
