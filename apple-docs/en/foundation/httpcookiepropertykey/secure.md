---
title: secure
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookiepropertykey/secure
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiepropertykey/secure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiepropertykey/secure.json'
content_hash: 'sha256:4e4173f766aed195'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookiePropertyKey](../httpcookiepropertykey.md)

# secure

<sub>Type Property</sub>

An `NSString` object indicating that the cookie should be transmitted only over secure channels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let secure: HTTPCookiePropertyKey
```

## Discussion

Providing any value for this key indicates that the cookie should remain secure.

## See Also

### Cookie property keys

- [NSHTTPCookieComment](comment.md) — An `NSString` object containing the comment for the cookie.
- [NSHTTPCookieCommentURL](commenturl.md) — An `NSURL` object or `NSString` object containing the comment URL for the cookie.
- [NSHTTPCookieDiscard](discard.md) — An `NSString` object stating whether the cookie should be discarded at the end of the session.
- [NSHTTPCookieDomain](domain.md) — An `NSString` object containing the domain for the cookie.
- [NSHTTPCookieExpires](expires.md) — An `NSDate` object or `NSString` object specifying the expiration date for the cookie.
- [NSHTTPCookieMaximumAge](maximumage.md) — An `NSString` object containing an integer value stating how long in seconds the cookie should be kept, at most.
- [NSHTTPCookieName](name.md) — An `NSString` object containing the name of the cookie (required).
- [NSHTTPCookieOriginURL](originurl.md) — An NSURL or `NSString` object containing the URL that set this cookie.
- [NSHTTPCookiePath](path.md) — An `NSString` object containing the path for the cookie.
- [NSHTTPCookiePort](port.md) — An `NSString` object containing comma-separated integer values specifying the ports for the cookie.
- [NSHTTPCookieSameSitePolicy](samesitepolicy.md) — A string indicating the same-site policy for the cookie.
- [NSHTTPCookieValue](value.md) — An `NSString` object containing the value of the cookie.
- [NSHTTPCookieVersion](version.md) — An `NSString` object that specifies the version of the cookie.
