---
title: signatureData
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/signaturedata-4pyv8
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/signaturedata-4pyv8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/signaturedata-4pyv8.json'
content_hash: 'sha256:57917860fee6216c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# signatureData

<sub>Instance Property</sub>

The signature component of the JWS transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var signatureData: Data { get }
```

## See Also

### Getting properties for transactions

- [jwsRepresentation](jwsrepresentation-21vgo.md) — The transaction signed by the App Store, in JWS Compact Serialization format.
- [deviceVerification](deviceverification-69lvx.md) — The device verification value to use to verify whether the transaction belongs to the device.
- [deviceVerificationNonce](deviceverificationnonce-9dfrn.md) — The UUID for computing the device verification value.
- [signedDate](signeddate-8x9bg.md) — The date that the App Store signed the JWS transaction.
- [headerData](headerdata-9egfp.md) — The header component of the JWS transaction.
- [payloadData](payloaddata-uyle.md) — The payload component of the JWS transaction.
- [signedData](signeddata-56usp.md) — The transaction data that the signature applies to.
- [signature](signature-7t1ne.md) — The signature component of the JSON web signature.
