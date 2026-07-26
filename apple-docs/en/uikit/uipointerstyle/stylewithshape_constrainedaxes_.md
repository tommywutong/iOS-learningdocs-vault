---
title: 'styleWithShape:constrainedAxes:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointerstyle/stylewithshape:constrainedaxes:'
source_url: 'https://developer.apple.com/documentation/uikit/uipointerstyle/stylewithshape:constrainedaxes:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerstyle/stylewithshape%3Aconstrainedaxes%3A.json'
content_hash: 'sha256:3ecfa9ab1d0276bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerStyle](../uipointerstyle.md)

# styleWithShape:constrainedAxes:

<sub>Type Method</sub>

Morphs the pointer into the provided shape when it moves over the current region.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) styleWithShape:(UIPointerShape *) shape constrainedAxes:(UIAxis) axes;
```

## Parameters

- `shape` — The [UIPointerShape](../uipointershape-swift.enum.md) to apply to the region.

- `axes` — An array of [UIAxis](../uiaxis.md) directions in which to constrain the pointer.

## See Also

### Creating a pointer style

- [styleWithEffect:shape:](stylewitheffect_shape_.md) — Applies the provided content effect and pointer shape to the current region.
- [+ hiddenPointerStyle](<hidden().md>) — Hides the pointer when it moves over the current region.
- [+ systemPointerStyle](<system().md>) — Morphs the pointer into a default system-style pointer.
