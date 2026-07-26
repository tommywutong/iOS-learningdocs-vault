---
title: 'writeData:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandle/writedata:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/writedata:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/writedata%3A.json'
content_hash: 'sha256:2cb9199c9e6805eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# writeData:

<sub>Instance Method</sub>

Attempts to write a specified set of data to the location specified by the receiver’s URL.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) writeData:(NSData *) data;
```

## Parameters

- `data` — The data to write.

## Return Value

[true](../../swift/true.md) if successful, [false](../../swift/false.md) otherwise.

## Discussion

Must be overridden by subclasses.
