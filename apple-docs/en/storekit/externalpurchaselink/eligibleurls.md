---
title: eligibleURLs
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, tvOS 17.5+, visionOS 1.2+, watchOS 10.5+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externalpurchaselink/eligibleurls
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchaselink/eligibleurls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchaselink/eligibleurls.json'
content_hash: 'sha256:21fec33e93ce397a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ExternalPurchaseLink](../externalpurchaselink.md)

# eligibleURLs

<sub>Type Property</sub>

An array of external purchase links for the current storefront that the app configured and from which it chooses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var eligibleURLs: [URL]? { get async }
```

## Discussion

Use this property if your app configures the [SKExternalPurchaseMultiLink](../../bundleresources/information-property-list/skexternalpurchasemultilink.md) property list key.

Use the [eligibleURLs](eligibleurls.md) to get the array of external purchase links for the current storefront that your app has configured in the [SKExternalPurchaseMultiLink](../../bundleresources/information-property-list/skexternalpurchasemultilink.md) property list key. Your app can select from any of the eligible URLs. Call [open(url:)](<open(url_).md>) with the URL you choose.

The [eligibleURLs](eligibleurls.md) array is `nil` if any of the following is true:

- The current App Store storefront doesn’t allow external purchase or the person isn’t eligible to make external purchases.
- Your app doesn’t configure the [com.apple.developer.storekit.external-purchase-link](../../bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link.md) entitlement.
- Your app doesn’t configure any links for the current storefront in the [SKExternalPurchaseMultiLink](../../bundleresources/information-property-list/skexternalpurchasemultilink.md) property list key

If this value is `nil` and your app also configures the [SKExternalPurchaseLink](../../bundleresources/information-property-list/skexternalpurchaselink.md) property list key, check [canOpen](canopen.md) to determine whether your app can continue to provide an external purchase link.

Otherwise, if this value is `nil`, check [canMakePayments](../appstore/canmakepayments.md) to determine whether your app can offer in-app purchases using the StoreKit [In-App Purchase](../in-app-purchase.md) APIs. For more information, see [canMakePayments](../appstore/canmakepayments.md).

## See Also

### Getting multiple external purchase links

- [SKExternalPurchaseMultiLink](../../bundleresources/information-property-list/skexternalpurchasemultilink.md) — A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [open(url:)](<open(url_).md>) — Presents a continuation sheet that enables people to choose whether your app shows the indicated URL link for external purchases.
