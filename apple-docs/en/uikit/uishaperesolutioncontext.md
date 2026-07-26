---
title: UIShapeResolutionContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uishaperesolutioncontext
source_url: 'https://developer.apple.com/documentation/uikit/uishaperesolutioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishaperesolutioncontext.json'
content_hash: 'sha256:71ea0ff0c82370eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIShapeResolutionContext

<sub>Class</sub>

The context for resolving a dynamic shape.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIShapeResolutionContext : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Determining the content shape

- [contentShape](uishaperesolutioncontext/contentshape.md) — The resolved shape of the content to which this shape can apply.

## See Also

### Creating a dynamic hover shape

- [shapeWithProvider:](uishape-c.class/shapewithprovider_.md) — Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [UIShapeProvider](uishapeprovider-31jrf.md) — An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [resolvedShapeInContext:](uishape-c.class/resolvedshapeincontext_.md) — Resolves the shape in the provided context.
- [UIResolvedShape](uiresolvedshape.md) — A shape that has completely resolved based on a context.
