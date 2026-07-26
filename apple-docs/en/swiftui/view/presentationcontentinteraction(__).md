---
title: 'presentationContentInteraction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/presentationcontentinteraction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/presentationcontentinteraction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/presentationcontentinteraction%28_%3A%29.json'
content_hash: 'sha256:f087503f6a41a70c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# presentationContentInteraction(_:)

<sub>Instance Method</sub>

Configures the behavior of swipe gestures on a presentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func presentationContentInteraction(_ behavior: PresentationContentInteraction) -> some View

```

## Parameters

- `behavior` — The requested behavior.

## Discussion

By default, when a person swipes up on a scroll view in a resizable presentation, the presentation grows to the next detent. A scroll view embedded in the presentation only scrolls after the presentation reaches its largest size. Use this modifier to control which action takes precedence.

For example, you can request that swipe gestures scroll content first, resizing the sheet only after hitting the end of the scroll view, by passing the [scrolls](../presentationcontentinteraction/scrolls.md) value to this modifier:

```swift
struct ContentView: View {
    @State private var showSettings = false

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView()
                .presentationDetents([.medium, .large])
                .presentationContentInteraction(.scrolls)
        }
    }
}
```

People can always resize your presentation using the drag indicator.

## See Also

### Configuring a sheet’s height

- [presentationDetents(_:)](<presentationdetents(__).md>) — Sets the available detents for the enclosing sheet.
- [presentationDetents(_:selection:)](<presentationdetents(__selection_).md>) — Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [presentationDragIndicator(_:)](<presentationdragindicator(__).md>) — Sets the visibility of the drag indicator on top of a sheet.
- [PresentationDetent](../presentationdetent.md) — A type that represents a height where a sheet naturally rests.
- [CustomPresentationDetent](../custompresentationdetent.md) — The definition of a custom detent with a calculated height.
- [PresentationContentInteraction](../presentationcontentinteraction.md) — A behavior that you can use to influence how a presentation responds to swipe gestures.
