---
title: TouchBar
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/touchbar
source_url: 'https://developer.apple.com/documentation/swiftui/touchbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/touchbar.json'
content_hash: 'sha256:5dad17a86f1f335d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TouchBar

<sub>Structure</sub>

A container for a view that you can show in the Touch Bar.

<sub>macOS</sub>

```swift
struct TouchBar<Content> where Content : View
```

## Topics

### Creating a Touch Bar view

- [init(content:)](<touchbar/init(content_).md>) — Creates a non-customizable Touch Bar view container.
- [init(id:content:)](<touchbar/init(id_content_).md>) — Creates a customizable Touch Bar view container with a globally unique identifier.

## See Also

### Managing Touch Bar input

- [touchBar(content:)](<view/touchbar(content_).md>) — Sets the content that the Touch Bar displays.
- [touchBar(_:)](<view/touchbar(__).md>) — Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [touchBarItemPrincipal(_:)](<view/touchbaritemprincipal(__).md>) — Sets principal views that have special significance to this Touch Bar.
- [touchBarCustomizationLabel(_:)](<view/touchbarcustomizationlabel(__).md>) — Sets a user-visible string that identifies the view’s functionality.
- [touchBarItemPresence(_:)](<view/touchbaritempresence(__).md>) — Sets the behavior of the user-customized view.
- [TouchBarItemPresence](touchbaritempresence.md) — Options that affect user customization of the Touch Bar.
