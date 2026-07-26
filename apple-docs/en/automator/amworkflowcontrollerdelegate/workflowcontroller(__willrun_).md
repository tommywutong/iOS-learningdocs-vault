---
title: 'workflowController(_:willRun:)'
framework: Automator
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 14.0+, macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/automator/amworkflowcontrollerdelegate/workflowcontroller(_:willrun:)'
source_url: 'https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontroller(_:willrun:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/automator/amworkflowcontrollerdelegate/workflowcontroller%28_%3Awillrun%3A%29.json'
content_hash: 'sha256:fb43d23aea6ed2ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Automator](../../automator.md) · [AMWorkflowControllerDelegate](../amworkflowcontrollerdelegate.md)

# workflowController(_:willRun:)

<sub>Instance Method</sub>

Notifies the delegate when the specified action is about to run.

<sub>macOS</sub>

```swift
optional func workflowController(_ controller: AMWorkflowController, willRun action: AMAction)
```

## Parameters

- `controller` — The controller object sending the message.

- `action` — The workflow action to run.

## See Also

### Preparing to Run

- [- workflowControllerWillRun:](<workflowcontrollerwillrun(__).md>) — Notifies the delegate when the workflow controller object is about to run.
