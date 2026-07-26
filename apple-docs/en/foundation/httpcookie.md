---
title: HTTPCookie
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie.json'
content_hash: 'sha256:7850271e2783b897'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# HTTPCookie

<sub>Class</sub>

A representation of an HTTP cookie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class HTTPCookie
```

## Overview

An [HTTPCookie](httpcookie.md) object is immutable, initialized from a dictionary that contains the attributes of the cookie. This class supports two different cookie versions:

- Version 0: The original cookie format defined by Netscape. Most cookies are in this format.
- Version 1: The cookie format defined in [RFC 6265](https://tools.ietf.org/html/rfc6265), HTTP State Management Mechanism.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating cookies

- [+ cookiesWithResponseHeaderFields:forURL:](<httpcookie/cookies(withresponseheaderfields_for_).md>) — Creates an array of HTTP cookies that corresponds to the provided response header fields for the provided URL.
- [- initWithProperties:](<httpcookie/init(properties_).md>) — Initializes an HTTP cookie object with the given cookie properties.

### Converting cookies to request headers

- [+ requestHeaderFieldsWithCookies:](<httpcookie/requestheaderfields(with_).md>) — Converts an array of cookies to a dictionary of header fields.

### Getting cookie host properties

- [domain](httpcookie/domain.md) — The domain of the cookie.
- [path](httpcookie/path.md) — The cookie’s path.
- [portList](httpcookie/portlist.md) — The cookie’s port list.

### Getting cookie metadata

- [name](httpcookie/name.md) — The cookie’s name.
- [value](httpcookie/value.md) — The cookie’s string value.
- [version](httpcookie/version.md) — The cookie’s version.

### Determining cookie lifespan

- [expiresDate](httpcookie/expiresdate.md) — The cookie’s expiration date.
- [sessionOnly](httpcookie/issessiononly.md) — A Boolean value that indicates whether the cookie should be discarded at the end of the session (regardless of expiration date).

### Securing cookies

- [HTTPOnly](httpcookie/ishttponly.md) — A Boolean value that indicates whether the cookie should only be sent to HTTP servers.
- [secure](httpcookie/issecure.md) — A Boolean value that indicates whether the cookie may only be sent over secure channels.
- [sameSitePolicy](httpcookie/samesitepolicy.md) — A Boolean value that indicates whether to restrict the cookie to requests sent back to the same site that created it.
- [HTTPCookieStringPolicy](httpcookiestringpolicy.md) — Values that indicate whether to restrict the cookie to requests sent back to the same site that created it.

### Accessing cookie properties as key-value pairs

- [properties](httpcookie/properties.md) — The cookie’s properties.
- [HTTPCookiePropertyKey](httpcookiepropertykey.md) — Constants that define the supported keys in a cookie attributes dictionary.

### Getting user-readable cookie metadata

- [comment](httpcookie/comment.md) — The cookie’s comment string.
- [commentURL](httpcookie/commenturl.md) — The cookie’s comment URL.

### Accepting cookies

- [AcceptPolicy](httpcookie/acceptpolicy.md) — Cookie acceptance policies implemented by the [HTTPCookieStorage](httpcookiestorage.md) class.

## See Also

### Cookies

- [HTTPCookieStorage](httpcookiestorage.md) — A container that manages the storage of cookies.
