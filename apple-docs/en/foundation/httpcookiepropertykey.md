---
title: HTTPCookiePropertyKey
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookiepropertykey
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiepropertykey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiepropertykey.json'
content_hash: 'sha256:5def2cfce37edfea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# HTTPCookiePropertyKey

<sub>Structure</sub>

Constants that define the supported keys in a cookie attributes dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct HTTPCookiePropertyKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Cookie property keys

- [NSHTTPCookieComment](httpcookiepropertykey/comment.md) — An `NSString` object containing the comment for the cookie.
- [NSHTTPCookieCommentURL](httpcookiepropertykey/commenturl.md) — An `NSURL` object or `NSString` object containing the comment URL for the cookie.
- [NSHTTPCookieDiscard](httpcookiepropertykey/discard.md) — An `NSString` object stating whether the cookie should be discarded at the end of the session.
- [NSHTTPCookieDomain](httpcookiepropertykey/domain.md) — An `NSString` object containing the domain for the cookie.
- [NSHTTPCookieExpires](httpcookiepropertykey/expires.md) — An `NSDate` object or `NSString` object specifying the expiration date for the cookie.
- [NSHTTPCookieMaximumAge](httpcookiepropertykey/maximumage.md) — An `NSString` object containing an integer value stating how long in seconds the cookie should be kept, at most.
- [NSHTTPCookieName](httpcookiepropertykey/name.md) — An `NSString` object containing the name of the cookie (required).
- [NSHTTPCookieOriginURL](httpcookiepropertykey/originurl.md) — An NSURL or `NSString` object containing the URL that set this cookie.
- [NSHTTPCookiePath](httpcookiepropertykey/path.md) — An `NSString` object containing the path for the cookie.
- [NSHTTPCookiePort](httpcookiepropertykey/port.md) — An `NSString` object containing comma-separated integer values specifying the ports for the cookie.
- [NSHTTPCookieSameSitePolicy](httpcookiepropertykey/samesitepolicy.md) — A string indicating the same-site policy for the cookie.
- [NSHTTPCookieSecure](httpcookiepropertykey/secure.md) — An `NSString` object indicating that the cookie should be transmitted only over secure channels.
- [NSHTTPCookieValue](httpcookiepropertykey/value.md) — An `NSString` object containing the value of the cookie.
- [NSHTTPCookieVersion](httpcookiepropertykey/version.md) — An `NSString` object that specifies the version of the cookie.

### Creating custom cookie property keys

- [init(_:)](<httpcookiepropertykey/init(__).md>) — Creates an HTTP cookie property key using the given string.
- [init(rawValue:)](<httpcookiepropertykey/init(rawvalue_).md>) — Creates an HTTP cookie property key using the given string.

### Type Properties

- [NSHTTPCookieSetByJavaScript](httpcookiepropertykey/setbyjavascript.md) — An NSString object indicating that the cookie is set via JavaScript.

## See Also

### Accessing cookie properties as key-value pairs

- [properties](httpcookie/properties.md) — The cookie’s properties.
