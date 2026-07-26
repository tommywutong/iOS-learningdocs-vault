---
title: deviceVerificationNonce
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/deviceverificationnonce
source_url: 'https://developer.apple.com/documentation/storekit/transaction/deviceverificationnonce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/deviceverificationnonce.json'
content_hash: 'sha256:d9a3da8788c896c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# deviceVerificationNonce

<sub>Instance Property</sub>

The UUID for computing the device verification value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let deviceVerificationNonce: UUID
```

## Discussion

Use the lowercased nonce when computing the [deviceVerification](deviceverification.md) value.

## See Also

### Verifying transactions

- [deviceVerification](deviceverification.md) — The device verification value you use to verify whether the transaction belongs to the device.
- [signedDate](signeddate.md) — The date that the App Store signed the JWS transaction.
