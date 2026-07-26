---
title: 'paymentQueue(_:updatedDownloads:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:updateddownloads:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:updateddownloads:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionobserver/paymentqueue%28_%3Aupdateddownloads%3A%29.json'
content_hash: 'sha256:4fd2ca0a5ea83be4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransactionObserver](../skpaymenttransactionobserver.md)

# paymentQueue(_:updatedDownloads:)

<sub>Instance Method</sub>

Tells the observer that the payment queue has updated one or more download objects.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
optional func paymentQueue(_ queue: SKPaymentQueue, updatedDownloads downloads: [SKDownload])
```

## Parameters

- `queue` — The payment queue that updated the downloads.

- `downloads` — The download objects that were updated.

## Discussion

When a download object is updated, its [downloadState](../skdownload/downloadstate.md) property describes how it changed.
