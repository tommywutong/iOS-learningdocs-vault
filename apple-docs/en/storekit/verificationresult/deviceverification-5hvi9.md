---
title: deviceVerification
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/deviceverification-5hvi9
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/deviceverification-5hvi9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/deviceverification-5hvi9.json'
content_hash: 'sha256:c07181250007cd5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# deviceVerification

<sub>Instance Property</sub>

The device verification value to use to verify whether the subscription renewal information belongs to the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var deviceVerification: Data { get }
```

## Discussion

For more information about using the device verification value, see [deviceVerification](../transaction/deviceverification.md).

This value is identical to the [deviceVerification](../product/subscriptioninfo/renewalinfo/deviceverification.md) value in [RenewalInfo](../product/subscriptioninfo/renewalinfo.md).

## See Also

### Getting properties for subscription renewal information

- [jwsRepresentation](jwsrepresentation-178oj.md) — The subscription renewal information signed by the App Store, in JWS Compact Serialization format.
- [deviceVerificationNonce](deviceverificationnonce-6mzfc.md) — The UUID for computing the device verification value.
- [signedDate](signeddate-3tvo5.md) — The date that the App Store signed the JWS subscription renewal information.
- [headerData](headerdata-3be0o.md) — The header component of the JWS subscription renewal information.
- [payloadData](payloaddata-abfv.md) — The payload component of the JWS subscription renewal information.
- [signedData](signeddata-1t80n.md) — The subscription renewal information data that the signature applies to.
- [signatureData](signaturedata-9uw8c.md) — The signature component of the JWS subscription renewal information.
- [signature](signature-95r7x.md) — The signature component of the JSON web signature.
