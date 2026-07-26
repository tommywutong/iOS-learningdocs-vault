---
title: 'init(source:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsapplescript/init(source:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsapplescript/init(source:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsapplescript/init%28source%3A%29.json'
content_hash: 'sha256:d37db927d21a7913'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleScript](../nsapplescript.md)

# init(source:)

<sub>Initializer</sub>

Initializes a newly allocated script instance from the passed source.

<sub>Mac Catalyst, macOS</sub>

```swift
init?(source: String)
```

## Parameters

- `source` — A string containing the source code of a script.

## Return Value

The initialized script object, `nil` if an error occurs.

## Discussion

This method is a designated initializer for `NSAppleScript`.

## See Also

### Initializing a Script

- [- initWithContentsOfURL:error:](<init(contentsof_error_).md>) — Initializes a newly allocated script instance from the source identified by the passed URL.
