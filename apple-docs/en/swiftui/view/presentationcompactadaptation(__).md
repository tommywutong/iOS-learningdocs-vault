---
title: 'presentationCompactAdaptation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/presentationcompactadaptation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/presentationcompactadaptation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/presentationcompactadaptation%28_%3A%29.json'
content_hash: 'sha256:ef48e72b08666747'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# presentationCompactAdaptation(_:)

<sub>Instance Method</sub>

Specifies how to adapt a presentation to compact size classes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func presentationCompactAdaptation(_ adaptation: PresentationAdaptation) -> some View

```

## Parameters

- `adaptation` — The adaptation to use in either a horizontally or vertically compact size class.

## Discussion

Some presentations adapt their appearance depending on the context. For example, a sheet presentation over a vertically-compact view uses a full-screen-cover appearance by default. Use this modifier to indicate a custom adaptation preference. For example, the following code uses a presentation adaptation value of [none](../presentationadaptation/none.md) to request that the system not adapt the sheet in compact size classes:

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
                .presentationCompactAdaptation(.none)
        }
    }
}
```

If you want to specify different adaptations for each dimension, use the [presentationCompactAdaptation(horizontal:vertical:)](<presentationcompactadaptation(horizontal_vertical_).md>) method instead.

## See Also

### Adapting a presentation size

- [presentationCompactAdaptation(horizontal:vertical:)](<presentationcompactadaptation(horizontal_vertical_).md>) — Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [PresentationAdaptation](../presentationadaptation.md) — Strategies for adapting a presentation to a different size class.
- [presentationSizing(_:)](<presentationsizing(__).md>) — Sets the sizing of the containing presentation.
- [PresentationSizing](../presentationsizing.md) — A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.
- [PresentationSizingRoot](../presentationsizingroot.md) — A proxy to a view provided to the presentation with a defined presentation size.
- [PresentationSizingContext](../presentationsizingcontext.md) — Contextual information about a presentation.
