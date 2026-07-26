---
title: 'presentMerchandising(_:from:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/appstore/presentmerchandising(_:from:)-8bblo'
source_url: 'https://developer.apple.com/documentation/storekit/appstore/presentmerchandising(_:from:)-8bblo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore/presentmerchandising%28_%3Afrom%3A%29-8bblo.json'
content_hash: 'sha256:bd40e07ee8a85e91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppStore](../appstore.md)

# presentMerchandising(_:from:)

<sub>Type Method</sub>

Display a merchandising view.

<sub>macOS</sub>

```swift
@MainActor static func presentMerchandising(_ kind: AppStoreMerchandisingKind, from window: NSWindow) async throws -> AppStoreMerchandisingKind.PresentationResult
```

## Parameters

- `kind` — The merchandising kind to merchandise.

- `window` — The view window to show the merchandising UI in proximity to.

## Return Value

The result of the App Store merchandising presentation.

## Discussion

> [!danger] Throws
> A `StoreKitError`.
