---
title: none
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlfileprotection/none
source_url: 'https://developer.apple.com/documentation/foundation/urlfileprotection/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlfileprotection/none.json'
content_hash: 'sha256:7db516d3e427282d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLFileProtection](../urlfileprotection.md)

# none

<sub>Type Property</sub>

An option that indicates the file has no special protections associated with it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let none: URLFileProtection
```

## Discussion

A file with this type of protection can be read from or written to at any time.

## See Also

### Protection levels

- [NSURLFileProtectionComplete](complete.md) — An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access for reading or writing to while the device is locked or booting.
- [NSURLFileProtectionCompleteUnlessOpen](completeunlessopen.md) — An option that instructs the system to store the file in an encrypted format on-disk after it closes.
- [NSURLFileProtectionCompleteUntilFirstUserAuthentication](completeuntilfirstuserauthentication.md) — An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access until after the device boots.
- [NSURLFileProtectionCompleteWhenUserInactive](completewhenuserinactive.md) — An option that instructs the system to store the file in an encrypted format on-disk that your app can access only after device unlock and before expiration.
