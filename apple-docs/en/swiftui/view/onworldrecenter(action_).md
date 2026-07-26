---
title: 'onWorldRecenter(action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onworldrecenter(action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onworldrecenter(action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onworldrecenter%28action%3A%29.json'
content_hash: 'sha256:5f4367e5ac6dfa7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onWorldRecenter(action:)

<sub>Instance Method</sub>

Adds an action to perform when recentering the view with the digital crown.

<sub>visionOS</sub>

```swift
nonisolated func onWorldRecenter(action: @escaping @MainActor () -> Void) -> some View

```

## Parameters

- `action` — A closure to run when the view is recentered. This will run when the app has been recentered and is about to fade back in, equivalent to `WorldRecenterPhase.ended`.

## Discussion

```swift
struct ContentView: View {
    @State private var mascot = Mascot()
    var body: some View {
        WelcomeView(mascot: mascot)
            .onWorldRecenter {
                mascot.wave()
            }
    }
}
```

When the user recenters their view, the app will fade out and then be repositioned. Once it has been repositioned, the action will be called and the app will fade back in. The action will be called if the app is not backgrounded or suspended.

## See Also

### Immersive spaces

- [onImmersionChange(initial:_:)](<onimmersionchange(initial___).md>) — Performs an action when the immersion state of your app changes.
- [immersiveEnvironmentPicker(content:)](<immersiveenvironmentpicker(content_).md>) — Add menu items to open immersive spaces from a media player’s environment picker.
