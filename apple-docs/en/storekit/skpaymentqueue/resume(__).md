---
title: 'resume(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymentqueue/resume(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/resume(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/resume%28_%3A%29.json'
content_hash: 'sha256:59d8f9aee3610088'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# resume(_:)

<sub>Instance Method</sub>

Resumes a set of downloads.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func resume(_ downloads: [SKDownload])
```

## Parameters

- `downloads` — An array of [SKDownload](../skdownload.md) objects to resume.

## See Also

### Downloading Content

- [- startDownloads:](<start(__).md>) — Adds a set of downloads to the download list. _(deprecated)_
- [- cancelDownloads:](<cancel(__).md>) — Removes a set of downloads from the download list. _(deprecated)_
- [- pauseDownloads:](<pause(__).md>) — Pauses a set of downloads. _(deprecated)_
