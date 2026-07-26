---
title: 'callAsFunction(_:compactJWS:options:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/purchaseaction/callasfunction(_:compactjws:options:)'
source_url: 'https://developer.apple.com/documentation/storekit/purchaseaction/callasfunction(_:compactjws:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/purchaseaction/callasfunction%28_%3Acompactjws%3Aoptions%3A%29.json'
content_hash: 'sha256:1f2f45c2d747769d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [PurchaseAction](../purchaseaction.md)

# callAsFunction(_:compactJWS:options:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction(_ advancedCommerceProduct: AdvancedCommerceProduct, compactJWS: String, options: Set<AdvancedCommerceProduct.PurchaseOption> = []) async throws -> AdvancedCommerceProduct.PurchaseResult
```
