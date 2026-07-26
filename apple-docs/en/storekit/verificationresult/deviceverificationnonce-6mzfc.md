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
doc_path: /documentation/storekit/verificationresult/deviceverificationnonce-6mzfc
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/deviceverificationnonce-6mzfc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/deviceverificationnonce-6mzfc.json'
content_hash: 'sha256:5ba6a0d48608d03b'
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

Use the lowercased nonce when computing the [deviceVerification](deviceverification-5hvi9.md) value.

This value is identical to the [deviceVerificationNonce](../product/subscriptioninfo/renewalinfo/deviceverificationnonce.md) value in [RenewalInfo](../product/subscriptioninfo/renewalinfo.md).

## See Also

### Getting properties for subscription renewal information

- [jwsRepresentation](jwsrepresentation-178oj.md) — The subscription renewal information signed by the App Store, in JWS Compact Serialization format.
- [deviceVerification](deviceverification-5hvi9.md) — The device verification value to use to verify whether the subscription renewal information belongs to the device.
- [signedDate](signeddate-3tvo5.md) — The date that the App Store signed the JWS subscription renewal information.
- [headerData](headerdata-3be0o.md) — The header component of the JWS subscription renewal information.
- [payloadData](payloaddata-abfv.md) — The payload component of the JWS subscription renewal information.
- [signedData](signeddata-1t80n.md) — The subscription renewal information data that the signature applies to.
- [signatureData](signaturedata-9uw8c.md) — The signature component of the JWS subscription renewal information.
- [signature](signature-95r7x.md) — The signature component of the JSON web signature.
