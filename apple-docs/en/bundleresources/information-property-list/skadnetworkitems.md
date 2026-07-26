---
title: SKAdNetworkItems
framework: Bundle Resources
symbol_kind: dictionary
role: symbol
role_heading: Property List Key
platforms: [iOS 11.3+, iPadOS 11.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/skadnetworkitems
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/skadnetworkitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/skadnetworkitems.json'
content_hash: 'sha256:eae40557ca7f783c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# SKAdNetworkItems

<sub>Property List Key</sub>

An array of dictionaries containing a list of ad network IDs.

## Discussion

Apps that display ads and initiate install-validation information to share with ad networks need to include the ad network IDs in this key.

Each dictionary contains one [SKAdNetworkIdentifier](skadnetworkitems/skadnetworkidentifier.md). Provide one dictionary for each ad network that you work with.

> [!important] Important
> Ad network IDs are case-sensitive and are in lowercase.

For more information, see [Configuring a source app](../../storekit/configuring-a-source-app.md).

## Topics

### Ad network identifiers

- [SKAdNetworkIdentifier](skadnetworkitems/skadnetworkidentifier.md) — A string that contains an ad network ID.

## See Also

### StoreKit

- [SKExternalLinkAccount](skexternallinkaccount.md) — A dictionary that contains localized URLs to an external website for account creation or management.
- [SKExternalPurchase](skexternalpurchase.md) — A string array of country codes that indicates your app supports external purchases.
- [SKExternalPurchaseCustomLinkRegions](skexternalpurchasecustomlinkregions.md) — An array of country code strings that indicate the regions where your app supports custom links for the communication and promotion of offers.
- [SKExternalPurchaseLink](skexternalpurchaselink.md) — A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.
- [SKExternalPurchaseMultiLink](skexternalpurchasemultilink.md) — A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [SKIncludeConsumableInAppPurchaseHistory](skincludeconsumableinapppurchasehistory.md) — A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.
- [SKExternalPurchaseLinkStreamingRegions](skexternalpurchaselinkstreamingregions.md) — A list of country codes that indicate the regions where your music-streaming app communicates and promotes offers.
