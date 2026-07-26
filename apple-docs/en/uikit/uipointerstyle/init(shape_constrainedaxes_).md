---
title: 'init(shape:constrainedAxes:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointerstyle/init(shape:constrainedaxes:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipointerstyle/init(shape:constrainedaxes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerstyle/init%28shape%3Aconstrainedaxes%3A%29.json'
content_hash: 'sha256:7250353f521ce942'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerStyle](../uipointerstyle.md)

# init(shape:constrainedAxes:)

<sub>Initializer</sub>

Morphs the pointer into the provided shape when hovering over the current region.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(shape: UIPointerShape, constrainedAxes: UIAxis = [])
```

## Parameters

- `shape` — The [UIPointerShape](../uipointershape-swift.enum.md) to use, defaults to `nil`.

- `constrainedAxes` — An array of [UIAxis](../uiaxis.md) directions in which to constrain the pointer. The default is no constraints.

## See Also

### Creating a pointer style

- [init(effect:shape:)](<init(effect_shape_).md>) — Applies the provided content effect and pointer shape to the current region.
- [+ hiddenPointerStyle](<hidden().md>) — Hides the pointer when it moves over the current region.
- [+ systemPointerStyle](<system().md>) — Morphs the pointer into a default system-style pointer.
