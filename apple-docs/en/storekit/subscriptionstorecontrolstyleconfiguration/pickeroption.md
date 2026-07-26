---
title: SubscriptionStoreControlStyleConfiguration.PickerOption
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption.json'
content_hash: 'sha256:8464ff7b6dda48ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../subscriptionstorecontrolstyleconfiguration.md)

# SubscriptionStoreControlStyleConfiguration.PickerOption

<sub>Structure</sub>

The properties of a picker option to use for selecting a subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup struct PickerOption
```

## Overview

You use `SubscriptionStoreControlStyleConfiguration.PickerOption` very similarly to [Option](option.md). The key differences are:

- The picker option represents a subscription option within the scope of an element of a picker control, where you can merchandise a standard option using any kind of control.
- Instead of getting an option from a [SubscriptionStoreControlStyleConfiguration](../subscriptionstorecontrolstyleconfiguration.md), you get a picker option when you create a [SubscriptionStorePicker](../subscriptionstorepicker.md).
- Instead of providing a [subscribe()](<option/subscribe().md>) method, the picker option provides an [isSelected](pickeroption/isselected.md) property to get the selection state.

The key difference is a `SubscriptionStoreControlStyleConfiguration.Option` provides a method to subscribe, and a `SubscriptionStoreControlStyleConfiguration.PickerOption` indicates the current selection state within a [SubscriptionStorePicker](../subscriptionstorepicker.md).

[PickerOption](pickeroption.md) is a dynamic member lookup type, so you don’t need to use [subscription](pickeroption/subscription.md) directly to access the properties of the `Product` value. Instead, access any properties of `Product` or [SubscriptionInfo](../product/subscriptioninfo.md) directly on the `PickerOption` value.

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Identifiable](../../swift/identifiable.md)

## Topics

### Getting properties of the subscription picker option

- [subscription](pickeroption/subscription.md) — The auto-renewable subscription that the picker option represents.
- [activeOffer](pickeroption/activeoffer.md)
- [isSelected](pickeroption/isselected.md) — A Boolean value that indicates whether the picker option is in a selected state.
- [icon](pickeroption/icon.md) — The subscription option’s icon.
- [id](pickeroption/id.md)

### Dynamic member lookup support

- [subscript(dynamicMember:)](<pickeroption/subscript(dynamicmember_)-2ahxy.md>) — Facilitates accessing optional subscription properties on a picker option value.
- [subscript(dynamicMember:)](<pickeroption/subscript(dynamicmember_)-4f3i1.md>) — Facilitates accessing subscription properties on a picker option value.
- [subscript(dynamicMember:)](<pickeroption/subscript(dynamicmember_)-8bsxh.md>) — Facilitates accessing product properties on a picker option value.

### Default Implementations

- [Identifiable Implementations](pickeroption/identifiable-implementations.md)

## See Also

### Getting subscription options to merchandise

- [options](options.md) — An array of subscription options for the subscription store view to merchandise.
- [sections](sections.md) — The subscription options to merchandise by sections.
- [Option](option.md) — Properties of an auto-renewable subscription option to merchandise.
- [Section](section.md) — The properties of a section of subscription options within a subscription store control.
- [Icon](icon.md) — A type-erased icon of a subscription option.
