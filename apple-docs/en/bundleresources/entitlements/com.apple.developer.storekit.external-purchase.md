---
title: com.apple.developer.storekit.external-purchase
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase.json'
content_hash: 'sha256:66e601a5e8594ccf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# com.apple.developer.storekit.external-purchase

<sub>Property List Key</sub>

A Boolean value that indicates whether your app can offer external purchases.

## Discussion

Qualifying apps may offer external purchases within the app. To offer external purchases in your app, complete a request for this entitlement. For more information about qualifying apps and to request this entitlement, see:

- [Using alternative payment options on the App Store in the European Union](https://developer.apple.com/go/?id=storekit-external-purchase-eu)
- [Distributing dating apps in the Netherlands](https://developer.apple.com/support/storekit-external-entitlement/)
- [Distributing apps using a third-party payment provider in South Korea](https://developer.apple.com/support/storekit-external-entitlement-kr/)

If your account receives this entitlement, which is also known as the StoreKit External Purchase entitlement, add it to your app by opening the project’s .`entitlements` file in Xcode. Then add the following key and set the corresponding value to `true`:

```xml
<plist>
<dict>
    <key>com.apple.developer.storekit.external-purchase</key>
    <true/>
</dict>
</plist>
```

For more information, see [External Purchase](../../storekit/external-purchase.md).

## See Also

### StoreKit

- [com.apple.developer.storekit.custom-purchase-link.allowed-regions](com.apple.developer.storekit.custom-purchase-link.allowed-regions.md) — An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.
- [com.apple.developer.storekit.external-link.account](com.apple.developer.storekit.external-link.account.md) — A Boolean value that indicates whether your app can link to an external website for account creation or management.
- [com.apple.developer.storekit.external-purchase-link](com.apple.developer.storekit.external-purchase-link.md) — A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [com.apple.developer.storekit.external-purchase-link-streaming](com.apple.developer.storekit.external-purchase-link-streaming.md) — An entitlement that grants a qualifying music-streaming app the ability to communicate and promote offers.
