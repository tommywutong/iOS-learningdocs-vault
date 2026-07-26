---
title: 'presentMerchandising(_:from:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, tvOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/appstore/presentmerchandising(_:from:)-hkrd'
source_url: 'https://developer.apple.com/documentation/storekit/appstore/presentmerchandising(_:from:)-hkrd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore/presentmerchandising%28_%3Afrom%3A%29-hkrd.json'
content_hash: 'sha256:c41a120fa194c4f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppStore](../appstore.md)

# presentMerchandising(_:from:)

<sub>Type Method</sub>

Display a merchandising view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
@MainActor static func presentMerchandising(_ kind: AppStoreMerchandisingKind, from controller: UIViewController) async throws -> AppStoreMerchandisingKind.PresentationResult
```

## Parameters

- `kind` — The merchandising kind to merchandise.

- `controller` — The view controller to show the merchandising UI in proximity to.

## Return Value

The result of the App Store merchandising presentation.

## Discussion

> [!danger] Throws
> A `StoreKitError`.
