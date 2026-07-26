---
title: cancel()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurldownload/cancel()
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownload/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownload/cancel%28%29.json'
content_hash: 'sha256:4165aa01e740f0e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownload](../nsurldownload.md)

# cancel()

<sub>Instance Method</sub>

Cancels the receiver’s download and deletes the downloaded file.

<sub>macOS</sub>

```swift
func cancel()
```

## Discussion

This method deletes the partially downloaded file unless you have previously called [deletesFileUponFailure](deletesfileuponfailure.md), passing [false](../../swift/false.md).
