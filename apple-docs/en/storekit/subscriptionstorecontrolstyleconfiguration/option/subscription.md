---
title: subscription
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscription
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscription.json'
content_hash: 'sha256:3257727324429ed2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../../subscriptionstorecontrolstyleconfiguration.md) · [Option](../option.md)

# subscription

<sub>Instance Property</sub>

The auto-renewable subscription to merchandise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var subscription: Product { get }
```

## Discussion

[Option](../option.md) is a dynamic member lookup type, which code refers to as `Option` when it’s a nested type. You don’t need to use the [subscription](subscription.md) property directly to access the properties of the [Product](../../product.md) value. Instead, access any properties of [Product](../../product.md) or [SubscriptionInfo](../../product/subscriptioninfo.md) directly on the `Option` value.

The following code example creates a button for each subscription option and displays its name. The [displayName](../../product/displayname.md) property is available on [Option](../option.md) to use as the button label.

```swift
struct DisplayNameButtonsControlStyle: SubscriptionStoreControlStyle {

    func makeBody(configuration: Configuration) -> some View {
        ForEach(configuration.options) { option in
            Button(option.displayName, action: option.subscribe)
        }
    }
}
```

> [!important] Important
> Use the [subscribe()](<subscribe().md>) method on the [Option](../option.md) value when a customer initiates a purchase. Don’t use [purchase(confirmIn:options:)](<../../product/purchase(confirmin_options_)-6dj6y.md>) or related purchase methods on this property for initiating a purchase.

## See Also

### Getting the subscription product and offer

- [id](id.md) — The product ID of the auto-renewable subscription.
- [activeOffer](activeoffer.md) — The subscription offer the customer is eligible for, and that applies to the subscription option.
