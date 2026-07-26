---
title: 'environment(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/environment(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/environment(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/environment%28_%3A%29.json'
content_hash: 'sha256:5370f9654a0a17f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# environment(_:)

<sub>Instance Method</sub>

Places an observable object in the view’s environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func environment<T>(_ object: T?) -> some View where T : AnyObject, T : Observable

```

## Parameters

- `object` — The object to set for this object’s type in the environment, or `nil` to clear an object of this type from the environment.

## Return Value

A view that has the specified object in its environment.

## Discussion

Use this modifier to place an object that you declare with the [Observable()](<../../observation/observable().md>) macro into a view’s environment. For example, you can add an instance of a custom observable `Profile` class to the environment of a `ContentView`:

```swift
@Observable class Profile { ... }

struct RootView: View {
    @State private var currentProfile: Profile?

    var body: some View {
        ContentView()
            .environment(currentProfile)
    }
}
```

You then read the object inside `ContentView` or one of its descendants using the [Environment](../environment.md) property wrapper:

```swift
struct ContentView: View {
    @Environment(Profile.self) private var currentProfile: Profile

    var body: some View { ... }
}
```

This modifier affects the given view, as well as that view’s descendant views. It has no effect outside the view hierarchy on which you call it. The environment of a given view hierarchy holds only one observable object of a given type.

> [!note] Note
> This modifier takes an object that conforms to the [Observable](../../observation/observable.md) protocol. To add environment objects that conform to the [ObservableObject](../../combine/observableobject.md) protocol, use [environmentObject(_:)](<environmentobject(__).md>) instead.

## See Also

### Modifying the environment of a view

- [environment(_:_:)](<environment(____).md>) — Sets the environment value of the specified key path to the given value.
- [transformEnvironment(_:transform:)](<transformenvironment(__transform_).md>) — Transforms the environment value of the specified key path with the given function.
