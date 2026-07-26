---
title: com.apple.developer.storekit.external-purchase-link
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link.json'
content_hash: 'sha256:ee36ecd59f3ddf3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# com.apple.developer.storekit.external-purchase-link

<sub>Property List Key</sub>

A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.

## Discussion

The [com.apple.developer.storekit.external-purchase-link](com.apple.developer.storekit.external-purchase-link.md) entitlement enables qualifying apps to include a link that directs people using the app to a website to make an external purchase. For more information, see [External Purchase](../../storekit/external-purchase.md).

If your account receives this entitlement, which is also known as the StoreKit External Purchase Link entitlement, you can add it to your app by opening the project’s `.entitlements` file in Xcode. Then add the following key and set the corresponding value to `true`:

```xml
<plist>
<dict>
    <key>com.apple.developer.storekit.external-purchase-link</key>
    <true/>
</dict>
</plist>
```

## See Also

### StoreKit

- [com.apple.developer.storekit.custom-purchase-link.allowed-regions](com.apple.developer.storekit.custom-purchase-link.allowed-regions.md) — An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.
- [com.apple.developer.storekit.external-link.account](com.apple.developer.storekit.external-link.account.md) — A Boolean value that indicates whether your app can link to an external website for account creation or management.
- [com.apple.developer.storekit.external-purchase](com.apple.developer.storekit.external-purchase.md) — A Boolean value that indicates whether your app can offer external purchases.
- [com.apple.developer.storekit.external-purchase-link-streaming](com.apple.developer.storekit.external-purchase-link-streaming.md) — An entitlement that grants a qualifying music-streaming app the ability to communicate and promote offers.
