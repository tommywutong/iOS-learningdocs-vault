---
title: MeshGradient.Locations
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/meshgradient/locations-swift.enum
source_url: 'https://developer.apple.com/documentation/swiftui/meshgradient/locations-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/meshgradient/locations-swift.enum.json'
content_hash: 'sha256:0e16c5d4367c5b84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MeshGradient](../meshgradient.md)

# MeshGradient.Locations

<sub>Enumeration</sub>

An array of 2D locations and their control points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Locations
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MeshGradient.Locations.bezierPoints(_:)](<locations-swift.enum/bezierpoints(__).md>) — Vertices explicitly specifying their location and control points.
- [MeshGradient.Locations.points(_:)](<locations-swift.enum/points(__).md>) — Vertices are only specified as their location, their control points are inferred from the locations of their neighbors.
