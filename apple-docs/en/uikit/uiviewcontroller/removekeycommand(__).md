---
title: 'removeKeyCommand(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/removekeycommand(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/removekeycommand(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/removekeycommand%28_%3A%29.json'
content_hash: 'sha256:28119ea6222ebb1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# removeKeyCommand(_:)

<sub>Instance Method</sub>

Removes the key command from the view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeKeyCommand(_ keyCommand: UIKeyCommand)
```

## Parameters

- `keyCommand` — The key command to remove.

## Discussion

This method lets you easily remove key commands without overriding the [keyCommands](../uiresponder/keycommands.md) property.

## See Also

### Related Documentation

- [keyCommands](../uiresponder/keycommands.md) — The key commands that trigger actions on this responder.

### Accessing the available key commands

- [performsActionsWhilePresentingModally](performsactionswhilepresentingmodally.md) — A Boolean value indicating whether the view controller performs menu-related actions.
- [- addKeyCommand:](<addkeycommand(__).md>) — Associates the specified keyboard shortcut with the view controller.
