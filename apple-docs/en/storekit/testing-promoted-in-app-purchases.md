---
title: Testing promoted In-App Purchases
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/testing-promoted-in-app-purchases
source_url: 'https://developer.apple.com/documentation/storekit/testing-promoted-in-app-purchases'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/testing-promoted-in-app-purchases.json'
content_hash: 'sha256:b6df9c6ba09eb4bf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md)

# Testing promoted In-App Purchases

<sub>Article</sub>

Test your In-App Purchases before making your app available in the App Store.

## Overview

Users can buy promoted In-App Purchases from the App Store, but you need to test this flow before making your product publicly available. Apple provides a system URL that triggers your app using the `itms-services://` protocol, so you can test In-App Purchases before they’re available in the App Store.

| **Protocol** | `itms-services://` |
|---|---|
| **Parameter** `action` | `purchaseIntent` |
| **Parameter** `bundleId` | The bundle ID for your app; for example: ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `com.example.app` |
| **Parameter** `productIdentifier` | The In-App Purchase product ID you want to test; for example: ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `com.example.product` |

The resulting URL looks like this:

`itms-services://?action=purchaseIntent&bundleId=com.example.app&productIdentifier=com.example.product`

Send this URL to yourself in an email or iMessage, and open it from your device. You’ll know the test is running when your app opens automatically. You can then test how your app handles the promoted In-App Purchase.

## See Also

### Promoted In-App Purchases

- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md) — Display promoted In-App Purchases on your product page and handle purchases that users initiate on the App Store.
- [PurchaseIntent](purchaseintent.md) — An instance that emits purchase intents, which indicate that the customer initiated a purchase outside of your app, for your app to complete.
- [PromotionInfo](product/promotioninfo.md) — Information about a promoted In-App Purchase that customizes its order and visibility on the device.
