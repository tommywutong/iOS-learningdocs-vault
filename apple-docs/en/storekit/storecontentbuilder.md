---
title: StoreContentBuilder
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/storecontentbuilder
source_url: 'https://developer.apple.com/documentation/storekit/storecontentbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storecontentbuilder.json'
content_hash: 'sha256:33cbe7822f6b4d32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# StoreContentBuilder

<sub>Structure</sub>

A result builder that creates store content from closures that you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct StoreContentBuilder
```

## Topics

### Building store content

- [buildBlock(_:)](<storecontentbuilder/buildblock(__).md>)
- [buildEither(first:)](<storecontentbuilder/buildeither(first_).md>)
- [buildEither(second:)](<storecontentbuilder/buildeither(second_).md>)
- [buildExpression(_:)](<storecontentbuilder/buildexpression(__).md>)
- [buildIf(_:)](<storecontentbuilder/buildif(__).md>)
- [buildLimitedAvailability(_:)](<storecontentbuilder/buildlimitedavailability(__).md>)
- [TupleStoreContent](tuplestorecontent.md)

## See Also

### Declaring the structure of a subscription store

- [SubscriptionOptionGroup](subscriptionoptiongroup.md) — A group of subscription options that includes optional views for labels and marketing content.
- [SubscriptionOptionGroupSet](subscriptionoptiongroupset.md) — A set of groups of subscription options that include optional views for labels and marketing content.
- [SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [SubscriptionOptionSection](subscriptionoptionsection.md)
- [StoreContent](storecontent.md) — A type that represents the content of a store.
