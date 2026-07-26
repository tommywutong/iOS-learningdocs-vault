---
title: deviceVerification
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/deviceverification
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/deviceverification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/deviceverification.json'
content_hash: 'sha256:4bd63cbc36f9a2d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# deviceVerification

<sub>Instance Property</sub>

The device verification value to use to verify whether the app transaction belongs to the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let deviceVerification: Data
```

## Discussion

For more information, see [deviceVerificationID](../appstore/deviceverificationid.md).

## See Also

### Verifying the app transaction

- [deviceVerificationNonce](deviceverificationnonce.md) — The UUID used to compute the device verification value.
- [signedDate](signeddate.md) — The date that the App Store signed the JWS app transaction.
