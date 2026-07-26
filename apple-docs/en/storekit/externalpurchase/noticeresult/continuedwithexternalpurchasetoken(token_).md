---
title: 'ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)'
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/externalpurchase/noticeresult/continuedwithexternalpurchasetoken(token:)'
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchase/noticeresult/continuedwithexternalpurchasetoken(token:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchase/noticeresult/continuedwithexternalpurchasetoken%28token%3A%29.json'
content_hash: 'sha256:a07cdbffa40e84b5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [ExternalPurchase](../../externalpurchase.md) · [NoticeResult](../noticeresult.md)

# ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)

<sub>Case</sub>

Describes when people chose to continue to view external purchases, and provides the external purchase token.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case continuedWithExternalPurchaseToken(token: String)
```

## Parameters

- `token` — The external purchase token.

## Discussion

When your app calls [presentNoticeSheet()](<../presentnoticesheet().md>) and it results in this value: [ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)](<continuedwithexternalpurchasetoken(token_).md>), your app can proceed to present external purchases.

> [!important] Important
> Record and use the token to report the customer’s external purchases to Apple. For more information, see [External Purchase Server API](../../../externalpurchaseserverapi.md).

``

## See Also

### Getting notice sheet results

- [ExternalPurchase.NoticeResult.cancelled](cancelled.md) — Describes when people chose to cancel and not view external purchases.
