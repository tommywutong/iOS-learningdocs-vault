---
title: 'introductoryOfferEligibility(compactJWS:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchaseoption/introductoryoffereligibility(compactjws:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/introductoryoffereligibility(compactjws:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/introductoryoffereligibility%28compactjws%3A%29.json'
content_hash: 'sha256:9a33c136c727d99e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# introductoryOfferEligibility(compactJWS:)

<sub>Type Method</sub>

Set the eligibility of an introductory offer for a purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 18.4, macOS 15.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
static func introductoryOfferEligibility(compactJWS: String) -> Product.PurchaseOption
```

## Parameters

- `compactJWS` — The signed JWT string with the introductory offer eligibility for the purchase.

## Discussion

For information about generating and signing this JWT, see [Include custom claims for introductory offer eligibility](../../generating-jws-to-sign-app-store-requests.md#Include-custom-claims-for-introductory-offer-eligibility).
