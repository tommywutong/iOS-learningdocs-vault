---
title: Binding
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/binding
source_url: 'https://developer.apple.com/documentation/swiftui/binding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/binding.json'
content_hash: 'sha256:2f79cffdcb2cfbdb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Binding

<sub>Structure</sub>

A property wrapper type that can read and write a value owned by a source of truth.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen @propertyWrapper @dynamicMemberLookup struct Binding<Value>
```

## Overview

Use a binding to create a two-way connection between a property that stores data, and a view that displays and changes the data. A binding connects a property to a source of truth stored elsewhere, instead of storing data directly. For example, a button that toggles between play and pause can create a binding to a property of its parent view using the `Binding` property wrapper.

```swift
struct PlayButton: View {
    @Binding var isPlaying: Bool

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") {
            isPlaying.toggle()
        }
    }
}
```

The parent view declares a property to hold the playing state, using the [State](state.md) property wrapper to indicate that this property is the value’s source of truth.

```swift
struct PlayerView: View {
    var episode: Episode
    @State private var isPlaying: Bool = false

    var body: some View {
        VStack {
            Text(episode.title)
                .foregroundStyle(isPlaying ? .primary : .secondary)
            PlayButton(isPlaying: $isPlaying) // Pass a binding.
        }
    }
}
```

When `PlayerView` initializes `PlayButton`, it passes a binding of its state property into the button’s binding property. Applying the `$` prefix to a property wrapped value returns its [projectedValue](state/projectedvalue.md), which for a state property wrapper returns a binding to the value.

Whenever the user taps the `PlayButton`, the `PlayerView` updates its `isPlaying` state.

A binding conforms to `Sendable` only if its wrapped value type also conforms to `Sendable`. It is always safe to pass a sendable binding between different concurrency domains. However, reading from or writing to a binding’s wrapped value from a different concurrency domain may or may not be safe, depending on how the binding was created. SwiftUI will issue a warning at runtime if it detects a binding being used in a way that may compromise data safety.

> [!note] Note
> To create bindings to properties of a type that conforms to the [Observable](../observation/observable.md) protocol, use the [Bindable](bindable.md) property wrapper. For more information, see [Migrating from the Observable Object protocol to the Observable macro](migrating-from-the-observable-object-protocol-to-the-observable-macro.md).

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [Copyable](../swift/copyable.md), [DynamicProperty](dynamicproperty.md), [Escapable](../swift/escapable.md), [Identifiable](../swift/identifiable.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Creating a binding

- [init(_:)](<binding/init(__).md>) — Creates a binding by projecting the base value to a hashable value.
- [init(projectedValue:)](<binding/init(projectedvalue_).md>) — Creates a binding from the value of another binding.
- [init(get:set:)](<binding/init(get_set_).md>) — Creates a binding with closures that read and write the binding value.
- [constant(_:)](<binding/constant(__).md>) — Creates a binding with an immutable value.

### Getting the value

- [wrappedValue](binding/wrappedvalue.md) — The underlying value referenced by the binding variable.
- [projectedValue](binding/projectedvalue.md) — A projection of the binding value that returns a binding.
- [subscript(dynamicMember:)](<binding/subscript(dynamicmember_).md>) — Returns a binding to the resulting value of a given key path.

### Managing changes

- [id](binding/id.md) — The stable identity of the entity associated with this instance, corresponding to the `id` of the binding’s wrapped value.
- [animation(_:)](<binding/animation(__).md>) — Specifies an animation to perform when the binding value changes.
- [transaction(_:)](<binding/transaction(__).md>) — Specifies a transaction for the binding.
- [transaction](binding/transaction.md) — The binding’s transaction.

### Subscripts

- [subscript(_:)](<binding/subscript(__).md>)

### Default Implementations

- [Identifiable Implementations](binding/identifiable-implementations.md)

## See Also

### Creating and sharing view state

- [Managing user interface state](managing-user-interface-state.md) — Encapsulate view-specific data within your app’s view hierarchy to make your views reusable.
- [State()](<state().md>) — Creates a property that can read and write a value managed by SwiftUI.
- [State(initialValue:)](<state(initialvalue_).md>) — Creates a property with an initial value that can read and write a value managed by SwiftUI.
- [State(wrappedValue:)](<state(wrappedvalue_).md>) — Creates a property with a wrapped value that can read and write a value managed by SwiftUI.
- [State](state.md) — A property wrapper type that can read and write a value managed by SwiftUI.
- [Bindable](bindable.md) — A property wrapper type that supports creating bindings to the mutable properties of observable objects.
