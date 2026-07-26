---
title: 'environment(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/environment(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/environment(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/environment%28_%3A_%3A%29.json'
content_hash: 'sha256:d8ab7d642062572b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# environment(_:_:)

<sub>Instance Method</sub>

Sets the environment value of the specified key path to the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func environment<V>(_ keyPath: WritableKeyPath<EnvironmentValues, V>, _ value: V) -> some View

```

## Parameters

- `keyPath` — A key path that indicates the property of the [EnvironmentValues](../environmentvalues.md) structure to update.

- `value` — The new value to set for the item specified by `keyPath`.

## Return Value

A view that has the given value set in its environment.

## Discussion

Use this modifier to set one of the writable properties of the [EnvironmentValues](../environmentvalues.md) structure, including custom values that you create. For example, you can set the value associated with the [truncationMode](../environmentvalues/truncationmode.md) key:

```swift
MyView()
    .environment(\.truncationMode, .head)
```

You then read the value inside `MyView` or one of its descendants using the [Environment](../environment.md) property wrapper:

```swift
struct MyView: View {
    @Environment(\.truncationMode) var truncationMode: Text.TruncationMode

    var body: some View { ... }
}
```

SwiftUI provides dedicated view modifiers for setting most environment values, like the [truncationMode(_:)](<truncationmode(__).md>) modifier which sets the [truncationMode](../environmentvalues/truncationmode.md) value:

```swift
MyView()
    .truncationMode(.head)
```

Prefer the dedicated modifier when available, and offer your own when defining custom environment values, as described in [Entry()](<../entry().md>).

This modifier affects the given view, as well as that view’s descendant views. It has no effect outside the view hierarchy on which you call it.

## See Also

### Modifying the environment of a view

- [environment(_:)](<environment(__).md>) — Places an observable object in the view’s environment.
- [transformEnvironment(_:transform:)](<transformenvironment(__transform_).md>) — Transforms the environment value of the specified key path with the given function.
