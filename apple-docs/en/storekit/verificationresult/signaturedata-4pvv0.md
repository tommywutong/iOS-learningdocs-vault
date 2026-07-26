---
title: signatureData
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/signaturedata-4pvv0
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/signaturedata-4pvv0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/signaturedata-4pvv0.json'
content_hash: 'sha256:7f012b45cccc917f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# signatureData

<sub>Instance Property</sub>

The signature component of the JWS app transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var signatureData: Data { get }
```

## See Also

### Getting properties for app transactions

- [jwsRepresentation](jwsrepresentation-6ma59.md) — The app transaction signed by the App Store, in JWS Compact Serialization format.
- [deviceVerification](deviceverification-6c8xu.md) — The device verification value to use to verify whether the app transaction belongs to the device.
- [deviceVerificationNonce](deviceverificationnonce-6082b.md) — The UUID for computing the device verification value.
- [signedDate](signeddate-24zch.md) — The date that the App Store signed the JWS app transaction.
- [headerData](headerdata-3drrl.md) — The header component of the JWS app transaction.
- [payloadData](payloaddata-97acz.md) — The payload component of the JWS app transaction.
- [signedData](signeddata-99fyo.md) — The app transaction data that the signature applies to.
- [signature](signature-6d5ue.md) — The signature component of the JSON web signature.
