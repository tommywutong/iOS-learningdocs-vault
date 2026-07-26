---
title: hasAmbiguousLayout
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.12+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nslayoutanchor/hasambiguouslayout
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutanchor/hasambiguouslayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutanchor/hasambiguouslayout.json'
content_hash: 'sha256:f62cfc724443eb0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutAnchor](../nslayoutanchor.md)

# hasAmbiguousLayout

<sub>Instance Property</sub>

A Boolean value indicating whether the constraints impacting the anchor specify its location ambiguously.

<sub>macOS</sub>

```swift
var hasAmbiguousLayout: Bool { get }
```

## See Also

### Debugging the anchor

- [constraintsAffectingLayout](constraintsaffectinglayout.md) — The constraints that impact the layout of the anchor.
- [name](name.md) — The name assigned to the anchor for debugging purposes.
- [item](item.md) — The layout item used to calculate the anchor’s position.
