---
title: 'canPerformAction(_:withSender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/canperformaction(_:withsender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/canperformaction(_:withsender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/canperformaction%28_%3Awithsender%3A%29.json'
content_hash: 'sha256:6c1fbc5d49dad910'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# canPerformAction(_:withSender:)

<sub>Instance Method</sub>

Requests the receiving responder to enable or disable the specified command in the user interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func canPerformAction(_ action: Selector, withSender sender: Any?) -> Bool
```

## Parameters

- `action` — A selector that identifies a method associated with a command. For the editing menu, this is one of the editing methods declared by the UIResponderStandardEditActions informal protocol (for example, `copy:`).

- `sender` — The object calling this method. For the editing menu commands, this is the shared [UIApplication](../uiapplication.md) object. Depending on the context, you can query the sender for information to help you determine whether a command should be enabled.

## Return Value

[true](../../swift/true.md) if the command identified by `action` should be enabled or [false](../../swift/false.md) if it should be disabled. Returning [true](../../swift/true.md) means that your class can handle the command in the current context.

## Discussion

This default implementation of this method returns [true](../../swift/true.md) if the responder class implements the requested action and calls the next responder if it doesn’t. Subclasses may override this method to enable menu commands based on the current state; for example, you would enable the Copy command if there’s a selection or disable the Paste command if the pasteboard didn’t contain data with the correct pasteboard representation type. If no responder in the responder chain returns [true](../../swift/true.md), the menu command is disabled. Note that if your class returns [false](../../swift/false.md) for a command, another responder further up the responder chain may still return [true](../../swift/true.md), enabling the command.

This method might be called more than once for the same action but with a different sender each time. You should be prepared for any kind of sender including `nil`.

For information on the editing menu, see the description of the [UIMenuController](../uimenucontroller.md) class.

## See Also

### Building and validating commands

- [- buildMenuWithBuilder:](<buildmenu(with_).md>) — Asks the receiving responder to add and remove items from a menu system.
- [- validateCommand:](<validate(__).md>) — Asks the receiving responder to validate the command.
- [- targetForAction:withSender:](<target(foraction_withsender_).md>) — Returns the target object that responds to an action.
