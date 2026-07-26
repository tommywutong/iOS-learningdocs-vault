---
title: deviceVerificationNonce
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/deviceverificationnonce
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/deviceverificationnonce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/deviceverificationnonce.json'
content_hash: 'sha256:eeba74f7112fa53f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# deviceVerificationNonce

<sub>Instance Property</sub>

The UUID used to compute the device verification value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let deviceVerificationNonce: UUID
```

## Discussion

For more information, see [deviceVerificationID](../appstore/deviceverificationid.md).

## See Also

### Verifying the app transaction

- [deviceVerification](deviceverification.md) — The device verification value to use to verify whether the app transaction belongs to the device.
- [signedDate](signeddate.md) — The date that the App Store signed the JWS app transaction.
