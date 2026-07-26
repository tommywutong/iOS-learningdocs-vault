---
title: standardError
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuserunixtask/standarderror
source_url: 'https://developer.apple.com/documentation/foundation/nsuserunixtask/standarderror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserunixtask/standarderror.json'
content_hash: 'sha256:a6466114d1a98078'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserUnixTask](../nsuserunixtask.md)

# standardError

<sub>Instance Property</sub>

The standard error stream.

<sub>macOS</sub>

```swift
var standardError: FileHandle? { get set }
```

## Discussion

Setting to `nil` will bind the stream to `/dev/null`.

The default is `nil`.

## See Also

### Standard Unix Streams

- [standardInput](standardinput.md) — The standard input stream.
- [standardOutput](standardoutput.md) — The standard output stream.
