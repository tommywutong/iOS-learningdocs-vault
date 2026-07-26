---
title: isEligible
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.1+, iPadOS 18.1+, macOS 15.1+, tvOS 18.1+, visionOS 2.1+, watchOS 11.1+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externalpurchasecustomlink/iseligible
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/iseligible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchasecustomlink/iseligible.json'
content_hash: 'sha256:a8aec4ced2b6b0b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ExternalPurchaseCustomLink](../externalpurchasecustomlink.md)

# isEligible

<sub>Type Property</sub>

A Boolean value that indicates at runtime whether the app can use this API for external purchases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var isEligible: Bool { get async }
```

## Discussion

Check this value if your app configures any of the following entitlements:

- [com.apple.developer.storekit.custom-purchase-link.allowed-regions](../../bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions.md)
- [com.apple.developer.storekit.external-purchase-link](../../bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link.md)
- [com.apple.developer.storekit.external-purchase-link-streaming](../../bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link-streaming.md)

If [isEligible](iseligible.md) is `true`, your app can use the [ExternalPurchaseCustomLink](../externalpurchasecustomlink.md) API.

This value is `true` if all the following conditions are met:

- The current App Store storefront allows external purchases and the person can make purchases.
- Your app configures any of the entitlements listed above.
- Your app configures the current App Store storefront in the property list key associated with the entitlement, [SKExternalPurchaseCustomLinkRegions](../../bundleresources/information-property-list/skexternalpurchasecustomlinkregions.md) or [SKExternalPurchaseLinkStreamingRegions](../../bundleresources/information-property-list/skexternalpurchaselinkstreamingregions.md), or has an entitlement that includes the current App Store storefront.

If [isEligible](iseligible.md) is `false`, don’t use the [ExternalPurchaseCustomLink](../externalpurchasecustomlink.md) API. The methods of the [ExternalPurchaseCustomLink](../externalpurchasecustomlink.md) API throw errors at runtime when [isEligible](iseligible.md) is `false`.
