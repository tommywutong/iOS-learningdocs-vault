---
title: 'sceneAccessory(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/sceneaccessory(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/sceneaccessory(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/sceneaccessory%28content%3A%29.json'
content_hash: 'sha256:e5742ff65eec64c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# sceneAccessory(content:)

<sub>Instance Method</sub>

Defines any scene accessories associated with `self`.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated func sceneAccessory<C>(@ContentBuilder content: () -> C) -> some View where C : SceneAccessoryContent

```

## Discussion

A scene accessory declares supplementary content that the system presents on the app’s behalf when an associated piece of system functionality becomes available, for example when an external display is connected. The app declares what content to provide; the system decides when and where to present it. Scene accessories enhance the app’s experience when available, but the app must remain fully functional without them.

For example, you can define a scene accessory for previewing a non-interactive presentation, which may be presented when an external display is connected:

```swift
struct RootView: View {
    var document: PresentationDocument

    var body: some View {
        PresentationDocumentView(document: document)
            .sceneAccessory {
                ExternalNonInteractiveAccessory {
                    PresentationPreview(document: document)
                }
            }
    }
}
```

Use the `SceneAccessoryContent/onAvailabilityChange` modifier to observe a scene accessory’s system-determined availability. Observe the lifecycle of the accessory’s content using `View/onAppear`, `View/onDisappear`, and [scenePhase](../environmentvalues/scenephase.md).

For example, you can present various controls based on the scene accessory’s current state:

```swift
struct RootView: View {
    @State private var isEnabled = false
    @State private var isAvailable = false
    @State private var isPresented = false
    var document: PresentationDocument

    var body: some View {
        PresentationDocumentView(document: document)
            .toolbar {
                if isAvailable {
                    // Include a toolbar button to enable the
                    // scene accessory when a display is available.
                    SecondaryDisplayToggle(isEnabled: $isEnabled)

                    // Include additional toolbar controls once the
                    // accessory is presented.
                    if isPresented {
                        SecondaryDisplayControls()
                    }
                }
            }
            .sceneAccessory {
                ExternalNonInteractiveAccessory(
                    isEnabled: $isEnabled
                ) {
                    PresentationPreview(document: document)
                        .onAppear { isPresented = true }
                        .onDisappear { isPresented = false }
                }
                .onAvailabilityChange { newValue in
                    isAvailable = newValue
                }
            }
    }
}
```

## See Also

### Presenting content on an external display

- [SceneAccessoryContent](../sceneaccessorycontent.md) — Conforming types represent items which define content for scene accessories. _(beta)_
- [ExternalNonInteractiveAccessory](../externalnoninteractiveaccessory.md) — A scene accessory that presents non-interactive content on an external display. _(beta)_
