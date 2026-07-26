---
title: 'offset(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/offset(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/offset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/offset%28_%3A%29.json'
content_hash: 'sha256:c92e0b7db9e0f507'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# offset(_:)

<sub>Instance Method</sub>

Offsets the view by the horizontal and vertical amount specified in the offset parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func offset(_ offset: CGSize) -> some VisualEffect

```

## Parameters

- `offset` — The distance to offset the view.

## Return Value

An effect that offsets the view by `offset`.

## See Also

### Translating

- [offset(x:y:)](<offset(x_y_).md>) — Offsets the view by the specified horizontal and vertical distances.
- [offset(z:)](<offset(z_).md>) — Brings a view forward in Z by the provided distance in points.
