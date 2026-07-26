---
title: 'init(properties:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookie/init(properties:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/init(properties:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/init%28properties%3A%29.json'
content_hash: 'sha256:f5c0b1bde43ef538'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# init(properties:)

<sub>Initializer</sub>

Initializes an HTTP cookie object with the given cookie properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(properties: [HTTPCookiePropertyKey : Any])
```

## Parameters

- `properties` — The properties for the new cookie object, expressed as key-value pairs.

## Return Value

A new cookie object, with the given properies.

## Discussion

This initializer returns `nil` if the provided properties are invalid. To successfully create a cookie, you must provide values for (at least) the [NSHTTPCookiePath](../httpcookiepropertykey/path.md), [NSHTTPCookieName](../httpcookiepropertykey/name.md), and [NSHTTPCookieValue](../httpcookiepropertykey/value.md) keys, and either the [NSHTTPCookieOriginURL](../httpcookiepropertykey/originurl.md) key or the [NSHTTPCookieDomain](../httpcookiepropertykey/domain.md) key.

See Accepting cookies for more information on the available cookie attribute constants and the constraints imposed on the values in the dictionary.

## See Also

### Creating cookies

- [+ cookiesWithResponseHeaderFields:forURL:](<cookies(withresponseheaderfields_for_).md>) — Creates an array of HTTP cookies that corresponds to the provided response header fields for the provided URL.
