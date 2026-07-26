---
title: 'loadProduct(withParameters:completionBlock:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.0+, macOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skstoreproductviewcontroller/loadproduct(withparameters:completionblock:)'
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/loadproduct(withparameters:completionblock:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductviewcontroller/loadproduct%28withparameters%3Acompletionblock%3A%29.json'
content_hash: 'sha256:4a94fbe3762c9806'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKStoreProductViewController](../skstoreproductviewcontroller.md)

# loadProduct(withParameters:completionBlock:)

<sub>Instance Method</sub>

Loads a new product screen to display.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func loadProduct(withParameters parameters: [String : Any], completionBlock block: ((Bool, (any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func loadProduct(withParameters parameters: [String : Any]) async throws -> Bool
```

## Parameters

- `parameters` — A dictionary describing the content you want the view controller to display. See [Product Dictionary Keys](../product-dictionary-keys.md) for keys that describe the product. See [Ad network install-validation keys](../ad-network-install-validation-keys.md) for keys that describe an impression in an advertising campaign.

- `block` — A block to be called when the product information has been loaded from the App Store. The completion block is called on the main thread and receives the following parameters: - **`result`** — [true](../../swift/true.md) if the product information was successfully loaded, otherwise [false](../../swift/false.md). - **`error`** — If an error occurred, this object describes the error. If the product information was successfully loaded, this value is `nil`.

## Discussion

For a seamless user experience, load the product information before presenting the [SKStoreProductViewController](../skstoreproductviewcontroller.md) view controller. However, if you load the product information while presenting the view controller, once loaded, the product data replaces the contents of the view controller.

## See Also

### Loading a new product screen

- [Offering media for sale in your app](../offering-media-for-sale-in-your-app.md) — Allow users to purchase media in the App Store from within your app.
- [- loadProductWithParameters:impression:completionBlock:](<loadproduct(withparameters_impression_completionblock_).md>)
- [loadProduct(parameters:impression:)](<loadproduct(parameters_impression_).md>)
- [loadProduct(parameters:impression:reengagementURL:)](<loadproduct(parameters_impression_reengagementurl_).md>)
- [Product Dictionary Keys](../product-dictionary-keys.md) — Keys for identifying products and the tokens for affiliates and campaigns.
