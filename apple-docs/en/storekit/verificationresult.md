---
title: VerificationResult
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult.json'
content_hash: 'sha256:6c96afcbbead38ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# VerificationResult

<sub>Enumeration</sub>

A type that describes the result of a StoreKit verification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum VerificationResult<SignedType>
```

## Overview

StoreKit automatically verifies the [Transaction](transaction.md), [RenewalInfo](product/subscriptioninfo/renewalinfo.md), and [AppTransaction](apptransaction.md) values. To access the wrapped values, check whether the values are verified or unverified.

In addition to getting a verification result from StoreKit, you might want to verify the signed information yourself, either on the device, or on your server for the most control and security. Perform the verification on the [jwsRepresentation](verificationresult/jwsrepresentation-178oj.md) property for subscription renewal information, the [jwsRepresentation](verificationresult/jwsrepresentation-21vgo.md) property for transactions, and the [jwsRepresentation](verificationresult/jwsrepresentation-6ma59.md) property for an app transaction.

To verify the [jwsRepresentation](verificationresult/jwsrepresentation-21vgo.md) on your server, consider using the verification functions in the App Store Server Library. The library provides the functions `verifyAndDecodeTransaction`, `verifyAndDecodeAppTransaction`, and `verifyAndDecodeRenewalInfo` in each language the library supports. For more information, see [Simplifying your implementation by using the App Store Server Library](../appstoreserverapi/simplifying-your-implementation-by-using-the-app-store-server-library.md).

The [jwsRepresentation](verificationresult/jwsrepresentation-21vgo.md) string is in JWS Compact Serialization format and is the same as its counterpart in the App Store server APIs, as follows:

| StoreKit string | Equivalent in the App Store Server API | Equivalent in App Store Server Notifications |
|---|---|---|
| [jwsRepresentation](verificationresult/jwsrepresentation-178oj.md) for subscription renewal information | [JWSRenewalInfo](../appstoreserverapi/jwsrenewalinfo.md) | [JWSRenewalInfo](../appstoreservernotifications/jwsrenewalinfo.md) |
| [jwsRepresentation](verificationresult/jwsrepresentation-21vgo.md) for transactions | [JWSTransaction](../appstoreserverapi/jwstransaction.md) | [JWSTransaction](../appstoreservernotifications/jwstransaction.md) |

The decoded payload of the [jwsRepresentation](verificationresult/jwsrepresentation-21vgo.md) contains  two additional fields: `deviceVerification` and `deviceVerificationNonce`. Use these fields on the device to verify that JWS information belongs to the device. For more information, see [deviceVerificationID](appstore/deviceverificationid.md).

> [!important] Important
> The decoded payloads of [jwsRepresentation](verificationresult/jwsrepresentation-21vgo.md) and [JWSTransaction](../appstoreserverapi/jwstransaction.md) strings contain [price](../appstoreserverapi/price.md) or [renewalPrice](../appstoreserverapi/renewalprice.md) fields specified in _milliunits_ of the currency.  StoreKit represents the `price` and [renewalPrice](product/subscriptioninfo/renewalinfo/renewalprice.md) values in is _units_ of the currency. Take care not to confuse these two representations when working with both APIs.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the verification results

- [VerificationResult.verified(_:)](<verificationresult/verified(__).md>) — The associated value passed StoreKit automatic verification checks.
- [VerificationResult.unverified(_:_:)](<verificationresult/unverified(____).md>) — The associated value failed StoreKit automatic verification checks.
- [payloadValue](verificationresult/payloadvalue.md) — The verified value of the signed type that StoreKit confirms as verified.
- [unsafePayloadValue](verificationresult/unsafepayloadvalue.md) — The associated value of the verification result that StoreKit doesn’t confirm as verified.
- [VerificationError](verificationresult/verificationerror.md) — Error cases for StoreKit JWS verification.

### Getting properties for transactions

- [jwsRepresentation](verificationresult/jwsrepresentation-21vgo.md) — The transaction signed by the App Store, in JWS Compact Serialization format.
- [deviceVerification](verificationresult/deviceverification-69lvx.md) — The device verification value to use to verify whether the transaction belongs to the device.
- [deviceVerificationNonce](verificationresult/deviceverificationnonce-9dfrn.md) — The UUID for computing the device verification value.
- [signedDate](verificationresult/signeddate-8x9bg.md) — The date that the App Store signed the JWS transaction.
- [headerData](verificationresult/headerdata-9egfp.md) — The header component of the JWS transaction.
- [payloadData](verificationresult/payloaddata-uyle.md) — The payload component of the JWS transaction.
- [signedData](verificationresult/signeddata-56usp.md) — The transaction data that the signature applies to.
- [signatureData](verificationresult/signaturedata-4pyv8.md) — The signature component of the JWS transaction.
- [signature](verificationresult/signature-7t1ne.md) — The signature component of the JSON web signature.

### Getting properties for subscription renewal information

- [jwsRepresentation](verificationresult/jwsrepresentation-178oj.md) — The subscription renewal information signed by the App Store, in JWS Compact Serialization format.
- [deviceVerification](verificationresult/deviceverification-5hvi9.md) — The device verification value to use to verify whether the subscription renewal information belongs to the device.
- [deviceVerificationNonce](verificationresult/deviceverificationnonce-6mzfc.md) — The UUID for computing the device verification value.
- [signedDate](verificationresult/signeddate-3tvo5.md) — The date that the App Store signed the JWS subscription renewal information.
- [headerData](verificationresult/headerdata-3be0o.md) — The header component of the JWS subscription renewal information.
- [payloadData](verificationresult/payloaddata-abfv.md) — The payload component of the JWS subscription renewal information.
- [signedData](verificationresult/signeddata-1t80n.md) — The subscription renewal information data that the signature applies to.
- [signatureData](verificationresult/signaturedata-9uw8c.md) — The signature component of the JWS subscription renewal information.
- [signature](verificationresult/signature-95r7x.md) — The signature component of the JSON web signature.

### Getting properties for app transactions

- [jwsRepresentation](verificationresult/jwsrepresentation-6ma59.md) — The app transaction signed by the App Store, in JWS Compact Serialization format.
- [deviceVerification](verificationresult/deviceverification-6c8xu.md) — The device verification value to use to verify whether the app transaction belongs to the device.
- [deviceVerificationNonce](verificationresult/deviceverificationnonce-6082b.md) — The UUID for computing the device verification value.
- [signedDate](verificationresult/signeddate-24zch.md) — The date that the App Store signed the JWS app transaction.
- [headerData](verificationresult/headerdata-3drrl.md) — The header component of the JWS app transaction.
- [payloadData](verificationresult/payloaddata-97acz.md) — The payload component of the JWS app transaction.
- [signedData](verificationresult/signeddata-99fyo.md) — The app transaction data that the signature applies to.
- [signatureData](verificationresult/signaturedata-4pvv0.md) — The signature component of the JWS app transaction.
- [signature](verificationresult/signature-6d5ue.md) — The signature component of the JSON web signature.

## See Also

### JWS verification

- [VerificationError](verificationresult/verificationerror.md) — Error cases for StoreKit JWS verification.
