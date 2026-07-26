---
title: 'workflowController(_:didRun:)'
framework: Automator
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 14.0+, macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/automator/amworkflowcontrollerdelegate/workflowcontroller(_:didrun:)'
source_url: 'https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontroller(_:didrun:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/automator/amworkflowcontrollerdelegate/workflowcontroller%28_%3Adidrun%3A%29.json'
content_hash: 'sha256:9573c4efc20a7339'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Automator](../../automator.md) · [AMWorkflowControllerDelegate](../amworkflowcontrollerdelegate.md)

# workflowController(_:didRun:)

<sub>Instance Method</sub>

Notifies the delegate when the specified action finishes running.

<sub>macOS</sub>

```swift
optional func workflowController(_ controller: AMWorkflowController, didRun action: AMAction)
```

## Parameters

- `controller` — The controller object sending the message.

- `action` — The workflow action that ran.

## See Also

### Running

- [- workflowControllerDidRun:](<workflowcontrollerdidrun(__).md>) — Notifies the delegate when the workflow controller object finishes running.
