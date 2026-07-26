---
title: ExternalPurchaseCustomLink.NoticeType
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.1+, iPadOS 18.1+, macOS 15.1+, tvOS 18.1+, visionOS 2.1+, watchOS 11.1+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externalpurchasecustomlink/noticetype
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/noticetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchasecustomlink/noticetype.json'
content_hash: 'sha256:2fb790fc56981015'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ExternalPurchaseCustomLink](../externalpurchasecustomlink.md)

# ExternalPurchaseCustomLink.NoticeType

<sub>Enumeration</sub>

The custom link out style that informs the type of disclosure notice to display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NoticeType
```

## Overview

Provide a notice type value when you call [showNotice(type:)](<shownotice(type_).md>).

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting notice types

- [ExternalPurchaseCustomLink.NoticeType.browser](noticetype/browser.md) — A notice type that indicates your app displays external purchases in a destination of your choice.
- [ExternalPurchaseCustomLink.NoticeType.withinApp](noticetype/withinapp.md) — A notice type that indicates that you display the destination in a web view or native experience within the app.

## See Also

### Displaying the disclosure sheet

- [showNotice(type:)](<shownotice(type_).md>) — Displays the system disclosure notice sheet and asks the customer whether to continue.
- [NoticeResult](noticeresult.md) — The result of showing the disclosure notice.
