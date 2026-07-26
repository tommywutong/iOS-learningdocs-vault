---
title: 'setCookies(_:for:mainDocumentURL:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookiestorage/setcookies(_:for:maindocumenturl:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestorage/setcookies(_:for:maindocumenturl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestorage/setcookies%28_%3Afor%3Amaindocumenturl%3A%29.json'
content_hash: 'sha256:bdaf9398871122cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStorage](../httpcookiestorage.md)

# setCookies(_:for:mainDocumentURL:)

<sub>Instance Method</sub>

Adds an array of cookies to the cookie storage if the storage’s cookie acceptance policy permits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setCookies(_ cookies: [HTTPCookie], for URL: URL?, mainDocumentURL: URL?)
```

## Parameters

- `cookies` — The cookies to add.

- `URL` — The URL associated with the added cookies.

- `mainDocumentURL` — The URL of the main HTML document for the top-level frame, if known. The value can be `nil`. This URL is used to determine whether the cookie should be accepted if the cookie accept policy is [NSHTTPCookieAcceptPolicyOnlyFromMainDocumentDomain](../httpcookie/acceptpolicy/onlyfrommaindocumentdomain.md).

## Discussion

Cookies in the array will replace existing cookies with the same name, domain, and path in the cookie storage. If the storage has an accept policy of [NSHTTPCookieAcceptPolicyNever](../httpcookie/acceptpolicy/never.md), the cookies are ignored.

To store cookies from a set of response headers, an application can use [+ cookiesWithResponseHeaderFields:forURL:](<../httpcookie/cookies(withresponseheaderfields_for_).md>) passing a header field dictionary and then use this method to store the resulting cookies in accordance with the cookie storage’s cookie acceptance policy.

If you override this method, also override [- storeCookies:forTask:](<storecookies(__for_).md>).

## See Also

### Adding and removing cookies

- [- removeCookiesSinceDate:](<removecookies(since_).md>) — Removes cookies that were stored after a given date.
- [- deleteCookie:](<deletecookie(__).md>) — Deletes the specified cookie from the cookie storage.
- [- setCookie:](<setcookie(__).md>) — Stores a specified cookie in the cookie storage if the cookie accept policy permits.
- [- storeCookies:forTask:](<storecookies(__for_).md>) — Stores an array of cookies in the cookie storage, on behalf of the provided task, if the cookie accept policy permits.
