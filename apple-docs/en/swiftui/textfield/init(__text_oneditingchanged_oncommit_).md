---
title: 'init(_:text:onEditingChanged:onCommit:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/textfield/init(_:text:oneditingchanged:oncommit:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfield/init(_:text:oneditingchanged:oncommit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield/init%28_%3Atext%3Aoneditingchanged%3Aoncommit%3A%29.json'
content_hash: 'sha256:92f15bb6e07512c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextField](../textfield.md)

# init(_:text:onEditingChanged:onCommit:)

<sub>Initializer</sub>

Creates a text field with a text label generated from a localized title string.

> [!warning] Deprecated
> Use [init(_:text:prompt:)](<init(__text_prompt_)-70zi2.md>) instead. Add the [onSubmit(of:_:)](<../view/onsubmit(of___).md>) view modifier for the `onCommit` behavior. Use [FocusState](../focusstate.md) and [focused(_:equals:)](<../view/focused(__equals_).md>) for the `onEditingChanged` behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ titleKey: LocalizedStringKey, text: Binding<String>, onEditingChanged: @escaping (Bool) -> Void, onCommit: @escaping () -> Void)
```

## Parameters

- `titleKey` — The key for the localized title of the text field, describing its purpose.

- `text` — The text to display and edit.

- `onEditingChanged` — The action to perform when the user begins editing `text` and after the user finishes editing `text`. The closure receives a Boolean value that indicates the editing status: `true` when the user begins editing, `false` when they finish.

- `onCommit` — An action to perform when the user performs an action (for example, when the user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a string

- [init(_:text:onCommit:)](<init(__text_oncommit_).md>) — Creates a text field with a text label generated from a localized title string. _(deprecated)_
- [init(_:text:onEditingChanged:)](<init(__text_oneditingchanged_).md>) — Creates a text field with a text label generated from a localized title string. _(deprecated)_
