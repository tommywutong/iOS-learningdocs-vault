---
title: 'documentInteractionController(_:canPerformAction:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+（6.0 起废弃）, iPadOS 3.2+（6.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:canperformaction:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:canperformaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller%28_%3Acanperformaction%3A%29.json'
content_hash: 'sha256:5079a16be979588b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionController(_:canPerformAction:)

<sub>Instance Method</sub>

Called when a document interaction controller needs to know whether the specified action can be performed on the associated document.

> [!warning] Deprecated
> Apps should use [UIActivityViewController](../uiactivityviewcontroller.md) for actions.

<sub>visionOS</sub>

```swift
optional func documentInteractionController(_ controller: UIDocumentInteractionController, canPerformAction action: Selector?) -> Bool
```

## Parameters

- `controller` — The document interaction controller managing an associated document.

- `action` — The selector representing the action in question.

## Return Value

[true](../../swift/true.md) if the specified action is supported for the associated document or [false](../../swift/false.md) if it is not. If you do not implement this method, the return value is assumed to be [false](../../swift/false.md).

## Discussion

When building the options menu (invoked, for example, by the user performing a long press gesture), a document interaction controller calls this method to find out if your app can perform various actions. If you implement this method for a given action, you must also implement the [- documentInteractionController:performAction:](<documentinteractioncontroller(__performaction_).md>) method for that action.

The supported `action` selectors for this method are `copy:` and `print:`. (The `print:` selector is available in iOS 4.2 and later. Printing is supported only on devices that support multitasking.)

For each action that you implement in the [- documentInteractionController:performAction:](<documentinteractioncontroller(__performaction_).md>) delegate method, return [true](../../swift/true.md) from this method if that action is available for the document.

## See Also

### Deprecated

- [- documentInteractionController:performAction:](<documentinteractioncontroller(__performaction_).md>) — Called when a document interaction controller wants its delegate to perform a specified action with the associated document. _(deprecated)_
