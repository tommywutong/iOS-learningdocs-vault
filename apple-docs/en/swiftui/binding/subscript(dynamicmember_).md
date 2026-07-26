---
title: 'subscript(dynamicMember:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/binding/subscript(dynamicmember:)'
source_url: 'https://developer.apple.com/documentation/swiftui/binding/subscript(dynamicmember:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/binding/subscript%28dynamicmember%3A%29.json'
content_hash: 'sha256:e2e9486c9f932bba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Binding](../binding.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns a binding to the resulting value of a given key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<Subject>(dynamicMember keyPath: WritableKeyPath<Value, Subject>) -> Binding<Subject> { get }
```

## Parameters

- `keyPath` — A key path to a specific resulting value.

## Return Value

A new binding.

## Overview

Use dynamic member lookup to project a property of the binding’s wrapped value from a key path into a new binding. The returned value is read from, and written to, the original binding. This can be useful when a view accepts a binding for a type that only matches a property of a value from an existing binding.

For example, the `PlayerView` controls the current position for an episode using a `Slider`, and whether the episode is a favorite using a `Toggle`. The view projects the `currentPosition` and `isFavorite` properties of `Episode` into bindings that each of these views accept using dynamic member lookup.

```swift
struct Episode {
    var title: LocalizedStringKey
    var duration: TimeInterval
    var currentPosition: TimeInterval
    var isFavorite: Bool
}

struct PlayerView: View {
    @Binding var episode: Episode

    var body: some View {
        Text(episode.title)
        Toggle("Favorite", isOn: $episode.isFavorite)
        Slider(
            value: $episode.currentPosition,
            in: 0...episode.duration
        )
    }
}
```

## See Also

### Getting the value

- [wrappedValue](wrappedvalue.md) — The underlying value referenced by the binding variable.
- [projectedValue](projectedvalue.md) — A projection of the binding value that returns a binding.
