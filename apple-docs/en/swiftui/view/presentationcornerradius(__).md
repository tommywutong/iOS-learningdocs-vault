---
title: 'presentationCornerRadius(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/presentationcornerradius(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/presentationcornerradius(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/presentationcornerradius%28_%3A%29.json'
content_hash: 'sha256:7cbc88f4d10dfa06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# presentationCornerRadius(_:)

<sub>Instance Method</sub>

Requests that the presentation have a specific corner radius.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func presentationCornerRadius(_ cornerRadius: CGFloat?) -> some View

```

## Parameters

- `cornerRadius` — The corner radius, or `nil` to use the system default.

## Discussion

Use this modifier to change the corner radius of a presentation.

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
                .presentationCornerRadius(21)
        }
    }
}
```

> [!note] Note
> Configuring a corner radius is not supported on watchOS, tvOS, or macOS.

## See Also

### Styling a sheet and its background

- [presentationBackground(_:)](<presentationbackground(__).md>) — Sets the presentation background of the enclosing sheet using a shape style.
- [presentationBackground(alignment:content:)](<presentationbackground(alignment_content_).md>) — Sets the presentation background of the enclosing sheet to a custom view.
- [presentationBackgroundInteraction(_:)](<presentationbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presentation.
- [PresentationBackgroundInteraction](../presentationbackgroundinteraction.md) — The kinds of interaction available to views behind a presentation.
