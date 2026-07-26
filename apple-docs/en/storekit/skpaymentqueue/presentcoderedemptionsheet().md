---
title: presentCodeRedemptionSheet()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentqueue/presentcoderedemptionsheet()
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/presentcoderedemptionsheet()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/presentcoderedemptionsheet%28%29.json'
content_hash: 'sha256:ac01072afbf6300d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# presentCodeRedemptionSheet()

<sub>Instance Method</sub>

Displays a sheet that enables customers to redeem offer codes that you configure in App Store Connect.

> [!warning] Deprecated
> Use [presentOfferCodeRedeemSheet(in:)](<../appstore/presentoffercoderedeemsheet(in_).md>) or [offerCodeRedemption(isPresented:onCompletion:)](<../../swiftui/view/offercoderedemption(ispresented_oncompletion_).md>) instead. For more information, see [Supporting offer codes in your app](../supporting-offer-codes-in-your-app.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func presentCodeRedemptionSheet()
```

## Discussion

The [- presentCodeRedemptionSheet](<presentcoderedemptionsheet().md>) function displays a system sheet where customers can enter and redeem offer codes. If you generate offer codes in App Store Connect, call this function to enable customers to redeem the offer. For information on implementing offer codes, see [Implementing offer codes in your app](../implementing-offer-codes-in-your-app.md).

> [!note] Note
> For apps with more than one scene, and on iOS 16 or later and iPadOS 16 or later, use [offerCodeRedemption(isPresented:onCompletion:)](<../../swiftui/view/offercoderedemption(ispresented_oncompletion_).md>) or [presentOfferCodeRedeemSheet(in:)](<../appstore/presentoffercoderedeemsheet(in_).md>) instead.

When your app calls [- presentCodeRedemptionSheet](<presentcoderedemptionsheet().md>), the system determines where to display the screen. Use [- presentCodeRedemptionSheet](<presentcoderedemptionsheet().md>) to support devices running iOS 14 through iOS 15, and iPadOS 14 through iPadOS 15.

> [!important] Important
> Set up offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI.

For information on configuring and generating offer codes, see [Set up offer codes](https://help.apple.com/app-store-connect/#/dev6a098e4b1).

This method applies to offer codes only; it doesn’t apply to promo codes for apps or in-app purchases. For more information on promo codes, see [Request and manage promo codes](https://help.apple.com/app-store-connect/#/dev50869de4a).

This function doesn’t affect Mac apps built with Mac Catalyst.
