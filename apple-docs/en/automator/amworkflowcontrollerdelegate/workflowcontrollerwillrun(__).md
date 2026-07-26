---
title: 'workflowControllerWillRun(_:)'
framework: Automator
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 14.0+, macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerwillrun(_:)'
source_url: 'https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerwillrun(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerwillrun%28_%3A%29.json'
content_hash: 'sha256:fa34b6f42ce6b7f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Automator](../../automator.md) · [AMWorkflowControllerDelegate](../amworkflowcontrollerdelegate.md)

# workflowControllerWillRun(_:)

<sub>Instance Method</sub>

Notifies the delegate when the workflow controller object is about to run.

<sub>macOS</sub>

```swift
optional func workflowControllerWillRun(_ controller: AMWorkflowController)
```

## Parameters

- `controller` — The workflow controller object to run.

## See Also

### Preparing to Run

- [- workflowController:willRunAction:](<workflowcontroller(__willrun_).md>) — Notifies the delegate when the specified action is about to run.
