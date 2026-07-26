---
title: 'VerificationResult.verified(_:)'
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/verificationresult/verified(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/verified(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/verified%28_%3A%29.json'
content_hash: 'sha256:09e6669fb0225dae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# VerificationResult.verified(_:)

<sub>Case</sub>

The associated value passed StoreKit automatic verification checks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case verified(SignedType)
```

## Discussion

The associated value in this case is the App Store-signed value.

## See Also

### Getting the verification results

- [VerificationResult.unverified(_:_:)](<unverified(____).md>) — The associated value failed StoreKit automatic verification checks.
- [payloadValue](payloadvalue.md) — The verified value of the signed type that StoreKit confirms as verified.
- [unsafePayloadValue](unsafepayloadvalue.md) — The associated value of the verification result that StoreKit doesn’t confirm as verified.
- [VerificationError](verificationerror.md) — Error cases for StoreKit JWS verification.
