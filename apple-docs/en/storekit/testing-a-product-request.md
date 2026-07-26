---
title: Testing a product request
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/testing-a-product-request
source_url: 'https://developer.apple.com/documentation/storekit/testing-a-product-request'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/testing-a-product-request.json'
content_hash: 'sha256:61e4851c3d419e7f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)

# Testing a product request

<sub>Article</sub>

Verify that requests for products function properly in the sandbox environment by inspecting the App Store response.

## Overview

After setting a breakpoint in your code, use the list of product identifiers that you tested in [Testing fetching product identifiers](testing-fetching-product-identifiers.md) to create and submit an instance of [SKProductsRequest](skproductsrequest.md). Then inspect the lists of valid and invalid product identifiers. If there are invalid product identifiers, review your products in App Store Connect and correct your JSON file or property list.

> [!note] Note
> Changes that you make to product metadata in App Store Connect can take up to one hour to appear in the sandbox environment.

See [Testing invalid product identifier handling](testing-invalid-product-identifier-handling.md) for more information.

## See Also

### Product identifiers and requests

- [Testing fetching product identifiers](testing-fetching-product-identifiers.md) — Verify that your app receives the correct product identifiers by inspecting or replicating your app’s process for retrieving the identifiers.
- [Testing invalid product identifier handling](testing-invalid-product-identifier-handling.md) — Verify that your app correctly handles invalid product identifiers.
