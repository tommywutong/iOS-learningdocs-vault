---
title: 'presentOfferCodeRedeemSheet(from:options:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/storekit/appstore/presentoffercoderedeemsheet(from:options:)-89agc'
source_url: 'https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(from:options:)-89agc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore/presentoffercoderedeemsheet%28from%3Aoptions%3A%29-89agc.json'
content_hash: 'sha256:d85a35903ad6b594'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppStore](../appstore.md)

# presentOfferCodeRedeemSheet(from:options:)

<sub>Type Method</sub>

Presents a sheet that enables users to redeem subscription offer codes that you configure in App Store Connect.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor static func presentOfferCodeRedeemSheet(from viewController: UIViewController, options: Set<RedeemOption> = []) async throws -> VerificationResult<Transaction>
```

## Parameters

- `viewController` — The `UIViewController` that StoreKit uses to display the offer code redemption sheet.

- `options` — A set of [RedeemOption](../redeemoption.md) values to configure the offer code redemption.

## Return Value

A [VerificationResult](../verificationresult.md) containing the [Transaction](../transaction.md) that the redemption produces.

## Discussion

> [!danger] Throws
> [StoreKitError](../storekiterror.md) if the system cannot present the sheet or the redemption fails.

## See Also

### Presenting the offer code redemption sheet

- [Supporting offer codes in your app](../supporting-offer-codes-in-your-app.md) — Enable customers to redeem offer codes through the App Store or within your app.
- [offerCodeRedemption(options:isPresented:onCompletion:)](<../../swiftui/view/offercoderedemption(options_ispresented_oncompletion_).md>) — Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect. _(beta)_
