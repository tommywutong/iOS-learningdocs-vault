---
title: 'sortedCookies(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookiestorage/sortedcookies(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestorage/sortedcookies(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestorage/sortedcookies%28using%3A%29.json'
content_hash: 'sha256:03056ddf7b2f93d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStorage](../httpcookiestorage.md)

# sortedCookies(using:)

<sub>Instance Method</sub>

Returns all of the cookie storage’s cookies, sorted according to a given set of sort descriptors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sortedCookies(using sortOrder: [NSSortDescriptor]) -> [HTTPCookie]
```

## Parameters

- `sortOrder` — The sort descriptors to use for sorting, as an array of [NSSortDescriptor](../nssortdescriptor.md) objects.

## Return Value

The cookie storage’s cookies, sorted according to `sortOrder`, as an array of [HTTPCookie](../httpcookie.md) objects.

## See Also

### Retrieving cookies

- [cookies](cookies.md) — The cookie storage’s cookies.
- [- getCookiesForTask:completionHandler:](<getcookiesfor(__completionhandler_).md>) — Fetches cookies relevant to the specified task and passes them to the completion handler.
- [- cookiesForURL:](<cookies(for_).md>) — Returns all the cookie storage’s cookies that are sent to a specified URL.
