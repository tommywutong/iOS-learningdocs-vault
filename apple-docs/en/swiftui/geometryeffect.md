---
title: GeometryEffect
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/geometryeffect
source_url: 'https://developer.apple.com/documentation/swiftui/geometryeffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryeffect.json'
content_hash: 'sha256:c8076cd5ed84271c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GeometryEffect

<sub>Protocol</sub>

An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated protocol GeometryEffect : Animatable, ViewModifier where Self.Body == Never
```

## Overview

The only change the effect makes to the view’s ancestors and descendants is to change the coordinate transform to and from them.

## Relationships

- **Inherits From**: [Animatable](animatable.md), [ViewModifier](viewmodifier.md)

## Topics

### Applying effects

- [effectValue(size:)](<geometryeffect/effectvalue(size_).md>) — Returns the current value of the effect.
- [ignoredByLayout()](<geometryeffect/ignoredbylayout().md>) — Returns an effect that produces the same geometry transform as this effect, but only applies the transform while rendering its view.

## See Also

### Synchronizing geometries

- [matchedGeometryEffect(id:in:properties:anchor:isSource:)](<view/matchedgeometryeffect(id_in_properties_anchor_issource_).md>) — Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [MatchedGeometryProperties](matchedgeometryproperties.md) — A set of view properties that may be synchronized between views using the `View.matchedGeometryEffect()` function.
- [Namespace](namespace.md) — A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).
- [geometryGroup()](<view/geometrygroup().md>) — Isolates the geometry (e.g. position and size) of the view from its parent view.
