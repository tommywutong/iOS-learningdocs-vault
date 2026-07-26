---
title: Testing fetching product identifiers
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/testing-fetching-product-identifiers
source_url: 'https://developer.apple.com/documentation/storekit/testing-fetching-product-identifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/testing-fetching-product-identifiers.json'
content_hash: 'sha256:6e103ddce0ebe318'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)

# Testing fetching product identifiers

<sub>Article</sub>

Verify that your app receives the correct product identifiers by inspecting or replicating your app’s process for retrieving the identifiers.

## Overview

If you embed your product identifiers in your app, set a breakpoint in your code after the code loads the identifiers. Verify that the instance of [NSArray](../foundation/nsarray.md) contains your expected list of product identifiers.

> [!note] Note
> Changes that you make to product metadata in App Store Connect can take up to one hour to appear in the sandbox environment.

If your app fetches your product identifiers from a server, manually fetch the JSON file using a web browser such as Safari, or a command-line utility such as `curl`. Verify that the data your server returns contains the expected list of product identifiers and that your server correctly implements standard HTTP caching mechanisms.

For more information on fetching product identifiers, see [Loading in-app product identifiers](loading-in-app-product-identifiers.md).

## See Also

### Product identifiers and requests

- [Testing invalid product identifier handling](testing-invalid-product-identifier-handling.md) — Verify that your app correctly handles invalid product identifiers.
- [Testing a product request](testing-a-product-request.md) — Verify that requests for products function properly in the sandbox environment by inspecting the App Store response.
