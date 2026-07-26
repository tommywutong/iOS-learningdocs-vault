---
title: PurchaseAction
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/purchaseaction
source_url: 'https://developer.apple.com/documentation/storekit/purchaseaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/purchaseaction.json'
content_hash: 'sha256:a865dc7f2edeb322'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# PurchaseAction

<sub>Structure</sub>

An action that starts an In-App Purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct PurchaseAction
```

## Overview

StoreKit provides several APIs you can use to enable customers to initiate a purchase. Choose the API that suits your app’s implementation, specifically:

- Use `PurchaseAction` for apps that use [SwiftUI](../swiftui.md), including multi-scene apps for visionOS.
- Use [purchase(confirmIn:options:)](<product/purchase(confirmin_options_)-3bivf.md>) for apps that use [UIKit](../uikit.md).
- Use [purchase(options:)](<product/purchase(options_).md>) if your app runs on watchOS or macOS.

> [!important] Important
> If you use StoreKit views such as [ProductView](productview.md), [StoreView](storeview.md), or [SubscriptionStoreView](subscriptionstoreview.md) you don’t need to call any other API to initiate a purchase. StoreKit manages the purchase action automatically, including presenting the purchase confirmation UI. For more information, see [StoreKit views](storekit-views.md).

### Use the purchase action API

Use `PurchaseAction` instead of [purchase(options:)](<product/purchase(options_).md>) for SwiftUI implementations, including multi-scene apps for visionOS. Call the instance to start an in-app purchase.

To use this API, read the `PurchaseAction` environment value to get an instance of the structure for a given [Environment](../swiftui/environment.md). You call the instance directly because it defines a [callAsFunction(_:options:)](<purchaseaction/callasfunction(__options_).md>) method that Swift calls when you call the instance.

When you initiate an in-app purchase, the system presents UI for the customer to confirm the purchase details. The purchase action you get from the environment automatically includes the UI context. It presents the confirmation UI in proximity to the scene in which the view displays.

The following code shows an example of starting an in-app purchase when a person taps a button:

```swift
struct PurchaseExample: View {
    @Environment(\.purchase) private var purchase: PurchaseAction
    let product: Product
    let purchaseOptions: [Product.PurchaseOption]

    var body: some View {
        Button {
            Task {
                let purchaseResult = try? await purchase(product, options: purchaseOptions)
                 // Process the purchase result.
            }
        } label: {
            Text(product.displayName)
        }
    }
}
```

Note that the second line in the code example can omit the type name, as follows, because the compiler can infer the type:

```swift
@Environment(\.purchase) private var purchase
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Calling the action

- [callAsFunction(_:options:)](<purchaseaction/callasfunction(__options_).md>) — Starts an in-app purchase for the indicated product and purchase options.

### Instance Methods

- [callAsFunction(_:compactJWS:options:)](<purchaseaction/callasfunction(__compactjws_options_).md>)

## See Also

### Purchase requests and results

- [purchase(options:)](<product/purchase(options_).md>) — Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [PurchaseResult](product/purchaseresult.md) — The result of a purchase.
