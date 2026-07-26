---
title: 'shapeWithProvider:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uishape-c.class/shapewithprovider:'
source_url: 'https://developer.apple.com/documentation/uikit/uishape-c.class/shapewithprovider:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishape-c.class/shapewithprovider%3A.json'
content_hash: 'sha256:ec450f6e09302b7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIShape](../uishape-c.class.md)

# shapeWithProvider:

<sub>Type Method</sub>

Creates a dynamic shape that resolves using the provided resolver closure and resolution context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) shapeWithProvider:(id<UIShapeProvider>) provider;
```

## See Also

### Creating a dynamic hover shape

- [UIShapeProvider](../uishapeprovider-31jrf.md) — An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [resolvedShapeInContext:](resolvedshapeincontext_.md) — Resolves the shape in the provided context.
- [UIShapeResolutionContext](../uishaperesolutioncontext.md) — The context for resolving a dynamic shape.
- [UIResolvedShape](../uiresolvedshape.md) — A shape that has completely resolved based on a context.
