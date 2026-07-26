---
title: selection
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shapestyle/selection
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/selection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/selection.json'
content_hash: 'sha256:3db5421ea95c9697'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# selection

<sub>Type Property</sub>

A style used to visually indicate selection following platform conventional colors and behaviors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static var selection: SelectionShapeStyle { get }
```

## Discussion

For example:

```swift
ForEach(items) {
   ItemView(value: item, isSelected: item.id == selectedID)
}

struct ItemView {
    var value: item
    var isSelected: Bool

    var body: some View {
        // construct the actual cell content
            .background(isSelected
                ? AnyShapeStyle(.selection)
                    : AnyShapeStyle(.fill.quaternary),
                in: .rect(cornerRadius: 6))
    }
}
```

On macOS and iPadOS this automatically reflects window key state and focus state, where the emphasized appearance will be used only when the window is key and the nearest focusable element is actually focused. On iPhone, this will always fill with the environment’s accent color.

When applied as a background of another view, it will automatically set the `EnvironmentValues.backgroundProminence` for the environment of that view to match the current prominence of the selection.

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).

## See Also

### Semantic styles

- [foreground](foreground.md) — The foreground style in the current context.
- [background](background.md) — The background style in the current context.
- [separator](separator.md) — A style appropriate for foreground separator or border lines.
- [tint](tint.md) — A style that reflects the current tint color.
- [placeholder](placeholder.md) — A style appropriate for placeholder text.
- [link](link.md) — A style appropriate for links.
- [fill](fill.md) — An overlay fill style for filling shapes.
- [windowBackground](windowbackground.md) — A style appropriate for elements that should match the background of their containing window.
