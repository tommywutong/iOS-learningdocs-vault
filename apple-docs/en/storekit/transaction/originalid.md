---
title: originalID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/originalid
source_url: 'https://developer.apple.com/documentation/storekit/transaction/originalid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/originalid.json'
content_hash: 'sha256:7625fb5f419bf705'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# originalID

<sub>Instance Property</sub>

The original transaction identifier of a purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let originalID: UInt64
```

## Discussion

The original transaction identifier, [originalID](originalid.md), is identical to [id](id.md) except when the user restores a purchase or renews a transaction. You can use this value to:

- Identify one or more renewals for the same subscription.
- Differentiate a purchase transaction from a restore or a renewal transaction. For restore and renewal transactions, the original transaction identifier, [originalID](originalid.md), and transaction identifier, [id](id.md), differ.
- Match a transaction in the app with a transaction you receive on your server in an [App Store Server Notifications](../../appstoreservernotifications.md) event.

## See Also

### Getting the original transaction identifier

- [originalPurchaseDate](originalpurchasedate.md) — The date of purchase for the original transaction.
