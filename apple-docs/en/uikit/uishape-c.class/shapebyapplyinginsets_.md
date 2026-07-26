---
title: 'shapeByApplyingInsets:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uishape-c.class/shapebyapplyinginsets:'
source_url: 'https://developer.apple.com/documentation/uikit/uishape-c.class/shapebyapplyinginsets:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishape-c.class/shapebyapplyinginsets%3A.json'
content_hash: 'sha256:ba9e336fe85e2603'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIShape](../uishape-c.class.md)

# shapeByApplyingInsets:

<sub>Instance Method</sub>

Creates a new modified shape by applying the provided insets to this shape.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (UIShape *) shapeByApplyingInsets:(UIEdgeInsets) insets;
```

## Discussion

You can use negative values to add inner padding to a shape.

If it isn’t possible to inset this shape (for example, if it’s a custom path), this method doesn’t have any effect. For some shapes like rounded rectangles, this method can also modify the corner radii of the shape to ensure the resulting corners are concentric.

## See Also

### Creating a shape by applying insets

- [shapeByApplyingInset:](shapebyapplyinginset_.md) — Creates a new modified shape by applying the provided inset to this shape.
