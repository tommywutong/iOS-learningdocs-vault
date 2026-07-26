---
title: ExternalPurchase.NoticeResult
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externalpurchase/noticeresult
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchase/noticeresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchase/noticeresult.json'
content_hash: 'sha256:5d1275ef4abbd795'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ExternalPurchase](../externalpurchase.md)

# ExternalPurchase.NoticeResult

<sub>Enumeration</sub>

The options available to people while viewing the external purchase notice sheet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NoticeResult
```

## Overview

These values return when your app calls [presentNoticeSheet()](<presentnoticesheet().md>).

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting notice sheet results

- [ExternalPurchase.NoticeResult.cancelled](noticeresult/cancelled.md) — Describes when people chose to cancel and not view external purchases.
- [ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)](<noticeresult/continuedwithexternalpurchasetoken(token_).md>) — Describes when people chose to continue to view external purchases, and provides the external purchase token.

## See Also

### Offering an external purchase

- [canPresent](canpresent.md) — A Boolean value that indicates whether the app can successfully present the notice sheet to inform people about external purchases.
- [presentNoticeSheet()](<presentnoticesheet().md>) — Presents a notice sheet from Apple that informs people of external purchases before showing them, and determines if your app can present external purchases
- [SKExternalPurchase](../../bundleresources/information-property-list/skexternalpurchase.md) — A string array of country codes that indicates your app supports external purchases.
