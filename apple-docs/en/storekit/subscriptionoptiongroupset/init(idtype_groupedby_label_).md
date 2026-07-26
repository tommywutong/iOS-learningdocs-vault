---
title: 'init(idType:groupedBy:label:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionoptiongroupset/init(idtype:groupedby:label:)'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionoptiongroupset/init(idtype:groupedby:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionoptiongroupset/init%28idtype%3Agroupedby%3Alabel%3A%29.json'
content_hash: 'sha256:71ac57c209d6f583'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionOptionGroupSet](../subscriptionoptiongroupset.md)

# init(idType:groupedBy:label:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(idType: GroupID.Type = GroupID.self, groupedBy transform: @escaping (Product) -> GroupID, @ViewBuilder label: @escaping (GroupID) -> Label) where MarketingContent == AutomaticSubscriptionStoreMarketingContent
```

## See Also

### Creating subscription option group sets

- [init(idType:groupedBy:label:marketingContent:)](<init(idtype_groupedby_label_marketingcontent_).md>)
