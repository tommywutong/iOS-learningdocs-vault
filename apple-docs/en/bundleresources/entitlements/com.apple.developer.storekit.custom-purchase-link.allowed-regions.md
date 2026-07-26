---
title: com.apple.developer.storekit.custom-purchase-link.allowed-regions
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 26.2+, iPadOS 26.2+, macOS 26.2+, tvOS 26.2+, visionOS 26.2+, watchOS 26.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions.json'
content_hash: 'sha256:1a20a2844fb83c24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# com.apple.developer.storekit.custom-purchase-link.allowed-regions

<sub>Property List Key</sub>

An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.

## Discussion

This entitlement enables a qualifying app to offer external purchases within the app or at a website of its choice, in specific regions.

If your account receives this entitlement, you can add it to your app by opening the project’s `.entitlements` file in Xcode. Then, add a key named `com.apple.developer.storekit.custom-purchase-link.allowed-regions`, followed by an array that enumerates the two-letter ISO-3166-1 country codes for the allowed regions. The example below describes an entitlement that includes Brazil and Japan as the allowed regions that the app supports.

```
<plist>
<dict>
    <key>com.apple.developer.storekit.custom-purchase-link.allowed-regions</key>
    <array>
    <string>br</string>
    <string>jp</string>
    </array>
</dict>
</plist>
```

> [!important] Important
> Provide the regions where you intend to offer this functionality. This must only include regions where Apple supports custom purchase link options.

For more information, see [External Purchase](../../storekit/external-purchase.md).

## See Also

### StoreKit

- [com.apple.developer.storekit.external-link.account](com.apple.developer.storekit.external-link.account.md) — A Boolean value that indicates whether your app can link to an external website for account creation or management.
- [com.apple.developer.storekit.external-purchase](com.apple.developer.storekit.external-purchase.md) — A Boolean value that indicates whether your app can offer external purchases.
- [com.apple.developer.storekit.external-purchase-link](com.apple.developer.storekit.external-purchase-link.md) — A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [com.apple.developer.storekit.external-purchase-link-streaming](com.apple.developer.storekit.external-purchase-link-streaming.md) — An entitlement that grants a qualifying music-streaming app the ability to communicate and promote offers.
