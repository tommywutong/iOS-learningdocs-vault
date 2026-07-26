---
title: 'loadProduct(withParameters:impression:completionBlock:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skstoreproductviewcontroller/loadproduct(withparameters:impression:completionblock:)'
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/loadproduct(withparameters:impression:completionblock:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductviewcontroller/loadproduct%28withparameters%3Aimpression%3Acompletionblock%3A%29.json'
content_hash: 'sha256:296b4d3a467c6527'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKStoreProductViewController](../skstoreproductviewcontroller.md)

# loadProduct(withParameters:impression:completionBlock:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func loadProduct(withParameters parameters: [String : Any], impression: SKAdImpression, completionBlock block: ((Bool, (any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func loadProduct(withParameters parameters: [String : Any], impression: SKAdImpression) async throws -> Bool
```

## See Also

### Loading a new product screen

- [Offering media for sale in your app](../offering-media-for-sale-in-your-app.md) — Allow users to purchase media in the App Store from within your app.
- [- loadProductWithParameters:completionBlock:](<loadproduct(withparameters_completionblock_).md>) — Loads a new product screen to display.
- [loadProduct(parameters:impression:)](<loadproduct(parameters_impression_).md>)
- [loadProduct(parameters:impression:reengagementURL:)](<loadproduct(parameters_impression_reengagementurl_).md>)
- [Product Dictionary Keys](../product-dictionary-keys.md) — Keys for identifying products and the tokens for affiliates and campaigns.
