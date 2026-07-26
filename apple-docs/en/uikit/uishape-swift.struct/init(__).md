---
title: 'init(_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uishape-swift.struct/init(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uishape-swift.struct/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishape-swift.struct/init%28_%3A%29.json'
content_hash: 'sha256:4e129f80e370085c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIShape](../uishape-swift.struct.md)

# init(_:)

<sub>Initializer</sub>

Creates a dynamic shape that resolves using the provided resolver closure and resolution context.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(_ provider: some UIShapeProvider)
```

## See Also

### Creating a dynamic hover shape

- [UIShapeProvider](../uishapeprovider-60loj.md) — An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [ResolutionContext](resolutioncontext.md) — The context for resolving a dynamic shape.
- [Resolved](resolved.md) — A shape that has completely resolved based on a context.
