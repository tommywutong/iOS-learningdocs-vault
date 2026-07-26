---
title: Product.PromotionInfo.Visibility.appStoreConnectDefault
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.4+, iPadOS 16.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/promotioninfo/visibility-swift.enum/appstoreconnectdefault
source_url: 'https://developer.apple.com/documentation/storekit/product/promotioninfo/visibility-swift.enum/appstoreconnectdefault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/promotioninfo/visibility-swift.enum/appstoreconnectdefault.json'
content_hash: 'sha256:c8bffbf1e763dede'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [PromotionInfo](../../promotioninfo.md) · [Visibility](../visibility-swift.enum.md)

# Product.PromotionInfo.Visibility.appStoreConnectDefault

<sub>Case</sub>

A visibility value for a promoted in-app purchase that uses the visibility setting from App Store Connect.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case appStoreConnectDefault
```

## Discussion

When a promoted in-app purchase has a visibility value of [Product.PromotionInfo.Visibility.appStoreConnectDefault](appstoreconnectdefault.md), the in-app purchase is:

- Visible if the setting in App Store Connect makes it visible
- Hidden if the setting in App Store Connect makes it hidden

Use this value to control the visibility for promoted in-app purchases in App Store Connect, globally, for all users. For example, if you have a product to promote on a holiday, start by manually setting it as hidden using App Store Connect. On the holiday, change the setting to make the promotion visible. If the promotion visibility in the app is the default ([Product.PromotionInfo.Visibility.appStoreConnectDefault](appstoreconnectdefault.md)), it becomes visible for all users automatically.

For more information about the visibility settings in App Store Connect, see [Promote in-app purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases).

## See Also

### Getting visibility states

- [Product.PromotionInfo.Visibility.hidden](hidden.md) — A visibility value that hides a promoted in-app purchase on the App Store on a user’s device.
- [Product.PromotionInfo.Visibility.visible](visible.md) — A visibility value that makes a promoted in-app purchase visible on the App Store on a user’s device.
