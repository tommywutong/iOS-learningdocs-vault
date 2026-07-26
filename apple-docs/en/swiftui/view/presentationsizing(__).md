---
title: 'presentationSizing(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/presentationsizing(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/presentationsizing(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/presentationsizing%28_%3A%29.json'
content_hash: 'sha256:65a126ccb016601f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# presentationSizing(_:)

<sub>Instance Method</sub>

Sets the sizing of the containing presentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func presentationSizing(_ sizing: some PresentationSizing) -> some View

```

## Parameters

- `sizing` — A value dictating size to propose to presentation content and how the presentation responds to changes in content size.

## Discussion

Use this modifier to apply a [PresentationSizing](../presentationsizing.md) to a presentation like [sheet(isPresented:onDismiss:content:)](<sheet(ispresented_ondismiss_content_).md>). The `sizing` parameter defines the size proposed to the content, and the presentation adopts the returned size. The default value is `automatic`.

Sizings can be modified to fix their dimensions based on the content, and optionally be sticky.

> [!info] See Also
> [fitted(horizontal:vertical:)](<../presentationsizing/fitted(horizontal_vertical_).md>) and [sticky(horizontal:vertical:)](<../presentationsizing/sticky(horizontal_vertical_).md>).

> [!note] Note
> If the presentation’s root container is a `NavigationSplitView`, the proposed width only applies to the `detail` column. The `sidebar` and `content` column widths use system-provided values, or those from [navigationSplitViewColumnWidth(_:)](<navigationsplitviewcolumnwidth(__).md>) or [navigationSplitViewColumnWidth(min:ideal:max:)](<navigationsplitviewcolumnwidth(min_ideal_max_).md>) modifiers.

For example, a presentation with facts about flowers could prefer `.page` sizing because its content is primarily informational. Since the user can choose different flowers from the picker, each with different lengths of information, the size is fitted vertically to size the sheet to the textual content, and vertically sticky is specified to prevent the presentation from changing size too frequently as the user changes selection.

```swift
struct ContentView: View {
    @State private var presentInfo = true

    var body: some View {
        ContentView.sheet(isPresented: $presentInfo) {
            VStack {
                Picker("Flower Species", selection: $flower) {
                    ForEach(Flower.allCases) {
                        Text($0.rawValue.uppercased()).tag($0)
                    }
                }
                Text(flower.emoji).font(.largeTitle)
                Text(flower.informationalText)
            }
            .frame(maxHeight: .infinity, alignment: .top)
            .padding()
            .presentationSizing(
                .page
                    .fitted(horizontal: false, vertical: true)
                    .sticky(horizontal: false, vertical: true))
        }
    }
}
```

## See Also

### Adapting a presentation size

- [presentationCompactAdaptation(horizontal:vertical:)](<presentationcompactadaptation(horizontal_vertical_).md>) — Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [presentationCompactAdaptation(_:)](<presentationcompactadaptation(__).md>) — Specifies how to adapt a presentation to compact size classes.
- [PresentationAdaptation](../presentationadaptation.md) — Strategies for adapting a presentation to a different size class.
- [PresentationSizing](../presentationsizing.md) — A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.
- [PresentationSizingRoot](../presentationsizingroot.md) — A proxy to a view provided to the presentation with a defined presentation size.
- [PresentationSizingContext](../presentationsizingcontext.md) — Contextual information about a presentation.
