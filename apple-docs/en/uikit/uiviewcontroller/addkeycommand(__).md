---
title: 'addKeyCommand(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/addkeycommand(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/addkeycommand(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/addkeycommand%28_%3A%29.json'
content_hash: 'sha256:d95ee6de78e95152'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# addKeyCommand(_:)

<sub>Instance Method</sub>

Associates the specified keyboard shortcut with the view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addKeyCommand(_ keyCommand: UIKeyCommand)
```

## Parameters

- `keyCommand` — The key command to add.

## Discussion

This method lets you easily add key commands to the view controller without overriding the [keyCommands](../uiresponder/keycommands.md) property. The key commands you add to a view controller are applied to the active responder chain. When the user performs a key command, UIKit searches the responder chain (starting with the first responder) for an object capable of handling the specified action.

## See Also

### Related Documentation

- [keyCommands](../uiresponder/keycommands.md) — The key commands that trigger actions on this responder.

### Accessing the available key commands

- [performsActionsWhilePresentingModally](performsactionswhilepresentingmodally.md) — A Boolean value indicating whether the view controller performs menu-related actions.
- [- removeKeyCommand:](<removekeycommand(__).md>) — Removes the key command from the view controller.
