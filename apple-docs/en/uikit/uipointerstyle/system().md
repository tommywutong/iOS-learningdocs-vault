---
title: system()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerstyle/system()
source_url: 'https://developer.apple.com/documentation/uikit/uipointerstyle/system()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerstyle/system%28%29.json'
content_hash: 'sha256:3af8eec25f0fb83e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerStyle](../uipointerstyle.md)

# system()

<sub>Type Method</sub>

Morphs the pointer into a default system-style pointer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func system() -> Self
```

## Discussion

To display custom accessories alongside the default pointer, use this pointer style and assign your accessories to the [accessories](accessories.md) property.

## See Also

### Creating a pointer style

- [init(effect:shape:)](<init(effect_shape_).md>) — Applies the provided content effect and pointer shape to the current region.
- [init(shape:constrainedAxes:)](<init(shape_constrainedaxes_).md>) — Morphs the pointer into the provided shape when hovering over the current region.
- [+ hiddenPointerStyle](<hidden().md>) — Hides the pointer when it moves over the current region.
