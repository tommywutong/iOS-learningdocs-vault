---
title: SKStoreProductParameterAffiliateToken
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameteraffiliatetoken
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameteraffiliatetoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameteraffiliatetoken.json'
content_hash: 'sha256:4e89ce95be48088e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterAffiliateToken

<sub>Global Variable</sub>

The key representing the affiliate identifier you wish to use for any purchase made through the view controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
let SKStoreProductParameterAffiliateToken: String
```

## Discussion

The value for this key is an instance of [NSString](../foundation/nsstring.md).

You receive an affiliate identifier when you sign up for the Affiliate Program. The affiliate associated with this view controller is paid a commission for any items purchased using the controller.

Learn more about the Affiliate Program at [https://apple.com/itunes/affiliates](https://apple.com/itunes/affiliates).

## See Also

### Affiliate and Analytics Keys

- [SKStoreProductParameterProductIdentifier](skstoreproductparameterproductidentifier.md) — The key representing the product identifier for the promoted product you want the store to display at the top of the page.
- [SKStoreProductParameterAdvertisingPartnerToken](skstoreproductparameteradvertisingpartnertoken.md) — The key representing the advertising partner you wish to use for any purchase made through the view controller.
- [SKStoreProductParameterCampaignToken](skstoreproductparametercampaigntoken.md) — The key representing an App Analytics campaign.
- [SKStoreProductParameterProviderToken](skstoreproductparameterprovidertoken.md) — The key representing the provider token for the developer that created the app specified by the [SKStoreProductParameterITunesItemIdentifier](skstoreproductparameteritunesitemidentifier.md) key.
- [SKStoreProductParameterCustomProductPageIdentifier](skstoreproductparametercustomproductpageidentifier.md) — The key that represents the custom product page identifier you want the store to display when you present the view controller.
