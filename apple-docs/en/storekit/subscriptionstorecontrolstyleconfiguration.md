---
title: SubscriptionStoreControlStyleConfiguration
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration.json'
content_hash: 'sha256:ed222a408ba41999'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionStoreControlStyleConfiguration

<sub>Structure</sub>

The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SubscriptionStoreControlStyleConfiguration
```

## Overview

When you define a custom subscription store control style by creating a type that conforms to the [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md) protocol, you implement the [makeBody(configuration:)](<subscriptionstorecontrolstyle/makebody(configuration_).md>) method. That method takes a `SubscriptionStoreControlStyleConfiguration` parameter, which has the information necessary to define the behavior and interactions of a subscription store view’s primary controls.

Decide whether your style supports dividing options into sections.

- If you support sections, use the [sections](subscriptionstorecontrolstyleconfiguration/sections.md) property to preserve the structure and accessory views you declare using [SubscriptionOptionSection](subscriptionoptionsection.md) instances.
- If you don’t support sections, use the [options](subscriptionstorecontrolstyleconfiguration/options.md) property to have a flattened array of the [Option](subscriptionstorecontrolstyleconfiguration/option.md) values to merchandise.

Provide a control that enables customers to subscribe to each option in either the `options` or `sections` properties.

To hide and sort the subscription options that your view displays, use the initializer of the [SubscriptionStoreView](subscriptionstoreview.md). For example, you can initialize the subscription store to contain only the subscription options that upgrade the customer’s current subscription.

Display only the subscription options that appear in either the `options` or `sections` properties. For example, declaring [SubscriptionOptionGroup](subscriptionoptiongroup.md) instances can hide certain subscription options from a control. To access information about other subscription options, use the [allOptions](subscriptionstorecontrolstyleconfiguration/alloptions.md) property.

In cases where a customer is actively subscribed, use [autoRenewPreference](subscriptionstorecontrolstyleconfiguration/autorenewpreference.md) to get the [Product](product.md) value of the subscription product that renews at the next billing.

## Topics

### Getting subscription options to merchandise

- [options](subscriptionstorecontrolstyleconfiguration/options.md) — An array of subscription options for the subscription store view to merchandise.
- [sections](subscriptionstorecontrolstyleconfiguration/sections.md) — The subscription options to merchandise by sections.
- [Option](subscriptionstorecontrolstyleconfiguration/option.md) — Properties of an auto-renewable subscription option to merchandise.
- [PickerOption](subscriptionstorecontrolstyleconfiguration/pickeroption.md) — The properties of a picker option to use for selecting a subscription.
- [Section](subscriptionstorecontrolstyleconfiguration/section.md) — The properties of a section of subscription options within a subscription store control.
- [Icon](subscriptionstorecontrolstyleconfiguration/icon.md) — A type-erased icon of a subscription option.

### Getting subscription group properties

- [groupDisplayName](subscriptionstorecontrolstyleconfiguration/groupdisplayname.md) — The localized display name of the subscription group that the subscription store view merchandises.
- [autoRenewPreference](subscriptionstorecontrolstyleconfiguration/autorenewpreference.md) — The auto-renewable subscripton product that renews at the next billing cycle.
- [allOptions](subscriptionstorecontrolstyleconfiguration/alloptions.md) — All subscription options in the subscription group.

### Getting subscription description visibility

- [descriptionVisibility](subscriptionstorecontrolstyleconfiguration/descriptionvisibility.md) — The visibility of product descriptions.

## See Also

### Styling subscription store controls

- [subscriptionStoreControlStyle(_:)](<../swiftui/view/subscriptionstorecontrolstyle(__).md>) — Sets the control style for subscription store views within a view.
- [subscriptionStoreControlStyle(_:placement:)](<../swiftui/view/subscriptionstorecontrolstyle(__placement_).md>) — Sets the control style and control placement for subscription store views within a view.
- [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md) — A type that specifies the appearance and interaction of controls in the subscription store view instances within the view hierarchy.
- [SubscriptionStoreControlPlacement](subscriptionstorecontrolplacement.md) — A type that specifies the placement of a subscription control in a subscription store view.
