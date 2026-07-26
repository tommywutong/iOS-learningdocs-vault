---
title: SubscriptionStorePickerOption
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorepickeroption
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorepickeroption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorepickeroption.json'
content_hash: 'sha256:1b067aecc36bbe9f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionStorePickerOption

<sub>Structure</sub>

A subscription option within a subscription picker control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct SubscriptionStorePickerOption<Label> where Label : View
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a subscription picker option

- [init(_:)](<subscriptionstorepickeroption/init(__)-4cb3l.md>)
- [init(_:)](<subscriptionstorepickeroption/init(__)-3iu97.md>)
- [init(_:label:)](<subscriptionstorepickeroption/init(__label_).md>)

### Supporting types

- [AutomaticSubscriptionStorePickerOptionLabel](automaticsubscriptionstorepickeroptionlabel.md)

## See Also

### Creating custom subscription store control styles

- [SubscriptionStoreButton](subscriptionstorebutton.md) — A button for subscribing to an in-app subscription with a localized label and optional caption.
- [SubscriptionStorePicker](subscriptionstorepicker.md) — A composite control with a picker for selecting a subscription option and a button for confirming the subscription.
