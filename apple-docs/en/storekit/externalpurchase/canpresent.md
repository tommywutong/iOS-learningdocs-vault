---
title: canPresent
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externalpurchase/canpresent
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchase/canpresent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchase/canpresent.json'
content_hash: 'sha256:5fe9b07318cf499d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ExternalPurchase](../externalpurchase.md)

# canPresent

<sub>Type Property</sub>

A Boolean value that indicates whether the app can successfully present the notice sheet to inform people about external purchases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var canPresent: Bool { get async }
```

## Discussion

Check this property, as shown below, to determine whether your app can successfully call [presentNoticeSheet()](<presentnoticesheet().md>) to inform people before showing external purchases:

```swift
await externalPurchase.canPresent 
```

Check the value of this property again whenever the App Store storefront changes by using the [updates](../storefront/updates.md) asynchronous sequence of [Storefront](../storefront.md).

This property is `true` if all the following conditions are met:

- The current App Store storefront allows external purchase, and the person is eligible to make external purchases.
- Your app configures the [com.apple.developer.storekit.custom-purchase-link.allowed-regions](../../bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions.md) entitlement, or it configures the  [com.apple.developer.storekit.external-purchase](../../bundleresources/entitlements/com.apple.developer.storekit.external-purchase.md) entitlement and the [SKExternalPurchase](../../bundleresources/information-property-list/skexternalpurchase.md), including the country code for the current App Store storefront.

Otherwise, this property is `false`.

When this property is `false`, check [canMakePayments](../appstore/canmakepayments.md) to determine whether your app can offer in-app purchases using the StoreKit [In-App Purchase](../in-app-purchase.md) APIs. For more information, see [canMakePayments](../appstore/canmakepayments.md).

## See Also

### Offering an external purchase

- [presentNoticeSheet()](<presentnoticesheet().md>) — Presents a notice sheet from Apple that informs people of external purchases before showing them, and determines if your app can present external purchases
- [NoticeResult](noticeresult.md) — The options available to people while viewing the external purchase notice sheet.
- [SKExternalPurchase](../../bundleresources/information-property-list/skexternalpurchase.md) — A string array of country codes that indicates your app supports external purchases.
