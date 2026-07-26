---
title: richTextSource
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsapplescript/richtextsource
source_url: 'https://developer.apple.com/documentation/foundation/nsapplescript/richtextsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsapplescript/richtextsource.json'
content_hash: 'sha256:60aa00bf1cae19ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleScript](../nsapplescript.md)

# richTextSource

<sub>Instance Property</sub>

Returns the syntax-highlighted source code of the receiver if the receiver has been compiled and its source code is available.

<sub>macOS</sub>

```swift
var richTextSource: NSAttributedString? { get }
```

## Discussion

Returns `nil` otherwise. It is possible for an instance of `NSAppleScript` that has been instantiated with [- initWithContentsOfURL:error:](<init(contentsof_error_).md>) to be a script for which the source code is not available, but is nonetheless executable.
