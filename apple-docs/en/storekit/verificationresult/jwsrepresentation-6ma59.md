---
title: jwsRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/jwsrepresentation-6ma59
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/jwsrepresentation-6ma59'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/jwsrepresentation-6ma59.json'
content_hash: 'sha256:3c20698bddafa4bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# jwsRepresentation

<sub>Instance Property</sub>

The app transaction signed by the App Store, in JWS Compact Serialization format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var jwsRepresentation: String { get }
```

## Discussion

Use this JSON Web Signature (JWS) value to perform your own JWS verification on your server or on the device.

To verify the [jwsRepresentation](jwsrepresentation-6ma59.md) on your server, consider using the App Store Server Library function `verifyAndDecodeAppTransaction`, available in each language the library supports. For more information, see [Simplifying your implementation by using the App Store Server Library](../../appstoreserverapi/simplifying-your-implementation-by-using-the-app-store-server-library.md).

The [jwsRepresentation](jwsrepresentation-6ma59.md)’s decoded payload contains the fields `deviceVerification` and `deviceVerificationNonce`. Use these fields on the device to verify that the JWS information belongs to the device. For more information, see [deviceVerificationID](../appstore/deviceverificationid.md).

## See Also

### Getting properties for app transactions

- [deviceVerification](deviceverification-6c8xu.md) — The device verification value to use to verify whether the app transaction belongs to the device.
- [deviceVerificationNonce](deviceverificationnonce-6082b.md) — The UUID for computing the device verification value.
- [signedDate](signeddate-24zch.md) — The date that the App Store signed the JWS app transaction.
- [headerData](headerdata-3drrl.md) — The header component of the JWS app transaction.
- [payloadData](payloaddata-97acz.md) — The payload component of the JWS app transaction.
- [signedData](signeddata-99fyo.md) — The app transaction data that the signature applies to.
- [signatureData](signaturedata-4pvv0.md) — The signature component of the JWS app transaction.
- [signature](signature-6d5ue.md) — The signature component of the JSON web signature.
