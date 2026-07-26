---
title: 'styleWithEffect:shape:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointerstyle/stylewitheffect:shape:'
source_url: 'https://developer.apple.com/documentation/uikit/uipointerstyle/stylewitheffect:shape:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerstyle/stylewitheffect%3Ashape%3A.json'
content_hash: 'sha256:77c31837178232e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerStyle](../uipointerstyle.md)

# styleWithEffect:shape:

<sub>Type Method</sub>

Applies the provided content effect and pointer shape to the current region.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) styleWithEffect:(UIPointerEffect *) effect shape:(UIPointerShape *) shape;
```

## Parameters

- `effect` — The [UIPointerEffect](../uipointereffect-swift.enum.md) to apply to the region.

- `shape` — The [UIPointerShape](../uipointershape-swift.enum.md) to apply to the region.

## See Also

### Creating a pointer style

- [styleWithShape:constrainedAxes:](stylewithshape_constrainedaxes_.md) — Morphs the pointer into the provided shape when it moves over the current region.
- [+ hiddenPointerStyle](<hidden().md>) — Hides the pointer when it moves over the current region.
- [+ systemPointerStyle](<system().md>) — Morphs the pointer into a default system-style pointer.
