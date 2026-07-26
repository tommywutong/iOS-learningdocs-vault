---
title: 'downloadDidFinish(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownloaddelegate/downloaddidfinish(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/downloaddidfinish(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownloaddelegate/downloaddidfinish%28_%3A%29.json'
content_hash: 'sha256:18b0584375b89896'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownloadDelegate](../nsurldownloaddelegate.md)

# downloadDidFinish(_:)

<sub>Instance Method</sub>

Sent when a download object has completed downloading successfully and has written its results to disk.

<sub>macOS</sub>

```swift
optional func downloadDidFinish(_ download: NSURLDownload)
```

## Parameters

- `download` — The URL download object sending the message.

## Discussion

The delegate will receive no further messages for `download`.

## See Also

### Download Completion

- [- download:didFailWithError:](<download(__didfailwitherror_).md>) — Sent if the download fails or if an I/O error occurs when the file is written to disk.
