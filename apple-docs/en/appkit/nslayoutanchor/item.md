---
title: item
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.12+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nslayoutanchor/item
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutanchor/item'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutanchor/item.json'
content_hash: 'sha256:87cf0e954277b7fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutAnchor](../nslayoutanchor.md)

# item

<sub>Instance Property</sub>

The layout item used to calculate the anchor’s position.

<sub>macOS</sub>

```swift
weak var item: AnyObject? { get }
```

## See Also

### Debugging the anchor

- [constraintsAffectingLayout](constraintsaffectinglayout.md) — The constraints that impact the layout of the anchor.
- [hasAmbiguousLayout](hasambiguouslayout.md) — A Boolean value indicating whether the constraints impacting the anchor specify its location ambiguously.
- [name](name.md) — The name assigned to the anchor for debugging purposes.
