---
title: 'workflowControllerDidRun(_:)'
framework: Automator
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 14.0+, macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerdidrun(_:)'
source_url: 'https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerdidrun(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerdidrun%28_%3A%29.json'
content_hash: 'sha256:198f42f0be9268eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Automator](../../automator.md) · [AMWorkflowControllerDelegate](../amworkflowcontrollerdelegate.md)

# workflowControllerDidRun(_:)

<sub>Instance Method</sub>

Notifies the delegate when the workflow controller object finishes running.

<sub>macOS</sub>

```swift
optional func workflowControllerDidRun(_ controller: AMWorkflowController)
```

## Parameters

- `controller` — The workflow controller object that finished running.

## See Also

### Running

- [- workflowController:didRunAction:](<workflowcontroller(__didrun_).md>) — Notifies the delegate when the specified action finishes running.
