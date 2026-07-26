---
title: role
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shape/role
source_url: 'https://developer.apple.com/documentation/swiftui/shape/role'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/role.json'
content_hash: 'sha256:50f3cb4d4afe4664'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# role

<sub>Type Property</sub>

An indication of how to style a shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static var role: ShapeRole { get }
```

## Discussion

SwiftUI looks at a shape’s role when deciding how to apply a [ShapeStyle](../shapestyle.md) at render time. The [Shape](../shape.md) protocol provides a default implementation with a value of [ShapeRole.fill](../shaperole/fill.md). If you create a composite shape, you can provide an override of this property to return another value, if appropriate.

## Default Implementations

### Shape Implementations

- [role](role-681up.md) — An indication of how to style a shape.
