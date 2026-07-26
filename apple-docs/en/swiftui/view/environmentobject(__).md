---
title: 'environmentObject(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/environmentobject(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/environmentobject(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/environmentobject%28_%3A%29.json'
content_hash: 'sha256:062fe42a8bdb4be0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# environmentObject(_:)

<sub>Instance Method</sub>

Supplies an observable object to a view’s hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func environmentObject<T>(_ object: T) -> some View where T : ObservableObject

```

## Parameters

- `object` — The object to store and make available to the view’s hierarchy.

## Discussion

Use this modifier to add an observable object to a view’s environment. The object must conform to the [ObservableObject](../../combine/observableobject.md) protocol.

Adding an object to a view’s environment makes the object available to subviews in the view’s hierarchy. To retrieve the object in a subview, use the [EnvironmentObject](../environmentobject.md) property wrapper.

> [!note] Note
> If the observable object conforms to the [Observable](../../observation/observable.md) protocol, use either [environment(_:)](<environment(__).md>) or the [environment(_:_:)](<environment(____).md>) modifier to add the object to the view’s environment.

## See Also

### Distributing model data throughout your app

- [environmentObject(_:)](<../scene/environmentobject(__).md>) — Supplies an `ObservableObject` to a view subhierarchy.
- [EnvironmentObject](../environmentobject.md) — A property wrapper type for an observable object that a parent or ancestor view supplies.
