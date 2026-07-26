---
title: 'target(forAction:withSender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/target(foraction:withsender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/target(foraction:withsender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/target%28foraction%3Awithsender%3A%29.json'
content_hash: 'sha256:881618f4b46eaaee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# target(forAction:withSender:)

<sub>Instance Method</sub>

Returns the target object that responds to an action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func target(forAction action: Selector, withSender sender: Any?) -> Any?
```

## Parameters

- `action` — A selector that identifies a method associated with a command.

- `sender` — The object calling this method. For the editing menu commands, this is the shared [UIApplication](../uiapplication.md) object. Depending on the context, you can query the sender for information to help you determine the target of the command.

## Return Value

The object whose action method is invoked to execute the command.

## Discussion

This method is called whenever an action needs to be invoked by the object. The default implementation calls the [- canPerformAction:withSender:](<canperformaction(__withsender_).md>) method to determine whether it can invoke the action. If the object can invoke the action, it returns itself, otherwise it passes the request up the responder chain. Your app should override this method if it wants to override how a target is selected.

## See Also

### Building and validating commands

- [- buildMenuWithBuilder:](<buildmenu(with_).md>) — Asks the receiving responder to add and remove items from a menu system.
- [- validateCommand:](<validate(__).md>) — Asks the receiving responder to validate the command.
- [- canPerformAction:withSender:](<canperformaction(__withsender_).md>) — Requests the receiving responder to enable or disable the specified command in the user interface.
