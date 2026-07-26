---
title: 'realityViewLayoutBehavior(_:)'
framework: RealityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/realityviewlayoutbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/realityviewlayoutbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/realityviewlayoutbehavior%28_%3A%29.json'
content_hash: 'sha256:10c9487f68ec9b7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# realityViewLayoutBehavior(_:)

<sub>Instance Method</sub>

A view modifier that controls the frame sizing and content alignment behavior for `RealityView`

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func realityViewLayoutBehavior(_ layoutOption: RealityViewLayoutOption) -> some View

```

## Discussion

This modifier is only accounted for after the end of the `make` closure. It isn’t checked on any calls to the `update` closure.

```swift
struct ModelWrapperView: View {
    let modelName: String
    var body: some View {
        RealityView { content in
            let model = try? await Entity(named: modelName)
            if let model {
                content.add(model)
            }
        }
        .realityViewLayoutBehavior(.fixedSize)
    }
}
```

See [RealityViewLayoutOption](../../realitykit/realityviewlayoutoption.md) for a list of options to pass into `realityViewLayoutBehavior(_:)`.

## See Also

### Configuring camera controls

- [realityViewCameraControls](../environmentvalues/realityviewcameracontrols.md) — The camera controls for the reality view.
- [realityViewCameraControls(_:)](<realityviewcameracontrols(__).md>) — Adds gestures that control the position and direction of a virtual camera.
