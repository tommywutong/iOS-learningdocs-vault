---
title: 'touchBar(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/touchbar(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/touchbar(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/touchbar%28content%3A%29.json'
content_hash: 'sha256:887815eb1658bea5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# touchBar(content:)

<sub>Instance Method</sub>

Sets the content that the Touch Bar displays.

<sub>macOS</sub>

```swift
nonisolated func touchBar<Content>(@ContentBuilder content: () -> Content) -> some View where Content : View

```

## Parameters

- `content` — A collection of views to be displayed by the Touch Bar.

## Return Value

A view that contains the Touch Bar content.

## Discussion

Use `touchBar(_:)` when you need to dynamically construct items to show in the Touch Bar. The content is displayed by the Touch Bar when appropriate, depending on focus.

In the example below, four buttons are added to a Touch Bar content struct and then added to the Touch Bar:

```swift
let touchBarItems = TouchBar(id: "myBarItems") {
    Button("♣️", action: {})
    Button("♥️", action: {})
    Button("♠️", action: {})
    Button("♦️", action: {})
}

TextField("TouchBar Demo", text: $placeholder)
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    .focusable()
    .touchBar(touchBarItems)
```

![A Touch Bar that shows content you create using a Touch Bar content](../../../../attachments/b8b2d24bdd0bd4469d5947a800928ab4/SwiftUI-View-touchBar@2x.png)

## See Also

### Managing Touch Bar input

- [touchBar(_:)](<touchbar(__).md>) — Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [touchBarItemPrincipal(_:)](<touchbaritemprincipal(__).md>) — Sets principal views that have special significance to this Touch Bar.
- [touchBarCustomizationLabel(_:)](<touchbarcustomizationlabel(__).md>) — Sets a user-visible string that identifies the view’s functionality.
- [touchBarItemPresence(_:)](<touchbaritempresence(__).md>) — Sets the behavior of the user-customized view.
- [TouchBar](../touchbar.md) — A container for a view that you can show in the Touch Bar.
- [TouchBarItemPresence](../touchbaritempresence.md) — Options that affect user customization of the Touch Bar.
