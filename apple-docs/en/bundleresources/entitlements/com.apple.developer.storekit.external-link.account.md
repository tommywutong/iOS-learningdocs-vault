---
title: com.apple.developer.storekit.external-link.account
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 15.4+, iPadOS 15.4+, tvOS 16.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.developer.storekit.external-link.account
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-link.account'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-link.account.json'
content_hash: 'sha256:efa30912469b3bb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# com.apple.developer.storekit.external-link.account

<sub>Property List Key</sub>

A Boolean value that indicates whether your app can link to an external website for account creation or management.

## Discussion

If your developer account has this entitlement, add it to your app by opening the project’s entitlements file in Xcode. Add the following key and set the corresponding value to `true`:

```xml
<plist>
<dict>
    <key>com.apple.developer.storekit.external-link.account</key>
    <true/>
</dict>
</plist>
```

## See Also

### StoreKit

- [com.apple.developer.storekit.custom-purchase-link.allowed-regions](com.apple.developer.storekit.custom-purchase-link.allowed-regions.md) — An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.
- [com.apple.developer.storekit.external-purchase](com.apple.developer.storekit.external-purchase.md) — A Boolean value that indicates whether your app can offer external purchases.
- [com.apple.developer.storekit.external-purchase-link](com.apple.developer.storekit.external-purchase-link.md) — A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [com.apple.developer.storekit.external-purchase-link-streaming](com.apple.developer.storekit.external-purchase-link-streaming.md) — An entitlement that grants a qualifying music-streaming app the ability to communicate and promote offers.
