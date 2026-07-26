---
title: 'touchBarItemPresence(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/touchbaritempresence(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/touchbaritempresence(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/touchbaritempresence%28_%3A%29.json'
content_hash: 'sha256:d06545df3ce58a84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# touchBarItemPresence(_:)

<sub>Instance Method</sub>

Sets the behavior of the user-customized view.

<sub>macOS</sub>

```swift
nonisolated func touchBarItemPresence(_ presence: TouchBarItemPresence) -> some View

```

## Parameters

- `presence` — One of the allowed [TouchBarItemPresence](../touchbaritempresence.md) descriptions.

## Return Value

A trait that describes the behavior for this Touch Bar view.

## Discussion

Use `touchBarItemPresence(_:)` to define the visibility requirements of a particular Touch Bar view during customization by the user.

Touch Bar views may be:

- `.required`: not allowed to be removed by the user.
- `.default`: shown by default prior to user customization, but removable.
- `.optional`: not visible by default, but can be added through the customization palette.

Each [TouchBarItemPresence](../touchbaritempresence.md) must be initialized with a string that is a globally unique identifier for this item.

In the example below, all of the Touch Bar items are visible in the Touch Bar by default, except for the “Clubs” item. It’s set to `.optional` but is configurable by the user:

```swift
TextField("TouchBar Demo", text: $placeholder)
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    .focusable()
    .touchBar {
        Button("♥️", action: selectHearts)
            .touchBarItemPresence(.required("heartsKey"))
        Button("♣️", action: selectClubs)
            .touchBarItemPresence(.optional("clubsKey"))
        Button("♠️", action: selectSpades)
            .touchBarItemPresence(.required("spadesKey"))
        Button("♦️", action: selectDiamonds)
            .touchBarItemPresence(.required("diamondsKey"))
}
```

![A view showing the configuration of the Touch Bar with required and](../../../../attachments/39aa265ad81c120e7f2f5130bfcb3d08/SwiftUI-touchBarItemPresence@2x.png)

## See Also

### Managing Touch Bar input

- [touchBar(content:)](<touchbar(content_).md>) — Sets the content that the Touch Bar displays.
- [touchBar(_:)](<touchbar(__).md>) — Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [touchBarItemPrincipal(_:)](<touchbaritemprincipal(__).md>) — Sets principal views that have special significance to this Touch Bar.
- [touchBarCustomizationLabel(_:)](<touchbarcustomizationlabel(__).md>) — Sets a user-visible string that identifies the view’s functionality.
- [TouchBar](../touchbar.md) — A container for a view that you can show in the Touch Bar.
- [TouchBarItemPresence](../touchbaritempresence.md) — Options that affect user customization of the Touch Bar.
