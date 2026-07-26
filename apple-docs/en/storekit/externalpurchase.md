---
title: ExternalPurchase
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externalpurchase
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchase.json'
content_hash: 'sha256:945bdc807111eb97'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# ExternalPurchase

<sub>Enumeration</sub>

An enumeration that enables qualifying apps to offer external purchases within the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ExternalPurchase
```

## Overview

This functionality is only available to and required by apps with the [com.apple.developer.storekit.external-purchase](../bundleresources/entitlements/com.apple.developer.storekit.external-purchase.md) entitlement. For more information, see:

- [Distributing apps using alternative payment providers in the European Union](https://developer.apple.com/go/?id=storekit-external-purchase-eu)
- [Distributing dating apps in the Netherlands](https://developer.apple.com/support/storekit-external-entitlement/)
- [Distributing apps using a third-party payment provider in South Korea](https://developer.apple.com/support/storekit-external-entitlement-kr/)

> [!note] Note
> You must check [canMakePayments](appstore/canmakepayments.md) before calling the External Purchase APIs. If [canMakePayments](appstore/canmakepayments.md) is `false`, don’t call the [ExternalPurchaseLink](externalpurchaselink.md) or [ExternalPurchase](externalpurchase.md) APIs.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Offering an external purchase

- [canPresent](externalpurchase/canpresent.md) — A Boolean value that indicates whether the app can successfully present the notice sheet to inform people about external purchases.
- [presentNoticeSheet()](<externalpurchase/presentnoticesheet().md>) — Presents a notice sheet from Apple that informs people of external purchases before showing them, and determines if your app can present external purchases
- [NoticeResult](externalpurchase/noticeresult.md) — The options available to people while viewing the external purchase notice sheet.
- [SKExternalPurchase](../bundleresources/information-property-list/skexternalpurchase.md) — A string array of country codes that indicates your app supports external purchases.

## See Also

### Implementing alternative payment service providers in the EU and South Korea

- [com.apple.developer.storekit.external-purchase](../bundleresources/entitlements/com.apple.developer.storekit.external-purchase.md) — A Boolean value that indicates whether your app can offer external purchases.
- [SKExternalPurchase](../bundleresources/information-property-list/skexternalpurchase.md) — A string array of country codes that indicates your app supports external purchases.
