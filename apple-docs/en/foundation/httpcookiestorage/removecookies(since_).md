---
title: 'removeCookies(since:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookiestorage/removecookies(since:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestorage/removecookies(since:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestorage/removecookies%28since%3A%29.json'
content_hash: 'sha256:a0d87964a93d4fd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStorage](../httpcookiestorage.md)

# removeCookies(since:)

<sub>Instance Method</sub>

Removes cookies that were stored after a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeCookies(since date: Date)
```

## Parameters

- `date` — The date after which cookies should be removed.

## See Also

### Adding and removing cookies

- [- deleteCookie:](<deletecookie(__).md>) — Deletes the specified cookie from the cookie storage.
- [- setCookie:](<setcookie(__).md>) — Stores a specified cookie in the cookie storage if the cookie accept policy permits.
- [- setCookies:forURL:mainDocumentURL:](<setcookies(__for_maindocumenturl_).md>) — Adds an array of cookies to the cookie storage if the storage’s cookie acceptance policy permits.
- [- storeCookies:forTask:](<storecookies(__for_).md>) — Stores an array of cookies in the cookie storage, on behalf of the provided task, if the cookie accept policy permits.
