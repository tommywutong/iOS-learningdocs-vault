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
doc_path: /documentation/storekit/verificationresult/signeddate-3tvo5
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/signeddate-3tvo5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/signeddate-3tvo5.json'
content_hash: 'sha256:dd86ff1470a7f549'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# signedDate

<sub>Instance Property</sub>

The date that the App Store signed the JWS subscription renewal information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var signedDate: Date { get }
```

## Discussion

Use the [signedDate](signeddate-8x9bg.md) to verify whether the certificate used to sign the transaction was valid when the App Store signed the transaction.

## See Also

### Getting properties for subscription renewal information

- [jwsRepresentation](jwsrepresentation-178oj.md) — The subscription renewal information signed by the App Store, in JWS Compact Serialization format.
- [deviceVerification](deviceverification-5hvi9.md) — The device verification value to use to verify whether the subscription renewal information belongs to the device.
- [deviceVerificationNonce](deviceverificationnonce-6mzfc.md) — The UUID for computing the device verification value.
- [headerData](headerdata-3be0o.md) — The header component of the JWS subscription renewal information.
- [payloadData](payloaddata-abfv.md) — The payload component of the JWS subscription renewal information.
- [signedData](signeddata-1t80n.md) — The subscription renewal information data that the signature applies to.
- [signatureData](signaturedata-9uw8c.md) — The signature component of the JWS subscription renewal information.
- [signature](signature-95r7x.md) — The signature component of the JSON web signature.
