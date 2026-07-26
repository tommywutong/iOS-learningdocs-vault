---
title: jwsRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/jwsrepresentation-21vgo
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/jwsrepresentation-21vgo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/jwsrepresentation-21vgo.json'
content_hash: 'sha256:4b863127c61630e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# jwsRepresentation

<sub>Instance Property</sub>

The transaction signed by the App Store, in JWS Compact Serialization format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var jwsRepresentation: String { get }
```

## Discussion

Use this JSON Web Signature (JWS) value to perform your own JWS verification on your server or on the device.

The [jwsRepresentation](jwsrepresentation-21vgo.md) is the same as the [JWSTransaction](../../appstoreserverapi/jwstransaction.md) that the App Store Server API returns and the [JWSTransaction](../../appstoreservernotifications/jwstransaction.md) that you receive from App Store Server Notifications. The [jwsRepresentation](jwsrepresentation-21vgo.md)’s decoded payload contains two additional fields: `deviceVerification` and `deviceVerificationNonce`. Use these fields on the device to verify that the JWS information belongs to the device. For more information, see [deviceVerificationID](../appstore/deviceverificationid.md).

To verify the [jwsRepresentation](jwsrepresentation-21vgo.md) on your server, consider using the App Store Server Library function `verifyAndDecodeTransaction`, available in each language the library supports. For more information, see [Simplifying your implementation by using the App Store Server Library](../../appstoreserverapi/simplifying-your-implementation-by-using-the-app-store-server-library.md).

> [!important] Important
> The decoded payloads of the [jwsRepresentation](jwsrepresentation-21vgo.md) and [JWSTransaction](../../appstoreserverapi/jwstransaction.md) strings contain [price](../../appstoreserverapi/price.md) fields that are specified in _milliunits_ of the currency;  StoreKit represents the `price`  in _units_ of currency. Take care not to confuse these two representations when working with both APIs.

## See Also

### Getting properties for transactions

- [deviceVerification](deviceverification-69lvx.md) — The device verification value to use to verify whether the transaction belongs to the device.
- [deviceVerificationNonce](deviceverificationnonce-9dfrn.md) — The UUID for computing the device verification value.
- [signedDate](signeddate-8x9bg.md) — The date that the App Store signed the JWS transaction.
- [headerData](headerdata-9egfp.md) — The header component of the JWS transaction.
- [payloadData](payloaddata-uyle.md) — The payload component of the JWS transaction.
- [signedData](signeddata-56usp.md) — The transaction data that the signature applies to.
- [signatureData](signaturedata-4pyv8.md) — The signature component of the JWS transaction.
- [signature](signature-7t1ne.md) — The signature component of the JSON web signature.
