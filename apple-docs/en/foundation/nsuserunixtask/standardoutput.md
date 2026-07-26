---
title: standardOutput
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuserunixtask/standardoutput
source_url: 'https://developer.apple.com/documentation/foundation/nsuserunixtask/standardoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserunixtask/standardoutput.json'
content_hash: 'sha256:d726a75ca73681ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserUnixTask](../nsuserunixtask.md)

# standardOutput

<sub>Instance Property</sub>

The standard output stream.

<sub>macOS</sub>

```swift
var standardOutput: FileHandle? { get set }
```

## Discussion

Setting to `nil` will bind the stream to `/dev/null`.

The default is `nil`.

## See Also

### Standard Unix Streams

- [standardError](standarderror.md) — The standard error stream.
- [standardInput](standardinput.md) — The standard input stream.
