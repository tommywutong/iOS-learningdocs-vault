---
title: completeWhenUserInactive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlfileprotection/completewhenuserinactive
source_url: 'https://developer.apple.com/documentation/foundation/urlfileprotection/completewhenuserinactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlfileprotection/completewhenuserinactive.json'
content_hash: 'sha256:9d9b4d1eda2aea6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLFileProtection](../urlfileprotection.md)

# completeWhenUserInactive

<sub>Type Property</sub>

An option that instructs the system to store the file in an encrypted format on-disk that your app can access only after device unlock and before expiration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let completeWhenUserInactive: URLFileProtection
```

## Discussion

After the first unlock, your app can access the file and continue to access it even if the person using it subsequently locks the device. After access expires, your app can’t access the file until the person using the device unlocks it again.

## See Also

### Protection levels

- [NSURLFileProtectionComplete](complete.md) — An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access for reading or writing to while the device is locked or booting.
- [NSURLFileProtectionCompleteUnlessOpen](completeunlessopen.md) — An option that instructs the system to store the file in an encrypted format on-disk after it closes.
- [NSURLFileProtectionCompleteUntilFirstUserAuthentication](completeuntilfirstuserauthentication.md) — An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access until after the device boots.
- [NSURLFileProtectionNone](none.md) — An option that indicates the file has no special protections associated with it.
