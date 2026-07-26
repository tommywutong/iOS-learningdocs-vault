---
title: 'init(_:text:onCommit:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/textfield/init(_:text:oncommit:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfield/init(_:text:oncommit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield/init%28_%3Atext%3Aoncommit%3A%29.json'
content_hash: 'sha256:e65ac3300269ea7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextField](../textfield.md)

# init(_:text:onCommit:)

<sub>Initializer</sub>

Creates a text field with a text label generated from a localized title string.

> [!warning] Deprecated
> Renamed TextField.init(_:text:onEditingChanged:). Use View.onSubmit(of:_:) for functionality previously provided by the onCommit parameter. Use FocusState\<T\> and View.focused(_:equals:) for functionality previously provided by the onEditingChanged parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleKey: LocalizedStringKey, text: Binding<String>, onCommit: @escaping () -> Void)
```

## Parameters

- `titleKey` — The key for the localized title of the text field, describing its purpose.

- `text` — The text to display and edit.

- `onCommit` — An action to perform when the user performs an action (for example, when the user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a string

- [init(_:text:onEditingChanged:onCommit:)](<init(__text_oneditingchanged_oncommit_).md>) — Creates a text field with a text label generated from a localized title string. _(deprecated)_
- [init(_:text:onEditingChanged:)](<init(__text_oneditingchanged_).md>) — Creates a text field with a text label generated from a localized title string. _(deprecated)_
