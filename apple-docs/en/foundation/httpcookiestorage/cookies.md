---
title: cookies
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookiestorage/cookies
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestorage/cookies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestorage/cookies.json'
content_hash: 'sha256:4fdbd368325fb89f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStorage](../httpcookiestorage.md)

# cookies

<sub>Instance Property</sub>

The cookie storage’s cookies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var cookies: [HTTPCookie]? { get }
```

## Discussion

If you want to sort the cookie storage’s cookies, you should use the [- sortedCookiesUsingDescriptors:](<sortedcookies(using_).md>) method instead of sorting the result of this method.

## See Also

### Retrieving cookies

- [- getCookiesForTask:completionHandler:](<getcookiesfor(__completionhandler_).md>) — Fetches cookies relevant to the specified task and passes them to the completion handler.
- [- cookiesForURL:](<cookies(for_).md>) — Returns all the cookie storage’s cookies that are sent to a specified URL.
- [- sortedCookiesUsingDescriptors:](<sortedcookies(using_).md>) — Returns all of the cookie storage’s cookies, sorted according to a given set of sort descriptors.
