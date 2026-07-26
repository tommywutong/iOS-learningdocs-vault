---
title: signature
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/signature-95r7x
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/signature-95r7x'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/signature-95r7x.json'
content_hash: 'sha256:69240e97bd4ec390'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# signature

<sub>Instance Property</sub>

The signature component of the JSON web signature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var signature: P256.Signing.ECDSASignature { get }
```

## Discussion

Use this [signature](signature-95r7x.md) with [Apple CryptoKit](../../cryptokit.md) if you verify the signature on the device.

## See Also

### Getting properties for subscription renewal information

- [jwsRepresentation](jwsrepresentation-178oj.md) — The subscription renewal information signed by the App Store, in JWS Compact Serialization format.
- [deviceVerification](deviceverification-5hvi9.md) — The device verification value to use to verify whether the subscription renewal information belongs to the device.
- [deviceVerificationNonce](deviceverificationnonce-6mzfc.md) — The UUID for computing the device verification value.
- [signedDate](signeddate-3tvo5.md) — The date that the App Store signed the JWS subscription renewal information.
- [headerData](headerdata-3be0o.md) — The header component of the JWS subscription renewal information.
- [payloadData](payloaddata-abfv.md) — The payload component of the JWS subscription renewal information.
- [signedData](signeddata-1t80n.md) — The subscription renewal information data that the signature applies to.
- [signatureData](signaturedata-9uw8c.md) — The signature component of the JWS subscription renewal information.
