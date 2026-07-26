---
title: SubscriptionStorePicker
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorepicker
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorepicker'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorepicker.json'
content_hash: 'sha256:6692cd0f9bc4d35e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionStorePicker

<sub>Structure</sub>

A composite control with a picker for selecting a subscription option and a button for confirming the subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct SubscriptionStorePicker<PickerContent, ConfirmationContent> where PickerContent : View, ConfirmationContent : View
```

## Overview

When implementing custom subscription store control styles conforming to [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md), you can use this view to utilize the standard subscription picker as a component of the view you provide from [makeBody(configuration:)](<subscriptionstorecontrolstyle/makebody(configuration_).md>). The subscription picker is a composite control: it contains both a picker for choosing an option, and a button to subscribe to the selected option.

This control is the same as used in standard control styles such as [picker](subscriptionstorecontrolstyle/picker.md).

There are two primary ways to create a subscription picker:

- Provide the [SubscriptionStoreControlStyleConfiguration](subscriptionstorecontrolstyleconfiguration.md) value to the subscription picker, and use the components of each option to declare the option’s label.
- Provide a collection of views for the picker’s content, using a [SubscriptionStorePickerOption](subscriptionstorepickeroption.md) to declare the options.

Either way, you also need to declare a view to confirm the subscription after someone selects an option.

You can optionally provide a binding to a [Option](subscriptionstorecontrolstyleconfiguration/option.md) to observe selection changes, or programmatically change selections. If you don’t provide a binding, the subscription picker manages its own selection state.

> [!important] Important
> Use the `SubscriptionStorePicker` only in the view you return from the required [makeBody(configuration:)](<subscriptionstorecontrolstyle/makebody(configuration_).md>) method of [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md). Using `SubscriptionStorePicker` in other contexts is not supported.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a subscription store picker

- [init(pickerContent:confirmation:)](<subscriptionstorepicker/init(pickercontent_confirmation_).md>)
- [init(_:pickerOptionContent:confirmation:)](<subscriptionstorepicker/init(__pickeroptioncontent_confirmation_).md>)

### Managing a subscription picker’s selection state

- [init(selection:pickerContent:confirmation:)](<subscriptionstorepicker/init(selection_pickercontent_confirmation_).md>)
- [init(_:selection:pickerOptionContent:confirmation:)](<subscriptionstorepicker/init(__selection_pickeroptioncontent_confirmation_).md>)

## See Also

### Creating custom subscription store control styles

- [SubscriptionStoreButton](subscriptionstorebutton.md) — A button for subscribing to an in-app subscription with a localized label and optional caption.
- [SubscriptionStorePickerOption](subscriptionstorepickeroption.md) — A subscription option within a subscription picker control.
