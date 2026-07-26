---
title: SubscriptionOptionGroupSet
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionoptiongroupset
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionoptiongroupset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionoptiongroupset.json'
content_hash: 'sha256:45b8e7562282c4d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionOptionGroupSet

<sub>Structure</sub>

A set of groups of subscription options that include optional views for labels and marketing content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct SubscriptionOptionGroupSet<GroupID, Label, MarketingContent> where GroupID : Hashable, Label : View, MarketingContent : View
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [StoreContent](storecontent.md)

## Topics

### Creating subscription option group sets

- [init(idType:groupedBy:label:)](<subscriptionoptiongroupset/init(idtype_groupedby_label_).md>)
- [init(idType:groupedBy:label:marketingContent:)](<subscriptionoptiongroupset/init(idtype_groupedby_label_marketingcontent_).md>)

### Creating the group style

- [subscriptionStoreOptionGroupStyle(_:)](<../swiftui/view/subscriptionstoreoptiongroupstyle(__).md>) — Sets the style subscription store views within this view use to display groups of subscription options.

## See Also

### Declaring the structure of a subscription store

- [SubscriptionOptionGroup](subscriptionoptiongroup.md) — A group of subscription options that includes optional views for labels and marketing content.
- [SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [SubscriptionOptionSection](subscriptionoptionsection.md)
- [StoreContent](storecontent.md) — A type that represents the content of a store.
- [StoreContentBuilder](storecontentbuilder.md) — A result builder that creates store content from closures that you provide.
