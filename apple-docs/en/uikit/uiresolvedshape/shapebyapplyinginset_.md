---
title: 'shapeByApplyingInset:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresolvedshape/shapebyapplyinginset:'
source_url: 'https://developer.apple.com/documentation/uikit/uiresolvedshape/shapebyapplyinginset:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresolvedshape/shapebyapplyinginset%3A.json'
content_hash: 'sha256:68ce2fb2628649d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResolvedShape](../uiresolvedshape.md)

# shapeByApplyingInset:

<sub>Instance Method</sub>

Creates a new modified shape by applying the provided inset to this shape.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (UIResolvedShape *) shapeByApplyingInset:(CGFloat) inset;
```

## Discussion

You can use negative values to add inner padding to a shape.

If it isn’t possible to inset this shape (for example, if it’s a custom path), this method doesn’t have any effect. For some shapes like rounded rectangles, this method can also modify the corner radii of the shape to ensure the resulting corners are concentric.

## See Also

### Creating a resolved shape by applying insets

- [shapeByApplyingInsets:](shapebyapplyinginsets_.md) — Creates a new modified shape by applying the provided insets to this shape.
