---
title: 'presentationBackground(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/presentationbackground(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/presentationbackground(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/presentationbackground%28_%3A%29.json'
content_hash: 'sha256:0fb4f1b4a540d7af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# presentationBackground(_:)

<sub>Instance Method</sub>

Sets the presentation background of the enclosing sheet using a shape style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func presentationBackground<S>(_ style: S) -> some View where S : ShapeStyle

```

## Parameters

- `style` — The shape style to use as the presentation background.

## Discussion

The following example uses the [thick](../material/thick.md) material as the sheet background:

```swift
struct ContentView: View {
    @State private var showSettings = false

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView()
                .presentationBackground(.thickMaterial)
        }
    }
}
```

The `presentationBackground(_:)` modifier differs from the [background(_:ignoresSafeAreaEdges:)](<background(__ignoressafeareaedges_).md>) modifier in several key ways. A presentation background:

- Automatically fills the entire presentation.
- Allows views behind the presentation to show through translucent styles on supported platforms.

> [!note] Note
> Sheet presentations on macOS do not support translucency or transparency — the background is always opaque.

## See Also

### Styling a sheet and its background

- [presentationCornerRadius(_:)](<presentationcornerradius(__).md>) — Requests that the presentation have a specific corner radius.
- [presentationBackground(alignment:content:)](<presentationbackground(alignment_content_).md>) — Sets the presentation background of the enclosing sheet to a custom view.
- [presentationBackgroundInteraction(_:)](<presentationbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presentation.
- [PresentationBackgroundInteraction](../presentationbackgroundinteraction.md) — The kinds of interaction available to views behind a presentation.
