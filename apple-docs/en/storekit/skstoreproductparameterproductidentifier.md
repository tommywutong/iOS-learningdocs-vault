---
title: SKStoreProductParameterProductIdentifier
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.0+, macOS 11.0+, tvOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameterproductidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameterproductidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameterproductidentifier.json'
content_hash: 'sha256:248df9bd81e881e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterProductIdentifier

<sub>Global Variable</sub>

The key representing the product identifier for the promoted product you want the store to display at the top of the page.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
let SKStoreProductParameterProductIdentifier: String
```

## Discussion

The value for this key is an instance of [NSString](../foundation/nsstring.md).

When your app uses an [SKStoreProductViewController](skstoreproductviewcontroller.md) to render an app page for another app, you can optionally choose to highlight an in-app purchase by displaying it at the top of the store page.  Set  [SKStoreProductParameterProductIdentifier](skstoreproductparameterproductidentifier.md) to the identifier of the product you want displayed at the top of the page.

The product indicated by the identifier must be set up as a promoted product in the App Store, otherwise the identifier is ignored. See [Promoting In-App Purchases](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/PromotingIn-AppPurchases/PromotingIn-AppPurchases.html#//apple_ref/doc/uid/TP40008267-CH11).

> [!note] Note
> Use the same product identifiers as used in the [productIdentifier](skproduct/productidentifier.md) variable in the [SKProduct](skproduct.md) class.

## See Also

### Affiliate and Analytics Keys

- [SKStoreProductParameterAdvertisingPartnerToken](skstoreproductparameteradvertisingpartnertoken.md) — The key representing the advertising partner you wish to use for any purchase made through the view controller.
- [SKStoreProductParameterAffiliateToken](skstoreproductparameteraffiliatetoken.md) — The key representing the affiliate identifier you wish to use for any purchase made through the view controller.
- [SKStoreProductParameterCampaignToken](skstoreproductparametercampaigntoken.md) — The key representing an App Analytics campaign.
- [SKStoreProductParameterProviderToken](skstoreproductparameterprovidertoken.md) — The key representing the provider token for the developer that created the app specified by the [SKStoreProductParameterITunesItemIdentifier](skstoreproductparameteritunesitemidentifier.md) key.
- [SKStoreProductParameterCustomProductPageIdentifier](skstoreproductparametercustomproductpageidentifier.md) — The key that represents the custom product page identifier you want the store to display when you present the view controller.
