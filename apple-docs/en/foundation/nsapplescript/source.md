---
title: source
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsapplescript/source
source_url: 'https://developer.apple.com/documentation/foundation/nsapplescript/source'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsapplescript/source.json'
content_hash: 'sha256:d3ba5be3bf285955'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleScript](../nsapplescript.md)

# source

<sub>Instance Property</sub>

The script source for the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var source: String? { get }
```

## Discussion

It is possible for an `NSAppleScript` that has been instantiated with [- initWithContentsOfURL:error:](<init(contentsof_error_).md>) to be a script for which the source code is not available but is nonetheless executable.

## See Also

### Getting Information About a Script

- [compiled](iscompiled.md) — A Boolean value that indicates whether the receiver’s script has been compiled.
