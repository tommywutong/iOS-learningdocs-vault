---
title: SubscriptionOptionSection
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionoptionsection
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionoptionsection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionoptionsection.json'
content_hash: 'sha256:33cad45bc37ac756'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionOptionSection

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct SubscriptionOptionSection<Header, Content, Footer> where Header : View, Content : StoreContent, Footer : View
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [StoreContent](storecontent.md)

## Topics

### Creating subscription option sections

- [init(_:isIncluded:footer:)](<subscriptionoptionsection/init(__isincluded_footer_)-17lo3.md>)
- [init(_:isIncluded:footer:)](<subscriptionoptionsection/init(__isincluded_footer_)-36k79.md>)
- [init(isIncluded:header:footer:)](<subscriptionoptionsection/init(isincluded_header_footer_).md>)

### Choosing a subscription option group style

- [subscriptionStoreOptionGroupStyle(_:)](<../swiftui/view/subscriptionstoreoptiongroupstyle(__).md>) — Sets the style subscription store views within this view use to display groups of subscription options.

## See Also

### Declaring the structure of a subscription store

- [SubscriptionOptionGroup](subscriptionoptiongroup.md) — A group of subscription options that includes optional views for labels and marketing content.
- [SubscriptionOptionGroupSet](subscriptionoptiongroupset.md) — A set of groups of subscription options that include optional views for labels and marketing content.
- [SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [StoreContent](storecontent.md) — A type that represents the content of a store.
- [StoreContentBuilder](storecontentbuilder.md) — A result builder that creates store content from closures that you provide.
