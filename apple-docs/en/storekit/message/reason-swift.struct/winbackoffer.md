---
title: winBackOffer
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/message/reason-swift.struct/winbackoffer
source_url: 'https://developer.apple.com/documentation/storekit/message/reason-swift.struct/winbackoffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/message/reason-swift.struct/winbackoffer.json'
content_hash: 'sha256:3aa7a68346d27203'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Message](../../message.md) · [Reason](../reason-swift.struct.md)

# winBackOffer

<sub>Type Property</sub>

A message the App Store sends when the customer is eligible for a win-back offer that you configure in App Store Connect.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let winBackOffer: Message.Reason
```

## Discussion

If the customer is eligible for a win-back offer, StoreKit displays the win-back offer message when the app launches. If your app customizes the way it displays win-back offers, you can suppress this message, as described in [Message](../../message.md).

For more information, see [Merchandising win-back offers in your app](../../merchandising-win-back-offers-in-your-app.md).

## See Also

### Getting the message reasons

- [billingIssue](billingissue.md) — A message the App Store sends that informs people of a billing problem and enables them to update billing information.
- [generic](generic.md) — A message the App Store sends for a generic reason.
- [priceIncreaseConsent](priceincreaseconsent.md) — A message the App Store sends when you increase the price of an auto-renewable subscription and the price increase requires the customer’s consent.
