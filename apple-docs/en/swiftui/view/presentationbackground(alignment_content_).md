---
title: 'presentationBackground(alignment:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/presentationbackground(alignment:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/presentationbackground(alignment:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/presentationbackground%28alignment%3Acontent%3A%29.json'
content_hash: 'sha256:b015efd92c99129b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# presentationBackground(alignment:content:)

<sub>Instance Method</sub>

Sets the presentation background of the enclosing sheet to a custom view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func presentationBackground<V>(alignment: Alignment = .center, @ContentBuilder content: () -> V) -> some View where V : View

```

## Parameters

- `alignment` — The alignment that the modifier uses to position the implicit [ZStack](../zstack.md) that groups the background views. The default is [center](../alignment/center.md).

- `content` — The view to use as the background of the presentation.

## Discussion

The following example uses a yellow view as the sheet background:

```swift
struct ContentView: View {
    @State private var showSettings = false

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView()
                .presentationBackground {
                    Color.yellow
                }
        }
    }
}
```

The `presentationBackground(alignment:content:)` modifier differs from the [background(alignment:content:)](<background(alignment_content_).md>) modifier in several key ways. A presentation background:

- Automatically fills the entire presentation.
- Allows views behind the presentation to show through translucent areas of the `content` on supported platforms.

> [!note] Note
> Sheet presentations on macOS do not support translucency or transparency — the background is always opaque.

## See Also

### Styling a sheet and its background

- [presentationCornerRadius(_:)](<presentationcornerradius(__).md>) — Requests that the presentation have a specific corner radius.
- [presentationBackground(_:)](<presentationbackground(__).md>) — Sets the presentation background of the enclosing sheet using a shape style.
- [presentationBackgroundInteraction(_:)](<presentationbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presentation.
- [PresentationBackgroundInteraction](../presentationbackgroundinteraction.md) — The kinds of interaction available to views behind a presentation.
