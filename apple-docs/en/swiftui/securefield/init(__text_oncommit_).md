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
doc_path: '/documentation/swiftui/securefield/init(_:text:oncommit:)'
source_url: 'https://developer.apple.com/documentation/swiftui/securefield/init(_:text:oncommit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/securefield/init%28_%3Atext%3Aoncommit%3A%29.json'
content_hash: 'sha256:c3f1d20bc675b2d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SecureField](../securefield.md)

# init(_:text:onCommit:)

<sub>Initializer</sub>

Creates an instance.

> [!warning] Deprecated
> Use [init(_:text:prompt:)](<init(__text_prompt_)-40n4d.md>) instead. Add the [onSubmit(of:_:)](<../view/onsubmit(of___).md>) view modifier for the `onCommit` behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ titleKey: LocalizedStringKey, text: Binding<String>, onCommit: @escaping () -> Void)
```

## Parameters

- `titleKey` — The key for the localized title of `self`, describing its purpose.

- `text` — The text to display and edit.

- `onCommit` — The action to perform when the user performs an action (usually pressing the Return key) while the secure field has focus.
