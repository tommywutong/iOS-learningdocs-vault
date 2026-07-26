---
title: 'environment(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/environment(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/environment(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/environment%28_%3A_%3A%29.json'
content_hash: 'sha256:343970b66baca487'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# environment(_:_:)

<sub>Instance Method</sub>

Sets the environment value of the specified key path to the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func environment<V>(_ keyPath: WritableKeyPath<EnvironmentValues, V>, _ value: V) -> some Scene

```

## Parameters

- `keyPath` — A key path that indicates the property of the [EnvironmentValues](../environmentvalues.md) structure to update.

- `value` — The new value to set for the item specified by `keyPath`.

## Return Value

A view that has the given value set in its environment.

## Discussion

Use this modifier to set one of the writable properties of the [EnvironmentValues](../environmentvalues.md) structure, including custom values that you create. For example, you can create a custom environment key `styleOverrides` to set a value that represents style settings that for the entire app:

```swift
WindowGroup {
    ContentView()
}
.environment(\.styleOverrides, StyleOverrides())
```

You then read the value inside `ContentView` or one of its descendants using the [Environment](../environment.md) property wrapper:

```swift
struct MyView: View {
    @Environment(\.styleOverrides) var styleOverrides: StyleOverrides

    var body: some View { ... }
}
```

This modifier affects the given scene, as well as that scene’s descendant views. It has no effect outside the view hierarchy on which you call it.

## See Also

### Modifying the environment of a scene

- [environment(_:)](<environment(__).md>) — Places an observable object in the scene’s environment.
- [transformEnvironment(_:transform:)](<transformenvironment(__transform_).md>) — Transforms the environment value of the specified key path with the given function.
