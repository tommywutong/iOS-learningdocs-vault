---
title: constraintsAffectingLayout
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.12+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nslayoutanchor/constraintsaffectinglayout
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutanchor/constraintsaffectinglayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutanchor/constraintsaffectinglayout.json'
content_hash: 'sha256:2c3da2ec7928b652'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutAnchor](../nslayoutanchor.md)

# constraintsAffectingLayout

<sub>Instance Property</sub>

The constraints that impact the layout of the anchor.

<sub>macOS</sub>

```swift
var constraintsAffectingLayout: [NSLayoutConstraint] { get }
```

## See Also

### Debugging the anchor

- [hasAmbiguousLayout](hasambiguouslayout.md) — A Boolean value indicating whether the constraints impacting the anchor specify its location ambiguously.
- [name](name.md) — The name assigned to the anchor for debugging purposes.
- [item](item.md) — The layout item used to calculate the anchor’s position.
