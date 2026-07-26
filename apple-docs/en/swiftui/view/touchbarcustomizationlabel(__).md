---
title: 'touchBarCustomizationLabel(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/touchbarcustomizationlabel(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/touchbarcustomizationlabel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/touchbarcustomizationlabel%28_%3A%29.json'
content_hash: 'sha256:85f299a49478c934'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# touchBarCustomizationLabel(_:)

<sub>Instance Method</sub>

Sets a user-visible string that identifies the view’s functionality.

<sub>macOS</sub>

```swift
nonisolated func touchBarCustomizationLabel(_ label: Text) -> some View

```

## Parameters

- `label` — A `Text` view containing the customization label.

## Return Value

A Touch Bar element with a set customization label.

## Discussion

This string is visible during user customization.

```swift
TextField("TouchBar Demo", text: $placeholder)
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    .focusable()
    .touchBar {
        Button("♥️", action: selectHearts)
            .touchBarCustomizationLabel(Text("Hearts"))
        Button("♣️", action: selectClubs)
            .touchBarCustomizationLabel(Text("Clubs"))
        Button("♠️", action: selectSpades)
            .touchBarCustomizationLabel(Text("Spades"))
        Button("♦️", action: selectDiamonds)
            .touchBarCustomizationLabel(Text("Diamonds"))
    }
```

![A Touch Bar customization view showing labels assigned to the Touch](../../../../attachments/cdb67ec595f9e8587676a192396b6286/SwiftUI-touchBarCustomizationLabel@2x.png)

## See Also

### Managing Touch Bar input

- [touchBar(content:)](<touchbar(content_).md>) — Sets the content that the Touch Bar displays.
- [touchBar(_:)](<touchbar(__).md>) — Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [touchBarItemPrincipal(_:)](<touchbaritemprincipal(__).md>) — Sets principal views that have special significance to this Touch Bar.
- [touchBarItemPresence(_:)](<touchbaritempresence(__).md>) — Sets the behavior of the user-customized view.
- [TouchBar](../touchbar.md) — A container for a view that you can show in the Touch Bar.
- [TouchBarItemPresence](../touchbaritempresence.md) — Options that affect user customization of the Touch Bar.
