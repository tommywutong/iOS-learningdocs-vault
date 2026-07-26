---
title: 'touchBarItemPrincipal(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/touchbaritemprincipal(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/touchbaritemprincipal(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/touchbaritemprincipal%28_%3A%29.json'
content_hash: 'sha256:3d05d5c28cbd1464'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# touchBarItemPrincipal(_:)

<sub>Instance Method</sub>

Sets principal views that have special significance to this Touch Bar.

<sub>macOS</sub>

```swift
nonisolated func touchBarItemPrincipal(_ principal: Bool = true) -> some View

```

## Parameters

- `principal` — A Boolean value that indicates whether to display this view prominently in the Touch Bar compared to other views.

## Return Value

A Touch Bar view with one element centered in the Touch Bar row.

## Discussion

Use `touchBarItemPrincipal(_:)` to designate a view as a significant view in the Touch Bar. Currently, that view will be placed in the center of the row.

The example below sets the last button as the principal button for the Touch Bar view.

```swift
let touchBarItems = TouchBar(id: "myBarItems") {
    Button("♣️", action: {})
    Button("♥️", action: {})
    Button("♠️", action: {})
    Button("♦️", action: {})
       .touchBarItemPrincipal(true)
}

TextField("TouchBar Demo", text: $placeholder)
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    .focusable()
    .touchBar(touchBarItems)
```

> [!note] Note
> Multiple visible bars may each specify a principal view, but the system only honors one of them.

![A Touch Bar view showing one element designated as the principal view](../../../../attachments/ebd3f9fdec8875dcd3bb0da49e893ee7/SwiftUI-touchBarItemPrincipal@2x.png)

## See Also

### Managing Touch Bar input

- [touchBar(content:)](<touchbar(content_).md>) — Sets the content that the Touch Bar displays.
- [touchBar(_:)](<touchbar(__).md>) — Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [touchBarCustomizationLabel(_:)](<touchbarcustomizationlabel(__).md>) — Sets a user-visible string that identifies the view’s functionality.
- [touchBarItemPresence(_:)](<touchbaritempresence(__).md>) — Sets the behavior of the user-customized view.
- [TouchBar](../touchbar.md) — A container for a view that you can show in the Touch Bar.
- [TouchBarItemPresence](../touchbaritempresence.md) — Options that affect user customization of the Touch Bar.
