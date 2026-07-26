---
title: sections
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/sections
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/sections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/sections.json'
content_hash: 'sha256:d3198bd52595e16e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../subscriptionstorecontrolstyleconfiguration.md)

# sections

<sub>Instance Property</sub>

The subscription options to merchandise by sections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sections: [SubscriptionStoreControlStyleConfiguration.Section] { get }
```

## Discussion

The [sections](sections.md) property represents the main content of your subscription store control style, including the auto-renewable subscription products.

Each [Section](section.md) element contains an array of [Option](option.md) values named [options](section/options.md). Use this structure to modify the appearance of a control depending on the section it belongs to.

The elements of [sections](sections.md) represent [SubscriptionOptionSection](../subscriptionoptionsection.md) instances. A minimal store has one implicit section, with the [sections](sections.md) property containing a single element. The single element’s [header](section/header-swift.property.md) and [footer](section/footer-swift.property.md) properties are both `nil`, and its [options](section/options.md) property is identical to the [options](options.md) property on [SubscriptionStoreControlStyleConfiguration](../subscriptionstorecontrolstyleconfiguration.md).

> [!note] Note
> Typically, a style needs only one of the properties: [options](options.md) or [sections](sections.md). Use the [sections](sections.md) property if your style supports sections.

Use the initializer of the [SubscriptionStoreView](../subscriptionstoreview.md) to determine the contents of the [sections](sections.md) array.

Display only the subscription options that appear in the [sections](sections.md) array. Use the [allOptions](alloptions.md) property to access information about all the options, for example, to compute comparisons between subscription options. The view your style creates needs to provide a control that enables the customer to subscribe to each option in the array.

If you configure a subscription store view to show the current auto-renewal preference, the [sections](sections.md) array contains the [autoRenewPreference](autorenewpreference.md) subscription product. There’s no need to specifically display the [autoRenewPreference](autorenewpreference.md) product in that case.

## See Also

### Getting subscription options to merchandise

- [options](options.md) — An array of subscription options for the subscription store view to merchandise.
- [Option](option.md) — Properties of an auto-renewable subscription option to merchandise.
- [PickerOption](pickeroption.md) — The properties of a picker option to use for selecting a subscription.
- [Section](section.md) — The properties of a section of subscription options within a subscription store control.
- [Icon](icon.md) — A type-erased icon of a subscription option.
