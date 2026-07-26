---
title: ExternalPurchase.NoticeResult.cancelled
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externalpurchase/noticeresult/cancelled
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchase/noticeresult/cancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchase/noticeresult/cancelled.json'
content_hash: 'sha256:e1c9544ffd6a64a8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [ExternalPurchase](../../externalpurchase.md) · [NoticeResult](../noticeresult.md)

# ExternalPurchase.NoticeResult.cancelled

<sub>Case</sub>

Describes when people chose to cancel and not view external purchases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case cancelled
```

## Discussion

If your app’s call to [presentNoticeSheet()](<../presentnoticesheet().md>) results in this value, you must not show external purchases.

## See Also

### Getting notice sheet results

- [ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)](<continuedwithexternalpurchasetoken(token_).md>) — Describes when people chose to continue to view external purchases, and provides the external purchase token.
