---
title: Product Dictionary Keys
framework: StoreKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/product-dictionary-keys
source_url: 'https://developer.apple.com/documentation/storekit/product-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product-dictionary-keys.json'
content_hash: 'sha256:b10be4de33ab002c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [SKStoreProductViewController](skstoreproductviewcontroller.md)

# Product Dictionary Keys

<sub>API Collection</sub>

Keys for identifying products and the tokens for affiliates and campaigns.

## Overview

These dictionary keys are used in the parameter for the [- loadProductWithParameters:completionBlock:](<skstoreproductviewcontroller/loadproduct(withparameters_completionblock_).md>) method.

The [SKStoreProductParameterITunesItemIdentifier](skstoreproductparameteritunesitemidentifier.md) key represents the product to display, and is always required. Other keys provide optional affiliate or promoted product information.

Learn more about the Affiliate Program at [https://apple.com/itunes/affiliates](https://apple.com/itunes/affiliates).

## Topics

### Required Key

- [SKStoreProductParameterITunesItemIdentifier](skstoreproductparameteritunesitemidentifier.md) — The key representing the iTunes identifier for the item you want the store to display when the view controller is presented.

### Affiliate and Analytics Keys

- [SKStoreProductParameterProductIdentifier](skstoreproductparameterproductidentifier.md) — The key representing the product identifier for the promoted product you want the store to display at the top of the page.
- [SKStoreProductParameterAdvertisingPartnerToken](skstoreproductparameteradvertisingpartnertoken.md) — The key representing the advertising partner you wish to use for any purchase made through the view controller.
- [SKStoreProductParameterAffiliateToken](skstoreproductparameteraffiliatetoken.md) — The key representing the affiliate identifier you wish to use for any purchase made through the view controller.
- [SKStoreProductParameterCampaignToken](skstoreproductparametercampaigntoken.md) — The key representing an App Analytics campaign.
- [SKStoreProductParameterProviderToken](skstoreproductparameterprovidertoken.md) — The key representing the provider token for the developer that created the app specified by the [SKStoreProductParameterITunesItemIdentifier](skstoreproductparameteritunesitemidentifier.md) key.
- [SKStoreProductParameterCustomProductPageIdentifier](skstoreproductparametercustomproductpageidentifier.md) — The key that represents the custom product page identifier you want the store to display when you present the view controller.

## See Also

### Loading a new product screen

- [Offering media for sale in your app](offering-media-for-sale-in-your-app.md) — Allow users to purchase media in the App Store from within your app.
- [- loadProductWithParameters:completionBlock:](<skstoreproductviewcontroller/loadproduct(withparameters_completionblock_).md>) — Loads a new product screen to display.
- [- loadProductWithParameters:impression:completionBlock:](<skstoreproductviewcontroller/loadproduct(withparameters_impression_completionblock_).md>)
- [loadProduct(parameters:impression:)](<skstoreproductviewcontroller/loadproduct(parameters_impression_).md>)
- [loadProduct(parameters:impression:reengagementURL:)](<skstoreproductviewcontroller/loadproduct(parameters_impression_reengagementurl_).md>)
