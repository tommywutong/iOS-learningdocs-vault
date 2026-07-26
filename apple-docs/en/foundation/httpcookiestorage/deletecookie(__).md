---
title: 'deleteCookie(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookiestorage/deletecookie(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestorage/deletecookie(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestorage/deletecookie%28_%3A%29.json'
content_hash: 'sha256:44b7be0c5a687ef1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStorage](../httpcookiestorage.md)

# deleteCookie(_:)

<sub>Instance Method</sub>

Deletes the specified cookie from the cookie storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func deleteCookie(_ cookie: HTTPCookie)
```

## Parameters

- `cookie` — The cookie to delete.

## See Also

### Adding and removing cookies

- [- removeCookiesSinceDate:](<removecookies(since_).md>) — Removes cookies that were stored after a given date.
- [- setCookie:](<setcookie(__).md>) — Stores a specified cookie in the cookie storage if the cookie accept policy permits.
- [- setCookies:forURL:mainDocumentURL:](<setcookies(__for_maindocumenturl_).md>) — Adds an array of cookies to the cookie storage if the storage’s cookie acceptance policy permits.
- [- storeCookies:forTask:](<storecookies(__for_).md>) — Stores an array of cookies in the cookie storage, on behalf of the provided task, if the cookie accept policy permits.
