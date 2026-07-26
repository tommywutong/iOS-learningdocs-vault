---
title: options
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/options
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/options.json'
content_hash: 'sha256:68dcefd60e44795b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../subscriptionstorecontrolstyleconfiguration.md)

# options

<sub>Instance Property</sub>

An array of subscription options for the subscription store view to merchandise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var options: [SubscriptionStoreControlStyleConfiguration.Option] { get }
```

## Discussion

The [options](options.md) property is an array that contains the main content of your subscription store control style, including the auto-renewable subscription products. Use the properties of each [options](options.md) value to declare your control style. Provide a control that enables the customer to subscribe to each option in the array. Call the [subscribe()](<option/subscribe().md>) method when the customer activates a control to subscribe.

Display only the subscription options that appear in the [options](options.md) array. Use the [allOptions](alloptions.md) property to access information about all the options, for example, to compute comparisons between subscription options.

To hide and sort subscription options, use the initializer of the [SubscriptionStoreView](../subscriptionstoreview.md). The [options](options.md) array maintains the sort order, and includes only the options you provide to the subscription store view’s initializer. For example, the following code initializes the subscription store to contain only the subscription options that upgrade the customer’s current subscription:

```swift
SubscriptionStoreView(groupID: "SAMPLE", visibleRelationships: .upgrade)
```

If you configure a subscription store view to show the current auto-renewal preference, the [options](options.md) array contains the [autoRenewPreference](autorenewpreference.md) subscription product. There’s no need to specifically display the [autoRenewPreference](autorenewpreference.md) product in that case.

> [!note] Note
> A subscription store control style needs only one of the properties, [options](options.md) or [sections](sections.md). Use [options](options.md) if your style doesn’t support sections.

If you declare a subscription store view using [SubscriptionOptionSection](../subscriptionoptionsection.md) instances, this property flattens the section structure and ignores any header or footer views.

## See Also

### Getting subscription options to merchandise

- [sections](sections.md) — The subscription options to merchandise by sections.
- [Option](option.md) — Properties of an auto-renewable subscription option to merchandise.
- [PickerOption](pickeroption.md) — The properties of a picker option to use for selecting a subscription.
- [Section](section.md) — The properties of a section of subscription options within a subscription store control.
- [Icon](icon.md) — A type-erased icon of a subscription option.
