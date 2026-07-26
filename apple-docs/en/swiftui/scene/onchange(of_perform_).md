---
title: 'onChange(of:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+（17.0 起废弃）, iPadOS 14.0+（17.0 起废弃）, Mac Catalyst 14.0+（17.0 起废弃）, macOS 11.0+（14.0 起废弃）, tvOS 14.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 7.0+（10.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/scene/onchange(of:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/onchange(of:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/onchange%28of%3Aperform%3A%29.json'
content_hash: 'sha256:3dca73b950978e45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# onChange(of:perform:)

<sub>Instance Method</sub>

Adds an action to perform when the given value changes.

> [!warning] Deprecated
> Use [onChange(of:initial:_:)](<onchange(of_initial___)-7r9vn.md>) or [onChange(of:initial:_:)](<onchange(of_initial___)-7b6vh.md>) instead. The trailing closure in each case takes either zero or two input parameters, compared to this method which takes one. Be aware that the replacements have slightly different behavior. This modifier’s closure captures values that represent the state before the change. The new modifiers capture values that correspond to the new state. The new behavior makes it easier to perform updates that rely on values other than the one that caused the modifier’s closure to run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onChange<V>(of value: V, perform action: @escaping (V) -> Void) -> some Scene where V : Equatable

```

## Parameters

- `value` — The value to check when determining whether to run the closure. The value must conform to the [Equatable](../../swift/equatable.md) protocol.

- `action` — A closure to run when the value changes. The closure provides a single `newValue` parameter that indicates the changed value.

## Return Value

A scene that triggers an action in response to a change.

## Discussion

Use this modifier to trigger a side effect when a value changes, like the value associated with an [Environment](../environment.md) value or a [Binding](../binding.md). For example, you can clear a cache when you notice that a scene moves to the background:

```swift
struct MyScene: Scene {
    @Environment(\.scenePhase) private var scenePhase
    @StateObject private var cache = DataCache()

    var body: some Scene {
        WindowGroup {
            MyRootView()
        }
        .onChange(of: scenePhase) { newScenePhase in
            if newScenePhase == .background {
                cache.empty()
            }
        }
    }
}
```

The system may call the action closure on the main actor, so avoid long-running tasks in the closure. If you need to perform such tasks, detach an asynchronous background task:

```swift
.onChange(of: scenePhase) { newScenePhase in
    if newScenePhase == .background {
        Task.detached(priority: .background) {
            // ...
        }
    }
}
```

The system passes the new value into the closure. If you need the old value, capture it in the closure.
