---
title: showPriceConsentIfNeeded()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+（18.0 起废弃）, iPadOS 13.4+（18.0 起废弃）, Mac Catalyst 13.4+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentqueue/showpriceconsentifneeded()
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/showpriceconsentifneeded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/showpriceconsentifneeded%28%29.json'
content_hash: 'sha256:dbc541b5f69bfafc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# showPriceConsentIfNeeded()

<sub>Instance Method</sub>

Asks the system to display the price consent sheet if the user hasn’t yet responded to a subscription price increase.

> [!warning] Deprecated
> Use Message.messages and Message.display(in:).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func showPriceConsentIfNeeded()
```

## Discussion

Call this method if the system called your delegate’s [- paymentQueueShouldShowPriceConsent:](<../skpaymentqueuedelegate/paymentqueueshouldshowpriceconsent(__).md>) method, and you chose to delay showing the price consent sheet.

This function displays the price consent sheet if both of the following are true:

- You’ve increased the price of the subscription in App Store Connect.
- The subscriber hasn’t yet responded to a price consent query.

Otherwise, this function has no effect.

> [!note] Note
> When you increase the price of a subscription, Apple informs affected subscribers through an email, push notification, and in-app price consent sheet and asks them to agree to the new price. If they don’t agree or take no action, their subscription expires at the end of their current billing cycle. For more information, see [Managing Prices](https://developer.apple.com/app-store/subscriptions/#managing-prices-for-existing-subscribers) and [Manage pricing for auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/devc9870599e).

In Mac apps built with Mac Catalyst, this function has no effect.

## See Also

### Related Documentation

- [- paymentQueueShouldShowPriceConsent:](<../skpaymentqueuedelegate/paymentqueueshouldshowpriceconsent(__).md>) — Asks the delegate whether to immediately display a price consent sheet. _(deprecated)_
