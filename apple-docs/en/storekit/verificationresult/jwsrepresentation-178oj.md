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
doc_path: /documentation/storekit/verificationresult/jwsrepresentation-178oj
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/jwsrepresentation-178oj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/jwsrepresentation-178oj.json'
content_hash: 'sha256:2ba22f52649f03c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# jwsRepresentation

<sub>Instance Property</sub>

The subscription renewal information signed by the App Store, in JWS Compact Serialization format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var jwsRepresentation: String { get }
```

## Discussion

Use this JSON Web Signature (JWS) value to perform your own JWS verification on your server or on the device.

The [jwsRepresentation](jwsrepresentation-21vgo.md) is the same as the [JWSRenewalInfo](../../appstoreserverapi/jwsrenewalinfo.md) that the App Store Server API returns, and the [JWSRenewalInfo](../../appstoreservernotifications/jwsrenewalinfo.md) that you receive from App Store Server Notifications. The [jwsRepresentation](jwsrepresentation-21vgo.md)’s decoded payload contains two additional fields: `deviceVerification` and `deviceVerificationNonce`. Use these fields on the device to verify that the JWS information belongs to the device. For more information, see [deviceVerificationID](../appstore/deviceverificationid.md).

To verify the [jwsRepresentation](jwsrepresentation-178oj.md) on your server, consider using the App Store Server Library function `verifyAndDecodeRenewalInfo`, available in each language the library supports. For more information, see [Simplifying your implementation by using the App Store Server Library](../../appstoreserverapi/simplifying-your-implementation-by-using-the-app-store-server-library.md).

> [!important] Important
> The decoded payloads of the [jwsRepresentation](jwsrepresentation-21vgo.md) and [JWSRenewalInfo](../../appstoreserverapi/jwsrenewalinfo.md) strings contain [renewalPrice](../../appstoreserverapi/renewalprice.md) fields that are specified in _milliunits_ of the currency; StoreKit represents the [renewalPrice](../product/subscriptioninfo/renewalinfo/renewalprice.md) in _units_ of currency. Take care not to confuse these two representations when working with both APIs.

## See Also

### Getting properties for subscription renewal information

- [deviceVerification](deviceverification-5hvi9.md) — The device verification value to use to verify whether the subscription renewal information belongs to the device.
- [deviceVerificationNonce](deviceverificationnonce-6mzfc.md) — The UUID for computing the device verification value.
- [signedDate](signeddate-3tvo5.md) — The date that the App Store signed the JWS subscription renewal information.
- [headerData](headerdata-3be0o.md) — The header component of the JWS subscription renewal information.
- [payloadData](payloaddata-abfv.md) — The payload component of the JWS subscription renewal information.
- [signedData](signeddata-1t80n.md) — The subscription renewal information data that the signature applies to.
- [signatureData](signaturedata-9uw8c.md) — The signature component of the JWS subscription renewal information.
- [signature](signature-95r7x.md) — The signature component of the JSON web signature.
