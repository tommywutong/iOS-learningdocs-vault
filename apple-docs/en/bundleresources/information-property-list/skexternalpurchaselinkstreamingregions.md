---
title: SKExternalPurchaseLinkStreamingRegions
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 18.2+, iPadOS 18.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/skexternalpurchaselinkstreamingregions
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchaselinkstreamingregions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/skexternalpurchaselinkstreamingregions.json'
content_hash: 'sha256:20434150b756f535'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# SKExternalPurchaseLinkStreamingRegions

<sub>Property List Key</sub>

A list of country codes that indicate the regions where your music-streaming app communicates and promotes offers.

## Discussion

Use this information property list key if your app has the [com.apple.developer.storekit.external-purchase-link-streaming](../entitlements/com.apple.developer.storekit.external-purchase-link-streaming.md) entitlement.

The strings in this array are lowercased ISO 3166-1 alpha-2 country codes. Valid country codes include those for the European Union: Austria (at), Belgium (be), Bulgaria (bg), Croatia (hr), Cyprus (cy), Czechia (cz), Denmark (dk), Estonia (ee), Finland (fi), France (fr), Germany (de), Greece (gr), Hungary (hu), Ireland (ie), Italy (it), Latvia (lv), Lithuania (lt), Luxembourg (lu), Malta (mt), Netherlands (nl), Poland (pl), Portugal (pt), Romania (ro), Slovakia (sk), Slovenia (si), Spain (es), Sweden (se); and Iceland (is) and Norway (no).

Include an entry for each country code where your music-streaming app communicates and promotes offers.

For more information, see [External Purchase](../../storekit/external-purchase.md).

## See Also

### StoreKit

- [SKAdNetworkItems](skadnetworkitems.md) — An array of dictionaries containing a list of ad network IDs.
- [SKExternalLinkAccount](skexternallinkaccount.md) — A dictionary that contains localized URLs to an external website for account creation or management.
- [SKExternalPurchase](skexternalpurchase.md) — A string array of country codes that indicates your app supports external purchases.
- [SKExternalPurchaseCustomLinkRegions](skexternalpurchasecustomlinkregions.md) — An array of country code strings that indicate the regions where your app supports custom links for the communication and promotion of offers.
- [SKExternalPurchaseLink](skexternalpurchaselink.md) — A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.
- [SKExternalPurchaseMultiLink](skexternalpurchasemultilink.md) — A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [SKIncludeConsumableInAppPurchaseHistory](skincludeconsumableinapppurchasehistory.md) — A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.
