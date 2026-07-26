---
title: 'getCookiesFor(_:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookiestorage/getcookiesfor(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestorage/getcookiesfor(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestorage/getcookiesfor%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:52a977cb1ccf47aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStorage](../httpcookiestorage.md)

# getCookiesFor(_:completionHandler:)

<sub>Instance Method</sub>

Fetches cookies relevant to the specified task and passes them to the completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getCookiesFor(_ task: URLSessionTask, completionHandler: @escaping @Sendable ([HTTPCookie]?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cookies(for task: URLSessionTask) async -> [HTTPCookie]?
```

## Parameters

- `task` — The task performing a request. The cookie storage can use the URL and other properties of this task’s request to determine which cookies to fetch.

- `completionHandler` — A completion handler that receives an array of cookies as its argument.

## See Also

### Retrieving cookies

- [cookies](cookies.md) — The cookie storage’s cookies.
- [- cookiesForURL:](<cookies(for_).md>) — Returns all the cookie storage’s cookies that are sent to a specified URL.
- [- sortedCookiesUsingDescriptors:](<sortedcookies(using_).md>) — Returns all of the cookie storage’s cookies, sorted according to a given set of sort descriptors.
