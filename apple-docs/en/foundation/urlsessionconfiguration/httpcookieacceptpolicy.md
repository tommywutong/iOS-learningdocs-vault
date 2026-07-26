---
title: httpCookieAcceptPolicy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/httpcookieacceptpolicy
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/httpcookieacceptpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/httpcookieacceptpolicy.json'
content_hash: 'sha256:c21d38b365356707'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# httpCookieAcceptPolicy

<sub>Instance Property</sub>

A policy constant that determines when cookies should be accepted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpCookieAcceptPolicy: HTTPCookie.AcceptPolicy { get set }
```

## Discussion

This property determines the cookie accept policy for all tasks within sessions based on this configuration.

The default value is [NSHTTPCookieAcceptPolicyOnlyFromMainDocumentDomain](../httpcookie/acceptpolicy/onlyfrommaindocumentdomain.md). You can change it to any of the constants defined in the [AcceptPolicy](../httpcookie/acceptpolicy.md) enumerated type.

If you want more direct control over what cookies are accepted, set this value to [NSHTTPCookieAcceptPolicyNever](../httpcookie/acceptpolicy/never.md) and then use the [allHeaderFields](../httpurlresponse/allheaderfields.md) and [+ cookiesWithResponseHeaderFields:forURL:](<../httpcookie/cookies(withresponseheaderfields_for_).md>) methods to extract cookies from the URL response object yourself.

## See Also

### Setting cookie policies

- [HTTPShouldSetCookies](httpshouldsetcookies.md) — A Boolean value that determines whether requests should contain cookies from the cookie store.
- [HTTPCookieStorage](httpcookiestorage.md) — The cookie store for storing cookies within this session.
- [HTTPCookie](../httpcookie.md) — A representation of an HTTP cookie.
