---
title: 'offerCodeRedemption(isPresented:onCompletion:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（27.0 起废弃）, iPadOS 16.0+（27.0 起废弃）, Mac Catalyst 16.0+（27.0 起废弃）, macOS 15.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/offercoderedemption(ispresented:oncompletion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/offercoderedemption(ispresented:oncompletion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/offercoderedemption%28ispresented%3Aoncompletion%3A%29.json'
content_hash: 'sha256:a6c8d8df7e95787a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# offerCodeRedemption(isPresented:onCompletion:)

<sub>Instance Method</sub>

> [!warning] Deprecated
> Use [offerCodeRedemption(options:isPresented:onCompletion:)](<offercoderedemption(options_ispresented_oncompletion_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: @escaping @MainActor (Result<Void, any Error>) -> Void = { _ in }) -> some View

```

## Parameters

- `isPresented` — A binding to a Boolean value that determines whether the system displays the sheet. You set the Boolean value to true to cause the system to display the sheet. The system sets it to false when it dismisses the sheet.

- `onCompletion` — A closure that returns the result of the presentation. In Mac apps built with Mac Catalyst, the completion handler returns a failure with an error prior to macOS 15.

## Discussion

Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.

The `offerCodeRedemption(isPresented:onCompletion:)` method displays a system sheet where customers can enter and redeem offer codes. If you generate offer codes in App Store Connect, call this function to enable customers to redeem the offer. To display the sheet using UIKit, see `presentOfferCodeRedeemSheet(in:)`.

> [!important] Important
> Set up offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI. For more information, see [Supporting offer codes in your app](../../storekit/supporting-offer-codes-in-your-app.md).

The following code example shows a view that displays the offer code redemption sheet upon a button press:

```swift
import SwiftUI
import StoreKit
    
    
struct ContentView: View {
    @State private var redeemSheetIsPresented = false
    
    
    var body: some View {
        Button("Present offer code redemption sheet.") {
            redeemSheetIsPresented = true
        }
        .offerCodeRedemption(isPresented: $redeemSheetIsPresented) { result in
            // Handle result
        }
    }
}
```

When customers redeem an offer code, StoreKit emits the resulting transaction in [updates](../../storekit/transaction/updates.md). Set up a transaction listener as soon as your app launches to receive new transactions while the app is running.

## See Also

### Technology-specific modifiers

- [postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)](<posttophotossharedalbumsheet(ispresented_items_photolibrary_defaultalbumidentifier_completion_).md>) — Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album. _(deprecated)_
- [subscriptionPromotionalOffer(offer:signature:)](<subscriptionpromotionaloffer(offer_signature_).md>) — Selects a promotional offer to apply to a purchase a customer makes from a subscription store view. _(deprecated)_
