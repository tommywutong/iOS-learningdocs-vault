---
title: 'rotate(by:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/rotate(by:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/rotate(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/rotate%28by%3A%29.json'
content_hash: 'sha256:59b5c727fa9578dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# rotate(by:)

<sub>Instance Method</sub>

Rotates subsequent drawing operations by an angle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func rotate(by angle: Angle)
```

## Parameters

- `angle` — The amount to rotate.

## Discussion

Calling this method is equivalent to updating the context’s [transform](transform.md) directly using the `angle` parameter:

```swift
transform = transform.rotated(by: angle.radians)
```

## See Also

### Applying transforms

- [scaleBy(x:y:)](<scaleby(x_y_).md>) — Scales subsequent drawing operations by an amount in each dimension.
- [translateBy(x:y:)](<translateby(x_y_).md>) — Moves subsequent drawing operations by an amount in each dimension.
- [concatenate(_:)](<concatenate(__).md>) — Appends the given transform to the context’s existing transform.
- [transform](transform.md) — The current transform matrix, defining user space coordinates.
