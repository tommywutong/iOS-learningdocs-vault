---
title: 'offerCodeRedemption(options:isPresented:onCompletion:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/offercoderedemption(options:ispresented:oncompletion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/offercoderedemption(options:ispresented:oncompletion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/offercoderedemption%28options%3Aispresented%3Aoncompletion%3A%29.json'
content_hash: 'sha256:0bdc739ac05d3c52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# offerCodeRedemption(options:isPresented:onCompletion:)

<sub>Instance Method</sub>

Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func offerCodeRedemption(options: Set<RedeemOption>, isPresented: Binding<Bool>, onCompletion: @escaping @MainActor (Result<VerificationResult<Transaction>, any Error>) -> Void) -> some View

```

## Parameters

- `options` — A set of `AppStore/RedeemOption` values that configure the code redemption.

- `isPresented` — A binding to a Boolean value that determines whether the system displays the sheet. You set the Boolean value to `true` to cause the system to display the sheet. The system sets it to `false` when it dismisses the sheet.

- `onCompletion` — A closure the system calls with the result of the redemption. On success, the closure receives a `VerificationResult` containing the [Transaction](../transaction.md) that the redemption produces. On failure, it receives the error that caused the redemption to fail.

## Discussion

The [offerCodeRedemption(options:isPresented:onCompletion:)](<offercoderedemption(options_ispresented_oncompletion_).md>) method displays a system sheet where customers can enter and redeem offer codes. If you generate offer codes in App Store Connect, call this method to enable customers to redeem the offer. To display the sheet using UIKit, see `presentOfferCodeRedeemSheet(from:options:)`.

> [!important] Important
> Set up offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI. For more information, see [Supporting offer codes in your app](../../storekit/supporting-offer-codes-in-your-app.md).

The following code example shows a view that displays the offer code redemption sheet when the customer taps a button:

```swift
import SwiftUI
import StoreKit

struct ContentView: View {
    @State private var redeemSheetIsPresented = false

    var body: some View {
        Button("Present offer code redemption sheet.") {
            redeemSheetIsPresented = true
        }
        .offerCodeRedemption(
            options: [],
            isPresented: $redeemSheetIsPresented
        ) { result in
            // Handle result
        }
    }
}
```

When the customer successfully redeems an offer code, the system delivers the resulting transaction through `onCompletion`, as a `VerificationResult` that wraps the [Transaction](../transaction.md).

## See Also

### Interacting with the App Store and Apple Music

- [appStoreOverlay(isPresented:configuration:)](<appstoreoverlay(ispresented_configuration_).md>) — Presents a StoreKit overlay when a given condition is true.
- [manageSubscriptionsSheet(isPresented:)](<managesubscriptionssheet(ispresented_).md>)
- [refundRequestSheet(for:isPresented:onDismiss:)](<refundrequestsheet(for_ispresented_ondismiss_).md>) — Display the refund request sheet for the given transaction.
- [musicPicker(isPresented:title:selection:)](<musicpicker(ispresented_title_selection_).md>) — Presents a music picker to select items from the Apple Music catalog and the user’s music library. _(beta)_
- [musicSubscriptionOffer(isPresented:options:onLoadCompletion:)](<musicsubscriptionoffer(ispresented_options_onloadcompletion_).md>) — Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.
- [currentEntitlementTask(for:priority:action:)](<currententitlementtask(for_priority_action_).md>) — Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [inAppPurchaseOptions(_:)](<inapppurchaseoptions(__).md>) — Add a function to call before initiating a purchase from StoreKit view within this view, providing a set of options for the purchase.
- [manageSubscriptionsSheet(isPresented:subscriptionGroupID:)](<managesubscriptionssheet(ispresented_subscriptiongroupid_).md>)
- [onInAppPurchaseCompletion(perform:)](<oninapppurchasecompletion(perform_).md>) — Add an action to perform when a purchase initiated from a StoreKit view within this view completes.
- [onInAppPurchaseStart(perform:)](<oninapppurchasestart(perform_).md>) — Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [productIconBorder()](<producticonborder().md>) — Adds a standard border to an in-app purchase product’s icon .
- [productViewStyle(_:)](<productviewstyle(__).md>) — Sets the style for In-App Purchase product views within a view.
- [productDescription(_:)](<productdescription(__).md>) — Configure the visibility of labels displaying an in-app purchase product description within the view.
- [storeButton(_:for:)](<storebutton(__for_).md>) — Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [storeProductTask(for:priority:action:)](<storeproducttask(for_priority_action_).md>) — Declares the view as dependent on an In-App Purchase product and returns a modified view.
