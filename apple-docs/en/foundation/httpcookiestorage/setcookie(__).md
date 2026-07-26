---
title: 'setCookie(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookiestorage/setcookie(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestorage/setcookie(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestorage/setcookie%28_%3A%29.json'
content_hash: 'sha256:378619d58fdfb085'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStorage](../httpcookiestorage.md)

# setCookie(_:)

<sub>Instance Method</sub>

Stores a specified cookie in the cookie storage if the cookie accept policy permits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setCookie(_ cookie: HTTPCookie)
```

## Parameters

- `cookie` — The cookie to store.

## Discussion

The cookie replaces an existing cookie with the same name, domain, and path, if one exists in the cookie storage. This method accepts the cookie only if the storage’s cookie accept policy is [NSHTTPCookieAcceptPolicyAlways](../httpcookie/acceptpolicy/always.md) or [NSHTTPCookieAcceptPolicyOnlyFromMainDocumentDomain](../httpcookie/acceptpolicy/onlyfrommaindocumentdomain.md). The cookie is ignored if the storage’s cookie accept policy is [NSHTTPCookieAcceptPolicyNever](../httpcookie/acceptpolicy/never.md).

## See Also

### Adding and removing cookies

- [- removeCookiesSinceDate:](<removecookies(since_).md>) — Removes cookies that were stored after a given date.
- [- deleteCookie:](<deletecookie(__).md>) — Deletes the specified cookie from the cookie storage.
- [- setCookies:forURL:mainDocumentURL:](<setcookies(__for_maindocumenturl_).md>) — Adds an array of cookies to the cookie storage if the storage’s cookie acceptance policy permits.
- [- storeCookies:forTask:](<storecookies(__for_).md>) — Stores an array of cookies in the cookie storage, on behalf of the provided task, if the cookie accept policy permits.
