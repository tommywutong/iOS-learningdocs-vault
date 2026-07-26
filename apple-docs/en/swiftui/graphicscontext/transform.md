---
title: transform
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/transform
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/transform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/transform.json'
content_hash: 'sha256:6b5198943a470c43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# transform

<sub>Instance Property</sub>

The current transform matrix, defining user space coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transform: CGAffineTransform { get set }
```

## Discussion

Modify this matrix to transform content that you subsequently draw into the context. Changes that you make don’t affect existing content.

## See Also

### Applying transforms

- [scaleBy(x:y:)](<scaleby(x_y_).md>) — Scales subsequent drawing operations by an amount in each dimension.
- [rotate(by:)](<rotate(by_).md>) — Rotates subsequent drawing operations by an angle.
- [translateBy(x:y:)](<translateby(x_y_).md>) — Moves subsequent drawing operations by an amount in each dimension.
- [concatenate(_:)](<concatenate(__).md>) — Appends the given transform to the context’s existing transform.
