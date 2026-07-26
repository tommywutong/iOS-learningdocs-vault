---
title: transaction
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownload/transaction
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/transaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/transaction.json'
content_hash: 'sha256:3f596465f2c85f51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# transaction

<sub>Instance Property</sub>

The transaction associated with the downloadable file.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var transaction: SKPaymentTransaction { get }
```

## Discussion

A download object is always associated with a payment transaction. The download object may only be queued after payment is processed and before the transaction is finished.

## See Also

### Getting Content Information

- [expectedContentLength](expectedcontentlength.md) — The length of the downloadable content, in bytes. _(deprecated)_
- [contentIdentifier](contentidentifier.md) — A string that uniquely identifies the downloadable content. _(deprecated)_
- [contentVersion](contentversion.md) — A string that identifies which version of the content is available for download. _(deprecated)_
- [contentLength](contentlength.md) — The length of the downloadable content, in bytes. _(deprecated)_
