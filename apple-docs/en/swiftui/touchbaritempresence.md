---
title: TouchBarItemPresence
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/touchbaritempresence
source_url: 'https://developer.apple.com/documentation/swiftui/touchbaritempresence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/touchbaritempresence.json'
content_hash: 'sha256:f32cb4c56ecf6c30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TouchBarItemPresence

<sub>Enumeration</sub>

Options that affect user customization of the Touch Bar.

<sub>macOS</sub>

```swift
enum TouchBarItemPresence
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting presence options

- [TouchBarItemPresence.default(_:)](<touchbaritempresence/default(__).md>) — The Touch Bar view is visible by default, but can be removed during customization.
- [TouchBarItemPresence.optional(_:)](<touchbaritempresence/optional(__).md>) — The Touch Bar view isn’t visible by default, but appears in the customization palette.
- [TouchBarItemPresence.required(_:)](<touchbaritempresence/required(__).md>) — The Touch Bar view is visible by default and cannot be removed during customization.

## See Also

### Managing Touch Bar input

- [touchBar(content:)](<view/touchbar(content_).md>) — Sets the content that the Touch Bar displays.
- [touchBar(_:)](<view/touchbar(__).md>) — Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [touchBarItemPrincipal(_:)](<view/touchbaritemprincipal(__).md>) — Sets principal views that have special significance to this Touch Bar.
- [touchBarCustomizationLabel(_:)](<view/touchbarcustomizationlabel(__).md>) — Sets a user-visible string that identifies the view’s functionality.
- [touchBarItemPresence(_:)](<view/touchbaritempresence(__).md>) — Sets the behavior of the user-customized view.
- [TouchBar](touchbar.md) — A container for a view that you can show in the Touch Bar.
