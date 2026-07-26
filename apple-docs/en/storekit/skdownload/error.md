---
title: error
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownload/error
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/error.json'
content_hash: 'sha256:8830acd0d5e581bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# error

<sub>Instance Property</sub>

The error that prevented the content from being downloaded.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

The value of this property is valid only when the [downloadState](downloadstate.md) property is set to [SKDownloadStateFailed](../skdownloadstate/failed.md).

## See Also

### Accessing a Completed Download

- [contentURL](contenturl.md) — The local location of the downloaded file. _(deprecated)_
