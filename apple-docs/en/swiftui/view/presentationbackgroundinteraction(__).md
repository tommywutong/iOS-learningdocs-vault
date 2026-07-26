---
title: 'presentationBackgroundInteraction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/presentationbackgroundinteraction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/presentationbackgroundinteraction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/presentationbackgroundinteraction%28_%3A%29.json'
content_hash: 'sha256:c2f917e9dc1922eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# presentationBackgroundInteraction(_:)

<sub>Instance Method</sub>

Controls whether people can interact with the view behind a presentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func presentationBackgroundInteraction(_ interaction: PresentationBackgroundInteraction) -> some View

```

## Parameters

- `interaction` — A specification of how people can interact with the view behind a presentation.

## Discussion

On many platforms, SwiftUI automatically disables the view behind a sheet that you present, so that people can’t interact with the backing view until they dismiss the sheet. Use this modifier if you want to enable interaction.

The following example enables people to interact with the view behind the sheet when the sheet is at the smallest detent, but not at the other detents:

```swift
struct ContentView: View {
    @State private var showSettings = false

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView()
                .presentationDetents(
                    [.height(120), .medium, .large])
                .presentationBackgroundInteraction(
                    .enabled(upThrough: .height(120)))
        }
    }
}
```

## See Also

### Styling a sheet and its background

- [presentationCornerRadius(_:)](<presentationcornerradius(__).md>) — Requests that the presentation have a specific corner radius.
- [presentationBackground(_:)](<presentationbackground(__).md>) — Sets the presentation background of the enclosing sheet using a shape style.
- [presentationBackground(alignment:content:)](<presentationbackground(alignment_content_).md>) — Sets the presentation background of the enclosing sheet to a custom view.
- [PresentationBackgroundInteraction](../presentationbackgroundinteraction.md) — The kinds of interaction available to views behind a presentation.
