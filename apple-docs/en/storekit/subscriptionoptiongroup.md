---
title: SubscriptionOptionGroup
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionoptiongroup
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionoptiongroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionoptiongroup.json'
content_hash: 'sha256:333252a624a77531'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionOptionGroup

<sub>Structure</sub>

A group of subscription options that includes optional views for labels and marketing content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct SubscriptionOptionGroup<Content, Label, MarketingContent> where Content : StoreContent, Label : View, MarketingContent : View
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [StoreContent](storecontent.md)

## Topics

### Creating subscription option groups

- [init(_:content:)](<subscriptionoptiongroup/init(__content_)-2nlpw.md>)
- [init(_:content:)](<subscriptionoptiongroup/init(__content_)-24grh.md>)
- [init(_:content:marketingContent:)](<subscriptionoptiongroup/init(__content_marketingcontent_)-9jybc.md>)
- [init(_:content:marketingContent:)](<subscriptionoptiongroup/init(__content_marketingcontent_)-550q0.md>)
- [init(_:isIncluded:)](<subscriptionoptiongroup/init(__isincluded_)-uhqa.md>)
- [init(_:isIncluded:)](<subscriptionoptiongroup/init(__isincluded_)-5f3ml.md>)
- [init(_:isIncluded:marketingContent:)](<subscriptionoptiongroup/init(__isincluded_marketingcontent_)-8vmdm.md>)
- [init(_:isIncluded:marketingContent:)](<subscriptionoptiongroup/init(__isincluded_marketingcontent_)-4d72a.md>)
- [init(content:)](<subscriptionoptiongroup/init(content_).md>)
- [init(content:label:)](<subscriptionoptiongroup/init(content_label_).md>)
- [init(content:label:marketingContent:)](<subscriptionoptiongroup/init(content_label_marketingcontent_).md>)
- [init(content:marketingContent:)](<subscriptionoptiongroup/init(content_marketingcontent_).md>)
- [init(isIncluded:)](<subscriptionoptiongroup/init(isincluded_).md>)
- [init(isIncluded:label:)](<subscriptionoptiongroup/init(isincluded_label_).md>)
- [init(isIncluded:label:marketingContent:)](<subscriptionoptiongroup/init(isincluded_label_marketingcontent_).md>)
- [init(isIncluded:marketingContent:)](<subscriptionoptiongroup/init(isincluded_marketingcontent_).md>)

### Supporting types

- [AutomaticSubscriptionOptionGroupLabel](automaticsubscriptionoptiongrouplabel.md)

## See Also

### Declaring the structure of a subscription store

- [SubscriptionOptionGroupSet](subscriptionoptiongroupset.md) — A set of groups of subscription options that include optional views for labels and marketing content.
- [SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [SubscriptionOptionSection](subscriptionoptionsection.md)
- [StoreContent](storecontent.md) — A type that represents the content of a store.
- [StoreContentBuilder](storecontentbuilder.md) — A result builder that creates store content from closures that you provide.
