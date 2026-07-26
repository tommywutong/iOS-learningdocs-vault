---
title: standardInput
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuserunixtask/standardinput
source_url: 'https://developer.apple.com/documentation/foundation/nsuserunixtask/standardinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserunixtask/standardinput.json'
content_hash: 'sha256:8faa3f7a9289e54b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserUnixTask](../nsuserunixtask.md)

# standardInput

<sub>Instance Property</sub>

The standard input stream.

<sub>macOS</sub>

```swift
var standardInput: FileHandle? { get set }
```

## Discussion

Setting to `nil` will bind the stream to `/dev/null`.

The default is `nil`.

## See Also

### Standard Unix Streams

- [standardError](standarderror.md) — The standard error stream.
- [standardOutput](standardoutput.md) — The standard output stream.
