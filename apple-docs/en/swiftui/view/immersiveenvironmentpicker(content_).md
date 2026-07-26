---
title: 'immersiveEnvironmentPicker(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/immersiveenvironmentpicker(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/immersiveenvironmentpicker(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/immersiveenvironmentpicker%28content%3A%29.json'
content_hash: 'sha256:78a58fcbd08979bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# immersiveEnvironmentPicker(content:)

<sub>Instance Method</sub>

Add menu items to open immersive spaces from a media player’s environment picker.

<sub>visionOS</sub>

```swift
nonisolated func immersiveEnvironmentPicker<Content>(@ContentBuilder content: () -> Content) -> some View where Content : View

```

## Discussion

These items are added alongside recently used system environments.

```swift
SystemPlayerView(player: player)
    .immersiveEnvironmentPicker {
        Button("Chalet", systemImage: "fireplace") {
            Task {
                await openImmersiveSpace(id: "Chalet")
            }
        }
    }
```

Use a [UIViewControllerRepresentable](../uiviewcontrollerrepresentable.md) instance to display a [AVPlayerViewController](../../avkit/avplayerviewcontroller.md) class in your SwiftUI interface.

```swift
struct SystemPlayerView: UIViewControllerRepresentable {
    let player: AVPlayer

    func makeUIViewController(context: Context) -> AVPlayerViewController {
        return AVPlayerViewController()
    }

    func updateUIViewController(_ avPlayerViewController: AVPlayerViewController, context: Context) {
        viewController.player = player
    }
}
```

Items will be donated to media players (like [AVPlayerViewController](../../avkit/avplayerviewcontroller.md)) downstream in the hierarchy.

> [!note] Note
> View the sample code in [Building an immersive media viewing experience](../../visionos/building-an-immersive-media-viewing-experience.md) to see an immersive space in action.
