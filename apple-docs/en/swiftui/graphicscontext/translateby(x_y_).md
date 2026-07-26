---
title: 'translateBy(x:y:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/translateby(x:y:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/translateby(x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/translateby%28x%3Ay%3A%29.json'
content_hash: 'sha256:3ffb3a1279282c65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# translateBy(x:y:)

<sub>Instance Method</sub>

Moves subsequent drawing operations by an amount in each dimension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func translateBy(x: CGFloat, y: CGFloat)
```

## Parameters

- `x` — The amount to move in the horizontal direction.

- `y` — The amount to move in the vertical direction.

## Discussion

Calling this method is equivalent to updating the context’s [transform](transform.md) directly using the given translation amount:

```swift
transform = transform.translatedBy(x: x, y: y)
```

## See Also

### Applying transforms

- [scaleBy(x:y:)](<scaleby(x_y_).md>) — Scales subsequent drawing operations by an amount in each dimension.
- [rotate(by:)](<rotate(by_).md>) — Rotates subsequent drawing operations by an angle.
- [concatenate(_:)](<concatenate(__).md>) — Appends the given transform to the context’s existing transform.
- [transform](transform.md) — The current transform matrix, defining user space coordinates.
