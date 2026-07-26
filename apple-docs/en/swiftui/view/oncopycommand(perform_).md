---
title: 'onCopyCommand(perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/oncopycommand(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/oncopycommand(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/oncopycommand%28perform%3A%29.json'
content_hash: 'sha256:7c1944d58530e6ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onCopyCommand(perform:)

<sub>Instance Method</sub>

Adds an action to perform in response to the system’s Copy command.

<sub>macOS</sub>

```swift
nonisolated func onCopyCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View

```

## Parameters

- `payloadAction` — An action closure returning the [NSItemProvider](../../foundation/nsitemprovider.md) items that should be copied to the Clipboard when the Copy command is triggered. If `action` is `nil`, the Copy command is considered disabled.

## Return Value

A view that triggers `action` when a system Copy command occurs.

## See Also

### Copying items using item providers

- [onCutCommand(perform:)](<oncutcommand(perform_).md>) — Adds an action to perform in response to the system’s Cut command.
- [onPasteCommand(of:perform:)](<onpastecommand(of_perform_).md>) — Adds an action to perform in response to the system’s Paste command.
- [onPasteCommand(of:validator:perform:)](<onpastecommand(of_validator_perform_).md>) — Adds an action to perform in response to the system’s Paste command with items that you validate.
