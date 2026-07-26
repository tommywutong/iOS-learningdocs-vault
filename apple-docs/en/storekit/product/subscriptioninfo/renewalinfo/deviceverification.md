---
title: deviceVerification
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/deviceverification
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/deviceverification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/deviceverification.json'
content_hash: 'sha256:c986c19c2cf8ce2d'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# deviceVerification

<sub>Instance Property</sub>

The device verification value to use to verify whether the renewal information belongs to the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let deviceVerification: Data
```

## Discussion

For more information, see [deviceVerificationID](../../../appstore/deviceverificationid.md).

## See Also

### Verifying subscription renewal information

- [deviceVerificationNonce](deviceverificationnonce.md) — The UUID to use to compute the device verification value.
- [signedDate](signeddate.md) — The date that the App Store signed the JWS renewal information.
