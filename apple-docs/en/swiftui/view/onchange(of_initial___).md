---
title: 'onChange(of:initial:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onchange(of:initial:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onchange(of:initial:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onchange%28of%3Ainitial%3A_%3A%29.json'
content_hash: 'sha256:711e41aafc20f15f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onChange(of:initial:_:)

<sub>Instance Method</sub>

Adds a modifier for this view that fires an action when a specific value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onChange<V>(of value: V, initial: Bool = false, _ action: @escaping () -> Void) -> some View where V : Equatable

```

## Parameters

- `value` — The value to check against when determining whether to run the closure.

- `initial` — Whether the action should be run when this view initially appears.

- `action` — A closure to run when the value changes.

## Return Value

A view that fires an action when the specified value changes.

## Discussion

You can use `onChange` to trigger a side effect as the result of a value changing, such as an `Environment` key or a `Binding`.

The system may call the action closure on the main actor, so avoid long-running tasks in the closure. If you need to perform such tasks, detach an asynchronous background task.

When the value changes, the new version of the closure will be called, so any captured values will have their values from the time that the observed value has its new value. In the following code example, `PlayerView` calls into its model when `playState` changes model.

```swift
struct PlayerView: View {
    var episode: Episode
    @State private var playState: PlayState = .paused

    var body: some View {
        VStack {
            Text(episode.title)
            Text(episode.showTitle)
            PlayButton(playState: $playState)
        }
        .onChange(of: playState) {
            model.playStateDidChange(state: playState)
        }
    }
}
```

## See Also

### Responding to data changes

- [onReceive(_:perform:)](<onreceive(__perform_).md>) — Adds an action to perform when this view detects data emitted by the given publisher.
