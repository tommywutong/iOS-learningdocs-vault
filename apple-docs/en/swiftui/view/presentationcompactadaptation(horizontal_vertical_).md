---
title: 'presentationCompactAdaptation(horizontal:vertical:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/presentationcompactadaptation(horizontal:vertical:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/presentationcompactadaptation(horizontal:vertical:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/presentationcompactadaptation%28horizontal%3Avertical%3A%29.json'
content_hash: 'sha256:4d5e53000b9a6008'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# presentationCompactAdaptation(horizontal:vertical:)

<sub>Instance Method</sub>

Specifies how to adapt a presentation to horizontally and vertically compact size classes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func presentationCompactAdaptation(horizontal horizontalAdaptation: PresentationAdaptation, vertical verticalAdaptation: PresentationAdaptation) -> some View

```

## Parameters

- `horizontalAdaptation` — The adaptation to use in a horizontally compact size class.

- `verticalAdaptation` — The adaptation to use in a vertically compact size class. In a size class that is both horizontally and vertically compact, SwiftUI uses the `verticalAdaptation` value.

## Discussion

Some presentations adapt their appearance depending on the context. For example, a popover presentation over a horizontally-compact view uses a sheet appearance by default. Use this modifier to indicate a custom adaptation preference.

```swift
struct ContentView: View {
    @State private var showInfo = false

    var body: some View {
        Button("View Info") {
            showInfo = true
        }
        .popover(isPresented: $showInfo) {
            InfoView()
                .presentationCompactAdaptation(
                    horizontal: .popover,
                    vertical: .sheet)
        }
    }
}
```

If you want to specify the same adaptation for both dimensions, use the [presentationCompactAdaptation(_:)](<presentationcompactadaptation(__).md>) method instead.

## See Also

### Adapting a presentation size

- [presentationCompactAdaptation(_:)](<presentationcompactadaptation(__).md>) — Specifies how to adapt a presentation to compact size classes.
- [PresentationAdaptation](../presentationadaptation.md) — Strategies for adapting a presentation to a different size class.
- [presentationSizing(_:)](<presentationsizing(__).md>) — Sets the sizing of the containing presentation.
- [PresentationSizing](../presentationsizing.md) — A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.
- [PresentationSizingRoot](../presentationsizingroot.md) — A proxy to a view provided to the presentation with a defined presentation size.
- [PresentationSizingContext](../presentationsizingcontext.md) — Contextual information about a presentation.
