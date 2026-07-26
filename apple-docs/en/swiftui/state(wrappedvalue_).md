---
title: 'State(wrappedValue:)'
framework: SwiftUI
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/state(wrappedvalue:)'
source_url: 'https://developer.apple.com/documentation/swiftui/state(wrappedvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/state%28wrappedvalue%3A%29.json'
content_hash: 'sha256:52c890566813805f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# State(wrappedValue:)

<sub>Macro</sub>

Creates a property with a wrapped value that can read and write a value managed by SwiftUI.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(accessor, names: named(init), named(get), named(set)) @attached(peer, names: prefixed(`_`), prefixed(__), prefixed(`$`)) macro State<Value>(wrappedValue: Value)
```

## Overview

> [!important] Important
> When you build with Xcode 26 or earlier, the system uses the [State](state.md) property wrapper instead.

Use state as the single source of truth for a given value type that you store in a view hierarchy. Create a state value in an [App](app.md), [Scene](scene.md), or [View](view.md) by applying the `@State` attribute to a property declaration with an initial value. Declare state as private to prevent setting it in an initializer, which can conflict with the storage management that SwiftUI provides:

```swift
struct PlayButton: View {
    @State private var isPlaying: Bool = false // Create the state.

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") { // Read the state.
            isPlaying.toggle() // Write the state.
        }
    }
}
```

For more information on sharing state properties with subviews, and storing [Observable](../observation/observable.md) objects in state, see [State()](<state().md>).

## See Also

### Creating and sharing view state

- [Managing user interface state](managing-user-interface-state.md) — Encapsulate view-specific data within your app’s view hierarchy to make your views reusable.
- [State()](<state().md>) — Creates a property that can read and write a value managed by SwiftUI.
- [State(initialValue:)](<state(initialvalue_).md>) — Creates a property with an initial value that can read and write a value managed by SwiftUI.
- [State](state.md) — A property wrapper type that can read and write a value managed by SwiftUI.
- [Bindable](bindable.md) — A property wrapper type that supports creating bindings to the mutable properties of observable objects.
- [Binding](binding.md) — A property wrapper type that can read and write a value owned by a source of truth.
