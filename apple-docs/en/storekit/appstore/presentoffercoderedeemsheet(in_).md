---
title: 'presentOfferCodeRedeemSheet(in:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+（27.0 起废弃）, iPadOS 16.0+（27.0 起废弃）, Mac Catalyst 16.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/storekit/appstore/presentoffercoderedeemsheet(in:)'
source_url: 'https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore/presentoffercoderedeemsheet%28in%3A%29.json'
content_hash: 'sha256:8a406cd7b186b3ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppStore](../appstore.md)

# presentOfferCodeRedeemSheet(in:)

<sub>Type Method</sub>

Displays a sheet in the window scene that enables customers to redeem an offer code that you configure in App Store Connect.

> [!warning] Deprecated
> Use [presentOfferCodeRedeemSheet(from:options:)](<presentoffercoderedeemsheet(from_options_)-89agc.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor static func presentOfferCodeRedeemSheet(in scene: UIWindowScene) async throws
```

## Parameters

- `scene` — The [UIWindowScene](../../uikit/uiwindowscene.md) that StoreKit uses to display the offer code redemption sheet.

## Discussion

The [presentOfferCodeRedeemSheet(in:)](<presentoffercoderedeemsheet(in_).md>) method displays a system sheet in the window scene, where customers can enter and redeem offer codes. If you generate offer codes in App Store Connect, call this function to enable customers to redeem the offer. To display the sheet using SwiftUI, see [offerCodeRedemption(isPresented:onCompletion:)](<../../swiftui/view/offercoderedemption(ispresented_oncompletion_).md>).

> [!important] Important
> Set up offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI.

For more information on offer codes, see [Supporting offer codes in your app](../supporting-offer-codes-in-your-app.md).

When customers redeem an offer code, StoreKit emits the resulting transaction in [updates](../transaction/updates.md). Set up a transaction listener as soon as your app launches to receive new transactions while the app is running. For more information, see [updates](../transaction/updates.md).

In Mac apps built with Mac Catalyst, this method throws a [StoreKitError.unknown](../storekiterror/unknown.md) error.

## See Also

### Deprecated

- [offerCodeRedemption(isPresented:onCompletion:)](<../../swiftui/view/offercoderedemption(ispresented_oncompletion_).md>) _(deprecated)_
- [presentOfferCodeRedeemSheet(from:)](<presentoffercoderedeemsheet(from_).md>) — Displays a sheet in the view that enables customers to redeem an offer code that you configure in App Store Connect. _(deprecated)_
