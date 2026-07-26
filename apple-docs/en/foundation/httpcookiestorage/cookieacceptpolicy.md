---
title: cookieAcceptPolicy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookiestorage/cookieacceptpolicy
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestorage/cookieacceptpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestorage/cookieacceptpolicy.json'
content_hash: 'sha256:1095e3d6f5973699'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStorage](../httpcookiestorage.md)

# cookieAcceptPolicy

<sub>Instance Property</sub>

The cookie storage’s cookie accept policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var cookieAcceptPolicy: HTTPCookie.AcceptPolicy { get set }
```

## Discussion

The default cookie accept policy is [NSHTTPCookieAcceptPolicyAlways](../httpcookie/acceptpolicy/always.md). Changing the cookie policy affects all currently running applications using the cookie storage.

## See Also

### Getting and setting the cookie accept policy

- [AcceptPolicy](../httpcookie/acceptpolicy.md) — Cookie acceptance policies implemented by the [HTTPCookieStorage](../httpcookiestorage.md) class.
