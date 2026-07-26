---
title: 'init(_:text:onEditingChanged:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/textfield/init(_:text:oneditingchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfield/init(_:text:oneditingchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield/init%28_%3Atext%3Aoneditingchanged%3A%29.json'
content_hash: 'sha256:e0673ed6560a74d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextField](../textfield.md)

# init(_:text:onEditingChanged:)

<sub>Initializer</sub>

Creates a text field with a text label generated from a localized title string.

> [!warning] Deprecated
> Renamed TextField.init(_:text:onEditingChanged:). Use View.onSubmit(of:_:) for functionality previously provided by the onCommit parameter. Use FocusState\<T\> and View.focused(_:equals:) for functionality previously provided by the onEditingChanged parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleKey: LocalizedStringKey, text: Binding<String>, onEditingChanged: @escaping (Bool) -> Void)
```

## Parameters

- `titleKey` — The key for the localized title of the text field, describing its purpose.

- `text` — The text to display and edit.

- `onEditingChanged` — The action to perform when the user begins editing `text` and after the user finishes editing `text`. The closure receives a Boolean value that indicates the editing status: `true` when the user begins editing, `false` when they finish.

## See Also

### Creating a text field with a string

- [init(_:text:onEditingChanged:onCommit:)](<init(__text_oneditingchanged_oncommit_).md>) — Creates a text field with a text label generated from a localized title string. _(deprecated)_
- [init(_:text:onCommit:)](<init(__text_oncommit_).md>) — Creates a text field with a text label generated from a localized title string. _(deprecated)_
