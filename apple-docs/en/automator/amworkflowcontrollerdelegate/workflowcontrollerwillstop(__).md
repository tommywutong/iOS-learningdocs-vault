---
title: 'workflowControllerWillStop(_:)'
framework: Automator
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 14.0+, macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerwillstop(_:)'
source_url: 'https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerwillstop(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerwillstop%28_%3A%29.json'
content_hash: 'sha256:58273fffda73b716'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Automator](../../automator.md) · [AMWorkflowControllerDelegate](../amworkflowcontrollerdelegate.md)

# workflowControllerWillStop(_:)

<sub>Instance Method</sub>

Tells the delegate that the workflow controller object is about to stop.

<sub>macOS</sub>

```swift
optional func workflowControllerWillStop(_ controller: AMWorkflowController)
```

## Parameters

- `controller` — The workflow controller object to stop.

## See Also

### Stopping

- [- workflowControllerDidStop:](<workflowcontrollerdidstop(__).md>) — Tells the delegate that the workflow controller object has stopped.
