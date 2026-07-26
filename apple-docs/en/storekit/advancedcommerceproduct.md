---
title: AdvancedCommerceProduct
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/advancedcommerceproduct
source_url: 'https://developer.apple.com/documentation/storekit/advancedcommerceproduct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/advancedcommerceproduct.json'
content_hash: 'sha256:9f233622acb64c9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# AdvancedCommerceProduct

<sub>Structure</sub>

A product configured as a generic SKU in App Store Connect for use with the Advanced Commerce API.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AdvancedCommerceProduct
```

## Overview

For more information about [Advanced Commerce API](../advancedcommerceapi.md), see [Advanced Commerce API](https://developer.apple.com/in-app-purchase/advanced-commerce-api/).

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the product ID and type

- [id](advancedcommerceproduct/id.md) — The generic product ID.
- [ProductType](advancedcommerceproduct/producttype.md)
- [type](advancedcommerceproduct/type.md) — The type of the product.

### Initiating purchases

- [PurchaseOption](advancedcommerceproduct/purchaseoption.md)
- [purchase(compactJWS:confirmIn:options:)](<advancedcommerceproduct/purchase(compactjws_confirmin_options_)-7x4bh.md>) — Processes a purchase for the product.
- [purchase(compactJWS:confirmIn:options:)](<advancedcommerceproduct/purchase(compactjws_confirmin_options_)-54lkw.md>) — Processes a purchase for the product.
- [purchase(compactJWS:options:)](<advancedcommerceproduct/purchase(compactjws_options_).md>) — Processes a purchase for the product.
- [PurchaseResult](advancedcommerceproduct/purchaseresult.md)

### Getting transactions and entitlements

- [allTransactions](advancedcommerceproduct/alltransactions.md) — All transactions associated with the generic product ID.
- [currentEntitlements](advancedcommerceproduct/currententitlements.md) — The transactions that entitle the customer to Advanced Commerce Items purchased using the generic product ID.
- [latestTransaction](advancedcommerceproduct/latesttransaction.md) — The most recent transaction associated with the generic product ID, if it exists.

### Initializing an instance

- [init(id:)](<advancedcommerceproduct/init(id_).md>) — Creates an Advanced Commerce product.

### Handling errors

- [InvalidRequestError](invalidrequesterror.md)

## See Also

### Advanced Commerce API interactions

- [Sending Advanced Commerce API requests from your app](sending-advanced-commerce-api-requests-from-your-app.md) — Send Advanced Commerce API requests from your app that you authorize with a JSON Web Signature (JWS) you generate on your server.
- [Generating JWS to sign App Store requests](generating-jws-to-sign-app-store-requests.md) — Create signed JSON Web Signature (JWS) strings on your server to authorize your API requests in your app.
