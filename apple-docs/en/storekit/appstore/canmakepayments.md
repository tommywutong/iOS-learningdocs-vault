---
title: canMakePayments
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/appstore/canmakepayments
source_url: 'https://developer.apple.com/documentation/storekit/appstore/canmakepayments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore/canmakepayments.json'
content_hash: 'sha256:f56c71a22ad62857'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppStore](../appstore.md)

# canMakePayments

<sub>Type Property</sub>

A Boolean value that indicates whether the person can make purchases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var canMakePayments: Bool { get }
```

## Discussion

Use [canMakePayments](canmakepayments.md) to determine at runtime whether a person can authorize payments. If the value is `false`, a person can’t authorize payments, so don’t offer In-App Purchases or external purchases.

> [!important] Important
> Your app might need to alter its behavior or appearance when people can’t make purchases. For example, don’t enable your user interface for making In-App Purchases or external purchases when purchases are blocked.

The following conditions can cause the value of [canMakePayments](canmakepayments.md) to be `false`:

- A person sets the Content & Privacy Restrictions in Screen Time to prevent purchases. For more information, see [Use parental controls on your child’s iPhone, iPad, and iPod touch](https://support.apple.com/en-us/HT201304).
- The device has a mobile device management (MDM) profile that prevents purchases. For more information, see [Device Management](../../devicemanagement.md).

If [canMakePayments](canmakepayments.md) is `true` and your app uses only StoreKit [In-App Purchase](../in-app-purchase.md) APIs, the person can authorize purchases in the App Store and your app can offer In-App Purchases.

### Determine whether to offer purchases for apps that use External  Purchase APIs

If your app has the entitlements to use the [External Purchase](../external-purchase.md) APIs, determine at runtime whether to use the [External Purchase](../external-purchase.md) API or the [In-App Purchase](../in-app-purchase.md) APIs by following these steps, in order:

1. Check [canMakePayments](canmakepayments.md). If [canMakePayments](canmakepayments.md) is `false`, don’t offer either external purchases or In-App Purchases. If [canMakePayments](canmakepayments.md) if `true`, continue to step 2.
2. Check the External Purchase API values: [canOpen](../externalpurchaselink/canopen.md), [canPresent](../externalpurchase/canpresent.md), and [isEligible](../externalpurchasecustomlink/iseligible.md). If any value is `true`, use only the [External Purchase](../external-purchase.md) APIs to offer external purchases.
3. If all the values ([canOpen](../externalpurchaselink/canopen.md), [canPresent](../externalpurchase/canpresent.md), and [isEligible](../externalpurchasecustomlink/iseligible.md)) are `false`, and [canMakePayments](canmakepayments.md) is `true`, use StoreKit [In-App Purchase](../in-app-purchase.md) APIs to offer In-App Purchases.

> [!note] Note
> The StoreKit APIs always enable your app to view existing transactions and receive auto-renewable subscription renewals, so your app can support your customer’s existing purchases made through the App Store.
