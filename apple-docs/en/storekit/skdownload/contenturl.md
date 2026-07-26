---
title: contentURL
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownload/contenturl
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/contenturl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/contenturl.json'
content_hash: 'sha256:b09cd0cc86ac3fdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# contentURL

<sub>Instance Property</sub>

The local location of the downloaded file.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var contentURL: URL? { get }
```

## Discussion

The value of this property is valid only when the [downloadState](downloadstate.md) property is set to [SKDownloadStateFinished](../skdownloadstate/finished.md). The URL becomes invalid after the transaction object associated with the download is finalized.

## See Also

### Accessing a Completed Download

- [error](error.md) — The error that prevented the content from being downloaded. _(deprecated)_
