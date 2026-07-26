---
title: SubscriptionStoreControlStyleConfiguration.Option
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/option
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option.json'
content_hash: 'sha256:601fac674d9f12db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../subscriptionstorecontrolstyleconfiguration.md)

# SubscriptionStoreControlStyleConfiguration.Option

<sub>Structure</sub>

Properties of an auto-renewable subscription option to merchandise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup struct Option
```

## Overview

You use `SubscriptionStoreControlStyleConfiguration.Option` very similarly to [Product](../product.md) values, with some important differences:

- The `offer` property indicates the offer that applies to the purchase. Display the terms of the `offer`, and ignore offer properties on [SubscriptionInfo](../product/subscriptioninfo.md), such as [introductoryOffer](../product/subscriptioninfo/introductoryoffer.md).
- If the `offer` is `nil`, no offer applies to the purchase.
- Call the [subscribe()](<option/subscribe().md>) method when a customer activates a control to subscribe to a subscription option, instead of methods on [Product](../product.md), such as [purchase(confirmIn:options:)](<../product/purchase(confirmin_options_)-6dj6y.md>).
- Access the decorative icon using the [icon](option/icon.md) property.

`SubscriptionStoreControlStyleConfiguration.Option` is a dynamic member lookup type, so you don’t need to use [subscription](option/subscription.md) directly to access the properties of the `Product` value. Instead, access the properties of `Product` or [SubscriptionInfo](../product/subscriptioninfo.md) directly on the `Option` value. In the example below, the [displayName](../product/displayname.md) property is available on `Option` to use as the button label:

```swift
struct DisplayNameButtonsControlStyle: SubscriptionStoreControlStyle {

    func makeBody(configuration: Configuration) -> some View {
        ForEach(configuration.options) { option in
            Button(option.displayName, action: option.subscribe)
        }
    }
}
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Identifiable](../../swift/identifiable.md)

## Topics

### Getting the subscription product and offer

- [subscription](option/subscription.md) — The auto-renewable subscription to merchandise.
- [id](option/id.md) — The product ID of the auto-renewable subscription.
- [activeOffer](option/activeoffer.md) — The subscription offer the customer is eligible for, and that applies to the subscription option.

### Getting the icon

- [icon](option/icon.md) — The subscription option’s icon.

### Purchasing a subscription option

- [subscribe()](<option/subscribe().md>) — Initiates a purchase when a customer activates a control to subscribe to the option.

### Looking up dynamic members

- [subscript(dynamicMember:)](<option/subscript(dynamicmember_)-8sl2m.md>) — Facilitates accessing optional subscription properties on an option value.
- [subscript(dynamicMember:)](<option/subscript(dynamicmember_)-wjww.md>) — Facilitates accessing subscription properties on an option value.
- [subscript(dynamicMember:)](<option/subscript(dynamicmember_)-9g2sm.md>) — Facilitates accessing product properties on an option value.

### Default Implementations

- [Identifiable Implementations](option/identifiable-implementations.md)

## See Also

### Getting subscription options to merchandise

- [options](options.md) — An array of subscription options for the subscription store view to merchandise.
- [sections](sections.md) — The subscription options to merchandise by sections.
- [PickerOption](pickeroption.md) — The properties of a picker option to use for selecting a subscription.
- [Section](section.md) — The properties of a section of subscription options within a subscription store control.
- [Icon](icon.md) — A type-erased icon of a subscription option.
