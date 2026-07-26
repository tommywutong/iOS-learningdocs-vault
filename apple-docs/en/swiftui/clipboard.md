---
title: Clipboard
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/clipboard
source_url: 'https://developer.apple.com/documentation/swiftui/clipboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/clipboard.json'
content_hash: 'sha256:a85d6ec576dac384'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Clipboard

<sub>API Collection</sub>

Enable people to move or duplicate items by issuing Copy and Paste commands.

## Overview

When people issue standard Copy and Cut commands, they expect to move items to the system’s Clipboard, from which they can paste the items into another place in the same app or into another app. Your app can participate in this activity if you add view modifiers that indicate how to respond to the standard commands.

![](../../../attachments/0c2b0415a2783976458448b003e0705f/clipboard-hero@2x.png)

In your copy and paste modifiers, provide or accept types that conform to the [Transferable](../coretransferable/transferable.md) protocol, or that inherit from the [NSItemProvider](../foundation/nsitemprovider.md) class. When possible, prefer using transferable items.

## Topics

### Copying transferable items

- [copyable(_:)](<view/copyable(__).md>) — Specifies a list of items to copy in response to the system’s Copy command.
- [cuttable(for:action:)](<view/cuttable(for_action_).md>) — Specifies an action that moves items to the Clipboard in response to the system’s Cut command.
- [pasteDestination(for:action:validator:)](<view/pastedestination(for_action_validator_).md>) — Specifies an action that adds validated items to a view in response to the system’s Paste command.

### Copying items using item providers

- [onCopyCommand(perform:)](<view/oncopycommand(perform_).md>) — Adds an action to perform in response to the system’s Copy command.
- [onCutCommand(perform:)](<view/oncutcommand(perform_).md>) — Adds an action to perform in response to the system’s Cut command.
- [onPasteCommand(of:perform:)](<view/onpastecommand(of_perform_).md>) — Adds an action to perform in response to the system’s Paste command.
- [onPasteCommand(of:validator:perform:)](<view/onpastecommand(of_validator_perform_).md>) — Adds an action to perform in response to the system’s Paste command with items that you validate.

## See Also

### Event handling

- [Gestures](gestures.md) — Define interactions from taps, clicks, and swipes to fine-grained gestures.
- [Input events](input-events.md) — Respond to input from a hardware device, like a keyboard or a Touch Bar.
- [Drag and drop](drag-and-drop.md) — Enable people to move or duplicate items by dragging them from one location to another.
- [Focus](focus.md) — Identify and control which visible object responds to user interaction.
- [System events](system-events.md) — React to system events, like opening a URL.
