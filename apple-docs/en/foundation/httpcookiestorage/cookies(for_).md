---
title: 'cookies(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookiestorage/cookies(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestorage/cookies(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestorage/cookies%28for%3A%29.json'
content_hash: 'sha256:9d3b68a54f6e0c55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStorage](../httpcookiestorage.md)

# cookies(for:)

<sub>Instance Method</sub>

Returns all the cookie storage’s cookies that are sent to a specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cookies(for URL: URL) -> [HTTPCookie]?
```

## Parameters

- `URL` — The URL to filter on.

## Return Value

An array of cookies whose URL matches the provided URL.

## Discussion

You can use the [+ requestHeaderFieldsWithCookies:](<../httpcookie/requestheaderfields(with_).md>) method of [HTTPCookie](../httpcookie.md) to turn the array returned by this method into a set of header fields to add to a [URLRequest](../urlrequest.md) object (or [NSMutableURLRequest](../nsmutableurlrequest.md) in Objective-C).

If you override this method, also override [- getCookiesForTask:completionHandler:](<getcookiesfor(__completionhandler_).md>).

## See Also

### Retrieving cookies

- [cookies](cookies.md) — The cookie storage’s cookies.
- [- getCookiesForTask:completionHandler:](<getcookiesfor(__completionhandler_).md>) — Fetches cookies relevant to the specified task and passes them to the completion handler.
- [- sortedCookiesUsingDescriptors:](<sortedcookies(using_).md>) — Returns all of the cookie storage’s cookies, sorted according to a given set of sort descriptors.
