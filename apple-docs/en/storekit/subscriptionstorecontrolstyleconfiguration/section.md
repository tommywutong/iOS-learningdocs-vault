---
title: SubscriptionStoreControlStyleConfiguration.Section
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/section
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/section'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/section.json'
content_hash: 'sha256:7261fc953e8ba8d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../subscriptionstorecontrolstyleconfiguration.md)

# SubscriptionStoreControlStyleConfiguration.Section

<sub>Structure</sub>

The properties of a section of subscription options within a subscription store control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Section
```

## Overview

Each value represents an instance of [SubscriptionOptionSection](../subscriptionoptionsection.md) when the system creates a [SubscriptionStoreView](../subscriptionstoreview.md).

Even if a subscription store instance doesn’t declare sections using [SubscriptionOptionSection](../subscriptionoptionsection.md), the instance always has at least one implicit section that contains the options within the group. Implicit sections have `nil` for the [header](section/header-swift.property.md) and [footer](section/footer-swift.property.md) accessory views.

## Relationships

- **Conforms To**: [Identifiable](../../swift/identifiable.md)

## Topics

### Getting a section’s content

- [options](section/options.md) — The subscription options to merchandise within a section.

### Getting accessory views

- [header](section/header-swift.property.md) — A decorative header view for a section that displays before the options.
- [footer](section/footer-swift.property.md) — A decorative footer view for a section that displays after the options.
- [Header](section/header-swift.struct.md) — A type-erased header of a section of subscription options.
- [Footer](section/footer-swift.struct.md) — A type-erased footer of a section of subscription options.

### Identifying a section

- [ID](section/id.md) — The stable identity of a section of subscription options.

## See Also

### Getting subscription options to merchandise

- [options](options.md) — An array of subscription options for the subscription store view to merchandise.
- [sections](sections.md) — The subscription options to merchandise by sections.
- [Option](option.md) — Properties of an auto-renewable subscription option to merchandise.
- [PickerOption](pickeroption.md) — The properties of a picker option to use for selecting a subscription.
- [Icon](icon.md) — A type-erased icon of a subscription option.
