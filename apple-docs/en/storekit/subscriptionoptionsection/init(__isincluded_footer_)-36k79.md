---
title: 'init(_:isIncluded:footer:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionoptionsection/init(_:isincluded:footer:)-36k79'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionoptionsection/init(_:isincluded:footer:)-36k79'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionoptionsection/init%28_%3Aisincluded%3Afooter%3A%29-36k79.json'
content_hash: 'sha256:61d6c63ad15c96e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionOptionSection](../subscriptionoptionsection.md)

# init(_:isIncluded:footer:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ title: some StringProtocol, isIncluded: @escaping (Product) -> Bool, @ViewBuilder footer: () -> Footer = EmptyView.init)
```

## See Also

### Creating subscription option sections

- [init(_:isIncluded:footer:)](<init(__isincluded_footer_)-17lo3.md>)
- [init(isIncluded:header:footer:)](<init(isincluded_header_footer_).md>)
