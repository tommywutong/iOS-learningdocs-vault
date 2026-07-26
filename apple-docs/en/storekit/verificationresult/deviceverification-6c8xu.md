---
title: deviceVerification
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/deviceverification-6c8xu
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/deviceverification-6c8xu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/deviceverification-6c8xu.json'
content_hash: 'sha256:bfe0fa0fe707a6d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# deviceVerification

<sub>Instance Property</sub>

The device verification value to use to verify whether the app transaction belongs to the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var deviceVerification: Data { get }
```

## Discussion

For more information about using the device verification value, see [deviceVerification](../transaction/deviceverification.md).

This value is identical to the [deviceVerification](../apptransaction/deviceverification.md) value in [AppTransaction](../apptransaction.md).

## See Also

### Getting properties for app transactions

- [jwsRepresentation](jwsrepresentation-6ma59.md) — The app transaction signed by the App Store, in JWS Compact Serialization format.
- [deviceVerificationNonce](deviceverificationnonce-6082b.md) — The UUID for computing the device verification value.
- [signedDate](signeddate-24zch.md) — The date that the App Store signed the JWS app transaction.
- [headerData](headerdata-3drrl.md) — The header component of the JWS app transaction.
- [payloadData](payloaddata-97acz.md) — The payload component of the JWS app transaction.
- [signedData](signeddata-99fyo.md) — The app transaction data that the signature applies to.
- [signatureData](signaturedata-4pvv0.md) — The signature component of the JWS app transaction.
- [signature](signature-6d5ue.md) — The signature component of the JSON web signature.
