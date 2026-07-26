---
title: 'storeCookies(_:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookiestorage/storecookies(_:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestorage/storecookies(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestorage/storecookies%28_%3Afor%3A%29.json'
content_hash: 'sha256:0c97b063da926a22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStorage](../httpcookiestorage.md)

# storeCookies(_:for:)

<sub>Instance Method</sub>

Stores an array of cookies in the cookie storage, on behalf of the provided task, if the cookie accept policy permits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func storeCookies(_ cookies: [HTTPCookie], for task: URLSessionTask)
```

## Parameters

- `cookies` — The cookies to add.

- `task` — The task that handles the response. Override this method and inspect this parameter if you need to alter your cookie storage strategy based on properties of the task.

## See Also

### Adding and removing cookies

- [- removeCookiesSinceDate:](<removecookies(since_).md>) — Removes cookies that were stored after a given date.
- [- deleteCookie:](<deletecookie(__).md>) — Deletes the specified cookie from the cookie storage.
- [- setCookie:](<setcookie(__).md>) — Stores a specified cookie in the cookie storage if the cookie accept policy permits.
- [- setCookies:forURL:mainDocumentURL:](<setcookies(__for_maindocumenturl_).md>) — Adds an array of cookies to the cookie storage if the storage’s cookie acceptance policy permits.
