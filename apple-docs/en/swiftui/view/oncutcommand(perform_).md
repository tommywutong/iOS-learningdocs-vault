---
title: 'onCutCommand(perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/oncutcommand(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/oncutcommand(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/oncutcommand%28perform%3A%29.json'
content_hash: 'sha256:3480c946f76e8dac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onCutCommand(perform:)

<sub>Instance Method</sub>

Adds an action to perform in response to the system’s Cut command.

<sub>macOS</sub>

```swift
nonisolated func onCutCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View

```

## Parameters

- `payloadAction` — An action closure that should delete the selected data and return [NSItemProvider](../../foundation/nsitemprovider.md) items corresponding to that data, which should be written to the Clipboard. If `action` is `nil`, the Cut command is considered disabled.

## Return Value

A view that triggers `action` when a system Cut command occurs.

## See Also

### Copying items using item providers

- [onCopyCommand(perform:)](<oncopycommand(perform_).md>) — Adds an action to perform in response to the system’s Copy command.
- [onPasteCommand(of:perform:)](<onpastecommand(of_perform_).md>) — Adds an action to perform in response to the system’s Paste command.
- [onPasteCommand(of:validator:perform:)](<onpastecommand(of_validator_perform_).md>) — Adds an action to perform in response to the system’s Paste command with items that you validate.
