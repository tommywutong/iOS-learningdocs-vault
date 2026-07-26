---
title: payloadValue
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/payloadvalue
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/payloadvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/payloadvalue.json'
content_hash: 'sha256:5ed7e52f3a069889'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# payloadValue

<sub>Instance Property</sub>

The verified value of the signed type that StoreKit confirms as verified.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var payloadValue: SignedType { get throws }
```

## Discussion

This property represents the value of a payload in a JSON Web Signature (JWS) value that passed StoreKit verification.

This property throws an error if the JWS value containing the payload doesn’t pass StoreKit’s verification and is therefore _unverified_. To access the payload of an unverified JWS value, get the associated value of the verification result, or use the [unsafePayloadValue](unsafepayloadvalue.md) property.

## See Also

### Getting the verification results

- [VerificationResult.verified(_:)](<verified(__).md>) — The associated value passed StoreKit automatic verification checks.
- [VerificationResult.unverified(_:_:)](<unverified(____).md>) — The associated value failed StoreKit automatic verification checks.
- [unsafePayloadValue](unsafepayloadvalue.md) — The associated value of the verification result that StoreKit doesn’t confirm as verified.
- [VerificationError](verificationerror.md) — Error cases for StoreKit JWS verification.
