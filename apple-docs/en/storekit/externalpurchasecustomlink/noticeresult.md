---
title: ExternalPurchaseCustomLink.NoticeResult
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.1+, iPadOS 18.1+, macOS 15.1+, tvOS 18.1+, visionOS 2.1+, watchOS 11.1+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externalpurchasecustomlink/noticeresult
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/noticeresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchasecustomlink/noticeresult.json'
content_hash: 'sha256:5dbffa0dca40b2fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ExternalPurchaseCustomLink](../externalpurchasecustomlink.md)

# ExternalPurchaseCustomLink.NoticeResult

<sub>Enumeration</sub>

The result of showing the disclosure notice.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NoticeResult
```

## Overview

This value is the result of calling [showNotice(type:)](<shownotice(type_).md>).

If the value is [ExternalPurchaseCustomLink.NoticeResult.continued](noticeresult/continued.md), the customer choses to continue and your app can communicate and promote offers for purchase in a distribution channel of your choice. Otherwise, don’t continue.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting notice results

- [ExternalPurchaseCustomLink.NoticeResult.cancelled](noticeresult/cancelled.md) — The customer chooses to cancel; don’t offer external purchases.
- [ExternalPurchaseCustomLink.NoticeResult.continued](noticeresult/continued.md) — The customer chooses to continue; the app can offer external purchases.

## See Also

### Displaying the disclosure sheet

- [showNotice(type:)](<shownotice(type_).md>) — Displays the system disclosure notice sheet and asks the customer whether to continue.
- [NoticeType](noticetype.md) — The custom link out style that informs the type of disclosure notice to display.
