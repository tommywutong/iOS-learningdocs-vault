---
title: Deprecated initializers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textfield-deprecated
source_url: 'https://developer.apple.com/documentation/swiftui/textfield-deprecated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield-deprecated.json'
content_hash: 'sha256:67e114a5e1e4481f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [Text input and output](text-input-and-output.md) · [TextField](textfield.md)

# Deprecated initializers

<sub>API Collection</sub>

Review deprecated text field initializers.

## Overview

Use view modifiers to specify change and commit behaviors for a text field when replacing these initializers. Use the [onSubmit(of:_:)](<view/onsubmit(of___).md>) view modifier to get the behavior provided by the `onCommit` parameter. Use [focused(_:equals:)](<view/focused(__equals_).md>) and [FocusState](focusstate.md) to get the behavior provided by the `onEditingChanged` parameter.

## Topics

### Creating a text field with a string

- [init(_:text:onEditingChanged:onCommit:)](<textfield/init(__text_oneditingchanged_oncommit_).md>) — Creates a text field with a text label generated from a localized title string. _(deprecated)_
- [init(_:text:onCommit:)](<textfield/init(__text_oncommit_).md>) — Creates a text field with a text label generated from a localized title string. _(deprecated)_
- [init(_:text:onEditingChanged:)](<textfield/init(__text_oneditingchanged_).md>) — Creates a text field with a text label generated from a localized title string. _(deprecated)_

### Creating a text field with a value

- [init(_:value:formatter:onEditingChanged:onCommit:)](<textfield/init(__value_formatter_oneditingchanged_oncommit_).md>) — Create an instance which binds over an arbitrary type, `V`. _(deprecated)_
- [init(_:value:formatter:onCommit:)](<textfield/init(__value_formatter_oncommit_).md>) — Create an instance which binds over an arbitrary type, `V`. _(deprecated)_
- [init(_:value:formatter:onEditingChanged:)](<textfield/init(__value_formatter_oneditingchanged_).md>) — Create an instance which binds over an arbitrary type, `V`. _(deprecated)_
