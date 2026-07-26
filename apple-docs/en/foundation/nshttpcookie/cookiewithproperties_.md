---
title: 'cookieWithProperties:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nshttpcookie/cookiewithproperties:'
source_url: 'https://developer.apple.com/documentation/foundation/nshttpcookie/cookiewithproperties:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshttpcookie/cookiewithproperties%3A.json'
content_hash: 'sha256:a469816176bff06f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# cookieWithProperties:

<sub>Type Method</sub>

Creates and initializes an HTTP cookie object using the provided properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSHTTPCookie *) cookieWithProperties:(NSDictionary<NSString *,id> *) properties;
```

## Parameters

- `properties` — The properties for the new cookie object, expressed as key value pairs.

## Return Value

The newly created cookie object. Returns `nil` if the provided properties are invalid.

## Discussion

To successfully create a cookie, you must provide values for (at least) the [NSHTTPCookiePath](../httpcookiepropertykey/path.md), [NSHTTPCookieName](../httpcookiepropertykey/name.md), and [NSHTTPCookieValue](../httpcookiepropertykey/value.md) keys, and either the [NSHTTPCookieOriginURL](../httpcookiepropertykey/originurl.md) key or the [NSHTTPCookieDomain](../httpcookiepropertykey/domain.md) key.

See Accepting cookies for more information on the available cookie attribute constants and the constraints imposed on the values in the dictionary.

## See Also

### Creating cookies

- [+ cookiesWithResponseHeaderFields:forURL:](<../httpcookie/cookies(withresponseheaderfields_for_).md>) — Creates an array of HTTP cookies that corresponds to the provided response header fields for the provided URL.
- [- initWithProperties:](<../httpcookie/init(properties_).md>) — Initializes an HTTP cookie object with the given cookie properties.
