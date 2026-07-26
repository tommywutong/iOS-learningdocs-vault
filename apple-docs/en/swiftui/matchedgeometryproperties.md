---
title: MatchedGeometryProperties
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/matchedgeometryproperties
source_url: 'https://developer.apple.com/documentation/swiftui/matchedgeometryproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/matchedgeometryproperties.json'
content_hash: 'sha256:e9a29cd761c5429d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MatchedGeometryProperties

<sub>Structure</sub>

A set of view properties that may be synchronized between views using the `View.matchedGeometryEffect()` function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct MatchedGeometryProperties
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Matching properties

- [frame](matchedgeometryproperties/frame.md) — Both the `position` and `size` properties.
- [position](matchedgeometryproperties/position.md) — The view’s position, in window coordinates.
- [size](matchedgeometryproperties/size.md) — The view’s size, in local coordinates.

## See Also

### Synchronizing geometries

- [matchedGeometryEffect(id:in:properties:anchor:isSource:)](<view/matchedgeometryeffect(id_in_properties_anchor_issource_).md>) — Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [GeometryEffect](geometryeffect.md) — An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.
- [Namespace](namespace.md) — A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).
- [geometryGroup()](<view/geometrygroup().md>) — Isolates the geometry (e.g. position and size) of the view from its parent view.
