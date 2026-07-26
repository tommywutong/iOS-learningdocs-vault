---
title: UIShape.Resolved
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uishape-swift.struct/resolved
source_url: 'https://developer.apple.com/documentation/uikit/uishape-swift.struct/resolved'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishape-swift.struct/resolved.json'
content_hash: 'sha256:ec2f6b0054e03db4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIShape](../uishape-swift.struct.md)

# UIShape.Resolved

<sub>Structure</sub>

A shape that has completely resolved based on a context.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct Resolved
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md)

## Topics

### Creating a resolved shape by applying insets

- [inset(by:)](<resolved/inset(by_)-9sjcg.md>) — Creates a new modified shape by applying the provided insets to this shape.
- [inset(by:)](<resolved/inset(by_)-1r5gp.md>) — Creates a new modified shape by applying the provided inset to this shape.

### Accessing the resolved shape’s attributes

- [shape](resolved/shape.md) — The abstract shape that produces this resolved shape.
- [boundingRect](resolved/boundingrect.md) — The bounding rectangle that frames the shape.
- [path](resolved/path.md) — The Bézier path representing this shape.

## See Also

### Creating a dynamic hover shape

- [init(_:)](<init(__).md>) — Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [UIShapeProvider](../uishapeprovider-60loj.md) — An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [ResolutionContext](resolutioncontext.md) — The context for resolving a dynamic shape.
