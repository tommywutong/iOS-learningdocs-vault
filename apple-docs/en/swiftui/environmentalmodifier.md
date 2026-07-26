---
title: EnvironmentalModifier
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentalmodifier
source_url: 'https://developer.apple.com/documentation/swiftui/environmentalmodifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentalmodifier.json'
content_hash: 'sha256:75cee47af692df0b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EnvironmentalModifier

<sub>Protocol</sub>

A modifier that must resolve to a concrete modifier in an environment before use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol EnvironmentalModifier : ViewModifier where Self.Body == Never
```

## Relationships

- **Inherits From**: [ViewModifier](viewmodifier.md)

## Topics

### Resolving a modifier

- [resolve(in:)](<environmentalmodifier/resolve(in_).md>) — Resolve to a concrete modifier in the given `environment`.
- [ResolvedModifier](environmentalmodifier/resolvedmodifier.md) — The type of modifier to use after being resolved.

## See Also

### Modifying a view

- [Configuring views](configuring-views.md) — Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md) — Bundle view modifiers that you regularly reuse into a custom view modifier.
- [modifier(_:)](<view/modifier(__).md>) — Applies a modifier to a view and returns a new view.
- [ViewModifier](viewmodifier.md) — A modifier that you apply to a view or another view modifier, producing a different version of the original value.
- [EmptyModifier](emptymodifier.md) — An empty, or identity, modifier, used during development to switch modifiers at compile time.
- [ModifiedContent](modifiedcontent.md) — A value with a modifier applied to it.
- [ManipulableModifier](manipulablemodifier.md)
- [ManipulableResponderModifier](manipulablerespondermodifier.md)
- [ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md)
- [ManipulationGeometryModifier](manipulationgeometrymodifier.md)
- [ManipulationGestureModifier](manipulationgesturemodifier.md)
- [ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md)
- [Manipulable](manipulable.md) — A namespace for various manipulable related types.
