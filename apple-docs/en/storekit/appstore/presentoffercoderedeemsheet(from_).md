---
title: 'presentOfferCodeRedeemSheet(from:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 15.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/storekit/appstore/presentoffercoderedeemsheet(from:)'
source_url: 'https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore/presentoffercoderedeemsheet%28from%3A%29.json'
content_hash: 'sha256:511a9c86cbc8dbe1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppStore](../appstore.md)

# presentOfferCodeRedeemSheet(from:)

<sub>Type Method</sub>

Displays a sheet in the view that enables customers to redeem an offer code that you configure in App Store Connect.

> [!warning] Deprecated
> Use [presentOfferCodeRedeemSheet(from:options:)](<presentoffercoderedeemsheet(from_options_)-gj8m.md>) instead.

<sub>macOS</sub>

```swift
@MainActor static func presentOfferCodeRedeemSheet(from controller: NSViewController) async throws
```

## Parameters

- `controller` — An [NSViewController](../../appkit/nsviewcontroller.md) that StoreKit uses to display the offer code redemption sheet.

## Discussion

This method displays a system sheet in the view, where customers can enter and redeem offer codes. Use this method if you generate offer codes in App Store Connect and your app uses AppKit.

> [!important] Important
> Set up offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI.

For more information on offer codes, see [Supporting offer codes in your app](../supporting-offer-codes-in-your-app.md).

When customers redeem an offer code, StoreKit emits the resulting transaction in [updates](../transaction/updates.md). Set up a transaction listener as soon as your app launches to receive new transactions while the app is running.

## See Also

### Deprecated

- [presentOfferCodeRedeemSheet(in:)](<presentoffercoderedeemsheet(in_).md>) — Displays a sheet in the window scene that enables customers to redeem an offer code that you configure in App Store Connect. _(deprecated)_
- [offerCodeRedemption(isPresented:onCompletion:)](<../../swiftui/view/offercoderedemption(ispresented_oncompletion_).md>) _(deprecated)_
