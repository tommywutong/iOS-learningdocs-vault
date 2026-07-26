---
title: wantsSoftwareDimming
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/wantssoftwaredimming
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/wantssoftwaredimming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/wantssoftwaredimming.json'
content_hash: 'sha256:31d96a1134840781'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# wantsSoftwareDimming

<sub>Instance Property</sub>

A Boolean value that indicates whether the screen may be dimmed lower than the hardware is normally capable of by emulating it in software.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var wantsSoftwareDimming: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). Enabling it may cause a loss in performance.

## See Also

### Managing brightness

- [brightness](brightness.md) — The brightness level of the screen.
