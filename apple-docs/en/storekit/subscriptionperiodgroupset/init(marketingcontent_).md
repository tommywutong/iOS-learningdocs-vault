---
title: 'init(marketingContent:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionperiodgroupset/init(marketingcontent:)'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionperiodgroupset/init(marketingcontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionperiodgroupset/init%28marketingcontent%3A%29.json'
content_hash: 'sha256:535f5f193e7fe140'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionPeriodGroupSet](../subscriptionperiodgroupset.md)

# init(marketingContent:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(@ViewBuilder marketingContent: @escaping (Product.SubscriptionPeriod?) -> MarketingContent) where Label == AutomaticSubscriptionOptionGroupLabel
```

## See Also

### Creating subscription period group sets

- [init()](<init().md>)
- [init(marketingContent:label:)](<init(marketingcontent_label_).md>)
