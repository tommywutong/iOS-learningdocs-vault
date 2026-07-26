---
title: unsafePayloadValue
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/unsafepayloadvalue
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/unsafepayloadvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/unsafepayloadvalue.json'
content_hash: 'sha256:2effc101fd7e56f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# unsafePayloadValue

<sub>Instance Property</sub>

The associated value of the verification result that StoreKit doesn’t confirm as verified.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unsafePayloadValue: SignedType { get }
```

## Discussion

This property represents the value of a payload in a JSON Web Signature (JWS) value that’s not confirmed to have passed StoreKit verification.

Use the [unsafePayloadValue](unsafepayloadvalue.md) for debugging purposes or other situations where the integrity of the data is unimportant. This property ignores any verification errors. To get a payload that passed verification, or to check for verification errors, use the [payloadValue](payloadvalue.md) property instead.

> [!important] Important
> Don’t trust the integrity of the values you receive from the [unsafePayloadValue](unsafepayloadvalue.md) property. This property contains data regardless of the verification result, and contains data even if StoreKit’s verification fails.

To determine if the JWS value fails verification, perform a verification on the [jwsRepresentation](jwsrepresentation-178oj.md) property for subscription renewal information, the [jwsRepresentation](jwsrepresentation-21vgo.md) property for transactions, or the [jwsRepresentation](jwsrepresentation-6ma59.md) property for app transactions.

## See Also

### Getting the verification results

- [VerificationResult.verified(_:)](<verified(__).md>) — The associated value passed StoreKit automatic verification checks.
- [VerificationResult.unverified(_:_:)](<unverified(____).md>) — The associated value failed StoreKit automatic verification checks.
- [payloadValue](payloadvalue.md) — The verified value of the signed type that StoreKit confirms as verified.
- [VerificationError](verificationerror.md) — Error cases for StoreKit JWS verification.
