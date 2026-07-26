---
title: clip()
framework: Core Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.9+, Swift 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cgrect/clip()
source_url: 'https://developer.apple.com/documentation/corefoundation/cgrect/clip()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cgrect/clip%28%29.json'
content_hash: 'sha256:601e9c5d2770dc06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CGRect](../cgrect.md)

# clip()

<sub>Instance Method</sub>

Modifies the current graphics context clipping path by intersecting it with this rect. This permanently modifies the graphics state, so the current state should be saved beforehand and restored afterwards.

<sub>macOS</sub>

```swift
func clip()
```

## Discussion

> [!info] Precondition
> There must be a set current NSGraphicsContext.
