---
title: headerData
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/headerdata-9egfp
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/headerdata-9egfp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/headerdata-9egfp.json'
content_hash: 'sha256:e00ae6774cd86b30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# headerData

<sub>Instance Property</sub>

The header component of the JWS transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var headerData: Data { get }
```

## See Also

### Getting properties for transactions

- [jwsRepresentation](jwsrepresentation-21vgo.md) — The transaction signed by the App Store, in JWS Compact Serialization format.
- [deviceVerification](deviceverification-69lvx.md) — The device verification value to use to verify whether the transaction belongs to the device.
- [deviceVerificationNonce](deviceverificationnonce-9dfrn.md) — The UUID for computing the device verification value.
- [signedDate](signeddate-8x9bg.md) — The date that the App Store signed the JWS transaction.
- [payloadData](payloaddata-uyle.md) — The payload component of the JWS transaction.
- [signedData](signeddata-56usp.md) — The transaction data that the signature applies to.
- [signatureData](signaturedata-4pyv8.md) — The signature component of the JWS transaction.
- [signature](signature-7t1ne.md) — The signature component of the JSON web signature.
