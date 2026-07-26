---
title: 'init(_:isIncluded:marketingContent:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionoptiongroup/init(_:isincluded:marketingcontent:)-8vmdm'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionoptiongroup/init(_:isincluded:marketingcontent:)-8vmdm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionoptiongroup/init%28_%3Aisincluded%3Amarketingcontent%3A%29-8vmdm.json'
content_hash: 'sha256:fba9cc6a9d668878'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionOptionGroup](../subscriptionoptiongroup.md)

# init(_:isIncluded:marketingContent:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ label: LocalizedStringKey, isIncluded: @escaping (Product) -> Bool, @ViewBuilder marketingContent: () -> MarketingContent) where Content == Never
```

## See Also

### Creating subscription option groups

- [init(_:content:)](<init(__content_)-2nlpw.md>)
- [init(_:content:)](<init(__content_)-24grh.md>)
- [init(_:content:marketingContent:)](<init(__content_marketingcontent_)-9jybc.md>)
- [init(_:content:marketingContent:)](<init(__content_marketingcontent_)-550q0.md>)
- [init(_:isIncluded:)](<init(__isincluded_)-uhqa.md>)
- [init(_:isIncluded:)](<init(__isincluded_)-5f3ml.md>)
- [init(_:isIncluded:marketingContent:)](<init(__isincluded_marketingcontent_)-4d72a.md>)
- [init(content:)](<init(content_).md>)
- [init(content:label:)](<init(content_label_).md>)
- [init(content:label:marketingContent:)](<init(content_label_marketingcontent_).md>)
- [init(content:marketingContent:)](<init(content_marketingcontent_).md>)
- [init(isIncluded:)](<init(isincluded_).md>)
- [init(isIncluded:label:)](<init(isincluded_label_).md>)
- [init(isIncluded:label:marketingContent:)](<init(isincluded_label_marketingcontent_).md>)
- [init(isIncluded:marketingContent:)](<init(isincluded_marketingcontent_).md>)
