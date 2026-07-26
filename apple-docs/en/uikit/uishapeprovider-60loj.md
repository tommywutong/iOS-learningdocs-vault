---
title: UIShapeProvider
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uishapeprovider-60loj
source_url: 'https://developer.apple.com/documentation/uikit/uishapeprovider-60loj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishapeprovider-60loj.json'
content_hash: 'sha256:86bbb57d3e43490e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIShapeProvider

<sub>Protocol</sub>

An interface for a type that provides a custom shape by resolving it dynamically based on a context.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
protocol UIShapeProvider : Equatable
```

## Relationships

- **Inherits From**: [Equatable](../swift/equatable.md)

- **Conforming Types**: [UIShape](uishape-swift.struct.md)

## Topics

### Resolving a custom shape

- [resolve(in:)](<uishapeprovider-60loj/resolve(in_).md>) — Resolves the shape in the provided context.

### Supporting types

- [Context](uishapeprovider-60loj/context.md) — The context for resolving a dynamic shape.
- [Resolved](uishapeprovider-60loj/resolved.md) — A shape that has completely resolved based on a context.

## See Also

### Creating a dynamic hover shape

- [init(_:)](<uishape-swift.struct/init(__).md>) — Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [ResolutionContext](uishape-swift.struct/resolutioncontext.md) — The context for resolving a dynamic shape.
- [Resolved](uishape-swift.struct/resolved.md) — A shape that has completely resolved based on a context.
