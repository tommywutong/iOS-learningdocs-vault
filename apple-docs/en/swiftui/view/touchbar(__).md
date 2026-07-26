---
title: 'touchBar(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/touchbar(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/touchbar(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/touchbar%28_%3A%29.json'
content_hash: 'sha256:32410d6443aad8ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# touchBar(_:)

<sub>Instance Method</sub>

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

<sub>macOS</sub>

```swift
nonisolated func touchBar<Content>(_ touchBar: TouchBar<Content>) -> some View where Content : View

```

## Parameters

- `touchBar` — A collection of views that the Touch Bar displays.

## Return Value

A view that contains the Touch Bar content.

## Discussion

Use [touchBar(_:)](<touchbar(__).md>) to provide a static set of views that are displayed by the Touch Bar when appropriate, depending on whether the view has focus.

The example below provides Touch Bar content in-line, that creates the content the Touch Bar displays:

```swift
func selectHearts() {/* ... */ }
func selectClubs() { /* ... */ }
func selectSpades() { /* ... */ }
func selectDiamonds() { /* ... */ }

TextField("TouchBar Demo", text: $placeholder)
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    .focusable()
    .touchBar {
        Button("♥️ - Hearts", action: selectHearts)
        Button("♣️ - Clubs", action: selectClubs)
        Button("♠️ - Spades", action: selectSpades)
        Button("♦️ - Diamonds", action: selectDiamonds)
    }
```

![A Touch Bar that shows content you create by using a static collection](../../../../attachments/50abda464413c0ca08d8e80cb02bce7b/SwiftUI-touchbar-static@2x.png)

## See Also

### Managing Touch Bar input

- [touchBar(content:)](<touchbar(content_).md>) — Sets the content that the Touch Bar displays.
- [touchBarItemPrincipal(_:)](<touchbaritemprincipal(__).md>) — Sets principal views that have special significance to this Touch Bar.
- [touchBarCustomizationLabel(_:)](<touchbarcustomizationlabel(__).md>) — Sets a user-visible string that identifies the view’s functionality.
- [touchBarItemPresence(_:)](<touchbaritempresence(__).md>) — Sets the behavior of the user-customized view.
- [TouchBar](../touchbar.md) — A container for a view that you can show in the Touch Bar.
- [TouchBarItemPresence](../touchbaritempresence.md) — Options that affect user customization of the Touch Bar.
