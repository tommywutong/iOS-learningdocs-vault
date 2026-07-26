---
title: signedDate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/signeddate
source_url: 'https://developer.apple.com/documentation/storekit/transaction/signeddate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/signeddate.json'
content_hash: 'sha256:209aa5e08157b4f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# signedDate

<sub>Instance Property</sub>

The date that the App Store signed the JWS transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let signedDate: Date
```

## Discussion

Use the [signedDate](signeddate.md) to verify whether the certificate used to sign the transaction was valid when the App Store signed the transaction.

## See Also

### Verifying transactions

- [deviceVerification](deviceverification.md) — The device verification value you use to verify whether the transaction belongs to the device.
- [deviceVerificationNonce](deviceverificationnonce.md) — The UUID for computing the device verification value.
