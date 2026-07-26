---
title: downloads
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymenttransaction/downloads
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransaction/downloads'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransaction/downloads.json'
content_hash: 'sha256:8c7952738052c60d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransaction](../skpaymenttransaction.md)

# downloads

<sub>Instance Property</sub>

An array of download objects representing the downloadable content associated with the transaction.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var downloads: [SKDownload] { get }
```

## Discussion

The contents of this property are undefined except when [transactionState](transactionstate.md) is set to [SKPaymentTransactionStatePurchased](../skpaymenttransactionstate/purchased.md). The [SKDownload](../skdownload.md) objects stored in this property must be used to download the transaction’s content before the transaction is finished. After the transaction is finished, the download objects are no longer queueable.
