---
title: priceIncreaseConsent
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/message/reason-swift.struct/priceincreaseconsent
source_url: 'https://developer.apple.com/documentation/storekit/message/reason-swift.struct/priceincreaseconsent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/message/reason-swift.struct/priceincreaseconsent.json'
content_hash: 'sha256:bc71d4a4484c53d4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Message](../../message.md) · [Reason](../reason-swift.struct.md)

# priceIncreaseConsent

<sub>Type Property</sub>

A message the App Store sends when you increase the price of an auto-renewable subscription and the price increase requires the customer’s consent.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let priceIncreaseConsent: Message.Reason
```

## Discussion

For more information about managing prices, see [Managing Prices](https://developer.apple.com/app-store/subscriptions/#managing-prices-for-existing-subscribers) and [Manage pricing for auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/devc9870599e).

## See Also

### Getting the message reasons

- [billingIssue](billingissue.md) — A message the App Store sends that informs people of a billing problem and enables them to update billing information.
- [generic](generic.md) — A message the App Store sends for a generic reason.
- [winBackOffer](winbackoffer.md) — A message the App Store sends when the customer is eligible for a win-back offer that you configure in App Store Connect.
