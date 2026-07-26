---
title: 'offset(x:y:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/offset(x:y:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/offset(x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/offset%28x%3Ay%3A%29.json'
content_hash: 'sha256:2856275257897428'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# offset(x:y:)

<sub>Instance Method</sub>

Offsets the view by the specified horizontal and vertical distances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func offset(x: CGFloat = 0, y: CGFloat = 0) -> some VisualEffect

```

## Parameters

- `x` — The horizontal distance to offset the view.

- `y` — The vertical distance to offset the view.

## Return Value

An effect that offsets the view by `x` and `y`.

## See Also

### Translating

- [offset(_:)](<offset(__).md>) — Offsets the view by the horizontal and vertical amount specified in the offset parameter.
- [offset(z:)](<offset(z_).md>) — Brings a view forward in Z by the provided distance in points.
