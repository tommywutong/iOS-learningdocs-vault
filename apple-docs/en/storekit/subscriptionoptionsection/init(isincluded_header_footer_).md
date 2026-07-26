---
title: 'init(isIncluded:header:footer:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionoptionsection/init(isincluded:header:footer:)'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionoptionsection/init(isincluded:header:footer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionoptionsection/init%28isincluded%3Aheader%3Afooter%3A%29.json'
content_hash: 'sha256:e40a97df5ecf8d87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionOptionSection](../subscriptionoptionsection.md)

# init(isIncluded:header:footer:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(isIncluded: @escaping (Product) -> Bool, @ViewBuilder header: () -> Header = EmptyView.init, @ViewBuilder footer: () -> Footer = EmptyView.init)
```

## See Also

### Creating subscription option sections

- [init(_:isIncluded:footer:)](<init(__isincluded_footer_)-17lo3.md>)
- [init(_:isIncluded:footer:)](<init(__isincluded_footer_)-36k79.md>)
