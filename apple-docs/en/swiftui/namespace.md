---
title: Namespace
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/namespace
source_url: 'https://developer.apple.com/documentation/swiftui/namespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/namespace.json'
content_hash: 'sha256:69ee1e315ef1688c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Namespace

<sub>Structure</sub>

A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen @propertyWrapper struct Namespace
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [DynamicProperty](dynamicproperty.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a namespace

- [init()](<namespace/init().md>)

### Getting the namespace

- [wrappedValue](namespace/wrappedvalue.md)
- [ID](namespace/id.md) — A namespace defined by the persistent identity of an `@Namespace` dynamic property.

## See Also

### Synchronizing geometries

- [matchedGeometryEffect(id:in:properties:anchor:isSource:)](<view/matchedgeometryeffect(id_in_properties_anchor_issource_).md>) — Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [MatchedGeometryProperties](matchedgeometryproperties.md) — A set of view properties that may be synchronized between views using the `View.matchedGeometryEffect()` function.
- [GeometryEffect](geometryeffect.md) — An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.
- [geometryGroup()](<view/geometrygroup().md>) — Isolates the geometry (e.g. position and size) of the view from its parent view.
