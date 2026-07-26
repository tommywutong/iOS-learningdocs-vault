---
title: EmptyModifier
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/emptymodifier
source_url: 'https://developer.apple.com/documentation/swiftui/emptymodifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/emptymodifier.json'
content_hash: 'sha256:d35aa2776c382b35'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EmptyModifier

<sub>Structure</sub>

An empty, or identity, modifier, used during development to switch modifiers at compile time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct EmptyModifier
```

## Overview

Use the empty modifier to switch modifiers at compile time during development. In the example below, in a debug build the [Text](text.md) view inside `ContentView` has a yellow background and a red border. A non-debug build reflects the default system, or container supplied appearance.

```swift
struct EmphasizedLayout: ViewModifier {
    func body(content: Content) -> some View {
        content
            .background(Color.yellow)
            .border(Color.red)
    }
}

struct ContentView: View {
    var body: some View {
        Text("Hello, World!")
            .modifier(modifier)
    }

    var modifier: some ViewModifier {
        #if DEBUG
            return EmphasizedLayout()
        #else
            return EmptyModifier()
        #endif
    }
}
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [ViewModifier](viewmodifier.md)

## Topics

### Creating an empty modifier

- [init()](<emptymodifier/init().md>)

### Getting the identity modifier

- [identity](emptymodifier/identity.md)

## See Also

### Modifying a view

- [Configuring views](configuring-views.md) — Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md) — Bundle view modifiers that you regularly reuse into a custom view modifier.
- [modifier(_:)](<view/modifier(__).md>) — Applies a modifier to a view and returns a new view.
- [ViewModifier](viewmodifier.md) — A modifier that you apply to a view or another view modifier, producing a different version of the original value.
- [ModifiedContent](modifiedcontent.md) — A value with a modifier applied to it.
- [EnvironmentalModifier](environmentalmodifier.md) — A modifier that must resolve to a concrete modifier in an environment before use.
- [ManipulableModifier](manipulablemodifier.md)
- [ManipulableResponderModifier](manipulablerespondermodifier.md)
- [ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md)
- [ManipulationGeometryModifier](manipulationgeometrymodifier.md)
- [ManipulationGestureModifier](manipulationgesturemodifier.md)
- [ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md)
- [Manipulable](manipulable.md) — A namespace for various manipulable related types.
