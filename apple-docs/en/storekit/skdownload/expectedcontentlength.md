---
title: expectedContentLength
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（16.0 起废弃）, iPadOS 13.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.15+（13.0 起废弃）, tvOS 13.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownload/expectedcontentlength
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/expectedcontentlength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/expectedcontentlength.json'
content_hash: 'sha256:2718095190283359'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# expectedContentLength

<sub>Instance Property</sub>

The length of the downloadable content, in bytes.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var expectedContentLength: Int64 { get }
```

## See Also

### Getting Content Information

- [contentIdentifier](contentidentifier.md) — A string that uniquely identifies the downloadable content. _(deprecated)_
- [contentVersion](contentversion.md) — A string that identifies which version of the content is available for download. _(deprecated)_
- [transaction](transaction.md) — The transaction associated with the downloadable file. _(deprecated)_
- [contentLength](contentlength.md) — The length of the downloadable content, in bytes. _(deprecated)_
