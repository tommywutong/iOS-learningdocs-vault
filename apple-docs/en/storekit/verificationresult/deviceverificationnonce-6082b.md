---
title: deviceVerificationNonce
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/deviceverificationnonce-6082b
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/deviceverificationnonce-6082b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/deviceverificationnonce-6082b.json'
content_hash: 'sha256:5731b52e370a484a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# deviceVerificationNonce

<sub>Instance Property</sub>

The UUID for computing the device verification value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var deviceVerificationNonce: UUID { get }
```

## Discussion

Use the lowercased nonce when computing the [deviceVerification](deviceverification-6c8xu.md) value.

This value is identical to the [deviceVerificationNonce](../apptransaction/deviceverificationnonce.md) value in [AppTransaction](../apptransaction.md).

## See Also

### Getting properties for app transactions

- [jwsRepresentation](jwsrepresentation-6ma59.md) — The app transaction signed by the App Store, in JWS Compact Serialization format.
- [deviceVerification](deviceverification-6c8xu.md) — The device verification value to use to verify whether the app transaction belongs to the device.
- [signedDate](signeddate-24zch.md) — The date that the App Store signed the JWS app transaction.
- [headerData](headerdata-3drrl.md) — The header component of the JWS app transaction.
- [payloadData](payloaddata-97acz.md) — The payload component of the JWS app transaction.
- [signedData](signeddata-99fyo.md) — The app transaction data that the signature applies to.
- [signatureData](signaturedata-4pvv0.md) — The signature component of the JWS app transaction.
- [signature](signature-6d5ue.md) — The signature component of the JSON web signature.
