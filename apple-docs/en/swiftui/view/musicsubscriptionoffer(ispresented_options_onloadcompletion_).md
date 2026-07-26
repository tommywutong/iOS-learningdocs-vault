---
title: 'musicSubscriptionOffer(isPresented:options:onLoadCompletion:)'
framework: MusicKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/musicsubscriptionoffer(ispresented:options:onloadcompletion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/musicsubscriptionoffer(ispresented:options:onloadcompletion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/musicsubscriptionoffer%28ispresented%3Aoptions%3Aonloadcompletion%3A%29.json'
content_hash: 'sha256:9fa795951a1d96da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# musicSubscriptionOffer(isPresented:options:onLoadCompletion:)

<sub>Instance Method</sub>

Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated func musicSubscriptionOffer(isPresented: Binding<Bool>, options: MusicSubscriptionOffer.Options = .default, onLoadCompletion: @escaping ((any Error)?) -> Void = { _ in }) -> some View

```

## Parameters

- `isPresented` — A binding to a Boolean value that you can set to `true` to show a sheet with subscription offers for Apple Music.

- `options` — Options to use for loading the subscription offer for Apple Music.

- `onLoadCompletion` — The function to call upon completing the initial loading process for this subscription offer. The subscription offer UI becomes visible when it calls this function with the error argument as `nil`. If there is an error in the loading process, the subscription offer calls this function with a non-`nil` error, and it resets the `isPresented` binding to `false`.

## Discussion

The example below displays a simple button that the user can activate to begin presenting subscription offers for Apple Music. The action handler of this button initiates the presentation of those offers by setting the `isShowingOffer` variable to `true`.

```swift
struct MusicSubscriptionOfferButton: View {
    @State var isShowingOffer = false
    var body: some View {
        Button("Apple Music Subscription Offer") {
            isShowingOffer = true
        }
        .musicSubscriptionOffer(isPresented: $isShowingOffer)
    }
}
```

You can also configure the Apple Music subscription offer by creating an instance of `MusicSubscriptionOffer.Options`, setting relevant properties on it, and passing it to `.musicSubscriptionOffer(…)`. For example, to present contextual offers that highlight a specific album, you can configure the subscription offer like the following:

```swift
struct MusicSubscriptionOfferButton: View {
    var album: Album
    @State var isShowingOffer = false
    @State var offerOptions = MusicSubscriptionOffer.Options(
        affiliateToken: "<affiliate_token>", 
        campaignToken: "<campaign_token>"
    )

    var body: some View {
        Button("Apple Music Subscription Offer") {
            offerOptions.itemID = album.id
            isShowingOffer = true
        }
        .musicSubscriptionOffer(
            isPresented: $isShowingOffer, 
            options: offerOptions
        )
    }
}
```

The initial value of `offerOptions` includes relevant tokens (affiliate and campaign tokens) that allow you to receive compensation for referring new Apple Music subscribers. For more information, see this presentation of the [Apple Services Performance Partners Program](https://affiliate.itunes.apple.com/resources/).

You may also set `isShowingOffer` to `false` to programmatically dismiss the subscription offer (or to abort its loading process).

## See Also

### Interacting with the App Store and Apple Music

- [appStoreOverlay(isPresented:configuration:)](<appstoreoverlay(ispresented_configuration_).md>) — Presents a StoreKit overlay when a given condition is true.
- [manageSubscriptionsSheet(isPresented:)](<managesubscriptionssheet(ispresented_).md>)
- [refundRequestSheet(for:isPresented:onDismiss:)](<refundrequestsheet(for_ispresented_ondismiss_).md>) — Display the refund request sheet for the given transaction.
- [offerCodeRedemption(options:isPresented:onCompletion:)](<offercoderedemption(options_ispresented_oncompletion_).md>) — Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect. _(beta)_
- [musicPicker(isPresented:title:selection:)](<musicpicker(ispresented_title_selection_).md>) — Presents a music picker to select items from the Apple Music catalog and the user’s music library. _(beta)_
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
