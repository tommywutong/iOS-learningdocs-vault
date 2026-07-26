---
title: UIShapeProvider
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uishapeprovider-31jrf
source_url: 'https://developer.apple.com/documentation/uikit/uishapeprovider-31jrf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishapeprovider-31jrf.json'
content_hash: 'sha256:629a52eb3728ed1f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIShapeProvider

<sub>Protocol</sub>

An interface for a type that provides a custom shape by resolving it dynamically based on a context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@protocol UIShapeProvider <NSObject>
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIShape](uishape-c.class.md)

## Topics

### Resolving a custom shape

- [resolvedShapeInContext:](uishapeprovider-31jrf/resolvedshapeincontext_.md) — Resolves the shape in the provided context.

## See Also

### Creating a dynamic hover shape

- [shapeWithProvider:](uishape-c.class/shapewithprovider_.md) — Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [resolvedShapeInContext:](uishape-c.class/resolvedshapeincontext_.md) — Resolves the shape in the provided context.
- [UIShapeResolutionContext](uishaperesolutioncontext.md) — The context for resolving a dynamic shape.
- [UIResolvedShape](uiresolvedshape.md) — A shape that has completely resolved based on a context.
