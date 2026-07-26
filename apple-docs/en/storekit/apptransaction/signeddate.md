---
title: signedDate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/signeddate
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/signeddate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/signeddate.json'
content_hash: 'sha256:3ed31ea7b95bfc13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# signedDate

<sub>Instance Property</sub>

The date that the App Store signed the JWS app transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let signedDate: Date
```

## Discussion

Use the [signedDate](signeddate.md) to verify whether the certificate used to sign the app transaction was valid when the App Store signed the transaction.

## See Also

### Verifying the app transaction

- [deviceVerification](deviceverification.md) — The device verification value to use to verify whether the app transaction belongs to the device.
- [deviceVerificationNonce](deviceverificationnonce.md) — The UUID used to compute the device verification value.
