---
title: SubscriptionStoreControlStyle
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyle
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyle.json'
content_hash: 'sha256:6e98baa45e166e08'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionStoreControlStyle

<sub>Protocol</sub>

A type that specifies the appearance and interaction of controls in the subscription store view instances within the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol SubscriptionStoreControlStyle
```

## Overview

Use the [subscriptionStoreControlStyle(_:)](<../swiftui/view/subscriptionstorecontrolstyle(__).md>) view modifier to configure the subscription store control style for a view hierarchy.

```swift
SubscriptionStoreView(groupID: "SAMPLE")
    .subscriptionStoreControlStyle(.prominentPicker)
```

You can also configure the control placement using the [subscriptionStoreControlStyle(_:placement:)](<../swiftui/view/subscriptionstorecontrolstyle(__placement_).md>) view modifier.

### Create custom styles

To create a custom style, declare a type that conforms to the `SubscriptionStoreControlStyle` protocol and implement the required [makeBody(configuration:)](<subscriptionstorecontrolstyle/makebody(configuration_).md>) method. For example, you can define a style that adds price comparison captions to buttons.

```swift
struct PriceComparisonButtonsSubscriptionStoreControlStyle: SubscriptionStoreControlStyle {

    func makeBody(configuration: Configuration) -> some View {
        // Return a view displaying a captioned button for each option.
    }
}
```

Inside the method, use the `configuration` parameter, which is a [SubscriptionStoreControlStyleConfiguration](subscriptionstorecontrolstyleconfiguration.md) value, to get the properties of the control, such as the subscriptions to merchandise. For examples that show constructing a view from the configuration value, see [makeBody(configuration:)](<subscriptionstorecontrolstyle/makebody(configuration_).md>).

The subscription store control style protocol has a [Placement](subscriptionstorecontrolstyle/placement.md) associated type, which represents the placements that the style supports. To optionally restrict the placements your custom style supports, explicitly declare a type alias named `Placement`. For more information about restricting placements, see [SubscriptionStoreControlPlacement](subscriptionstorecontrolplacement.md). If you don’t declare the type alias, your custom style automatically uses the [AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement.md) as its [Placement](subscriptionstorecontrolstyle/placement.md) associated type.

The following code example declares a `Placement` type alias:

```swift
struct PriceComparisonButtonsSubscriptionStoreControlStyle: SubscriptionStoreControlStyle {

    // Support the same placements as the standard buttons style.
    typealias Placement = ButtonsSubscriptionStoreControlStyle.Placement

    func makeBody(configuration: Configuration) -> some View {
        // Return a view displaying a captioned button for each option.
    }
}
```

To provide easy access to the new style, declare a corresponding static variable in an extension to `SubscriptionStoreControlStyle`.

```swift
extension SubscriptionStoreControlStyle where Self == 
PriceComparisonButtonsSubscriptionStoreControlStyle {
    static var priceComparisonButtons: Self { Self() }
}
```

Then, use your custom style as follows:

```swift
SubscriptionStoreView(groupID: "SAMPLE")
    .subscriptionStoreControlStyle(.priceComparisonButtons)
```

## Relationships

- **Conforming Types**: [AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md), [ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md), [CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md), [PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md), [PagedProminentPickerSubscriptionStoreControlStyle](pagedprominentpickersubscriptionstorecontrolstyle.md), [PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md), [ProminentPickerSubscriptionStoreControlStyle](prominentpickersubscriptionstorecontrolstyle.md)

## Topics

### Getting built-in subscription store control styles

- [automatic](subscriptionstorecontrolstyle/automatic.md) — A subscription store control style that resolves its appearance automatically, based on the current context.
- [buttons](subscriptionstorecontrolstyle/buttons.md) — A subscription store control style that displays a subscribe button for each subscription plan.
- [picker](subscriptionstorecontrolstyle/picker.md) — A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [prominentPicker](subscriptionstorecontrolstyle/prominentpicker.md) — A subscription store control style that displays subscription plans as a prominent picker control, with a single button to subscribe.
- [pagedPicker](subscriptionstorecontrolstyle/pagedpicker.md) — A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
- [pagedProminentPicker](subscriptionstorecontrolstyle/pagedprominentpicker.md) — A subscription store control style that displays subscription plans as a prominent paged picker control, with a single button to subscribe.
- [compactPicker](subscriptionstorecontrolstyle/compactpicker.md) — A subscription store control style that displays subscription plans as a compact control, with a single button to subscribe.

### Creating custom subscription store control styles

- [makeBody(configuration:)](<subscriptionstorecontrolstyle/makebody(configuration_).md>) — Creates a view that represents the body of a subscription store control.
- [Configuration](subscriptionstorecontrolstyle/configuration.md) — The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.
- [SubscribeButton](subscriptionstorecontrolstyle/subscribebutton.md) — A button for subscribing to an in-app subscription.
- [SubscriptionPicker](subscriptionstorecontrolstyle/subscriptionpicker.md) — A composite control for selecting a subscription option and confirming the subscription.
- [SubscriptionPickerOption](subscriptionstorecontrolstyle/subscriptionpickeroption.md) — A subscription option within a subscription picker control.
- [SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey.md) — A placement for a subscription store control in a store view.
- [Placement](subscriptionstorecontrolstyle/placement.md) — The placement of subscription controls in a subscription store.
- [Body](subscriptionstorecontrolstyle/body.md) — A view that represents the body of a subscription store control.

### Supporting types

- [AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md) — The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md) — A subscription store control style that displays a subscribe button for each subscription plan.
- [PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [ProminentPickerSubscriptionStoreControlStyle](prominentpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a prominent picker control, with a single button to subscribe.
- [CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
- [PagedProminentPickerSubscriptionStoreControlStyle](pagedprominentpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a paged prominent picker control, with a single button to subscribe.
- [AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement.md) — A system-defined placement for a subscription store view.

## See Also

### Styling subscription store controls

- [subscriptionStoreControlStyle(_:)](<../swiftui/view/subscriptionstorecontrolstyle(__).md>) — Sets the control style for subscription store views within a view.
- [subscriptionStoreControlStyle(_:placement:)](<../swiftui/view/subscriptionstorecontrolstyle(__placement_).md>) — Sets the control style and control placement for subscription store views within a view.
- [SubscriptionStoreControlStyleConfiguration](subscriptionstorecontrolstyleconfiguration.md) — The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.
- [SubscriptionStoreControlPlacement](subscriptionstorecontrolplacement.md) — A type that specifies the placement of a subscription control in a subscription store view.
