---
title: completeUntilFirstUserAuthentication
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlfileprotection/completeuntilfirstuserauthentication
source_url: 'https://developer.apple.com/documentation/foundation/urlfileprotection/completeuntilfirstuserauthentication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlfileprotection/completeuntilfirstuserauthentication.json'
content_hash: 'sha256:fddea219f63bfcd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLFileProtection](../urlfileprotection.md)

# completeUntilFirstUserAuthentication

<sub>Type Property</sub>

An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access until after the device boots.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let completeUntilFirstUserAuthentication: URLFileProtection
```

## Discussion

After the user unlocks the device for the first time, your app can access the file and continue to access it even if the user subsequently locks the device.

## See Also

### Protection levels

- [NSURLFileProtectionComplete](complete.md) — An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access for reading or writing to while the device is locked or booting.
- [NSURLFileProtectionCompleteUnlessOpen](completeunlessopen.md) — An option that instructs the system to store the file in an encrypted format on-disk after it closes.
- [NSURLFileProtectionCompleteWhenUserInactive](completewhenuserinactive.md) — An option that instructs the system to store the file in an encrypted format on-disk that your app can access only after device unlock and before expiration.
- [NSURLFileProtectionNone](none.md) — An option that indicates the file has no special protections associated with it.
