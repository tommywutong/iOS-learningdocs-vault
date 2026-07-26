---
title: SKStoreProductParameterProviderToken
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.3+, iPadOS 8.3+, Mac Catalyst 13.0+, macOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameterprovidertoken
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameterprovidertoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameterprovidertoken.json'
content_hash: 'sha256:1c46bd7c2178e72f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterProviderToken

<sub>Global Variable</sub>

The key representing the provider token for the developer that created the app specified by the [SKStoreProductParameterITunesItemIdentifier](skstoreproductparameteritunesitemidentifier.md) key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
let SKStoreProductParameterProviderToken: String
```

## Discussion

The value for this key is an instance of [NSString](../foundation/nsstring.md).

Use your own provider token when cross promoting your own apps. This token lets you track the effectiveness of the cross promotion effort separate from any affiliate campaign that shares the same campaign token.

When promoting apps for other developers, use their provider token instead. In this case, the token lets the developer track the effectiveness of your App Analytics campaign for their apps.

The key must be used in combination with your campaign token, [SKStoreProductParameterCampaignToken](skstoreproductparametercampaigntoken.md). For more information, see [App Store Connect Developer Guide](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/About.html#//apple_ref/doc/uid/TP40011225).

## See Also

### Affiliate and Analytics Keys

- [SKStoreProductParameterProductIdentifier](skstoreproductparameterproductidentifier.md) — The key representing the product identifier for the promoted product you want the store to display at the top of the page.
- [SKStoreProductParameterAdvertisingPartnerToken](skstoreproductparameteradvertisingpartnertoken.md) — The key representing the advertising partner you wish to use for any purchase made through the view controller.
- [SKStoreProductParameterAffiliateToken](skstoreproductparameteraffiliatetoken.md) — The key representing the affiliate identifier you wish to use for any purchase made through the view controller.
- [SKStoreProductParameterCampaignToken](skstoreproductparametercampaigntoken.md) — The key representing an App Analytics campaign.
- [SKStoreProductParameterCustomProductPageIdentifier](skstoreproductparametercustomproductpageidentifier.md) — The key that represents the custom product page identifier you want the store to display when you present the view controller.
