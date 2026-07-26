---
title: 'onAvailabilityChange(perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/sceneaccessorycontent/onavailabilitychange(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/sceneaccessorycontent/onavailabilitychange(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sceneaccessorycontent/onavailabilitychange%28perform%3A%29.json'
content_hash: 'sha256:89344d1a5b99e695'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SceneAccessoryContent](../sceneaccessorycontent.md)

# onAvailabilityChange(perform:)

<sub>Instance Method</sub>

Defines a callback for observing the availability of `self`.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated func onAvailabilityChange(perform action: @escaping (Bool) -> Void) -> some SceneAccessoryContent

```

## Discussion

When the availability of a scene accessory changes, the specified closure will be called.

For example, you can include additional controls based on the availability:

```swift
struct RootView: View {
    @State private var isEnabled = false
    @State private var isAvailable = false
    var document: PresentationDocument

    var body: some View {
        PresentationDocumentView(document: document)
            .toolbar {
                if isAvailable {
                    // Include a toolbar button to enable the
                    // scene accessory when a display is available.
                    SecondaryDisplayToggle(isEnabled: $isEnabled)
                }
            }
            .sceneAccessory {
                ExternalNonInteractiveAccessory(
                    isEnabled: $isEnabled
                ) {
                    PresentationPreview(document: document)
                }
                .onAvailabilityChange { newValue in
                    isAvailable = newValue
                }
            }
    }
}
```
