---
title: jsonRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/jsonrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/jsonrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/jsonrepresentation.json'
content_hash: 'sha256:a63035c709709302'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# jsonRepresentation

<sub>Instance Property</sub>

The JSON representation of the subscription renewal information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var jsonRepresentation: Data { get }
```

## Discussion

The [jsonRepresentation](jsonrepresentation.md) is UTF-8 string data that has the same JSON schema as the [JWSRenewalInfoDecodedPayload](../../../../appstoreserverapi/jwsrenewalinfodecodedpayload.md) object. You can use the JSON data to decode the subscription renewal information into your own data type, or use the [RenewalInfo](../renewalinfo.md) value and its properties directly.

The JSON Web Signature (JWS) Compact Serialization for the subscription renewal information is available in the [jwsRepresentation](../../../verificationresult/jwsrepresentation-178oj.md) property of the [VerificationResult](../../../verificationresult.md). The JWS string consists of three Base64URL-encoded components, separated by a period: a header, a payload, and a signature. The [jsonRepresentation](../../../transaction/jsonrepresentation.md) is the Base64URL-decoded payload component.

> [!note] Note
> If you send the subscription renewal information to your server or store it, use the [jwsRepresentation](../../../verificationresult/jwsrepresentation-178oj.md) and validate the signature before parsing it.
