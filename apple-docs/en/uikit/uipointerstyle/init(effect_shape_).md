---
title: 'init(effect:shape:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointerstyle/init(effect:shape:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipointerstyle/init(effect:shape:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerstyle/init%28effect%3Ashape%3A%29.json'
content_hash: 'sha256:e1c13c6758eed861'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerStyle](../uipointerstyle.md)

# init(effect:shape:)

<sub>Initializer</sub>

Applies the provided content effect and pointer shape to the current region.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(effect: UIPointerEffect, shape: UIPointerShape? = nil)
```

## Parameters

- `effect` — The [UIPointerEffect](../uipointereffect-swift.enum.md) to apply to the region.

- `shape` — The [UIPointerShape](../uipointershape-swift.enum.md) to use, defaults to `nil`.

## See Also

### Creating a pointer style

- [init(shape:constrainedAxes:)](<init(shape_constrainedaxes_).md>) — Morphs the pointer into the provided shape when hovering over the current region.
- [+ hiddenPointerStyle](<hidden().md>) — Hides the pointer when it moves over the current region.
- [+ systemPointerStyle](<system().md>) — Morphs the pointer into a default system-style pointer.
