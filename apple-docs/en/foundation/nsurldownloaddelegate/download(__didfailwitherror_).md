---
title: 'download(_:didFailWithError:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownloaddelegate/download(_:didfailwitherror:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:didfailwitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownloaddelegate/download%28_%3Adidfailwitherror%3A%29.json'
content_hash: 'sha256:44cc1d8315c5eebd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownloadDelegate](../nsurldownloaddelegate.md)

# download(_:didFailWithError:)

<sub>Instance Method</sub>

Sent if the download fails or if an I/O error occurs when the file is written to disk.

<sub>macOS</sub>

```swift
optional func download(_ download: NSURLDownload, didFailWithError error: any Error)
```

## Parameters

- `download` — The URL download object sending the message.

- `error` — The error that caused the failure of the download.

## Discussion

Any partially downloaded file will be deleted.

### Special Considerations

Once the delegate receives this message, it will receive no further messages for `download`.

## See Also

### Download Completion

- [- downloadDidFinish:](<downloaddidfinish(__).md>) — Sent when a download object has completed downloading successfully and has written its results to disk.
