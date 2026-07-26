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
doc_path: '/documentation/swiftui/view/onchange(of:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onchange(of:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onchange%28of%3Aperform%3A%29.json'
content_hash: 'sha256:505717091f912dec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onChange(of:perform:)

<sub>Instance Method</sub>

Adds an action to perform when the given value changes.

> [!warning] Deprecated
> Use [onChange(of:initial:_:)](<onchange(of_initial___)-8wgw9.md>) or [onChange(of:initial:_:)](<onchange(of_initial___)-4psgg.md>) instead. The trailing closure in each case takes either zero or two input parameters, compared to this method which takes one. Be aware that the replacements have slightly different behavior. This modifier’s closure captures values that represent the state before the change. The new modifiers capture values that correspond to the new state. The new behavior makes it easier to perform updates that rely on values other than the one that caused the modifier’s closure to run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onChange<V>(of value: V, perform action: @escaping (V) -> Void) -> some View where V : Equatable

```

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

## See Also

### Input and events modifiers

- [dropDestination(for:action:isTargeted:)](<dropdestination(for_action_istargeted_).md>) — Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify. _(deprecated)_
- [onTapGesture(count:coordinateSpace:perform:)](<ontapgesture(count_coordinatespace_perform_)-36x9h.md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction. _(deprecated)_
- [onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)](<onlongpressgesture(minimumduration_maximumdistance_pressing_perform_).md>) — Adds an action to perform when this view recognizes a long press gesture. _(deprecated)_
- [onLongPressGesture(minimumDuration:pressing:perform:)](<onlongpressgesture(minimumduration_pressing_perform_).md>) — Adds an action to perform when this view recognizes a long press gesture. _(deprecated)_
- [onPasteCommand(of:perform:)](<onpastecommand(of_perform_)-4f78f.md>) — Adds an action to perform in response to the system’s Paste command. _(deprecated)_
- [onPasteCommand(of:validator:perform:)](<onpastecommand(of_validator_perform_)-964k1.md>) — Adds an action to perform in response to the system’s Paste command with items that you validate. _(deprecated)_
- [onDrop(of:delegate:)](<ondrop(of_delegate_)-2vr9o.md>) — Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate. _(deprecated)_
- [onDrop(of:isTargeted:perform:)](<ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [focusable(_:onFocusChange:)](<focusable(__onfocuschange_).md>) — Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus. _(deprecated)_
- [onContinuousHover(coordinateSpace:perform:)](<oncontinuoushover(coordinatespace_perform_)-8gyrl.md>) — Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds. _(deprecated)_
