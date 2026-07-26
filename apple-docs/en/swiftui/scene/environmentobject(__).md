---
title: 'environmentObject(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/environmentobject(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/environmentobject(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/environmentobject%28_%3A%29.json'
content_hash: 'sha256:b4f390b74cb677d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# environmentObject(_:)

<sub>Instance Method</sub>

Supplies an `ObservableObject` to a view subhierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func environmentObject<T>(_ object: T) -> some Scene where T : ObservableObject

```

## Parameters

- `object` — The object to store and make available to the scene’s subhierarchy.

## Discussion

The object can be read by any child by using `EnvironmentObject`:

```swift
final class Profile: ObservableObject { ... }

@main
struct MyApp: App {
    var body: some View {
        WindowGroup {
            ContentView()
        }
        .environment(ProfileService.currentProfile)
    }
}
```

You then read the object inside `ContentView` or one of its descendants using the [EnvironmentObject](../environmentobject.md) property wrapper:

```swift
struct ContentView: View {
    @EnvironmentObject private var currentAccount: Account

    var body: some View { ... }
}
```

## See Also

### Distributing model data throughout your app

- [environmentObject(_:)](<../view/environmentobject(__).md>) — Supplies an observable object to a view’s hierarchy.
- [EnvironmentObject](../environmentobject.md) — A property wrapper type for an observable object that a parent or ancestor view supplies.
