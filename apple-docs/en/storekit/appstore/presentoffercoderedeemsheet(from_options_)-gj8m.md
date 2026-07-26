---
title: 'presentOfferCodeRedeemSheet(from:options:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/storekit/appstore/presentoffercoderedeemsheet(from:options:)-gj8m'
source_url: 'https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(from:options:)-gj8m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore/presentoffercoderedeemsheet%28from%3Aoptions%3A%29-gj8m.json'
content_hash: 'sha256:4da80047b230926c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppStore](../appstore.md)

# presentOfferCodeRedeemSheet(from:options:)

<sub>Type Method</sub>

Presents a sheet that enables users to redeem subscription offer codes that you configure in App Store Connect.

<sub>macOS</sub>

```swift
@MainActor static func presentOfferCodeRedeemSheet(from window: NSWindow, options: Set<RedeemOption> = []) async throws -> VerificationResult<Transaction>
```

## Parameters

- `window` — The `NSWindow` that StoreKit uses to display the offer code redemption sheet.

- `options` — A set of [RedeemOption](../redeemoption.md) values to configure the offer code redemption.

## Return Value

A [VerificationResult](../verificationresult.md) containing the [Transaction](../transaction.md) that the redemption produces.

## Discussion

> [!danger] Throws
> [StoreKitError](../storekiterror.md) if the system cannot present the sheet or the redemption fails.
