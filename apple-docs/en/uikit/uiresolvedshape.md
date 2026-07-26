---
title: UIResolvedShape
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresolvedshape
source_url: 'https://developer.apple.com/documentation/uikit/uiresolvedshape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresolvedshape.json'
content_hash: 'sha256:0faf02248b58a65f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIResolvedShape

<sub>Class</sub>

A shape that has completely resolved based on a context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIResolvedShape : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md)

## Topics

### Creating a resolved shape by applying insets

- [shapeByApplyingInsets:](uiresolvedshape/shapebyapplyinginsets_.md) — Creates a new modified shape by applying the provided insets to this shape.
- [shapeByApplyingInset:](uiresolvedshape/shapebyapplyinginset_.md) — Creates a new modified shape by applying the provided inset to this shape.

### Accessing the resolved shape’s attributes

- [shape](uiresolvedshape/shape.md) — The abstract shape that produces this resolved shape.
- [boundingRect](uiresolvedshape/boundingrect.md) — The bounding rectangle that frames the shape.
- [path](uiresolvedshape/path.md) — The Bézier path representing this shape.

## See Also

### Creating a dynamic hover shape

- [shapeWithProvider:](uishape-c.class/shapewithprovider_.md) — Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [UIShapeProvider](uishapeprovider-31jrf.md) — An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [resolvedShapeInContext:](uishape-c.class/resolvedshapeincontext_.md) — Resolves the shape in the provided context.
- [UIShapeResolutionContext](uishaperesolutioncontext.md) — The context for resolving a dynamic shape.
