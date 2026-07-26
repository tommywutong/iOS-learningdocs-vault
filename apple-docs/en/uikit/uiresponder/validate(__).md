---
title: 'validate(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/validate(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/validate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/validate%28_%3A%29.json'
content_hash: 'sha256:e37539e5f51255c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# validate(_:)

<sub>Instance Method</sub>

Asks the receiving responder to validate the command.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func validate(_ command: UICommand)
```

## Parameters

- `command` — A mutable command object.

## Discussion

Override this method in your view controller to make changes to a command before the command system renders it as a menu item.

## See Also

### Building and validating commands

- [- buildMenuWithBuilder:](<buildmenu(with_).md>) — Asks the receiving responder to add and remove items from a menu system.
- [- canPerformAction:withSender:](<canperformaction(__withsender_).md>) — Requests the receiving responder to enable or disable the specified command in the user interface.
- [- targetForAction:withSender:](<target(foraction_withsender_).md>) — Returns the target object that responds to an action.
