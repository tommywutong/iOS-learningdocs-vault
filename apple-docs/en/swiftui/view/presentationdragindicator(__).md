---
title: 'presentationDragIndicator(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/presentationdragindicator(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/presentationdragindicator(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/presentationdragindicator%28_%3A%29.json'
content_hash: 'sha256:1dd2b56b0b8253c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# presentationDragIndicator(_:)

<sub>Instance Method</sub>

Sets the visibility of the drag indicator on top of a sheet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func presentationDragIndicator(_ visibility: Visibility) -> some View

```

## Parameters

- `visibility` — The preferred visibility of the drag indicator.

## Discussion

You can show a drag indicator when it isn’t apparent that a sheet can resize or when the sheet can’t dismiss interactively.

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
                .presentationDragIndicator(.visible)
        }
    }
}
```

## See Also

### Configuring a sheet’s height

- [presentationDetents(_:)](<presentationdetents(__).md>) — Sets the available detents for the enclosing sheet.
- [presentationDetents(_:selection:)](<presentationdetents(__selection_).md>) — Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [presentationContentInteraction(_:)](<presentationcontentinteraction(__).md>) — Configures the behavior of swipe gestures on a presentation.
- [PresentationDetent](../presentationdetent.md) — A type that represents a height where a sheet naturally rests.
- [CustomPresentationDetent](../custompresentationdetent.md) — The definition of a custom detent with a calculated height.
- [PresentationContentInteraction](../presentationcontentinteraction.md) — A behavior that you can use to influence how a presentation responds to swipe gestures.
