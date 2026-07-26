---
title: 'concatenate(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/concatenate(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/concatenate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/concatenate%28_%3A%29.json'
content_hash: 'sha256:978b19cab76d6620'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# concatenate(_:)

<sub>Instance Method</sub>

Appends the given transform to the context’s existing transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func concatenate(_ matrix: CGAffineTransform)
```

## Parameters

- `matrix` — A transform to append to the existing transform.

## Discussion

Calling this method is equivalent to updating the context’s [transform](transform.md) directly using the `matrix` parameter:

```swift
transform = matrix.concatenating(transform)
```

## See Also

### Applying transforms

- [scaleBy(x:y:)](<scaleby(x_y_).md>) — Scales subsequent drawing operations by an amount in each dimension.
- [rotate(by:)](<rotate(by_).md>) — Rotates subsequent drawing operations by an angle.
- [translateBy(x:y:)](<translateby(x_y_).md>) — Moves subsequent drawing operations by an amount in each dimension.
- [transform](transform.md) — The current transform matrix, defining user space coordinates.
