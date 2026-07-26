---
title: StoreContent
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/storecontent
source_url: 'https://developer.apple.com/documentation/storekit/storecontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storecontent.json'
content_hash: 'sha256:ad23630ef95158e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# StoreContent

<sub>Protocol</sub>

A type that represents the content of a store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol StoreContent
```

## Relationships

- **Conforming Types**: [SubscriptionOptionGroup](subscriptionoptiongroup.md), [SubscriptionOptionGroupSet](subscriptionoptiongroupset.md), [SubscriptionOptionSection](subscriptionoptionsection.md), [SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md), [TupleStoreContent](tuplestorecontent.md)

## Topics

### Implementing store content

- [body](storecontent/body-swift.property.md)
- [Body](storecontent/body-swift.associatedtype.md)

### Configuring store content

- [subscriptionStoreOptionGroupStyle(_:)](<storecontent/subscriptionstoreoptiongroupstyle(__).md>)
- [subscriptionStoreButtonLabel(_:)](<storecontent/subscriptionstorebuttonlabel(__).md>)
- [storeButton(_:for:)](<storecontent/storebutton(__for_).md>)
- [subscriptionStoreControlStyle(_:placement:)](<storecontent/subscriptionstorecontrolstyle(__placement_).md>)
- [productDescription(_:)](<storecontent/productdescription(__).md>)

### Configuring backgrounds

- [subscriptionStoreControlBackground(_:)](<storecontent/subscriptionstorecontrolbackground(__)-10hv8.md>)
- [subscriptionStoreControlBackground(_:)](<storecontent/subscriptionstorecontrolbackground(__)-3xzai.md>)
- [subscriptionStorePickerItemBackground(_:)](<storecontent/subscriptionstorepickeritembackground(__).md>)
- [subscriptionStorePickerItemBackground(_:in:)](<storecontent/subscriptionstorepickeritembackground(__in_).md>)

### Supporting types

- [IdentifiedStoreContent](identifiedstorecontent.md) — The type of SwiftUI view that StoreKit transforms store content into.

## See Also

### Declaring the structure of a subscription store

- [SubscriptionOptionGroup](subscriptionoptiongroup.md) — A group of subscription options that includes optional views for labels and marketing content.
- [SubscriptionOptionGroupSet](subscriptionoptiongroupset.md) — A set of groups of subscription options that include optional views for labels and marketing content.
- [SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [SubscriptionOptionSection](subscriptionoptionsection.md)
- [StoreContentBuilder](storecontentbuilder.md) — A result builder that creates store content from closures that you provide.
