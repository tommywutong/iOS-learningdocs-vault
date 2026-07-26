---
title: 'pause(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymentqueue/pause(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/pause(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/pause%28_%3A%29.json'
content_hash: 'sha256:080a70402a7d40a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# pause(_:)

<sub>Instance Method</sub>

Pauses a set of downloads.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func pause(_ downloads: [SKDownload])
```

## Parameters

- `downloads` — An array of [SKDownload](../skdownload.md) objects to pause.

## See Also

### Downloading Content

- [- startDownloads:](<start(__).md>) — Adds a set of downloads to the download list. _(deprecated)_
- [- cancelDownloads:](<cancel(__).md>) — Removes a set of downloads from the download list. _(deprecated)_
- [- resumeDownloads:](<resume(__).md>) — Resumes a set of downloads. _(deprecated)_
