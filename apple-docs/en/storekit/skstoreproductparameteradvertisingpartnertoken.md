---
title: SKStoreProductParameterAdvertisingPartnerToken
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.0+, macOS 11.0+, tvOS 9.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameteradvertisingpartnertoken
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameteradvertisingpartnertoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameteradvertisingpartnertoken.json'
content_hash: 'sha256:eb95d1de2e7b8fae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterAdvertisingPartnerToken

<sub>Global Variable</sub>

The key representing the advertising partner you wish to use for any purchase made through the view controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
let SKStoreProductParameterAdvertisingPartnerToken: String
```

## Discussion

The value for this key is an instance of [NSString](../foundation/nsstring.md).

## See Also

### Affiliate and Analytics Keys

- [SKStoreProductParameterProductIdentifier](skstoreproductparameterproductidentifier.md) — The key representing the product identifier for the promoted product you want the store to display at the top of the page.
- [SKStoreProductParameterAffiliateToken](skstoreproductparameteraffiliatetoken.md) — The key representing the affiliate identifier you wish to use for any purchase made through the view controller.
- [SKStoreProductParameterCampaignToken](skstoreproductparametercampaigntoken.md) — The key representing an App Analytics campaign.
- [SKStoreProductParameterProviderToken](skstoreproductparameterprovidertoken.md) — The key representing the provider token for the developer that created the app specified by the [SKStoreProductParameterITunesItemIdentifier](skstoreproductparameteritunesitemidentifier.md) key.
- [SKStoreProductParameterCustomProductPageIdentifier](skstoreproductparametercustomproductpageidentifier.md) — The key that represents the custom product page identifier you want the store to display when you present the view controller.
