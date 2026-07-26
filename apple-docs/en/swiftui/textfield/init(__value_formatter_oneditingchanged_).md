---
title: 'init(_:value:formatter:onEditingChanged:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/textfield/init(_:value:formatter:oneditingchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfield/init(_:value:formatter:oneditingchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield/init%28_%3Avalue%3Aformatter%3Aoneditingchanged%3A%29.json'
content_hash: 'sha256:59277841b82eb599'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextField](../textfield.md)

# init(_:value:formatter:onEditingChanged:)

<sub>Initializer</sub>

Create an instance which binds over an arbitrary type, `V`.

> [!warning] Deprecated
> Renamed TextField.init(_:value:formatter:onEditingChanged:). Use View.onSubmit(of:_:) for functionality previously provided by the onCommit parameter. Use FocusState\<T\> and View.focused(_:equals:) for functionality previously provided by the onEditingChanged parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<S, V>(_ title: S, value: Binding<V>, formatter: Formatter, onEditingChanged: @escaping (Bool) -> Void) where S : StringProtocol
```

## Parameters

- `title` — The title of the text field, describing its purpose.

- `value` — The underlying value to be edited.

- `formatter` — A formatter to use when converting between the string the user edits and the underlying value of type `V`. In the event that `formatter` is unable to perform the conversion, `binding.value` isn’t modified.

- `onEditingChanged` — The action to perform when the user begins editing `text` and after the user finishes editing `text`. The closure receives a Boolean value that indicates the editing status: `true` when the user begins editing, `false` when they finish.

## See Also

### Creating a text field with a value

- [init(_:value:formatter:onEditingChanged:onCommit:)](<init(__value_formatter_oneditingchanged_oncommit_).md>) — Create an instance which binds over an arbitrary type, `V`. _(deprecated)_
- [init(_:value:formatter:onCommit:)](<init(__value_formatter_oncommit_).md>) — Create an instance which binds over an arbitrary type, `V`. _(deprecated)_
