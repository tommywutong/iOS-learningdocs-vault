---
title: UIShape.ResolutionContext
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uishape-swift.struct/resolutioncontext
source_url: 'https://developer.apple.com/documentation/uikit/uishape-swift.struct/resolutioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishape-swift.struct/resolutioncontext.json'
content_hash: 'sha256:68a3699c00bc8513'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIShape](../uishape-swift.struct.md)

# UIShape.ResolutionContext

<sub>Structure</sub>

The context for resolving a dynamic shape.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct ResolutionContext
```

## Topics

### Determining the content shape

- [contentShape](resolutioncontext/contentshape.md) — The resolved shape of the content to which this shape can apply.

## See Also

### Creating a dynamic hover shape

- [init(_:)](<init(__).md>) — Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [UIShapeProvider](../uishapeprovider-60loj.md) — An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [Resolved](resolved.md) — A shape that has completely resolved based on a context.
