---
title: 'start(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymentqueue/start(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/start(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/start%28_%3A%29.json'
content_hash: 'sha256:5385677d6358061f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# start(_:)

<sub>Instance Method</sub>

Adds a set of downloads to the download list.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func start(_ downloads: [SKDownload])
```

## Parameters

- `downloads` — An array of [SKDownload](../skdownload.md) objects to begin downloading.

## Discussion

In order for a download object to be queued, it must be associated with a transaction that has been successfully purchased, but not yet finished.

## See Also

### Downloading Content

- [- cancelDownloads:](<cancel(__).md>) — Removes a set of downloads from the download list. _(deprecated)_
- [- pauseDownloads:](<pause(__).md>) — Pauses a set of downloads. _(deprecated)_
- [- resumeDownloads:](<resume(__).md>) — Resumes a set of downloads. _(deprecated)_
