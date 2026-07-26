---
title: 'resolvedShapeInContext:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uishape-c.class/resolvedshapeincontext:'
source_url: 'https://developer.apple.com/documentation/uikit/uishape-c.class/resolvedshapeincontext:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishape-c.class/resolvedshapeincontext%3A.json'
content_hash: 'sha256:62f36543ee4b3f98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIShape](../uishape-c.class.md)

# resolvedShapeInContext:

<sub>Instance Method</sub>

Resolves the shape in the provided context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (UIResolvedShape *) resolvedShapeInContext:(UIShapeResolutionContext *) context;
```

## See Also

### Creating a dynamic hover shape

- [shapeWithProvider:](shapewithprovider_.md) — Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [UIShapeProvider](../uishapeprovider-31jrf.md) — An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [UIShapeResolutionContext](../uishaperesolutioncontext.md) — The context for resolving a dynamic shape.
- [UIResolvedShape](../uiresolvedshape.md) — A shape that has completely resolved based on a context.
